from collections import namedtuple

def can_take_order(driver, num_packages):
    return driver.car_capacity >= num_packages
def main():
    #add code here
    #create a driver with a name, car type, and car capacity
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    Driver = namedtuple("driver", ["name", "car_type", "car_capacity"])
    iris = Driver("Iris", "Prius", 7)
    mickie = Driver("Mickie", "Tucson", 15)
    jose = Driver("Jose", "Porsche", 26)
    #check if they can take a certain order, given their car's capacity.
    print(can_take_order(jose,20))
    

if __name__ == "__main__":
    main()