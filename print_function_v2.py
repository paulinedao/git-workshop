def example():
    return "This is an example function!"

# Add your function here
def daniella_says():
    return "Daniella says hi!"
# Main function to execute all contributed functions
def main():
    # Add your function to the list
    functions = [example, daniella_says] 
    for func in functions:
        print(func())

# Run the main function
if __name__ == "__main__":
    main()