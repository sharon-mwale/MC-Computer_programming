if __name__ =="__main__":
    def sum_digits(n):
        if n < 10:
            return n
        else:
            return n % 10 + sum_digits(n // 10)
    result = sum_digits(123)
    print(result)  # Output: 6

 