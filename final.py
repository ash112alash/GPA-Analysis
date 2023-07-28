###########################################################################################################
# START OF IMPORTS AND SETTINGS
###########################################################################################################

# import libraries needed for this program
import csv, numpy as np, pandas as pd, matplotlib.pyplot as plt
from scipy.stats import linregress

# adjust display settings for DataFrame to show more rows and columns from it
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

###########################################################################################################
# END OF IMPORTS AND SETTINGS
###########################################################################################################


###########################################################################################################
# START OF MENU OPTIONS 1 THRU. 8
###########################################################################################################  

# function name: overview
# arguments: none
# return: none
# description: outputs an overview of your topic and data set
def overview():
    print('\n####################################################################################################################')
    print('\t\t\t\t\tSleepStudy\n')
    print("SleepStudy includes data that was collected from a study of sleep patterns of 254 college students. To collect data of college students, a sample of students completed skills tests to measure cognitive function, completed a survey that asked many questions about attitudes and habits, and kept a sleep diary to record time and quality of sleep over a two week period. The dataset includes data on college students' number of drinks per week, happiness score and depression status, etc. ")
    print('')
    print("""GPA: Grade point average (0-4 scale)
PoorSleepQuality: Measure of sleep quality (higher values are poorer sleep)
StressScore: Measure amount of stress
Stress: Coded stress score: normal or high
AlcoholUse: Self-reported: Abstain, Light, Moderate, or Heavy
          """)
    print('\n####################################################################################################################\n')

###########################################################################################################
# END OF MENU OPTIONS 1 THRU. 8
###########################################################################################################    


###########################################################################################################
# START OF GETTING AND CHECKING USER INPUT CHOICE(S)
########################################################################################################### 

# function name: check_choice
# arguments: 2 integer values representing the minimum and maximum numbered options in the menu
# return: the valid input (i.e., a positive digit between the passed minimum and maximum arguments)
# description: asks the user for their choice and then checks that the user's input is a valid digit 
#              between the minimum and maximum arguments passed to it 
#              it keeps asking the for input until the user enters valid input (i.e., a positive digit 
#              between between the passed minimum and maximum arguments)
def check_choice(minimum, maximum):
    # define string variable that is empty to hold user's input
    some_input = ''
    
    # loop until the user's input is no longer empty
    while some_input == '':
        # ask the user to input their choice and store in a variable
        some_input = input('Choice: ')
        
        # check if the user's input does not contain only digits
        if some_input.isdigit() == False:
            # output an error message stating that the user did not enter input with only digits
            print('\nYou did not enter input with only digits! Try again.\n')
        
        # otherwise (i.e., the user's input contains only digits)
        else:
            # convert the user's input to an integer
            # "1" --> 1
            some_input = int(some_input)

            # check if the user's input is less than the minimum or greater than the maximum
            if some_input < minimum or some_input > maximum:
                # output an error message stating that the user did not enter input between 1 and 5
                print('\nYou did not enter a valid choice. Choose any option from ' + str(minimum) + ' to ' + str(maximum) + '.\n')
    
    # return the user's input 
    return some_input


# function name: get_choice
# arguments: none
# return: the valid input (i.e., a positive digit between 1 and 5)
# description: outputs the list of five choices for the main menu and calls the check_choice function 
#              passing it 1 as the minimum and 5 as the maximum to obtain a valid input from the user 
def get_choice():
    # output the list of options the user can choose from
    # choice 1 --> Overview of the [YOUR DATA SET NAME] Data Set
    # choice 2 --> Data-Driven Questions and Predictions
    # choice 3 --> Basic Statistics on [YOUR DATA SET NAME]
    # choice 4 --> Simple Data Visualizations on [YOUR DATA SET NAME]
    # choice 5 --> Survey Analysis
    # choice 6 --> Data Set Analysis
    # choice 7 --> Findings and Observations
    # choice 8 --> Quit
    print('Choose one of the options below to view the data analysis for this data set and its data-driven question.\n')    
    
    print('1. Overview of the SleepStudy Data Set')
    print('2. Data-Driven Questions and Predictions')
    print('3. Basic Statistics on SleepStudy')
    print('4. Simple Data Visualizations on SleepStudy')
    print('5. Survey Analysis')
    print('6. Data Set Analysis')
    print('7. Findings and Observations')
    print('8. Quit.\n')
    
    
    # call the check_choice function passing it 1 as the minimum and 8 as the maximum
    #      store the returned value in a variable
    choice = check_choice(1, 8)
     
        
    # return the user's input that was stored in the variable above
    return choice

