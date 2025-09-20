# string that store my 
name="rehan khan"
print(name)

# integer that store my age
age=19
print(age)
# list that store hobbies
hobbies=["coding", "cricket", "repairing"]
print(hobbies)

dic={
    
    "name":"rehan khan",
     "age":19,
     "hobbies":["coding", "cricket", "repairing"],
     }

print("name:",dic["name"])
print("hobbies:",",".join(dic["hobbies"]))
print("city:",dic.get("city","swat"))
print("age:",dic["age"])    


# **************************************************************************
dic={
    "name":"rehan khan",
    "age":"19",
    "city":"swat",
    "skills":["pyhton","repairing","ecoomerce"],
    "friend":["jawad","fawad","aimal"]
}
dic["skills"].append("java")
dic["friend"].append("hamza")
dic["hobbies"]="hunting"
for key, value in dic.items():
    if isinstance (value, list):
        print(key,":",",".join(value))
    else:
        print(key,":",value)
print(f"there are {len(dic['skills'])} skills in the list")

print(f"my best friend is  {dic['friend'][-1]}")
    
