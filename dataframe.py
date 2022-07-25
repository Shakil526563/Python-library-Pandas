import pandas as pb
dataset={"name":['shakil','munna','afnan'],'age':[14,25,55]}
data=pb.DataFrame(dataset)
print(data)
print(data.loc[2])
"""loc attribute full name is location attribute .use this attribute ,we will find out the 
location of data",and also multiple index will assign """
print(data.loc[[0,2]])