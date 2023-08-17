   
import random

# Example for testing
# bed_id = "b1"
# patient_day = 1
# patient_schedule = {1: {1600:0,1700:0,1800:0}}
# patient_id = "p1"
def change_bed_occupancy(bed_id, patient_schedule, patient_day, patient_id, bed_objects_list):
    # change the bed occupancy from available (meaning 0) to the patient id
    for bed in bed_objects_list:
        # print("this is the bed_id whose bed occupancy i will change to the patient id ", bed.bed_id)
        if bed.bed_id == bed_id:
            # print("yes")
            # change the occupancy based on the possible_sched
            # print("this is the patient_day whose bed occupancy i will change to the patient ID", patient_id, patient_day)
            for time_p in patient_schedule:
                # print(bed_schedule[patient_day][time_p])
                # change from 0 to the patient_id
                # print("This is the time that I will change to 0 ", bed.bed_schedule[patient_day][time_p])
                bed.bed_schedule[patient_day][time_p] = patient_id

def free_up_bed_occupancy(bed_id, patient_schedule, patient_day, patient_id, bed_objects_list):
    # change the bed occupancy from available (meaning 0) to the patient id
    for bed in bed_objects_list:
        # print("this is the bed_id whose bed occupancy i will free up", bed.bed_id)
        # print("this is the patient_schedule whose bed occupancy i will free up ", patient_schedule)
        if bed.bed_id == bed_id:
            # print("yes")
            # change the occupancy based on the possible_sched
            # print("this is the patient_day ", patient_day)
            for time_p in patient_schedule:
                # print("This is the time that I will change to 0 ", time_p)
                # change from 0 to the patient_id
                bed.bed_schedule[patient_day][time_p] = 0

# requested_time_slot = {1600:0,1700:0,1800:0}}
# requested_day = 1
# requested_time = 1600

def check_bed_availability(bed_id, requested_time_slot, requested_day, bed_objects_list):
    availablility_counter = 0
    for bed in bed_objects_list:
        if bed.bed_id == bed_id:
            # check if its free
            for requested_time in requested_time_slot:
                if bed.bed_schedule[requested_day][requested_time] == 0: 
                    # print("requested day ", requested_day, " requested time ", requested_time)
                    availablility_counter += 1

            if availablility_counter == len(requested_time_slot):
                return True
            else:
                return False

def reserve_patient_beds(all_possible_patient_schedules, patient_schedules_in_list, patient_schedules_out_list, bed_objects_list):
    # Example for testing
    # bed_id = "b1"
    # patient_day = 1
    # patient_schedule = {1: {1600:0,1700:0,1800:0}}
    # patient_id = "p1"
    #change_bed_occupancy(bed_id, single_patient_day_schedule, patient_day, patient_id)

    ## Look through the first matched availability
    for patient_sched in all_possible_patient_schedules:
        patient_schedules_out_dict = {}
        patient_schedules_in_dict = {}
        days = list(patient_sched['possible_allocated_schedule'].keys())
        # print("this is the length ", len(patient_sched['possible_allocated_schedule']))
        for requested_day in days:
            # print("this is the requested day ", requested_day)
            # print("this is patient_sched['possible_allocated_schedule'][requested_day]", patient_sched['possible_allocated_schedule'][requested_day])
            requested_sched = patient_sched['possible_allocated_schedule'][requested_day]
            # print(patient_sched['possible_allocated_schedule'])
            bed_id = patient_sched['bed']
            #check_bed_availability(bed_id, requested_time_slot, requested_day)
            # print("first if statement ", bed_id, requested_sched, " day ", requested_day, " for patient ", patient_sched['patient'])
            if check_bed_availability(bed_id, requested_sched, requested_day, bed_objects_list) == True:
                # print("you passed the bed availablity test") 

                ## Add the patient's schedule to the patient_schedules_in_dict and list
                patient_schedules_in_dict = {
                    'patient': patient_sched['patient'],
                    'bed': patient_sched['bed'],
                    'day': requested_day,
                    'schedule': patient_sched['possible_allocated_schedule'][requested_day]
                }
                patient_schedules_in_list.append(patient_schedules_in_dict)

                #print(requested_sched)
                change_bed_occupancy(bed_id, requested_sched, requested_day, patient_sched['patient'], bed_objects_list)

                ## Remove the patient schedule from patient_schedules_out_list
                if patient_schedules_in_dict in patient_schedules_out_list:
                    patient_schedules_out_list.remove(patient_schedules_in_dict)

            else:
                # bed turns out is not available so add the patient's schedule to the patient_schedules_out_dict and list
                patient_schedules_out_dict = {
                    'patient': patient_sched['patient'],
                    'bed': patient_sched['bed'],
                    'day': requested_day,
                    'schedule': patient_sched['possible_allocated_schedule'][requested_day]
                }
                # if the schedule is not already in the out list, then add it to the out list
                if patient_schedules_out_dict not in patient_schedules_out_list:
                    patient_schedules_out_list.append(patient_schedules_out_dict)
                    # print("Unfortunately this ", patient_schedules_out_dict, " could not be added the bed is not available on", requested_day)

                # make sure to remove it from the patient_schedules_in_list
                if patient_schedules_out_dict in patient_schedules_in_list:
                    patient_schedules_in_list.remove(patient_schedules_out_dict)

                # make sure to free up the bed occupancy because it was previously in the in_list
                free_up_bed_occupancy(bed_id, requested_sched, requested_day, patient_sched['patient'], bed_objects_list)
                
    return patient_schedules_out_list, patient_schedules_in_list

