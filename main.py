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
            command = input().strip()
        except KeyboardInterrupt:
            # handle ctrl + c
            print()
            continue
        except EOFError:
            # handle ctrl + d
            print()
            break

        commands_str = command
        # split command to get command and arguments
        commands = commands_str.split()
        # check if command is empty
        if len(commands) == 0:
            continue
        # get command
        command = commands[0]

        # check command
        if command == "exit":
            break
        elif command == "help":
            print("help - show this message")
            print("exit - exit program")

            print("Power Set:")
            print("\tlist power ...")
            print("\tsave power ...")
            print("\tcount power ...")
            print("")

            print("Combinations:")
            print("\tlist combinations with repeat ...")
            print("\tsave combinations with repeat ...")
            print("\tcount combinations with repeat ...")

            print("\tlist combinations without repeat ...")
            print("\tsave combinations without repeat ...")
            print("\tcount combinations without repeat ...")
            print("")

            print("Permutations:")
            print("\tlist permutations with repeat ...")
            print("\tsave permutations with repeat ...")
            print("\tcount permutations with repeat ...")

            print("\tlist permutations without repeat ...")
            print("\tsave permutations without repeat ...")
            print("\tcount permutations without repeat ...")

        # Power
        elif commands_str.startswith("list power"):
            arguments = commands_str[len("list power"):].strip()
            your_combinations = YourCombinations(arguments)
            for i in your_combinations.powerSet():
                print(i)
        elif commands_str.startswith("save power"):
            arguments = commands_str[len("save power"):].strip()
            your_combinations = YourCombinations(arguments)
            file = open("power_set.txt", "w")
            file.write(str(your_combinations.powerSet()))
            file.close()
            print("Saved to power_set.txt")
        elif commands_str.startswith("count power"):
            arguments = commands_str[len("count power"):].strip()
            your_combinations = YourCombinations(arguments)
            print("Count Power set:")
            print(len(your_combinations.powerSet()))

        # Combinations with repeat
        elif commands_str.startswith("list combinations with repeat"):a
            arguments = commands_str[len("list combinations with repeat"):].strip()
            for i in your_combinations.combinations(int(arguments[0]), True):
                print(i)
        elif commands_str.startswith("save combinations with repeat"):
            arguments = commands_str[len("save combinations with repeat"):].strip()
            file = open("combinations_with_repeat.txt", "w")
            file.write(str(your_combinations.combinations(int(arguments[0]), True)))
            file.close()
            print("Saved to combinations_with_repeat.txt")
        elif commands_str.startswith("count combinations with repeat"):
            arguments = commands_str[len("count combinations with repeat"):].strip()
            print(len(your_combinations.combinations(int(arguments[0]), True)))

        # Combinations without repeat
        elif commands_str.startswith("list combinations without repeat"):
            arguments = commands_str[len("list combinations without repeat"):].strip()
            for i in your_combinations.combinations(int(arguments[0])):
                print(i)
        elif commands_str.startswith("save combinations without repeat"):
            arguments = commands_str[len("save combinations without repeat"):].strip()
            file = open("combinations_without_repeat.txt", "w")
            file.write(str(your_combinations.combinations(int(arguments[0]))))
            file.close()
            print("Saved to combinations_without_repeat.txt")
        elif commands_str.startswith("count combinations without repeat"):
            arguments = commands_str[len("count combinations without repeat"):].strip()
            print(len(your_combinations.combinations(int(arguments[0]))))

        # Permutations with repeat
        elif commands_str.startswith("list permutations with repeat"):
            arguments = commands_str[len("list permutations with repeat"):].strip()
            for i in your_combinations.permutations(int(arguments[0]), True):
                print(i)
        elif commands_str.startswith("save permutations with repeat"):
            arguments = commands_str[len("save permutations with repeat"):].strip()
            file = open("permutations_with_repeat.txt", "w")
            file.write(str(your_combinations.permutations(int(arguments[0]), True)))
            file.close()
            print("Saved to permutations_with_repeat.txt")
        elif commands_str.startswith("count permutations with repeat"):
            arguments = commands_str[len("count permutations with repeat"):].strip()
            print(len(your_combinations.permutations(int(arguments[0]), True)))

        # Permutations without repeat
        elif commands_str.startswith("list permutations without repeat"):
            arguments = commands_str[len("list permutations without repeat"):].strip()
            for i in your_combinations.permutations(int(arguments[0]), False):
                print(i)
        elif commands_str.startswith("save permutations without repeat"):
            arguments = commands_str[len("save permutations without repeat"):].strip()
            file = open("permutations_without_repeat.txt", "w")
            file.write(str(your_combinations.permutations(int(arguments[0]), False)))
            file.close()
            print("Saved to permutations_without_repeat.txt")
        elif commands_str.startswith("count permutations without repeat"):
            arguments = commands_str[len("count permutations without repeat"):].strip()
            print(len(your_combinations.permutations(int(arguments[0]), False)))

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
