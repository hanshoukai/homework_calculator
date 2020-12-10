class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            b == 0
            raise ZeroDivisionError("除数不能为零")
        except ZeroDivisionError as e:
            print("引发异常：", repr(e))
            raise
        finally:
            return a / b
