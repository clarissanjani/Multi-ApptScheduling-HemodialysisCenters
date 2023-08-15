def calculate_objective_function(patient_id, confirmed_schedule, weight, leftover, prescribed_total_dialysis_hours, num_required_dialysis_sessions, num_patients, max_allowed_deviation): 
    # print(patient_id)
    # print(confirmed_schedule)
    # print("Weight is ", weight, " and the penalty is ", count_penalty(leftover), "the prescribed dialysis hours is ", prescribed_total_dialysis_hours)
    # print("The number of confirmed time slots is ", len(confirmed_schedule), " and the total confirmed hours is ", count_total_confirmed_hours(confirmed_schedule))
    first_term_result = get_first_term(weight, leftover, num_required_dialysis_sessions, num_patients, max_allowed_deviation)
    second_term_result, confirmed_total_dialysis_hours = get_second_term(weight, prescribed_total_dialysis_hours, confirmed_schedule, prescribed_total_dialysis_hours)
    
    num_confirmed_timeslots = len(confirmed_schedule)
    obj_function_inc = first_term_result + second_term_result
    count_one = 0
    count_two = 0
    count_three = 0
    count_zero = 0
    
    if len(confirmed_schedule) == 1:
        count_one = 1
    elif len(confirmed_schedule) == 2:
        count_two = 1
    elif len(confirmed_schedule) == 3:
        count_three = 1
    elif len(confirmed_schedule) == 0:
        count_zero = 1
        
    # print("this is from  calculate_obj_function", obj_function_inc, num_confirmed_timeslots, count_one, count_two, count_three, count_zero)
        
    return obj_function_inc, num_confirmed_timeslots, count_one, count_two, count_three, count_zero, confirmed_total_dialysis_hours

def get_first_term(weight, leftover, num_required_dialysis_sessions, num_patients, max_allowed_deviation):
    return weight * count_penalty(leftover, num_required_dialysis_sessions, num_patients, max_allowed_deviation)

def get_second_term(weight, prescribed_total_diaylsis_hours, confirmed_schedule, prescribed_total_dialysis_hours):
    hour_diff = prescribed_total_dialysis_hours - count_total_confirmed_hours(confirmed_schedule)
    confirmed_total_dialysis_hours = count_total_confirmed_hours(confirmed_schedule)
    
    if hour_diff < 0: 
        multiplier = 0
    else:
        multiplier = hour_diff
    
    return weight * multiplier, confirmed_total_dialysis_hours



# TODO CHANGE THE DOCSTRING
def count_leftover_appointments(num_allocated_appointments, num_required_dialysis_sessions):
    """
    The function is to create patient profiles for each of the patients

    Args:
        patient_number (int): The length of the rectangle

    Returns:
        patient_profile_dict (dict): Return a dictionary of patient profiles with the patient number, 
        ideal schedule, priority and weight
    """
    # beta_j is the total number of leftover appointmnets
    return num_required_dialysis_sessions - num_allocated_appointments


# count penalty
def count_penalty(num_leftover_appointments, num_required_dialysis_sessions, num_patients, max_allowed_deviation):
    # the number of leftover appointmnets are 0, then there is no penalty
    if num_leftover_appointments == 0:
        penalty = 0
    else:
        penalty = (num_required_dialysis_sessions * num_patients * max_allowed_deviation) ** num_leftover_appointments
    
    return penalty


def count_total_confirmed_hours(patient_sched):
    total_hours = 0

    for schedule in patient_sched:
        schedule_hours = len(schedule['schedule'])
        total_hours += schedule_hours

    return total_hours