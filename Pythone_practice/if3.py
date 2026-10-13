score = int(input("input score"))
attendance = int(input("enter attendece"))
summitted = True

if score >= 60:
    if attendance >=  80:
        if summitted:
            print("pass with good standing")
        else:
            print("pass but assignment is missing")
    else:
        print("pass but low attendance")
else:
    print("fail")