def decimal_to_base(n:int, base:int) -> str:
    """Convert a decimal integer n to a string in the given base (2-36)."""
    if not (2 <= base <= 36):
        raise ValueError("Base must be between 2 and 36")
    if n == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    negative = n < 0
    n = abs(n)
    while n > 0:
        result = digits[n % base] + result
        n //= base
    if negative:
        result = "-" + result
    return result

def convert_base(num_str:str, from_base:int, to_base:int) -> str:
    """
    Convert num_str from from_base to to_base.
    num_str: string representation of the number in from_base
    from_base, to_base: integers between 2 and 36
    Returns: string representation of the number in to_base
    """
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        raise ValueError("Bases must be between 2 and 36")
    # Convert input string to decimal integer
    decimal_value = int(num_str, from_base)
    # Convert decimal integer to target base
    return decimal_to_base(decimal_value, to_base)

def main():
    print("Base Converter")
    try:
        num_str = input("Enter the number: ")
        from_base = int(input("Enter the base of the number (2-36): "))
        to_base = int(input("Enter the base to convert to (2-36): "))
        converted = convert_base(num_str, from_base, to_base)
        print(f"{num_str} (base {from_base}) in base {to_base} is: {converted}")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
