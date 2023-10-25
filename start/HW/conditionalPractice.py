def send_message():
    for x in range(10):
        print("YES IT IS!?!")

def isTodayGood():
    isIt = input("Is today a good day?! ")
    
    if isIt == "y":
        send_message()

isTodayGood()