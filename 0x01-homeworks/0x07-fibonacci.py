if __name__ =="__main__":
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    result = fibonacci(8)
    print(result)  