###########################################################################################################
# END OF GETTING AND CHECKING USER INPUT CHOICE(S)
########################################################################################################### 



###########################################################################################################
# Start of Data Driven Questions
###########################################################################################################
def dq():
    print("""Question 1: 
Should a student prioritize sleep to earn a higher GPA? 
Prediction: 
I predict that a student who sleeps longer will have a higher GPA score because research reports have stated that a good night's sleep helps increase academic performance.

Question 2: 
Does drinking alcohol decrease GPA?
Prediction:
I predict that drinking alcohol more will decrease GPA because research articles mention that alcohol has a negative effect on GPA. 

Question 3:
Will a high stress score decrease GPA?
Prediction:
I believe that a stressed student isn't able to focus, so, I predict that the more stressed the student, the lower the GPA will be.

    """)

###########################################################################################################
# End of Data Driven Questions
###########################################################################################################



###########################################################################################################
# Start of Basic Data Statistics
###########################################################################################################
    
def option1():
    Brown_Uni_GPA = 3.71
    Stanford_Uni_GPA = 3.66
    print('The combined Average GPA of students studying in Brown and Stanford University is:', ((Brown_Uni_GPA+Stanford_Uni_GPA)/2), "\n")

    
def option2():
    Virginia_GPA = 3.36
    Florida_GPA = 3.32
    print('The combined Average GPA of students studying in Florida and Virginia is:', ((Virginia_GPA+Florida_GPA)/2),"\n")
    
def option3():
    Male_GPA = 2.9
    Female_GPA = 3.1
    print('The average GPA of Students in the United States is:', float((Male_GPA+Female_GPA)/2),"\n")
    
def option4():
    HS_GPA = 3.36
    College_GPA = 2.7
    print('The difference between High school GPA and College GPA in the United States is:', round(((HS_GPA+College_GPA)/2),2),"\n")

    
def basic_stats():
    print("\t\t\t\t SleepStudy Basic Stats")
    print("""I used statistics from the following website because it contained a lot of useful statistics on GPA in the United States. https://www.daniel-wong.com/average-gpa/
Also, I used data that was collected at Brown University, Stanford University, male students, female students, high school students, college students, and students studying in Florida and Virginia. I used these data because I wanted to see data from around the United States instead of one or two areas.\n""")

    
    choice = ''
    while choice != 5:
        print("""Choose one of the following numbered options to view data on GPA. 
        1. The combined Average GPA of students studying in Brown and Stanford University.
        2. The combined Average GPA of students studying in Florida and Virginia.
        3. The average GPA of Students in the United States. 
        4. The difference between High school GPA and College GPA in the United States.
        5. Back to main menu
        """)
        
        choice = check_choice(1,5)
        
        if choice == 1:
            option1()
        elif choice == 2:
            option2()
        elif choice == 3:
            option3()
        elif choice == 4:
            option4()
        elif choice == 5:
            print('Sending back to main menu')
        
###########################################################################################################
# End of Basic Data Statistics
###########################################################################################################




###########################################################################################################
# Start of Simple Visualizations
###########################################################################################################


def scatter_visual(x,y):        
    plt.scatter(x, y)
    plt.title("Average High School GPA By Ethnicity")
    plt.xlabel("Ethnicity")
    plt.ylabel("Average GPA")
    
    plt.yticks([2.6,2.7,2.8,2.9,3.0,3.1,3.2,3.3])
    
    plt.show()
    
