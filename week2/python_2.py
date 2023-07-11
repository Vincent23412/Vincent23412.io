# Using a loop to complete functions below to calculate the sum of bonus of all employees in
# TWD and print it.
# 1. Bonus should depend on salary, performance and role fields. Define your own rules
# and calculate a bonus for each employee based on it.
# 2. The sum of bonus of all employees cannot exceed 10000 TWD based on your rules
# and example data.
# 3. You can assume the USD to TWD Exchange Rate is 30.
# 4. Salary is default to TWD if there is no specific mark


bouns_performance = {
    'above average' :0.1,
    'average' :0.05,
    'below average' :0.01
}
bouns_role = {
    'Engineer' :0.05,
    'CEO' :0.1,
    'Sales' :0.01
}

def calculate_sum_of_bonus(data):
# write down your bonus rules in comments
# your code here, based on your own rules
    for i in data['employees'] :
        final_sum = 0
        i['salary'] = str(i['salary']).replace(',','')
        if 'USD' in str(i['salary']) :
            final_sum = int(i['salary'][:-3]) * 30 * (1+bouns_performance[i['performance']]) * (1+bouns_role[i['role']])
        else :
            final_sum = int(i['salary']) * (1+bouns_performance[i['performance']]) * (1+bouns_role[i['role']])

        print(final_sum)
calculate_sum_of_bonus({
    "employees":[
        {
        "name":"John",
        "salary":"1000USD",
        "performance":"above average",
        "role":"Engineer"
        },
        {
        "name":"Bob",
        "salary":60000,
        "performance":"average",
        "role":"CEO"
        },
        {
        "name":"Jenny",
        "salary":"50,000",
        "performance":"below average",
        "role":"Sales"
        }
]}) 