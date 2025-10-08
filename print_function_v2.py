def example():
    return "This is an example function!"

# Add your function here
def suraya_says():
    return "Howdy guys!"

# Main function to execute all contributed functions
def main():
    # Add your function to the list
    functions = [example, suraya_says] 
    for func in functions:
        print(func())

# Run the main function
if __name__ == "__main__":
    main()