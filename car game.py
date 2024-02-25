#command = input('>')
#if command.upper() == 'help':
#    print("start - to start the car")
#    print("stop - to stop the car")
#   print("quit - to exit")
#elif command.upper() == 'start':
#   print("car started... Ready to go")
#elif command.upper() == "stop":
#    print("car stopped")
#elif command.upper() == "quit":
#    print("you can exit")
#else:
#    print("I don't understand")
command = ""
started = False
while  True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("""
start- to star the car
stop- to stop the car
quit- to exit        
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand")
