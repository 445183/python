arr=list([60,61,65,63,98,99,90,95,91,96])

num_sum=0
num_len=len(arr)

for i in arr:
    num_sum+=i

mean=num_sum/num_len

diff_sum=0
for i in arr:
    diff=mean-i
    if diff<0:
        diff=diff*-1
    diff_sum+=diff

std_der=diff_sum/num_len

print(std_der)