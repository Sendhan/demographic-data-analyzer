import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race = df['race'].squeeze()
    race_count = {}
    for i in range(32561) :
      race_name = race.iloc[i]
      if race_name not in race_count :
        race_count[race_name] = 1
      else :
        race_count[race_name] += 1
    race_count = pd.Series(race_count)


    # What is the average age of men?
    Sum_Total_of_Men_age = 0
    Men_count = 0
    average_age_men = None
    age = df['age'].squeeze()
    gender = df['sex'].squeeze()
    for i in range(32561) :
      Age = age.iloc[i]
      Gender = gender.iloc[i]
      if Gender == "Male" :
        Men_count += 1
        Sum_Total_of_Men_age += Age
        
    average_age_men = round(Sum_Total_of_Men_age/Men_count, 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = None
    no_of_bachelors = 0
    Education = df["education"].squeeze()
    for i in range(32561) :
      education = Education.iloc[i]
      if education == "Bachelors" :
        no_of_bachelors += 1
        
    percentage_bachelors = round((no_of_bachelors/32561)*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None
    no_of_high_edu = 0
    no_of_low_edu = 0 

    for i in range(32561) :
      education = Education.iloc[i]
      if education == "Bachelors" or education == "Masters" or education == "Doctorate" :
        no_of_high_edu += 1
      else :
        no_of_low_edu += 1
        
    higher_education = no_of_high_edu
    lower_education = no_of_low_edu

    # percentage with salary >50K
    salary = df["salary"].squeeze()

    higher_education_rich = None
    lower_education_rich = None
    total_high_edu_rich = 0
    total_low_edu_rich = 0

    for i in range(32561) :
      education = Education.iloc[i]
      Salary = salary.iloc[i]
      if (education == "Bachelors" or education == "Masters" or education == "Doctorate") and (Salary == ">50K") :
        total_high_edu_rich += 1
      elif (education != "Bachelors" and education != "Masters" and education != "Doctorate") and (Salary == ">50K") :
        total_low_edu_rich += 1
        
    higher_education_rich = round((total_high_edu_rich/higher_education)*100,1)
    lower_education_rich = round((total_low_edu_rich/lower_education)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None
    hrs_work = df["hours-per-week"].squeeze()
    min_work_hours = hrs_work.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None
    num_min_workers = 0

    rich_percentage = 0

    min_work_rich = 0
    for i in range(32561) :
      Salary = salary.iloc[i]
      work_hrs = hrs_work.iloc[i]
      if work_hrs == min_work_hours :
        num_min_workers += 1
        if Salary == ">50K" :
            min_work_rich += 1
            
    rich_percentage = round((min_work_rich/num_min_workers)*100, 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None
    
    country = df["native-country"].squeeze()
    country_dict = {}
    for i in range(32561) :
      Salary = salary.iloc[i]
      Country = country.iloc[i]
      if Salary == ">50K" :
        if Country not in country_dict :
            country_dict[Country] = 1
        else :
            country_dict[Country] += 1
            
    Max = 0
    for keys in country_dict :
      temp = country_dict[keys]
      if temp > Max :
        Max = temp
        highest_earning_country = keys

    high_earning_country_count = 0
    high_salary_count = 0
    for i in range(32561) :
      Country = country.iloc[i]
      Salary = salary.iloc[i]
      if Country == highest_earning_country :
        high_earning_country_count += 1
      if Salary == ">50K" :
        high_salary_count += 1

    highest_earning_country_percentage = round((country_dict[highest_earning_country]/high_salary_count)*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None
    occupation = df["occupation"].squeeze()
    occ_india_high = {}
    for i in range(32561) :
     Country = country.iloc[i]
     if Country == "India" :
        Salary = salary.iloc[i]
        if Salary == ">50K" :
            Occupation = occupation.iloc[i]
            if Occupation not in occ_india_high :
                occ_india_high[Occupation] = 1
            else :
                 occ_india_high[Occupation] += 1
           
    Max = 0
    for keys in occ_india_high :
      temp = occ_india_high[keys]
      if Max < temp  :
        Max = temp
        top_IN_occupation = keys

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
