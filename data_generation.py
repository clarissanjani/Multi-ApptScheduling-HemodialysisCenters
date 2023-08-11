## Instal packages
import random

## Declare some variables
## VARIABLES RELATED TO THE WEIGHT
# priority weights, key = ζ chance of having priority, value = w weight in the objecive function
priority_weights = {0.6: 1, 0.25: 1.4, 0.15: 2}
# weight list already predefined based on  Reihaneh's data generation scheme. Based on the priority assigned, the patient gets the
# corresponding weight
weights_list = [1, 1.4, 2]

## VARIABLES FOR GENERATING THE DICTIONARY OF PATIENT AND BED AVAILABILITIES
# give higher preference to giving availability so generating 1
not_available = 0
available = 1

probabilities_availability = [0.8, 0.2]

random_number = random.choices([available, not_available], probabilities_availability)[0]

def generate_patient_random_priority(num_patients, priority, probabilities):
    """
    Generate priority of patients based on the probability of getting a certain priority. This will determine the
    priority in the queue in the simulated annealing approach
 
    Args: 
        num_patients (int) : integer defining the number of patients
        priority (list) : list consisting of 1, 2, 3 which corresponds to the priority that the person gets assigned
        probabilities (list) : list of probabilities that define how likely a patient is to get priority 1, 2, or 3

    Returns:
        A list of priorities that were assigned based on the priorities of getting them. Each item in the list corresponds to a patient
    """
    # assign patient weights randomly based on the probabilities for all the patients in scope
    random_priority = random.choices(priority, probabilities, k=num_patients)
    return random_priority

def generate_prescribed_dialysis_hours(num_patients):
    """
    Generate a list of prescribed dialysis hours for patients

    Args: 
        num_patients (int) : integer defining the number of patients

    Returns:
        A list of prescribed dialysis hours for all the patients that will then be assigned to each patient profile
    """
    prescribed_dialysis_hours_list = []

    for i in range(0, num_patients):
        prescribed_dialysis_hours = random.randint(3, 5) * 3
        prescribed_dialysis_hours_list.append(prescribed_dialysis_hours)

    return prescribed_dialysis_hours_list


def generate_available_time_slots(num_slots_per_day, num_of_slots_per_hour):
    """
    Generate time slots based on the number of time slots per day

    Args: 
        num_slots_per_day (int): 14 hours * number of slots per hour
        num_slots_per_hour (int): Number of slots per hour, 1 if each slot is an hour, 2 if each slot is 30 mins, etc

    Returns:
        A list of available time slots based on the number of slots per day and number of slots per hour
    """

    # define a the list of open time slots based on the num of slots per hour.
    available_time_slot_list = []

    # start at 8 am and end after 14 hours
    start = 8
    end = 8 + 14

    # for i in the range of the start time till the max number of time slots
    for i in range(start, int(start + num_slots_per_day / num_of_slots_per_hour)):
        # add the top of the hours

        # if there is only one slot per hour then just concentrate on adding 00 to the end
        if num_of_slots_per_hour == 1:
            available_time_slot = int(str(i) + str("00"))
            available_time_slot_list.append(int(available_time_slot))
        else:
            available_time_slot_list.append(int(str(i) + str("00")))
            # for j in the range of the number of max time slots per hour
            for j in range(1, num_of_slots_per_hour):
                # add everything else thats not between the top of the hours eg not in between 8:00 and 9:00
                minute_of_hour = int((j / num_of_slots_per_hour) * 60)
                available_time_slot = int(str(i) + str(minute_of_hour))
                available_time_slot_list.append(int(available_time_slot))

    # add the final end time
    available_time_slot_list.append(int(str(end) + str("00")))

    return available_time_slot_list


def create_empty_availability_dict(available_time_slot_list):
    """
    Create the dictionary of patient and bed availabilities

    Args:

    Returns:
        availability_dict (dictionary): A dictionary of the availabilities marked as 0 or 1 for
        the possible available time slots for the bed and patient
    """
    # create an empty dictionary that will be used to populate with the patient's availability based on the defined time slots
    availability_dict = {}

    # define as 1 or 0 for all available open time slots
    for i in available_time_slot_list:
        # define patient availability as 0 or 1 and add to dictionary
        availability = random.randint(0, 1)
        # create entry in dictionary to match the open time slot and the patient availability
        availability_dict[i] = availability

    return availability_dict


def create_empty_bed_availability_dict(available_time_slot_list):
    """
    Create the dictionary of bed availabilities with all starting at 0

    Args:

    Returns:
        availability_dict (dictionary): A dictionary of the availabilities marked as 0 for
        the possible available time slots for the bed
    """
    # create an empty dictionary that will be used to populate with the patient's availability based on the defined time slots
    availability_dict = {}

    # define as 1 or 0 for all available open time slots
    for i in available_time_slot_list:
        # define patient availability as 0 or 1 and add to dictionary
        availability = 0
        # create entry in dictionary to match the open time slot and the patient availability
        availability_dict[i] = availability

    return availability_dict


def create_bed_profile(bed_number, available_time_slot_list):
    """
    The function is to create patient profiles for each of the patients

    Args:
        patient_number (int): The length of the rectangle

    Returns:
        patient_profile_dict (dict): Return a dictionary of patient profiles with the patient number,
        ideal schedule, priority and weight
    """
    bed_profile_dict = {}
    bed_availability_dict = {}

    # add the bed's name
    bed_profile_dict['bed'] = "b" + str(bed_number + 1)

    # add the ideal schedule of the bed to the dictionary for six days of the week
    for i in range(1, 7):
        # create the patient_availability_dict based on the function
        bed_empty_availability_dict = create_empty_bed_availability_dict(available_time_slot_list)
        # the key is the day number
        bed_availability_dict[i] = bed_empty_availability_dict

    bed_profile_dict['bed_availability'] = bed_availability_dict

    return bed_profile_dict


def create_patient_profile(patient_number, available_time_slot_list, random_priority, prescribed_dialysis_hours_list):
    """
    The function is to create patient profiles for each of the patients

    Args:
        patient_number (int): The length of the rectangle

    Returns:
        patient_profile_dict (dict): Return a dictionary of patient profiles with the patient number,
        ideal schedule, priority and weight
    """
    patient_profile_dict = {}
    patient_availability_dict = {}

    # add the patient's name
    patient_profile_dict['patient'] = "p" + str(patient_number + 1)

    # add the ideal schedule of the patient to the dictionary for six days of the week
    for i in range(1, 7):
        # create the patient_availability_dict based on the function
        patient_empty_availability_dict = create_empty_availability_dict(available_time_slot_list)
        patient_availability_dict[i] = patient_empty_availability_dict

    # add the priority of the patient
    patient_profile_dict['priority'] = random_priority[patient_number]

    # get the value of the weight from taking the random priority - 1 which then gives you the index from the weights list
    patient_profile_dict['weight'] = weights_list[random_priority[patient_number] - 1]

    patient_profile_dict['prescribed_dialysis_hours'] = prescribed_dialysis_hours_list[patient_number]

    patient_profile_dict['patient_availability'] = patient_availability_dict

    return patient_profile_dict