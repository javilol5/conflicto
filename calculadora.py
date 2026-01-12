class Calculadora:

    def __init__(self, num1, num2, operador):
        self.__setNum1(num1)
        self.__setNum2(num2) # Comentario del colaborador
        self.__setOperador(operador)

    def __setNum1(self, num1):
        if num1.isdigit():
            self.__num1 = float(num1)
        else:
            raise ValueError("Numero o operador invalido")

    def __setNum2(self, num2):
        if num2.isdigit():
            self.__num2 = float(num2)
        else:
            raise ValueError("Numero o operador invalido")

    def __setOperador(self, operador):
        if operador in ("/", "*", "-", "+"):
            self.__operador = operador
        else:
            raise ValueError("Numero o operador invalido")


    def getNum1(self):
        return self.__num1
    def getNum2(self):
        return self.__num2
    def getOperador(self):
        return self.__operador

    def calcular(self):
        if self.__operador == "+":
            return self.__num1 + self.__num2
        elif self.__operador == "-":
            return self.__num1 - self.__num2
        elif self.__operador == "*":
            return self.__num1 * self.__num2
        elif self.__operador == "/":
            if self.__num2 != 0:
                return self.__num1 / self.__num2
            else:
                division0 = r"""
                     _.-^^---....,,--
                 _--                  --_
                <                        >)
                |                         |
                 \._                   _./
                    ```--. . , ; .--'''
                          | |   |
                       .-=||  | |=-.
                       `-=#$%&%$#=-'
                          | ;  :|
                 _____.,-#%&$@%#~,._____
                 NO SE PUEDE DIVIDIR POR 0
                """

                return division0


if __name__ == "__main__":
    calculo1 = Calculadora("1", "2", "+")
    print(calculo1.calcular())