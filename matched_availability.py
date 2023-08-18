
   
"""
    Functions related to matching the availability of the patient and the bed for scheduling appointments
"""


def match_bed_patient_availability(all_patients_availability_list, all_beds_availablity_list):
    all_patients_matched_availability = []

    # Loop through the patients
    for dict2 in all_patients_availability_list:
        patient_matched_availability = {}
        patient_matched_availability['patient'] = dict2['patient']
        print(patient_matched_availability['patient'])

        # Loop through the days of the week
        for day in range(1, 7):
            print("day ", day)

            matched_availability = {}  # Initialize matched availability dictionary for each day
            empty_matched_availability = {}

            # Loop through the values in the bed_schedule and ideal_schedule
            for dict1 in all_beds_availablity_list:
                bed_availability = dict1['bed_availability']
                bed_id = dict1['bed']

                for key, patient_availability in dict2['patient_availability'][day].items():
                    bed_availability_value = bed_availability[day].get(key, None)

                    if bed_availability_value is not None and patient_availability == bed_availability_value == 0:
                        matched_availability.setdefault(day, {})
                        matched_availability[day][key] = bed_availability_value
                        empty_matched_availability[day] = matched_availability[day]

                # Assign matched availability for each bed separately
                patient_matched_availability_bed = patient_matched_availability.copy()
                patient_matched_availability_bed['bed'] = bed_id
                patient_matched_availability_bed['matched_availability'] = empty_matched_availability

                all_patients_matched_availability.append(patient_matched_availability_bed)
    
    return all_patients_matched_availability

def get_combination_patients_beds(all_patients_matched_availability):
    consolidated_dict = {}

    # Iterate over each entry in the original list
    for entry in all_patients_matched_availability:
        patient = entry['patient']
        bed = entry['bed']
        matched_availability = entry['matched_availability']

        # Create a unique key for each bed-patient combination
        key = f"{bed}-{patient}"

        # Check if the key already exists in the consolidated dictionary
        if key in consolidated_dict:
            # If the key exists, update the matched_availability for the corresponding patient and bed
            consolidated_dict[key]['matched_availability'].update(matched_availability)
        else:
            # If the key doesn't exist, create a new entry in the consolidated dictionary
            consolidated_dict[key] = {
                'patient': patient,
                'bed': bed,
                'matched_availability': matched_availability
            }
    
    return consolidated_dict


def allocate_single_appointment_schedule(single_patient_matched_availability_dict):
    """
    The function allocates the single appointment schedules based on the 3 - 5 consecutive values of 0 (which indicates availability) of the matched availability of the bed and patient
    I define that it the schedule must match 3 - 5 times consecutively because that means that both patient and bed is free for 3 - 5 hours, thus it would be possible to schedule a
    dialysis treatment

    Args:
        single_patient_matched_availability_dict (dict): matched availability of a patient and a bed

    Returns:
        consecutive_zeroes (dict): Return a dictionary where the matched availability of the patient and bed is consecutive for between 3 - 5 times
    """
    consecutive_zeros = {}
    consecutive_count = 0
    temp_dict = {}
    last_day = None
    last_time = None

    for day, availability in single_patient_matched_availability_dict.items():
        # Iterate through each day and availability
        # day, availability == 3 {1500: 0, 2100: 0, 2200: 0, 900: 0, 1000: 0, 1100: 0, 1200: 0, 1700: 0, 1800: 0, 1900: 0}
        for time, value in availability.items():
            # If the availability value is 0 (indicating availability)
            if value == 0:
                # If it's the first time, or the time is consecutive to the last processed time
                if last_day is None or last_time is None or (day == last_day and time == last_time + 100):
                    consecutive_count += 1
                    # Add the time to the temporary dictionary
                    temp_dict[time] = 0
                else:
                    # If the consecutive count is between 3 and 5 (inclusive)
                    if consecutive_count >= 3 and consecutive_count <= 5:
                        # Create a new dictionary for the day if it doesn't exist
                        if last_day not in consecutive_zeros:
                            consecutive_zeros[last_day] = {}
                        # Update the consecutive zeros for the day
                        consecutive_zeros[last_day].update(temp_dict)
                    # Start a new count for the current time slot
                    consecutive_count = 1
                    # Reset the temporary dictionary with the current time slot
                    temp_dict = {time: 0}
            else:
                # If the consecutive count is between 3 and 5 (inclusive)
                if consecutive_count >= 3 and consecutive_count <= 5:
                    if last_day not in consecutive_zeros:
                        # Create a new dictionary for the day if it doesn't exist
                        consecutive_zeros[last_day] = {}
                    # Update the consecutive zeros for the day
                    consecutive_zeros[last_day].update(temp_dict)
                # Reset the consecutive count
                consecutive_count = 0
                # Reset the temporary dictionary
                temp_dict = {}
            # Update the last processed day
            last_day = day
            # Update the last processed time
            last_time = time

    if consecutive_count >= 3 and consecutive_count <= 5:
        # If there are consecutive zeros at the end of the iteration
        if last_day not in consecutive_zeros:
            # Create a new dictionary for the day if it doesn't exist
            consecutive_zeros[last_day] = {}
        # Update the consecutive zeros for the day
        consecutive_zeros[last_day].update(temp_dict)

    print(consecutive_zeros)
    return consecutive_zeros