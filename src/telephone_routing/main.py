from module import Module

if __name__ == "__main__":
    print("Processing data...")
    module = Module()
    print("Load all operators completed!")
    while True:
        input_number = input("Enter a telephone number: \n")
        if input_number == "exit":
            print("Exiting...")
            break
        else:
            result = module.routing_service.find_cheapest_operator(input_number)
            match result.status:
                case "success":
                    print(
                        f"Cheapest Operator: {result.data['operator']}, Price: {result.data['price']}"
                    )
                case "invalid":
                    print(f"Invalid telephone number: {input_number}")
                case "not_found":
                    print(
                        f"No operator supporting this telephone number: {input_number}"
                    )