def check_time_spacing(patient_schedules_out_list, patient_schedules_in_list, bed_objects_list):
    assigned_days = {}

    patient_schedules_in_list_copy = patient_schedules_in_list.copy()
    
    for schedule in patient_schedules_in_list_copy:
        patient = schedule['patient']
        bed = schedule['bed']
        day = schedule['day']
        schedule_data = schedule['schedule']

        # Check if the patient is already assigned a day
        if patient in assigned_days:
            # print(assigned_days)
            # Check if the assigned day is consecutive to the current day
            if assigned_days[patient] + 1 == day:
                # Add the patient's information to the patient_schedule_out_list
                patient_schedule_out_dict = {
                    'patient': patient,
                    'bed': bed,
                    'day': assigned_days[patient] + 1,
                    'schedule': schedule_data
                }
                patient_schedules_out_list.append(patient_schedule_out_dict)
                # Remove the conflicting appointment from patient_schedules_in_list
                patient_schedules_in_list.remove(schedule)

                free_up_bed_occupancy(bed, schedule_data, day, patient, bed_objects_list)
            else:
                assigned_days[patient] = day
        else:
            assigned_days[patient] = day
            
    return patient_schedules_out_list, patient_schedules_in_list, assigned_days

def remove_non_consecutive_schedules(patient_schedules_out_list, patient_schedules_in_list):
    modified_list = []

    for entry in patient_schedules_in_list:
        schedule = entry['schedule']
        # Sorts times within the schedule in ascending order.
        sorted_times = sorted(schedule.keys())

        # Find consecutive intervals
        consecutive_intervals = []
        current_interval = []

        for time in sorted_times:
            # Identifies consecutive intervals of time where the time difference between consecutive times is exactly 100 (which seems to represent a time slot duration).
            if not current_interval or time - current_interval[-1] == 100:
                current_interval.append(time)
            else:
                consecutive_intervals.append(current_interval)
                current_interval = [time]

        consecutive_intervals.append(current_interval)

        # Filter out non-consecutive intervals
        filtered_intervals = [interval for interval in consecutive_intervals if len(interval) > 1]

        # Create modified schedule dictionary
        modified_schedule = {'patient': entry['patient'], 'bed': entry['bed'], 'day': entry['day'], 'schedule': {}}

        if len(filtered_intervals) > 0:
            # Append only the first consecutive interval
            first_interval = filtered_intervals[0]
            for time in first_interval:
                modified_schedule['schedule'][time] = schedule[time]

        # Once all patient schedules have been processed, the function returns the modified_list, which contains the patient schedules with non-consecutive intervals removed.
        modified_list.append(modified_schedule)

    return modified_list


