Advanced Seminar Operations & Supply Chain Management: Operations Research
==============================
Chronic kidney disease (CKD) is a long-term (chronic) condition that affects the kidneys. The kidneys are two bean-shaped organs that are located below the ribcage. They filter waste products from the blood and help to regulate blood pressure, red blood cell production, and other important functions. When you have CKD, your kidneys gradually lose their ability to function properly. This can lead to a buildup of waste products in the blood, which can cause a variety of health such as fatigue, trouble sleeping, and shortness of breath.

This seminar paper implements the FCFS approach, as well as the simulated annealing algorithm as an alternative to the approach of Reihaneh et al. which used the branch and bound algorithm. I compare both the FCFS and simulated annealing approach to that of what Reihaneh et al. did. The goal of this paper is to explore a simpler approach using a metaheuristic such as simulated annealing to produce a less optimal solution, but with better computational efficiency in cases of larger populations. The goal was achieved in the case of simulated annealing, and as expected the solution was not as good as that of Reihaneh et al. paper.

## Project Details
**Description**: As part of seminar course at Technical University of Munich, I have created this Github repository. Further technical details of the project can be seen below. 

----

## Environment
The project was developed with Python 3.9. I used Pycharm as the IDE as well as used JupyterLab to run the notebooks. It is possible to run the notebooks also on Jupyter Notebook.

## Project Structure
Each task has its own separate folder structure with the relevant JupyterLab / Jupyter Notebook and python scripts. All the scripts are being called in the Jupyter notebook. 

 ------------
     ├── README.md                        
     ├── Anjani_SimulatedAnnealing.ipynb
     ├── Anjani_FCFS.ipynb
     ├── calculate_value.py
     ├── data_generation.py
     ├── matched_availability.py
     ├── schedule_appointment.py
     └── .gitignore

The description of the efiles are as follows
  - **Anjani_FCFS.ipynb**: Jupyter notebook that implements the whole FCFS apporach in hemodialysis centers
  - **Anjani_SimulatedAnnealing.ipynb**: Jupyter notebook that implemetns only the simulated annealing concept
  - **calculate_value.py**: Script used to calculate the values related to the objective function
  - **data_generation.py**: Script used to generate the data on the patients and beds
  - **matched_availability.py**: Script used to match availability of the patients and the beds
  - **schedule_appointment.py**: Script used to perform anything related to scheduling appoitnemtns including making any changes to the patients and beds schedule, as well as checking the feasibility of the schedule

## How to access the file

To run the file, run the following in the folder directory if using Jupyter Notebook in the terminal. 

```
jupyter notebook
```

To run the file, run the following in the folder directory if using JupyterLab in the terminal. 

```
jupyter-lab
```

### Running the First-Come-First-Serve Approach
1. Change the values of num_beds, num_patients, and max allowed deviation  (n,m,δ) 
2. Run the code all the way to just before it reaches no 6
3. In no 6, the graphs for further analysis can be generated. Make sure to follow the instructions on the part of the code that should be commented out which can be seen below. Only when the data is initially empty should the following code be active, and in other cases it should be commented out. 

```
parameter_tuning_df = []
parameter_tuning_df  = pd.DataFrame(columns=parameter_tuning_tbl_initial_rows)
```
4. Run step 6 until the end to see all the graphs that you were able to generate

### Running the Simulated Annealing Approach

----

## Known issues

Document any known significant shortcomings with the software.

## Getting help

For any issues related to the software, please feel free to contact e.clarissa.anjani@tum.de

----

## Credits and References
Reihaneh, M., Ansari, S., & Farhadi, F. (2023). Patient appointment scheduling at hemodialysis centers: An exact branch and price approach. In European Journal of Operational Research (Vol. 309, Issue 1, pp. 35–52). Elsevier BV. https://doi.org/10.1016/j.ejor.2023.01.024
