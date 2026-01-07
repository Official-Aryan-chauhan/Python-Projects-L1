# First Calculator calculator
import datetime
present_date_time = datetime.datetime.now()
print('Welcome') #For Good Presentation 
print(f"Today Date and Time {present_date_time}")

while True:
    length = int(input("For How Many Numbers You Have To Perform Calculation : "))
    
    if length == 0:
        print("Zero Length !")
    else:
        storing_point = []
        for i in range(length):
            given_value = float(input("Enter The Value : "))
            storing_point.append(given_value)

        operator_choice = input("Enter The Operator : ").lower()
        if not operator_choice in ("add","+",'-',"sub","mul","divide","subtract","/","div","division","*","multiply"):
            print("Invalid Operator,Please Check It")
            print("Make Sure Your Operators are from folllowing choices","\n","add","+",'-',"sub","mul","divide","subtract","/","div","division","*","multiply" )
        else:    
            def oprations(op):    
                if op == "add" or op == "+":
                    return sum(storing_point)
            
                elif op == "subtract" or op =="-" or op == "sub":
                    net = storing_point[0]
                    for i in storing_point[1:]:
                        net -= i    
                    return net
            
                elif op == "multiply" or op == "*" or op=="mul":
                    net_m = 1 
                    for i in storing_point:
                        net_m = net_m*i
                    return net_m
                
                elif op == "division" or op =="/" or op =="divide" or op=="div":
                    net_d = storing_point[0]
                    for i in storing_point[1:]:
                        if i == 0:
                            raise ZeroDivisionError("Divison By Zero Is Not Possible !")
                        else: 
                            net_d = net_d/i
                    return round(net_d,2) 
                

            print(f"Your {operator_choice} of {length} numbers => {oprations(operator_choice)}")
