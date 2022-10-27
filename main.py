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
            print("version - show version")
            print("exit - exit program")
            print("set ... ... ...")
            print("")

            print("Power Set:")
            print("\tlist power")
            print("\tsave power")
            print("\tcount power")

            print("Combinations:")
            print("\tlist combinations with repeat <n>")
            print("\tsave combinations with repeat <n>")
            print("\tcount combinations with repeat <n>")

            print("\tlist combinations without repeat <n>")
            print("\tsave combinations without repeat <n>")
            print("\tcount combinations without repeat <n>")
            print("")

            print("Permutations:")
            print("\tlist permutations with repeat <n>")
            print("\tsave permutations with repeat <n>")
            print("\tcount permutations with repeat <n>")

            print("\tlist permutations without repeat <n>")
            print("\tsave permutations without repeat <n>")
            print("\tcount permutations without repeat <n>")
        elif command == "version":
            print("1.0.0")
        elif command == "set":
            arguments = commands[1:]
            your_combinations = YourCombinations(arguments)

        # Power
        elif commands_str.startswith("list power"):
            for i in your_combinations.powerSet():
                print(i)
        elif commands_str.startswith("save power"):
            file = open("power_set.txt", "w")
            # file.write(str(your_combinations.powerSet()))
            for i in your_combinations.powerSet():
                file.write(str(i) + "\n")
            file.close()
            print("Saved to power_set.txt")
        elif commands_str.startswith("count power"):
            print("Count Power set:")
            print(len(your_combinations.powerSet()))

        # Combinations with repeat
        elif commands_str.startswith("list combinations with repeat"):
            argument_length = commands_str[len("list combinations with repeat"):].strip()
            if not argument_length.isdigit() or int(argument_length) <= 0:
                print("Invalid argument")
                continue

            for i in your_combinations.combinations(int(argument_length), True):
                print(i)
        elif commands_str.startswith("save combinations with repeat"):
            argument_length = commands_str[len("save combinations with repeat"):].strip()
            if not argument_length.isdigit() or int(argument_length) <= 0:
                print("Invalid argument")
                continue

            file = open("combinations_with_repeat.txt", "w")
            # file.write(str(your_combinations.combinations(int(argument_length), True)))
            for i in your_combinations.combinations(int(argument_length), True):
                file.write(str(i) + "\n")
            file.close()
            print("Saved to combinations_with_repeat.txt")
        elif commands_str.startswith("count combinations with repeat"):
            argument_length = commands_str[len("count combinations with repeat"):].strip()
            if not argument_length.isdigit() or int(argument_length) <= 0:
                print("Invalid argument")
                continue

            print(len(your_combinations.combinations(int(argument_length), True)))

        # Combinations without repeat
        elif commands_str.startswith("list combinations without repeat"):
            argument_length = commands_str[len("list combinations without repeat"):].strip()
            if not argument_length.isdigit() or int(argument_length) <= 0:
                print("Invalid argument")
                continue

            for i in your_combinations.combinations(int(argument_length)):
                print(i)
        elif commands_str.startswith("save combinations without repeat"):
            argument_length = commands_str[len("save combinations without repeat"):].strip()
            if not argument_length.isdigit() or int(argument_length) <= 0:
                print("Invalid argument")
                continue

            file = open("combinations_without_repeat.txt", "w")
            # file.write(str(your_combinations.combinations(int(argument_length))))
            for i in your_combinations.combinations(int(argument_length), False):
                file.write(str(i) + "\n")
            file.close()
            print("Saved to combinations_without_repeat.txt")
        elif commands_str.startswith("count combinations without repeat"):
            argument_length = commands_str[len("count combinations without repeat"):].strip()
            if not argument_length.isdigit() or int(argument_length) <= 0:
                print("Invalid argument")
                continue

            print(len(your_combinations.combinations(int(argument_length))))

        # Permutations with repeat
        elif commands_str.startswith("list permutations with repeat"):
            argument_length = commands_str[len("list permutations with repeat"):].strip()
            if not argument_length.isdigit() or int(argument_length) <= 0:
                print("Invalid argument")
                continue

            for i in your_combinations.permutations(int(argument_length), True):
                print(i)
        elif commands_str.startswith("save permutations with repeat"):
            argument_length = commands_str[len("save permutations with repeat"):].strip()
            if not argument_length.isdigit() or int(argument_length) <= 0:
                print("Invalid argument")
                continue

            file = open("permutations_with_repeat.txt", "w")
            # file.write(str(your_combinations.permutations(int(argument_length), True)))
            for i in your_combinations.permutations(int(argument_length), True):
                file.write(str(i) + "\n")
            file.close()
            print("Saved to permutations_with_repeat.txt")
        elif commands_str.startswith("count permutations with repeat"):
            argument_length = commands_str[len("count permutations with repeat"):].strip()
            if not argument_length.isdigit() or int(argument_length) <= 0:
                print("Invalid argument")
                continue

            print(len(your_combinations.permutations(int(argument_length), True)))

        # Permutations without repeat
        elif commands_str.startswith("list permutations without repeat"):
            argument_length = commands_str[len("list permutations without repeat"):].strip()
            if not argument_length.isdigit() or int(argument_length) <= 0:
                print("Invalid argument")
                continue
            for i in your_combinations.permutations(int(arguments), False):
                print(i)
        elif commands_str.startswith("save permutations without repeat"):
            argument_length = commands_str[len("save permutations without repeat"):].strip()
            if not argument_length.isdigit() or int(argument_length) <= 0:
                print("Invalid argument")
                continue

            file = open("permutations_without_repeat.txt", "w")
            # file.write(str(your_combinations.permutations(int(arguments), False)))
            for i in your_combinations.permutations(int(argument_length), False):
                file.write(str(i) + "\n")
            file.close()
            print("Saved to permutations_without_repeat.txt")
        elif commands_str.startswith("count permutations without repeat"):
            argument_length = commands_str[len("count permutations without repeat"):].strip()
            if not argument_length.isdigit() or int(argument_length) <= 0:
                print("Invalid argument")
                continue
            print(len(your_combinations.permutations(int(arguments), False)))

        else:
            print("Unknown command. Type 'help' to show help message.")

# main function
def main():
    # show help message
    print("Fast Combinations and Permutations Calculator - version 1.0.0")
    print("")
    print("Type 'help' to show help message.")
    # call cli
    cli()

# start point
if __name__ == "__main__":
    main()
