# There is a number sequence: 0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15, ...
# Find out the nth term in this sequence

def get_number(index):
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