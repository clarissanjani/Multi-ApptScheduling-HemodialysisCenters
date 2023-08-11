# define a class to generate set of m patient objects
class patient: 
    def __init__(self, patient_id, prescribed_total_dialysis_hours, processing_time, ideal_schedule, confirmed_schedule, weight, leftover):
        self.patient_id = patient_id
        # Total dialysis hours prescribed for j
        self.prescribed_total_dialysis_hours = prescribed_total_dialysis_hours 
        # processing time: the patient’s check-in time, put-on time on a dialysis machine (a technician puts the patient on a bed (or a chair), and connects them to the dialysis machine), 
        # dialysis time on the dialysis machine, and take-offtime (a technician takes the patient off the bed, disconnects them from the dialysis machine and cleans the bed).
        self.processing_time = processing_time 
        # ideal time slots for starting dialysis sessions
        self.ideal_schedule = ideal_schedule
        # set of feasible time slots for j
        self.confirmed_schedule = confirmed_schedule
        # weight of patient j in objective function
        self.weight = weight 
        # Number of leftover appointments of j
        self.leftover = leftover 
        
    def __str__(self):
        return f"{self.patient_id}"  # for debug mode
    
    def add_confirmed_schedule(confirmed_schedule):
        self.confirmed_schedule.append(confirmed_schedule)
        
    def calculate_schedule_length(self):
        return len(self.confirmed_schedule)
    

# define a class to generate set of n identical bed objects
class bed:
    def __init__(self, bed_id, bed_schedule):
        self.bed_id = bed_id
        self.bed_schedule = bed_schedule
    
    def __str__(self):
        return f"{self.bed_id}"  # for debug mode
 


class FCFS_confirmed_schedule:
    def __init__(self, patient_schedules_in, patient_schedules_out, objective, contribution, penalty):
        # patient schedules that work out are stored inside
        self.patient_schedules_in = patient_schedules_in
        # patient schedules that did not work out get stored outside
        self.patient_schedules_out = patient_schedules_out
        # objective function value to minimize
        self.objective = objective
        # contribution of a_j to the value of the objective function 
        self.contribution = contribution
        # dual value associated with Constraint 2c TODO: IS THIS NEEDED? Constraint (2c) 
        # restricts the number of available beds to n .
        # self.lambda_dual = lambda_dual
        # penalty
        self.penalty = penalty 
    
    
    ## NOT NEEDED?
    def copy_FCFS_confirmed_schedule(self):
        new_FCFS_confirmed_schedule = FCFS_confirmed_schedule()
        new_patient_id = copy.deepcopy(patient_id)
        new_patient_schedules_in = copy.deepcopy(self.patient_schedules_in)
        new_patient_schedules_out = copy.deepcopy(self.patient_schedules_out)
        new_allocation_objective = self.objective
        new_allocation_contribution = self.contribution
        # new_lambda_dual = self.lambda_dual
        new_penalty = self.penalty
        return new_FCFS_confirmed_schedule
    
    ## NOT NEEDED?
    def add_time_slot(self, time_slot):
        """
        add possible time slot to the schedule
        """
        # update to the schedules
        self.patient_schedules_in.add(time_slot)
        self.patient_schedules_out.remove(time_slot)
        
    
    ## NOT NEEDED?
    def remove_time_slot(self, time_slot):
        """
        remove time slot from the schedule
        """
        # add the item to the knapsack and update the capacity left, objective and sets
        self.patient_schedules_in.remove(time_slot)
        self.patient_schedules_out.add(time_slot)
    
    ## NOT NEEDED?
    def set_binary_z_0(self, binary_z):
        """
        set binary_z to 0 if it schedule is NOT according to a_j
        """
        self.binary_z = 0
    
    ## NOT NEEDED?
    def set_binary_z_1(self, binary_z):
        """
        set binary_z to 1 if schedule is according to a_j
        """
        self.binary_z = 1
    
    ## NOT NEEDED?
    def make_feasible(self, time_slot):
        """
        remove time slot that is not feasible
        """
        if check_if_feasible == False:
            self.FCFS_confirmed_schedule.remove_time_slot(time_slot)
        
    ## NOT NEEDED?
    def check_if_feasible(self):
        """
        if it is feasible with the schedule of the patients
        """
        # another patient does not currently stay there
    