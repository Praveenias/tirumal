#break pass continue

#break -->break the loop

for i in [1,2,3]:
    if i==2:
        break
    print("break:",i)

#pass --> just pass the line

for i in [1,2,3]:
    if i==2:
        pass
    print("pass:",i)
    
#continue --> leave the line to the for loop

for i in [1, 2, 3]:
    if i == 2:
        continue
    print("continue:", i)
    
# output:
# break: 1
# pass: 1
# pass: 2
# pass: 3
# continue: 1
# continue: 3
