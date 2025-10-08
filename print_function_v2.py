def example():
    return "This is an example function!"

# Add your function here
def Dinia_says_hello():
    return "Welcome"

# Main function to execute all contributed functions
def main():
    # Add your function to the list
    functions = [example, Dinia_says_hello] 
    for func in functions:
        print(func())

# Run the main function
if __name__ == "__main__":
    main()