def remove_occupied_beds(patient_schedules_out_list, patient_schedules_in_list, bed_objects_list, multi_appt_assigned_days):
    assigned_beds = {}
    # Create a copy of the patient_schedules_in_list to avoid modifying it during iteration
    patient_schedules_in_list_copy = patient_schedules_in_list.copy()
    
    # shuffle list
    random.shuffle(patient_schedules_in_list_copy)
    
    for schedule in patient_schedules_in_list_copy:
        patient_day = str(schedule['patient']) + str(schedule['day'])
        patient = schedule['patient']
        bed = schedule['bed']
        day = schedule['day']
        schedule_data = schedule['schedule']
        
        # Check if the patient is already assigned a day
        if patient_day in assigned_beds and patient in multi_appt_assigned_days:
            # Add the patient's information to the patient_schedule_out_list
            patient_schedules_out_dict = {
                'patient': patient,
                'bed': bed,
                'day': multi_appt_assigned_days[patient] + 1,
                'schedule': schedule_data
            }
            patient_schedules_out_list.append(patient_schedules_out_dict)
            # Remove the conflicting appointment from patient_schedules_in_list
            patient_schedules_in_list.remove(schedule)

            free_up_bed_occupancy(bed, schedule_data, day, patient, bed_objects_list)
        else:
            assigned_beds[patient_day] = bed
    
    return patient_schedules_out_list, patient_schedules_in_list


def reorder_list(patient_objects_list):
    """
      Reorders the list of patient objects based on the weight value of the patient object. Patient with highest weight comes first

      Args:
        patient_objects_list: The list of patient objects.

      Returns:
        A reordered list of patient objects.
      """

    sorted_list = sorted(patient_objects_list, key=lambda patient: patient.weight, reverse=True)
    
    return sorted_list


def reserve_patient_beds_by_weight(copy_all_possible_patient_schedules, reordered_patient_object_list, bed_objects_list, patient_schedules_in_list, patient_schedules_out_list):
    """
      Uses the reordered patient list (the one by weight) and reserves the patient beds
      Args:
        patient_objects_list: The list of patient objects.

      Returns:
        A reordered list of patient objects.
      """
    for patient in reordered_patient_object_list:
        for patient_sched in copy_all_possible_patient_schedules:
            # print(patient_sched)
            # process the patients with the highest weight:
            if patient.patient_id == patient_sched['patient']:
                patient_schedules_out_dict = {}
                patient_schedules_in_dict = {}
                days = list(patient_sched['possible_allocated_schedule'].keys())
                # shuffle the days randomly
                random.shuffle(days)
                # print("this is the length ", len(patient_sched['possible_allocated_schedule']))
                for requested_day in days:
                    # print("this is the requested day ", requested_day)
                    # print("this is patient_sched['possible_allocated_schedule'][requested_day]", patient_sched['possible_allocated_schedule'][requested_day])
                    requested_sched = patient_sched['possible_allocated_schedule'][requested_day]
                    # print(patient_sched['possible_allocated_schedule'])
                    bed_id = patient_sched['bed']
                    #check_bed_availability(bed_id, requested_time_slot, requested_day)
                    # print("first if statement ", bed_id, requested_sched, " day ", requested_day, " for patient ", patient_sched['patient'])
                    if check_bed_availability(bed_id, requested_sched, requested_day, bed_objects_list) == True:
                        # print("you passed the bed availablity test") 

                        ## Add the patient's schedule to the patient_schedules_in_dict and list
                        patient_schedules_in_dict = {
                            'patient': patient_sched['patient'],
                            'bed': patient_sched['bed'],
                            'day': requested_day,
                            'schedule': patient_sched['possible_allocated_schedule'][requested_day]
                        }
                        patient_schedules_in_list.append(patient_schedules_in_dict)

                        #print(requested_sched)
                        change_bed_occupancy(bed_id, requested_sched, requested_day, patient_sched['patient'], bed_objects_list)

                        ## Remove the patient schedule from patient_schedules_out_list
                        if patient_schedules_in_dict in patient_schedules_out_list:
                            patient_schedules_out_list.remove(patient_schedules_in_dict)

                    else:
                        # bed turns out is not available so add the patient's schedule to the patient_schedules_out_dict and list
                        patient_schedules_out_dict = {
                            'patient': patient_sched['patient'],
                            'bed': patient_sched['bed'],
                            'day': requested_day,
                            'schedule': patient_sched['possible_allocated_schedule'][requested_day]
                        }
                        # if the schedule is not already in the out list, then add it to the out list
                        if patient_schedules_out_dict not in patient_schedules_out_list:
                            patient_schedules_out_list.append(patient_schedules_out_dict)
                            # print("Unfortunately this ", patient_schedules_out_dict, " could not be added the bed is not available on", requested_day)

                        # make sure to remove it from the patient_schedules_in_list
                        if patient_schedules_out_dict in patient_schedules_in_list:
                            patient_schedules_in_list.remove(patient_schedules_out_dict)

                        # make sure to free up the bed occupancy because it was previously in the in_list
                        free_up_bed_occupancy(bed_id, requested_sched, requested_day, patient_sched['patient'], bed_objects_list)
                
    return patient_schedules_out_list, patient_schedules_in_list


