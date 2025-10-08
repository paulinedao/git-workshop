def example():
    return "This is an example function!"


# Add your function here
def new_function():
    return "Hello!"


# Main function to execute all contributed functions
def main():
    # Add your function to the list
    functions = [example, new_function]
    for func in functions:
        print(func())


# Run the main function
if __name__ == "__main__":
    main()