def line_visual(x,y):
    plt.plot(x, y)
    plt.title("Average High School GPA Since 1990")
    plt.xlabel("Year")
    plt.ylabel("Average GPA")
    
    plt.xticks([1990,1995,2000,2005,2010,2015,2021])
    plt.yticks([2.6,2.7,2.8,2.9,3.0])
    
    plt.show()
    
    
def bar_visual(x,y):
    plt.bar(x, y)
    plt.title("Average High School GPA By Course")
    plt.xlabel("Course")
    plt.ylabel("Average GPA")
    
    plt.show()
    
    
def pie_visual(label_pie, scores):
    plt.pie(scores, labels = label_pie)
    plt.title("Should You Prioritze Sleep to Earn a Higher GPA")
    plt.legend(bbox_to_anchor=(1, 0, 0.75, 0.75),loc = 'upper right')
    plt.show()
    

def minimum_val(some_list):
    minimum = some_list[0]
    for i in some_list:
        if i < minimum:
            minimum = i
    return minimum

def maximum_val(some_list):
    maximum = some_list[0]
    for i in some_list:
        if i > maximum:
            maximum = i
    return maximum

def average_val(some_list):
    total = 0.0
    for i in some_list:
        total += i
    average = total/len(some_list)
    return average
    
def simple_visualizations():
    print("\t\t\t\t SleepStudy Visualizations")
    print("For the first three graphs, the data that I used was collected from this website https://www.prosperityforamerica.org/average-high-school-gpa/#ftoc-heading-9. For the pie chart, I collected the data from my online survey because I wanted to include a graph that I collected.")
    
    choice = ''
    while choice != 5:
        print("""Choose one of the following numbered options to view visualizations of GPA Factors. 
        1. Scatter Chart: Average High School GPA By Ethnicity.
        2. Line Chart: Average High School GPA Since 1990.
        3. Bar Chart: Average High School GPA By Course.
        4. Pie Chart: Should You Prioritze Sleep to Earn a Higher GPA?
        5. Back to main menu
        """)
        
        choice = check_choice(1,5)
        
        if choice == 1:
            x_scatter = ["Black","Hispanic","White","Asian/Pacific"]
            y_scatter = [2.69,2.84,3.09,3.26]
            scatter_visual(x_scatter,y_scatter)
            
            scatter_min = minimum_val(y_scatter)
            print("The minimum GPA value in the chart is", scatter_min)
            
            scatter_max = maximum_val(y_scatter)
            print("The maximum GPA value in the chart is", scatter_max)
            
            scatter_avg = average_val(y_scatter)
            print("The average GPA of the chart is", scatter_avg, '\n')
    
        elif choice == 2:
            x_line = [1990,1994,1998,2000,2009,2021]
            y_line = [2.6,2.7,2.8,2.9,3.0,3.0]
            line_visual(x_line,y_line)
            
            line_min = minimum_val(y_line)
            print("The minimum GPA value in the chart is", line_min)
    
            line_max = maximum_val(y_line)
            print("The maximum GPA value in the chart is", line_max)
            
            line_avg = average_val(y_line)
            print("The average GPA of the chart is", line_avg, '\n')
            
        elif choice == 3:
            x_bar = ['Math','Science','English','Social Studies']
            y_bar = [2.65,2.7,2.85,2.89]
            bar_visual(x_bar, y_bar)
            
            bar_min = minimum_val(y_bar)
            print("The minimum GPA value in the chart is", bar_min)
            
            bar_max = maximum_val(y_bar)
            print("The maximum GPA value in the chart is", bar_max)
    
            bar_avg = average_val(y_bar)
            print("The average GPA of the chart is", bar_avg, '\n')
            
            
        elif choice == 4: 
            label_pie = ['Maybe','No','Yes'] 
            score_pie = [5,5,13]
            pie_visual(label_pie,score_pie)
            
            pie_min = minimum_val(score_pie)
            print("The minimum number of responses for an option in the chart is", pie_min)
            
            pie_max = maximum_val(score_pie)
            print("The maximum number of responses for an option in the chart is", pie_max)
            
            pie_avg = average_val(score_pie)
            print("The average number of responses for an option in the chart is", pie_avg, '\n')
            
        elif choice == 5: 
            print('Sending back to main menu')


