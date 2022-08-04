while True:
    try:
        n = int(input("please enter an integer: "))
        break
    except IOError:
        print("not an integer! please again 123")
    except ValueError:
        print("not an integer! please again 456")

print("you successfully enterd an integer!")