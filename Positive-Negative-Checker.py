def checker(value):
    if value > 0:
        return f"Given NO : {value} is Positive"
    elif value < 0:
        return f"Given NO : {value} is Negative"
    else:
        return f"Value is Zero !"

    # a basic project while learning the use of Python Logics and flows...
    
while True:
    user_value = int(input("Input Value : "))
    
    print(checker(user_value))
