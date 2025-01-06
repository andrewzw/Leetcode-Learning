def minimumBribes(q):
    n = len(q)
    count = 0
    for i in range(n):
        num = q[i]
        index = i+1
        
        curr_diff = (num-index)
        if curr_diff > 2:
            print("Too chaotic")
            return

        start_j = max(0, num - 2)
        for j in range(start_j,i):
            if q[j] > num:
                count += 1
            
    print(count)
    return




q = [1, 2, 5, 3, 7, 8, 6, 4] 
q = [2, 1, 5, 3, 4] 
#minimumBribes(q)


temp = q.copy()
temp.sort()
# print('Sorted   :',temp)
# print('Unsorted :',q)

#simple solution
def minimumBribes(q):
    print('Unsorted:',q)    
    n = len(q)
    bribes = 0

    for i in range(n-1, 0, -1): #start from the end
        print(q, 'index:', i, 'i+1:', i+1)
        if(q[i] != i+1): #bribes
        
            if(q[i-1] == i+1):
                print('q[i-1]:', q[i-1], '\n')
                q[i],q[i-1] = q[i-1], q[i]           
                bribes += 1

            elif(q[i-2] == i+1):
                print('q[i-2]:', q[i-2], '\n')
                # Example : 2 1 5 3 4, 2 1 3 4 5
                q[i],q[i-1], q[i-2]= q[i-2], q[i], q[i-1]

                bribes += 2
            else:
                return("Too chaotic")
     
    return bribes



tests ={3: [2 ,1 ,5 ,3 ,4],
    #'Too chaotic' : [2, 5, 1, 3, 4],
    #'Too chaotic' : [5, 1, 2, 3, 7, 8, 6, 4],
    #7: [1, 2, 5, 3, 7, 8, 6, 4],
    #4: [1, 2, 5, 3, 4, 7, 8, 6]
}

for test in tests:
  
    print('Results:' ,minimumBribes(tests[test]), '\nExpected:', test)
    
    print('-----------------')