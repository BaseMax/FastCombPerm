from YourCombinations import YourCombinations

# cli to ask user to enter and prompt
def cli():
    # infinity loop to ask user input
    while True:
        print("> ", end = "")
        # get user input
        user_input = input()
        # split user input
        user_input = user_input.split(" ")
        # check user input
        if user_input[0] == "exit":
            break
        elif user_input[0] == "help":
            print("help - show this message")
            print("exit - exit program")
            print("set - set elements")
            print("power - show power set")
            print("combinations - show combinations")
            print("permutations - show permutations")
        elif user_input[0] == "set":
            elements = user_input[1:]
            your_combinations = YourCombinations(elements)
        elif user_input[0] == "power":
            # show power set
            print("Power set:")
            for i in your_combinations.powerSet():
                print(i)
        elif user_input[0] == "combinations":
            # show combinations
            print("Combinations size {} with repetition:".format(user_input[1]))
            for i in your_combinations.combinations(int(user_input[1]), True):
                print(i)
            print("Combinations size {} without repetition:".format(user_input[1]))
            for i in your_combinations.combinations(int(user_input[1])):
                print(i)
        elif user_input[0] == "permutations":
            # show permutations
            print("Permutations size {} with repetition:".format(user_input[1]))
            for i in your_combinations.permutations(int(user_input[1]), True):
                print(i)
            print("Permutations size {} without repetition:".format(user_input[1]))
            for i in your_combinations.permutations(int(user_input[1])):
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
