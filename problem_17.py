ones = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
}
tens = {
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
    60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
}

def number_to_words(n):
    if n in ones:
        return ones[n]
    if n in tens:
        return tens[n]
    if n < 100:
        quotient, reminder = divmod(n, 10) #21-->quotient=2,reminder = 1
        return tens[quotient * 10] + (ones[reminder]) #tens[2*10]=tens[20]=twenty  ones[1] = one
    if n < 1000:
        quotient, reminder = divmod(n, 100)
        word = ones[quotient] + "hundred"
        if reminder:
            word += "and" + number_to_words(reminder)
        return word
    if n == 1000:
        return "onethousand"

total = sum(len(number_to_words(i)) for i in range(1, 1001))
print(total)  # 21124