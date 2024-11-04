from module import Module

if __name__ == "__main__":
    print("Processing data")
    module = Module()
    while True:
        input_number = input("Enter a telephone number: \n")
        if input_number == "exit":
            print("Exiting...")
            break
        else:
            result = module.routing_service.find_cheapest_operator(input_number)
            print(result)
