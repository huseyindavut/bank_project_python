def convert_to_kbps(value: str) -> float:
    """
    Converts the throughput value to Kbps based on its unit.
    Expected units: Kbps, Mbps, Gbps.
    """
    number, unit = value.split()
    number = float(number)

    # Conversion based on the unit
    if unit.lower() == 'kbps':
        return number
    elif unit.lower() == 'mbps':
        return number * 1000  # 1 Mbps = 1000 Kbps
    elif unit.lower() == 'gbps':
        return number * 1000000  # 1 Gbps = 1000000 Kbps
    else:
        raise ValueError(f"Unknown unit: {unit}")

def calculate_jfi(throughputs: list) -> float:
    """
    Calculate the Jains Fairness Index based on a list of throughput values.
    """
    N = len(throughputs)
    sum_x = sum(throughputs)
    sum_x_squared = sum(x ** 2 for x in throughputs)

    # JFI formula
    jfi = (sum_x ** 2) / (N * sum_x_squared)
    return jfi

def main():
    # Read throughput values from the file
    input_file = r'C:\Users\saski\Desktop\python\throughput_values.txt'

    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()

        # Process each line and convert throughput values to Kbps
        throughputs = []
        for line in lines:
            throughput_value = line.strip()
            if throughput_value:
                throughputs.append(convert_to_kbps(throughput_value))

        # Calculate JFI
        jfi = calculate_jfi(throughputs)
        print(f"The Jains fairness index is: {jfi:.4f}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
