def kg_to_tons(kg):
    # 1 metric ton = 1000 kg, so we divide the kg value by 1000
    return kg / 1000

def main():
    print("--- KG to Metric Tons Converter ---")
    try:
        # Prompt the user for input
        kg_input = float(input("Enter weight in kilograms (kg): "))
        
        if kg_input < 0:
            print("Weight cannot be negative!")
        else:
            # Perform calculation
            tons_output = kg_to_tons(kg_input)
            print(f"{kg_input} kg is equal to {tons_output:.3f} tons.")
            
    except ValueError:
        print("Invalid input. Please enter a numerical value of kilograms.")

if __name__ == "__main__":
    main()
