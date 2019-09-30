# LA CLASE ES EL BLUEPRINT(PLANO) DE UN OBJETO QUE AUN NO SE CREO

class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount


    def deposit(self, amount):
        self.balance=self.balance + amount


    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# EN LA LINEA DE ABAJO CREAMOS UNA SUBCLASS Y ES POR ESO QUE EL ARGUMENTO QUE
# SE PASA ES LA BASE CLASS EN ESTE CASO ES ACCOUNT.

class Checking(Account):
    """This class generates checking account objects"""
    # LINEA DE ABAJO ES PARA CREAR UNA VARIABLE DE CLASE QUE NO SUELEN USARSE
    # MUY SEGUIDO PERO SU UTILIDAD ES QUE SE PUEDEN USAR EN TODAS LAS INSTANCIAS
    # DEL OBJETO
    type="checking"
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

# LA LINEA DE ABAJO ES EL OBJETO
checking=Checking("balance.txt", 1)
checking.transfer(110)
print(checking.balance)
checking.commit()


# account=Account("balance.txt")
# print(account.balance)
# account.deposit(200)
# print(account.balance)
# account.commit()
