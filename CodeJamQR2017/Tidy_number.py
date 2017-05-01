def check_tidiness(number):
    while number >0:
        if (number%10) >= ((number/10)%10) :
            number=number/10
        else:
             return -1
    return 0
def check_tidiness2(number):
    elements=[]
    copy_n=number
    while number>0:
        elements.append(number%10)
        number=number/10
    for i in range(0,len(elements)-1):
        if(elements[i] < elements[i+1]):
            return -1
    return 0

input_file=open("B-small-practice.in","r")
output_file=open("output","wb")
tn_testcases=int(input_file.readline())
testcase_n=1
while(tn_testcases>0):

    number=long(input_file.readline())
    #print number
    while(number>0):
        a=check_tidiness2(number)
        if a<0:
            number=number-1
        else:
            output_file.write("Case #%d: %d\n"%(testcase_n,number))
            #print number
            break
    testcase_n+=1
    tn_testcases-=1
input_file.close()
output_file.close()
