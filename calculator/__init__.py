Number = int | float

# modificata da Lorenzo Fattori, 2024-06-10
# Questa classe implementa la logica di una calcolatrice. 
# La calcolatrice mantiene un'espressione come stringa, e fornisce metodi per aggiungere cifre, 
# operazioni e il punto decimale all'espressione. 
# Il metodo compute_result() valuta l'espressione e restituisce il risultato. 
# Se l'espressione è invalida, viene sollevata un'eccezione con un messaggio di errore.
class Calculator:

    def __init__(self):
        self.reset()

    def _ensure_is_digit(self, value: int | str):
        if isinstance(value, str):
            value = int(value)
        if value not in range(10):
            raise ValueError("Value must a digit in [0, 9]: " + value)
        return value
    
    def reset(self):
        self.expression = ""

    def _append(self, value):
        self.expression += str(value)
    
    def digit(self, value: int | str):
        value = self._ensure_is_digit(value)
        self._append(value)
    
    def plus(self):
        self._append("+")

    def minus(self):
        self._append("-")
    
    def multiply(self):
        self._append("*")
    
    def divide(self):
        self._append("/")

    def dot(self):
        self._append(".")
    
    def compute_result(self) -> Number:
        try:
            result = eval(self.expression)
            if isinstance(result, Number):
                self.expression = str(result)
                return result
            else:
                raise ValueError("Result is not a number: " + str(result))
        except SyntaxError as e:
            expression = self.expression
            self.expression = ""
            raise ValueError("Invalid expression: " + expression) from e
