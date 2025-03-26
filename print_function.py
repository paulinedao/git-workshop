# Contributors' Functions

def example():
    return "This is an example function!"

def juls_says():
    return "Hello, it's Juls!"
# Add your function here
def roselly_says():
    return "Summer is coming"

def alessia_says():
    return "Ciao!"

def yania_says():
    return "Everyone"

def lorena_says():
    return "Hi everyone! I'm Lorena"

def pauline_says():
    return "Hello, World!"

def yania_says_again():
    return "says what?"
    
# Main function to execute all contributed functions
def main():
    # Add your function to the list
    functions = [example, pauline_says, yania_says_again, yania_says, roselly_says, lorena_says, juls_says, alessia_says] 
    
    for func in functions:
        print(func())

# Run the main function
if __name__ == "__main__":
    main()