###########################################################################################################
# End of Simple Visualizations
###########################################################################################################
 
    
    
    
###########################################################################################################
# Start of Survey Analysis
###########################################################################################################




def read_csv(file):
    ages = []
    linear_scale = []
    choice_yes = 0
    choice_no = 0
    choice_maybe = 0
    
    # opens file and uses for loop to check each data entry. Uses if statements to clean data entries.
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if check_age(row["How old are you? (Response MUST be numerical)"]) == False:
                print('Error in line', reader.line_num, row["How old are you? (Response MUST be numerical)"],'is not a valid age')
            else:
                ages.append(int(row["How old are you? (Response MUST be numerical)"]))
            if check_linear_scale(row["On a scale of 1-5, how stressed are you the night before an exam?"]) == False:
                print('Error in line', reader.line_num, row["On a scale of 1-5, how stressed are you the night before an exam?"],'is not a valid response')
            else:
                linear_scale.append(int(row["On a scale of 1-5, how stressed are you the night before an exam?"]))
            if check_multiple_choice(row["Should you prioritize sleep to earn a higher GPA?"]) == False:
                print('Error in line', reader.line_num, row["Should you prioritize sleep to earn a higher GPA?"],'is not a valid option')
            else:
                choice_yes += row["Should you prioritize sleep to earn a higher GPA?"].count('Yes')
                choice_no += row["Should you prioritize sleep to earn a higher GPA?"].count('No')
                choice_maybe += row["Should you prioritize sleep to earn a higher GPA?"].count('Maybe')
    return linear_scale, choice_yes, choice_no, choice_maybe
    


        
def check_age(some_age):
    valid = False
    if some_age.isdigit():
        some_age = int(some_age)
        if some_age > 0 and some_age < 150:
            valid = True
    else:
        i = 0
        while some_age[i].isdigit():
            i+=1
        if i > 0:
            some_age = int(some_age[0:i])
            if some_age > 0 and some_age < 150:
                valid = True
    return valid     

def check_linear_scale(some_number):
    valid = True
    if some_number.isdigit() == False:
        valid = False
    elif int(some_number) < 1 or int(some_number) > 5:
        valid = False
    return valid

def check_multiple_choice(some_choice):
    valid = True
    if some_choice == "Yes" or some_choice == "Maybe" or some_choice == "No":
        valid = True
    else: 
        valid = False
    return valid


def plt_linear_rating(some_list):
    some_list.sort()
    plt.hist(some_list, bins = 5)
    plt.title("On a scale of 1-5, how stressed are you the night before an exam?")
    plt.xlabel("(1 = not stressed -------- 5 = very stressed)")
    plt.ylabel("Count")
    
    plt.show()

    
def plt_counts(choice_yes, choice_no, choice_maybe):
    pie_label = ['Yes','No', 'Maybe']
    pie_scores = [choice_yes, choice_no, choice_maybe]
    plt.pie(pie_scores, labels = pie_label)
    plt.title("Should You Prioritze Sleep to Earn a Higher GPA")
    plt.legend(bbox_to_anchor=(1, 0, 0.75, 0.75),loc = 'upper right')
    plt.show()



def compute(some_list):
    mean = np.mean(some_list)
    mean = round(mean, 2)
    return mean


def survey_analysis(linear_scale, choice_yes, choice_no, choice_maybe):
    choice = ''
    while choice != 4:
        print("""Choose one of the following numbered options to view visualizations of GPA Factors. 
        1. Histogram: On a scale of 1-5, how stressed are you the night before an exam?
        2. Data Statistic Computation: Calculating the average stress of students based on the scale of 1-5.
        3. Pie Chart: Should You Prioritze Sleep to Earn a Higher GPA?
        4. Back to main menu
        """)
        
        if choice == 1: 
            plt_linear_rating(linear_scale)
        elif choice == 2: 
            avg = compute(linear_scale)
            print('The average stress of students based on the survey response on a scale of 1-5 is', avg)
        elif choice == 3:
            plt_counts(choice_yes, choice_no, choice_maybe)
        elif choice == 4:
            print('Back to main menu')
            
        
        choice = check_choice(1,4)
        
