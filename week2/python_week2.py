print('task1')
def find_and_print(messages):
    # 判斷依據:敘述裡面有年齡，有關投票或是合法的言論

    old = []
    for name,describe in messages.items() :
        # numbers = re.findall(r'\d+', describe)
        numbers = find_num(describe)
        if numbers :
            if numbers > 17 :
                old.append(name)
        if 'vote' in describe or 'legal' in describe :
            old.append(name)
        
    print(old)
    return name
            
def find_num(word):
    for i in word.split() :
        try :
            return int(i)
        except :
            pass


find_and_print({
    "Bob":"My name is Bob. I'm 18 years old.",
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.",
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning."
})

print('----------')
print('task2')


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
    # 獎金依據：表現高於平均：本薪*0.1 平均：本薪*0.05 低於平均：本薪*0.01
    # 獎金依據：CEO：本薪*0.1 Engineer：本薪*0.05 Sales：本薪*0.01


    for i in data['employees'] :
        final_sum = 0
        i['salary'] = str(i['salary']).replace(',','')
        if 'USD' in str(i['salary']) :
            final_sum = int(i['salary'][:-3]) * 30 * bouns_performance[i['performance']] + int(i['salary'][:-3]) * 30 * bouns_role[i['role']]
        else :
            final_sum = int(i['salary']) * bouns_performance[i['performance']] +  int(i['salary']) *bouns_role[i['role']]

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

print('-----------')
print('task3')

def func(*data):
    # 先把中間名稱取出來，再看看出現幾次

    middle = []
    for i in data :
        middle.append(i[1])
    ans = []
    for i in range(len(middle)) :
        if middle.count(middle[i]) == 1 :
            ans.append(True)
        else :
            ans.append(False)
    if set(ans) == {False} :
        print('沒有')
    for i in range(len(ans)) :
        if ans[i] == True :
            print(data[i])


# your code here
func("彭大牆", "王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

print('---------')
print('task4')

def get_number(index):
    # 創造出串列，取出最後一個

    seq = [0] * (index+1)
    for i in range(index) :
        if i % 2 == 0 :
            seq[i+1] = seq[i] + 4
        else :
            seq[i+1] = seq[i] - 1
    print(seq[-1])



get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15


print('-----')
print('task5')


def find_index_of_car(seats, status, number):
    # 先找出status=1而且位置夠的，然後再回傳購的最小值
    sort = []
    for i in range(len(seats)) :
        if status[i] == 1 and seats[i] >= number:
            sort.append(seats[i]-number)
        else :
            sort.append(10000)
    print(sort)
    if len(set(sort)) == 1 :
        print(-1)
    else : 
        print(sort.index(min(sort)))


find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2