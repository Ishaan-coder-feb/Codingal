class RomanConverter:
    def __init__(self):
        self.value_map = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

    def int_to_roman(self, num):
        """
        Convert an integer to a Roman numeral.

        :param num: Integer value to be converted (1 <= num <= 3999)
        :return: Roman numeral as a string
        """
        if not 1 <= num <= 3999:
            raise ValueError("Number out of range (must be between 1 and 3999)")

        roman_numeral = ""
        for value, numeral in self.value_map:
            while num >= value:
                roman_numeral += numeral
                num -= value
        return roman_numeral
if __name__ == "__main__":
    converter = RomanConverter()

    try:
        number = int(input("Enter an integer (1-3999): "))
        roman_numeral = converter.int_to_roman(number)
        print(f"The Roman numeral representation of {number} is {roman_numeral}")
    except ValueError as e:
        print(e)
