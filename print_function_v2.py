def example():
    return "This is an example function!"


# Add your function here
def new_function():
    return "Hello!"


def sylwia_says():
    return "Hello"


def iolan_says():
    return "Hola desde la primera fila! :)"


def wafaa_says():
    return "hola"


# Main function to execute all contributed functions
def main():
    # Add your function to the list
    functions = [example, wafaa_says, iolan_says, sylwia_says, new_function]
    for func in functions:
        print(func())


# Run the main function
if __name__ == "__main__":
    main()
