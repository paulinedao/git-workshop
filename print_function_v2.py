def example():
    return "This is an example function!"

def ana_says():
    return "Quiero comer"
def main():
    # Add your function to the list
    functions = [example, ana_says] 
    for func in functions:
        print(func())

# Run the main function
if __name__ == "__main__":
    main()