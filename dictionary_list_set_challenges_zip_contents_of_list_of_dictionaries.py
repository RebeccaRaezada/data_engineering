#if we have input= [ {'nbr':[1,2,3]},{'name':['jan','feb','mar']} ]
#and we want output= [ {1:jan}, {2:feb}, {3:mar}]

pair1 = input[0]
pair2=  input[1]
res_dict=[]
nbr_set=pair1.values()[0]
name_set=pair2.values()[0]

# One way in python3 with zip function
zip_iterator = zip(nbr_set,name_set)
res_dict= dict(zip_iterator)
print(res_dict)

# Second Way for python2 or without zip function
for x in range(len(pair1.values()[0])):
    
    for y in range(len(pair2.values()[0])):
        
        if x==y:
            res_dict.append({nbr_set[x]:name_set[x]})
            
print(res_dict)