###########################################################################################################
# End of Survey Analysis
###########################################################################################################
            
            
        
        
###########################################################################################################
# Start of Data Set Analysis
###########################################################################################################

def read_as_dataframe(df):
    df = pd.read_csv(df)
    return df


def clean_dataframe(df):    
    df = df.dropna()
    df = df.drop_duplicates()
    df = df.reset_index(drop = True)
    return df

def process_df(df_file):  
    df = read_as_dataframe(df_file)
    print(df.info(),'\n')
    
    print("I don't notice any obvious errors in this dataset, but I will still use the drop duplicate and missing value commands incase of errors that I didn't notice \n")
    print('The dataset has',len(df.index), 'rows before cleaning','\n')
    df_clean = clean_dataframe(df)
    
    print('The dataset has',len(df_clean.index), 'rows after cleaning','\n')
    print("Since there are 253 rows before and after cleaning, it shows that I didn't have to clean the dataset")
    
    return df_clean
    

    
def get_subset(df, condition):
    my_filter = df['AlcoholUse'] == condition
    subset = df[my_filter]
    return subset

def groupby_sum_table(df):
    average_gpa_alcohol = df.groupby('AlcoholUse', as_index = False)['GPA'].mean()
    average_gpa_alcohol = average_gpa_alcohol.sort_values('GPA', ascending = False)
    average_gpa_alcohol = average_gpa_alcohol.reset_index(drop = True)
    return average_gpa_alcohol

def piv_sum_table(df):    
    average_gpa_stress = df.pivot_table('GPA', columns = 'Stress')
    average_gpa_stress = average_gpa_stress.reset_index(drop = True)
    return average_gpa_stress



def scatter_chart(df):
    x = df['GPA']
    y = df["PoorSleepQuality"]
    
    plt.scatter(x,y)
    
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    plt.plot(x, intercept+slope*x, 'r', label = 'fitted line')
    plt.title('Average GPA Compared with Sleep Quality')
    plt.xlabel('GPA')
    plt.ylabel('Sleep Quality (higher values are poorer sleep)')
    
    plt.show()

def line_chart(df):
    avg_gpa_stress = df.groupby('Stress', as_index = False)['GPA'].mean()
    sort_stress = avg_gpa_stress.sort_values('GPA',  ascending = True)
    
    x = sort_stress['Stress']
    y = sort_stress['GPA']
    
    plt.plot(x,y)
    plt.title('Average GPA Compared with Stress')
    plt.xlabel('Stress Level')
    plt.ylabel('GPA')
    
    plt.show()

    
def bar_chart(df):
    x = df['AlcoholUse']
    y = df['GPA']
    
    plt.bar(x,y)
    plt.title('Average GPA Compared with Alcohol Use')
    plt.xlabel('Alcohol Use')
    plt.ylabel('GPA')
    
    plt.show()
    
def sum_table_line_chart(average_gpa_alcohol):
    x = average_gpa_alcohol["AlcoholUse"]
    y = average_gpa_alcohol['GPA']
    
    plt.plot(x,y)
    plt.title('Average GPA Compared with AlcoholUse')
    plt.xlabel('Alcohol Use')
    plt.ylabel('GPA')
    
    plt.show()
    
    
    
