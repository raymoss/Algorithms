def toggle(window_size,window_index,elements):
    i=0
    if (window_size+window_index) > len(elements):
        return -1
    while i<window_size:
        elements[window_index+i]=not elements[window_index+i]
        i=i+1
    return 0
input_file=open("A-large-practice.in","r")
output_file=open("output","wb")
tn_testcases=int(input_file.readline())
#print n_testcases
testcase_n=0
while(tn_testcases > 0):
    testcase_n=testcase_n+1
    count=0
    lines=input_file.readline().strip().split(" ")
    """for x in lines:
        print x
        print "hello"
    break
    """
    elements=[]
    i=0
    window_size=int(lines[1])
    #print window_size
    for x in lines[0]:
        if x=='-':
            elements.append(False)
        else:
            elements.append(True)
        i=i+1
    #print elements
    #print len(elements)
    #break
    j=0
    lost=0
    while j<len(elements):
        if elements[j]==False:
            a=toggle(window_size,j,elements)
            #print elements
            if (a<0):
                lost=1
                break
            count=count+1
        j=j+1
    if lost==0:
        output_file.write("Case #%d: %d\n"%(testcase_n,count))
    else:
        output_file.write("Case #%d: IMPOSSIBLE\n"%(testcase_n))
    #print count
    tn_testcases=tn_testcases-1
input_file.close()
