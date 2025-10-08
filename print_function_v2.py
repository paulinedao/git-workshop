def example():
    return "This is an example function!"

def iolan_says():
    return "Hola desde la primera fila! :)"

# Main function to execute all contributed functions
def main():
    # Add your function to the list
    functions = [example, iolan_says] 
    for func in functions:
        print(func())

# Run the main function
if __name__ == "__main__":
    main()