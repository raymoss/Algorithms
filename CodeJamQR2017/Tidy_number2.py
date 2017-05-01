input_file=open("B-large-practice.in","r")
output_file=open("output","wb")
tn_testcases=int(input_file.readline())
testcase_n=1
while(tn_testcases>0):
    number=long(input_file.readline())
    elements=[]
    copy_n=number
    while number>0:
        elements.append(number%10)
        number=number/10
    elements.reverse()
    #print elements
    #break
    i=0
    while(i< len(elements)-1):
        check=0
        if(elements[i]>elements[i+1]):
            elements[i]=elements[i]-1
            check=1
            #print elements
            for j in range(i+1,len(elements)):
                elements[j]=9
                #print elements
        if check==1:
            i=0
        else:
            i+=1
    s=map(str,elements)
    s="".join(s)
    output_file.write("Case #%d: %d\n"%(testcase_n,int(s)))
    testcase_n+=1
    tn_testcases-=1
input_file.close()
output_file.close()
