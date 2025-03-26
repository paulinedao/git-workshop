# Contributors' Functions

def example():
    return "This is an example function!"

# Add your function here
def yania_says():
    return "Everyone"

def pauline_says():
    return "Hello, World!"

def yania_says_again():
    return "says what?"
    
def alexandra_says():
    return "I'm comfused!"  
# Main function to execute all contributed functions
def main():
    # Add your function to the list
    functions = [example, pauline_says, yania_says_again, yania_says alexandra_says] 
    for func in functions:
        print(func())

# Run the main function
if __name__ == "__main__":
    main()
