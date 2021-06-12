dictionary ={ 
    "name" : "sathiyajith", 
    "rollno" : 56, 
    "cgpa" : 8.6, 
    "phonenumber" : "9976770500"
} 
  
with open("sample.json", "w") as outfile: 
    json.dump(dictionary, outfile) 


with open("sample.json", "r") as outfile: 
    con = json.load(outfile)
    for key,value in con.items():
            print(key)
            print(value)
    #print(con)
