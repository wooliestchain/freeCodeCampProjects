import pandas as pd

def demographic_data_analyzer(print_data = True):
    demo = pd.read_csv('adult.data.csv')

    # Number of people by race
    race = demo['race'].value_counts()

    average_men_age = demo[demo['sex'] == 'Male' ]
    average_men_age = round(demo['age'].mean(),1)


    bachelor = demo[demo['education'] == 'Bachelors']
    percentage_bachelor = round(bachelor.shape[0]/demo.shape[0]*100, 2)

    high_edu = demo[demo['education'].isin(["Bachelors", "Masters", "Doctorate"])]

    high_edu_salary = round(high_edu[high_edu['salary'] == ">50K"].shape[0] / high_edu.shape[0]*100, 1)

    low_edu = demo[~demo['education'].isin(["Bachelors", "Masters", "Doctorate"])]
    low_edu_salary = round(low_edu[low_edu['salary'] == ">50K"].shape[0] / low_edu.shape[0]*100,1)

    min_work_hour = demo['hours-per-week'].min()

    min_hour = demo[demo['hours-per-week'] == min_work_hour]

    min_workers = demo[demo['hours-per-week'] == min_work_hour].shape[0]

    rich_min_worker = round(demo[demo['hours-per-week'] == ">50K"].shape[0] / min_workers * 100,1)

    num_high_salary_per_country = demo[demo['salary'] == ">50K"]['native-country'].value_counts()
    num_country = demo['native-country'].value_counts()
    percentage = num_high_salary_per_country / num_country * 100

    highest_earning_country = percentage.idxmax()
    highest_earning_country_percentage = round(percentage.max(), 1)


    high_salary_India_occ = demo[(demo['salary'] == ">50K") & (demo['native-country'] == "India")]['occupation'].value_counts()

    top_IN_occupation = high_salary_India_occ.idxmax()


    if print_data:
        print("Number of each race:\n", race)
        print("Average age of men:", average_men_age)
        print(f"Percentage with Bachelors degrees: {percentage_bachelor}%")
        print(f"Percentage with higher education that earn >50K: {high_edu_salary}%")
        print(f"Percentage without higher education that earn >50K: {low_edu_salary}%")
        print(f"Min work time: {rich_min_worker} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race,
        'average_age_men': average_men_age,
        'percentage_bachelors': percentage_bachelor,
        'higher_education_rich': high_edu_salary,
        'lower_education_rich': low_edu_salary,
        'min_work_hours': rich_min_worker,
        'rich_percentage': percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
            highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

demographic_data_analyzer()