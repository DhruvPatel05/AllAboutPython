while input(">" ).upper() != "HELP":
    print("I don't understand that...")
else :
    print("""
    start - to start the car
    stop - to stop the car
    quit - to exit
    """)
    car_command = ""
    machine_command = ""
    started = False
    # while car_command != "QUIT":
    while True:
        car_command = input("> ")
        # print(car_command.upper())
        if car_command.upper() == "START":
            # if machine_command.upper() == "START":
            if started:
                print("Car is already started")
            else:
                started = True
                print("Car started... Ready to go!")
        elif car_command.upper() == "STOP":
            # if machine_command.upper() == "STOP":
            if not started:
                print("Car is already stopped.")
            else:
                started = False
                print("Car stopped.")
        elif car_command.upper() == "QUIT":
            # print("Inside",car_command.upper())
            break
        else:
            print("I don't understand that...")
        # machine_command = car_command
    # else:
    #     print("Outside")
    #     exit()
