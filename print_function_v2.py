def example():
    return "This is an example function!"

def brina_says():
    return "Bye Bye!"

# Main function to execute all contributed functions
def main():
    # Add your function to the list
    functions = [example,brina_says] 
    for func in functions:
        print(func())

# Run the main function
if __name__ == "__main__":
    main()