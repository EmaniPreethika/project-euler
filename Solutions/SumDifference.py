#https://projecteuler.net/problem=6
#Sum of squares of first n numbers: n(n+1)(2n+1)/6
#Sum of first N numbers : n*(n+1)/2
'''You can calculate the abve two by running it though a for loop but that would be 2 * O(N) ~ O(N). But by calculating via formula the time complexity reduces to O(1)
'''
class SumSquareDifference:
    def __init__(self):
        self.sum_of_squares = 0
        self.square_of_sum_of_numbers = 0
        self.result = 0

    def calculate(self, n):
        self.sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
        self.square_of_sum_of_numbers = (n * (n + 1) // 2) ** 2
        self.result = self.square_of_sum_of_numbers - self.sum_of_squares

        return self.result


def main():
    n = int(input("Enter Number: "))
    obj = SumSquareDifference()
    result = obj.calculate(n)
    print(result)
    
if __name__ == "__main__":
    main()