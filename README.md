Advanced Seminar Operations & Supply Chain Management: Operations Research
==============================
Chronic kidney disease (CKD) is a long-term (chronic) condition that affects the kidneys. The kidneys are two bean-shaped organs that are located below the ribcage. They filter waste products from the blood and help to regulate blood pressure, red blood cell production, and other important functions. When you have CKD, your kidneys gradually lose their ability to function properly. This can lead to a buildup of waste products in the blood, which can cause a variety of health such as fatigue, trouble sleeping, and shortness of breath.

## Project Details
**Description**: As part of seminar course at Technical University of Munich, I have created a final report included in this Git repository, with the code accompanied. Further technical details of the project can be seen below. 

----

## Environment
The project was developed with Python 3.9. I used Pycharm as the IDE as well as used JupyterLab to run the notebooks. It is possible to run the notebooks also on Jupyter Notebook.

## Project Structure
Each task has its own separate folder structure with the relevant JupyterLab / Jupyter Notebook and python scripts. All the scripts are being called in the Jupyter notebook. 

 ------------
     ├── README.md                        
     ├── Anjani_SimulatedAnnealingCode.ipynb
     ├── calculate_value.py
     ├── data_generation.py
     ├── matched_availability.py
     ├── schedule_appointment.py
     └── .gitignore

The description of the efiles are as follows
  - **Anjani_SimulatedAnnealingCode.ipynb**: Main Jupyter notebook for running both the FCFS and simulated annealing approach. The Jupyter notebook calls the other scripts
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
## Running the code

### Running the First-Come-First-Serve Approach

### Running the Simulated Annealing Approach

### Running the Visualizations

----

## Known issues

Document any known significant shortcomings with the software.

## Getting help

Instruct users how to get help with this software; this might include links to an issue tracker, wiki, mailing list, etc.

----

## Credits and References
Reihaneh, M., Ansari, S., & Farhadi, F. (2023). Patient appointment scheduling at hemodialysis centers: An exact branch and price approach. In European Journal of Operational Research (Vol. 309, Issue 1, pp. 35–52). Elsevier BV. https://doi.org/10.1016/j.ejor.2023.01.024
