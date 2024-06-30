class Temperature:
    def __init__(self):
        self.__celsius = 0
        self.__fahrenheit = 0

    def Celsius_to_fahrenheit(self):

        try :
            self.__celsius = int(input("enter the temperature in celsius :"))

        except ValueError:
            print("invlalid number......")

        else :

            self.__fahrenheit = (9/5) * self.__celsius + 32
            print(" temprature in fahrenheit is :",self.__fahrenheit,"F")

    def Fahrenheit_to_celsius(self):

        try:
            self.__fahrenheit = int(input("enter the temperature in fahrenheit :"))

        except ValueError:
            print("invlalid number......")

        else :

            self.__celsius = (self.__fahrenheit - 32) * 5/9
            print(" temprature in celsius is :",self.__celsius,"C")


temp = Temperature()
temp.Celsius_to_fahrenheit()
temp.Fahrenheit_to_celsius