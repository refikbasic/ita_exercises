import random

thisset={"banana","jabuka","visnja"}
thisset.add("mango")
#print(thisset)

thisset.update(["papaja","rajcica","kifla"])  
#print(thisset)                              

thisset={"banana","jabuka","visnja"}
x=thisset.pop()     
#print(x)            
#print(thisset)      

set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)  
#print(set3)
set1.update(set2)       
#print(set1)

prvisetprviclan=random.randrange(1,100)
prvisetdrugiclan=random.randrange(1,100)  
drugisetprviclan=random.randrange(1,100)   
drugisetdrugiclan=random.randrange(1,100)
set1={prvisetprviclan,prvisetdrugiclan}
set2={drugisetprviclan,drugisetdrugiclan}
set1.update(set2)       
set1.clear()           
