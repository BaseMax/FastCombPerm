from YourCombinations import YourCombinations

# cli to ask user to enter and prompt
def cli():
    # infinity loop to ask user input
    while True:
        print("> ", end = "")
        # handle up and down key
        # to get previous and next command
        # from history
        # up: \x1b[A
        # down: \x1b[B
        try:
            command = input()
        except KeyboardInterrupt:
            # handle ctrl + c
            print()
            continue
        except EOFError:
            # handle ctrl + d
            print()
            break

        # split command to get command and arguments
        commands = command.split()
        # check if command is empty
        if len(commands) == 0:
            continue
        # get command
        command = commands[0]
        # get arguments
        arguments = commands[1:]

        # check command
        if command == "exit":
            break
        elif command == "help":
            print("help - show this message")
            print("exit - exit program")
            print("set - set elements")
            print("power - show power set")
            print("combinations - show combinations")
            print("permutations - show permutations")
        elif command == "set":
            your_combinations = YourCombinations(arguments)
        elif command == "power":
            # show power set
            print("Power set:")
            for i in your_combinations.powerSet():
                print(i)
        elif command == "combinations":
            # show combinations
            print("Combinations size {} with repetition:".format(arguments[0]))
            for i in your_combinations.combinations(int(arguments[0]), True):
                print(i)
            print("Combinations size {} without repetition:".format(arguments[0]))
            for i in your_combinations.combinations(int(arguments[0])):
                print(i)
        elif command == "permutations":
            # show permutations
            print("Permutations size {} with repetition:".format(arguments[0]))
            for i in your_combinations.permutations(int(arguments[0]), True):
                print(i)
            print("Permutations size {} without repetition:".format(arguments[0]))
            for i in your_combinations.permutations(int(arguments[0])):
                print(i)
        else:
            print("Unknown command. Type 'help' to show help message.")

# main function
def main():
    # show help message
    print("Type 'help' to show help message.")
    # call cli
    cli()

# start point
if __name__ == "__main__":
    main()
