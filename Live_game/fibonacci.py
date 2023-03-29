
class FCC:

    def __init__(self) -> None:
        self._numbers = list()

    def fibonacci(self, last, current):
        if current > 1000:
            next = last + current
            print(last)
            self.fibonacci(last = current, current = next)
        else:
            print('listo!')

generator = FCC()
generator.fibonacci(last = 0, current = 1)
            
