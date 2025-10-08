def example():
    return "This is an example function!"

# Add your function here
def miao_says(sentence):
    return "I'm hungry!"

# Main function to execute all contributed functions
def main():
    # Add your function to the list
    functions = [example, miao_says] 
    for func in functions:
        print(func())

# Run the main function
if __name__ == "__main__":
    main()