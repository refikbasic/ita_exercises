auto={
    "brand":"Ford",        
    "model":"Mustang",
    "year":1964
}
#print(auto)
x=auto["model"]          
#print(x)
x=auto.get("model")        
#print(x)
auto["year"]=2018         
#print(auto)
auto["color"]="crvena"      
#print(auto)

auto.pop("model")          
#print(auto)

del auto["color"]          
#print(auto)