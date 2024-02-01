x = int(input())
total_sum, last_value = 1, 1
for i in range(x - 1):
    index_num = i + 1
    last_value += index_num
    total_sum += last_value
print(total_sum)

"""
x= int(input())
series=[1]
last_value = 1
for i in range(x-1):
    index_num = (i+1)
    series.append(last_value + index_num)
    #print("last_value",series)
    last_value = series[-1]
a=sum(series)
print(a)




For eg 1: n=3
_ _ _
W1
W2
R    W1
R    R     R
-> 7 ans

eg 2: n=4
_ _ _ _

W1
W2
W3
R   W1
R   W2
R	R	W1
R	R	R  	R


if we see the columns:
numbers are: 1, 2, 4, 7, 11, ....
 (index)     1  2  3  4  5

 adding current number of series with the indexed one will give the next number of the series. sum of the series elements is the answer.

"""