def data_analysis(df):
    subset1 = get_subset(df, 'Abstain')
    subset2 = get_subset(df, 'Light')
    subset3 = get_subset(df, 'Moderate')
    subset4 = get_subset(df, 'Heavy')
    
    
    choice = ''
    while choice != 7:
        print("""Choose one of the following numbered options to view pivot tabels and visualizations of the dataset. 
        1. Scatter Chart: Average GPA Compared with Sleep Quality
        2. Line Chart: Average GPA Compared with Stress
        3. Bar Chart: Average GPA Compared with Alcohol Use
        4. Summary Table Line Chart: Average GPA Compared with Alcohol Use
        5. Summary Table: Average GPA of each level of use of Alcohol
        6. Summary Table: Average GPA of each level of stress.
        7. Back to main menu
        """)
        
        
    choice = ''
    while choice != 7:
        print("""Choose one of the following numbered options to view pivot tabels and visualizations of the dataset. 
        1. Scatter Chart: Average GPA Compared with Sleep Quality
        2. Line Chart: Average GPA Compared with Stress
        3. Bar Chart: Average GPA Compared with Alcohol Use
        4. Summary Table Line Chart: Average GPA Compared with Alcohol Use
        5. Summary Table: Average GPA of each level of use of Alcohol
        6. Summary Table: Average GPA of each level of stress.
        7. Back to main menu
        """)
        
        check_choice(1,7)
        
        if choice == 1:
            scatter_chart(df)
        elif choice == 2:
            line_chart(df)
        elif choice == 3:
            bar_chart(df)
        elif choice == 4: 
            sum_table_line_chart(average_gpa_alcohol)
        elif choice == 5:
            average_gpa_alcohol = groupby_sum_table(df)
            print(average_gpa_alcohol, "\n")
        elif choice == 6:
            average_gpa_stress = piv_sum_table(df)
            print(average_gpa_stress,'\n')
        elif choice == 7: 
            print('Back to main menu')
            
        
        choice = check_choice(1,7)
                    
        
            

    
    
###########################################################################################################
# End of Data Set Analysis
########################################################################################################### 


    


###########################################################################################################
# START OF SETUP --> WELCOME MESSAGE AND MAIN FUNCTION
###########################################################################################################

# function name: welcome_msg
# arguments: none
# return: none
# description: outputs the title of the program and where the data was collected from (i.e., website, data set)
def welcome_msg():
    dq = 'Should a student prioritize sleep to earn a higher GPA?'
    
    print('\t\t\t\t\t SleepStudy: ')
    print('\t\t\t\t' + dq.upper())
    print('\n')
    print('\t\t\t Welcome to the SleepStudy data set analysis program!\n')    
        
        
# function name: main
# arguments: none
# return: none
# description: setups the program and manages calls to other functions defined to handle the eight options
#              it repeats the eight options until the user chooses the option to quit
def main():
    # call welcome_msg function to output the title of the program and where the data was collected from
    welcome_msg()
    
    
    # flag variable keeping track of if the survey data has already been processed/cleaned
    #      assume at the beginning of program that survey data has NOT been processed/cleaned
    #      update this flag variable when the 5th or 7th option have been chosen for the first time
    survey_processed = False
    
    
    # flag variable keeping track of if the DataFrame containing the data from your data set you found online 
    #      has already been processed/cleaned
    #      assume at the beginning of program that DataFrame has NOT been processed/cleaned
    #      update this flag variable when the 6th or 7th option have been chosen for the first time
    data_processed = False
    
    
    # define string variable that is empty to hold user's input
    choice = ''
    
    
    # loop until the user chooses the choice to quit the program
    while choice != 8:
        
        # call the get_choice function to get the choice from the user and store in variable
        choice = get_choice()
        
        # check if the user chose the first option
        if choice == 1:
            # call overview function to output an overview of your topic and data set
            overview()
            
        elif choice == 2:
            dq()
            
        elif choice == 3:
            basic_stats()
        
        elif choice == 4:
            simple_visualizations()
        elif choice == 5 or choice == 6 or choice == 7:
            if choice == 5 or choice == 7:
                if survey_processed == False:
                    survey_file = 'GPA_Factors.csv'
                    linear_scale, choice_yes, choice_no, choice_maybe = read_csv(survey_file)
                    survey_processed = True
                if choice == 5:
                    survey_analysis(linear_scale, choice_yes, choice_no, choice_maybe)
            elif choice == 6 or choice == 7:
                if data_processed == False:
                    df_file = 'SleepStudy.csv'
                    df_clean = process_df(df_file)
                    data_processed = True
                if choice == 6:
                    data_analysis(df_clean)
            

        
###########################################################################################################
# END OF SETUP --> WELCOME MESSAGE AND MAIN FUNCTION
###########################################################################################################



# call the main function to run your program  
main()
