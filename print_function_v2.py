def example():
    return "This is an example function!"

# Add your function here
def ana_says():
    return "I wanna eat more!!"

def ana_also_says():
    return "WORK MORE"

# Main function to execute all contributed functions
def main():
    # Add your function to the list
    functions = [example, ana_says, ana_also_says] 
    for func in functions:
        print(func())

# Run the main function
if __name__ == "__main__":
    main()