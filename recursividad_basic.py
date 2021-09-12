def countdown(number):
    print(number)
    if number>0 :
        countdown(number - 1)
    else:
        print("BOOOM")
        
countdown(5)