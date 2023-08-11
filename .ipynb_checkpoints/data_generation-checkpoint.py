import random

## Declare some variables
## VARIABLES RELATED TO THE WEIGHT
# priority weights, key = ζ chance of having priority, value = w weight in the objecive function
priority_weights = {0.6: 1, 0.25: 1.4, 0.15: 2}
# weight list already predefined based on  Reihaneh's data generation scheme. Based on the priority assigned, the patient gets the
# corresponding weight
weights_list = [1, 1.4, 2]

# define the priority that the patient should bea ssigned and the probability of the patient getting them
priority = [1,2,3]
probabilities = [0.6, 0.25, 0.15]

def generate_patient_random_priority(num_patients):
    # assign patient weights randomly based on the probabilities for all the patients in scope
    random_priority = random.choices(priority, probabilities, k=num_patients)
    return random_priority

def generate_prescribed_dialysis_hours(num_patients):
    prescribed_dialysis_hours_list = []

    for i in range(0, num_patients):
        prescribed_dialysis_hours = random.randint(3, 5) * 3
        prescribed_dialysis_hours_list.append(prescribed_dialysis_hours)

    return prescribed_dialysis_hours_list

def generate_available_time_slots(num_slots_per_day, num_of_slots_per_hour):
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
