cars = {
    "bmw" : {
        "state" : True,
        "3 series" : {
            "drive" : "rear",
            "fuel" : "diesel",
            "ccm": "1998",
            "state" : True
        },
        "5 series" : {
            "drive" : "rear",
            "fuel" : "petrol",
            "ccm": "3000",
            "state" : True
        }
    },
    'audi': {
        "q3" : {
            "drive" : "front",
            "fuel" : "diesel",
            "ccm": "2000",
            "state" : True
        },
        "q5" : {
            "drive" : "quattro",
            "fuel" : "petrol",
            "ccm": "4000",
            "state" : True
        },
        "state" : True
    },
    'mercedes': {
        "E class" : {
            "drive" : "rear",
            "fuel" : "diesel",
            "ccm": "2200",
            "state" : True
        },
        "C class" : {
            "drive" : "front",
            "fuel" : "diesel",
            "ccm": "2000",
            "state" : True
        },
        "state" : True
    }
}
car_brand=input('Please input car brand: ')
car_brand=car_brand.lower()
if car_brand in cars and cars[car_brand]['state']==True:
    series = input("Please enter brand car model: ")
    if series in cars[car_brand] and cars[car_brand][series]["state"] == True :
        print(cars[car_brand][series])
    else :
        print("We don`t have that car model.")
else:
    print("This vehicle isn`t available")