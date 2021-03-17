#if we have input= [ {'nbr':[1,2,3]},{'name':['jan','feb','mar']} ]
#and we want output= [ {1:jan}, {2:feb}, {3:mar}]

pair1 = input[0]
pair2=  input[1]
res_dict=[]
nbr_set=pair1.values()[0]
name_set=pair2.values()[0]

# One way in python3 with zip function
zip_iterator = zip(nbr_set,name_set)
zipped_res_dict= dict(zip_iterator)
print(zipped_res_dict)

# Second Way for python2 or without zip function
for x in range(len(pair1.values()[0])):
        
	res_dict.append({nbr_set[x]:name_set[x]})
            
print(res_dict)
#explanation- arlier i had a nested for loop for nbr and names separately and then compared when outer_loop_num=inner_loop_num, it caused the time complexity to be n^2, but I realised it can be linear by getting rid of two loops.  
