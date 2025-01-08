# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
queue = []
queries = []

for query in sys.stdin:
    cleaned = query.strip()
    queries.append(cleaned)
    
n = int(queries[0])
for i in range(1, n):
    curr_q = queries[i][0].strip()
    element = queries[i][1:].strip()
    
    if curr_q == '1':
        queue.append(element)
    elif curr_q == '2':
        queue = queue[1:]
    elif curr_q == '3':
        print(queue[0])
        
        
#print(queue)