def set_values_patient(multi_appt_patient_objects_list, best_neighbor):
    for obj in multi_appt_patient_objects_list:
        print(obj.patient_id)
        schedule_list = []
        for patient_sched in best_neighbor:
            if obj.patient_id == patient_sched['patient']:
                schedule_entry = {}
                schedule_entry['bed'] = patient_sched['bed']
                schedule_entry['schedule'] = patient_sched['possible_allocated_schedule']
                schedule_list.append(schedule_entry)
                obj.confirmed_schedule = schedule_list
    
    return multi_appt_patient_objects_list


def SA_set_values_patient(multi_appt_patient_objects_list, best_neighbor):
    for obj in multi_appt_patient_objects_list:
        print(obj.patient_id)
        schedule_list = []
        for patient_sched in best_neighbor:
            if obj.patient_id == patient_sched['patient']:
                schedule_entry = {}
                schedule_entry['bed'] = patient_sched['bed']
                schedule_entry['schedule'] = patient_sched['schedule']
                schedule_list.append(schedule_entry)
                obj.confirmed_schedule = schedule_list
    
    return multi_appt_patient_objects_list


def check_occupied_beds(patient_schedules_in_list, bed_objects_list):
    """
      Check that the beds that I marked as occupied are really occupied in the bed_objects_list

      Args:
        patient_schedules_in_list (list): list of patient objects
        bed_objects_list (list): list of patient objects

      Returns:
        
    """
    # Given patient_schedule_list and bed_schedule_dict

    for patient_schedule in patient_schedules_in_list:
        patient_day = patient_schedule['day']
        patient_bed = patient_schedule['bed']
        patient_name = patient_schedule['patient']
        patient_schedule_times = patient_schedule['schedule']
        for bed in bed_objects_list: 
            for bed_sched in bed.bed_schedule:
                # Find the corresponding day in the bed schedule
                if patient_day in bed_sched:
                    bed_day_schedule = bed_sched[patient_day]

                    # Update the bed schedule with patient name for each time slot
                    for time_slot, value in patient_schedule_times.items():
                        if value != 0:  # Assuming non-zero value indicates the patient is scheduled
                            bed_day_schedule[time_slot] = patient_name


def check_occupied_beds(patient_schedules_in_list, bed_objects_list):
    """
      Check that the beds that I marked as occupied are really occupied in the bed_objects_list

      Args:
        patient_schedules_in_list (list): list of patient objects
        bed_objects_list (list): list of patient objects

      Returns:
        
    """
    # Given patient_schedule_list and bed_schedule_dict
    for bed in bed_objects_list:
        for patient_schedule in patient_schedules_in_list:
            patient_day = patient_schedule['day']
            patient_name = patient_schedule['patient']
            patient_schedule_times = patient_schedule['schedule']
            patient_bed = patient_schedule['bed']
            # print("THIS IS THE BED_ID", bed.bed_id)
            if patient_day in bed.bed_schedule and bed.bed_id == patient_bed:
                for time_slot, value in patient_schedule_times.items():
                    if time_slot in bed.bed_schedule[patient_day]:
                        # Check if the time slot is not occupied
                        if bed.bed_schedule[patient_day][time_slot] == 0:
                            bed.bed_schedule[patient_day][time_slot] = patient_name
                            # print("Bed", bed.bed_id, "Day", patient_day, "Time Slot", time_slot, "Assigned to", patient_name)