class InsufficientFundsError(Exception):
    def __init__(self,message):
        print(message)


class ATM_Simulator:
    def __init__(self):
         self.__Account_No = 0
         self.__Balance = 0

    def Choose_No(self):
        print("...Welcom to ATM simulator program....")
        print("\nBank Account Menu:")
        print(" 1.  Deposit")
        print(" 2.  Withdrawal ")
        print(" 3.   Check balance")
        print(" 4. Exit")
        Choose_no = int(input("Enter your choice (1-4):"))
        if Choose_no == 1:
            try :
                self.Deposit_Amount()

            except ValueError:
                print("Account_No not matched ,please try again")

            except Exception:
                print("Deposit amount must be positive")

        elif Choose_no == 2:
            try:
                self.Withdrawal()

            except ValueError:
                print("Account_No not matched ,please try again")


            except InsufficientFundsError:
                pass

            except Exception:
                print(" withdrawal amount must be positive")


        elif Choose_no == 3:
            try:
                self.Check_Balance()

            except ValueError:
                print("Account_No not matched ,please try again")

        elif Choose_no == 4:
            print("Thank you for using the Bank Account program. Goodbye!")

        else :
            print("Invalid choice. Please try again.")

     # settter method
    def Set_Account_No(self,Account_No):
        self.__Account_No = Account_No
        print("account Created Succesfuly")


    def Set_Balance(self,Balance):
        self.__Balance = Balance


    def Get_Accountno(self):
        return self.__Account_No

    def Get_Balance(self):
        return self.__Balance

    def Deposit_Amount(self):
        Account_No = int(input("Please enter your bank account no :"))

        if Account_No != self.__Account_No:
            raise ValueError("Account_No not matched ,please try again")

        amount  = int(input("enter amount "))

        if amount <= 0:
            raise Exception("Deposit amount must be positive")

        self.__Balance = self.__Balance + amount
        print(f"Deposited: ${amount}")

        return self.Choose_No()

    def Withdrawal(self):

        Account_No = int(input("Please enter your bank account no :"))

        if Account_No != self.__Account_No:
            raise ValueError("Account_No not matched ,please try again")

        amount = int(input("enter amount "))
        if amount > self.__Balance :
            raise InsufficientFundsError("Insufficient funds in the account")

        if amount <= 0:
            raise Exception("Withdrawal amount must be positive")

        self.__Balance = self.__Balance - amount
        print(f"Withdrawn: ${amount}")

        return self.Choose_No()

    def Check_Balance(self):

        Account_No = int(input("Please enter your bank account no :"))

        if Account_No != self.__Account_No:
            raise ValueError()

        else :
            print("Your Current Balance is ",self.__Balance)

            return self.Choose_No()


obj = ATM_Simulator()
obj.Set_Account_No(12345678)
obj.Set_Balance(12000)
obj.Choose_No()
