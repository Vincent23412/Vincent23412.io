# Find out whose middle name is unique among all the names, and print it. You can assume
# every input is a Chinese name with 2 ~ 3 words. If there are only 2 words in a name, the
# middle name is defined as the second word


def func(*data):
    word_str = ''
    for i in data :
        word_str += i[1:]
    ans = []
    for i in data :
        unique = True
        for j in i :
            if word_str.count(j) > 1 :
                unique = False
        ans.append(unique)
    
    for i in range(len(data)) :
        if len(data[i][1:]) > len(set(data[i][1:])) :
            ans[i] = True
    for i in range(len(data)) :
        if ans[i] == True :
            print(data[i])
    if set(ans) == {False} :
        print('沒有')




# your code here
func("彭大牆", "王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有