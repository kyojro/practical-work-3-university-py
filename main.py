# объект - единица информации в памяти.
# экземпляр - конкретный объект какого-то класса.
# класс - инструкция по созданию объектов определенного типа.
# метод - функция в классе для воздействия на объект.
# поля или свойства - переменные в классе.
# атрибуты - все имена в классе: переменных и методов.
class Purse:
    # __init__ = метод_конструктор.
    # код внутри этого метода исполняется тогда,
    # когда создается экземпляр какого-то класса.

    # нужно для того, чтобы во время создания класса,
    # передать ему какие-то значения(то есть - свойства)
    def __init__(self, valuta, name="Unknown"):
        if valuta not in ("USD", "EUP"):
            raise ValueError
        self.__money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany

    def top_down_balance(self, howmany):
        if self.__money - howmany < 0:
            print("Error, u dont have balance")
            raise ValueError("Error")
        self.__money = self.__money - howmany
        return howmany

    def info(self):
        print(self.__money)

    # __del__ = метод_деструктор.
    # код исполнится во время удаления объекта.
    def __del__(self):
        print("Delete purse")


x = Purse("USD")
y = Purse("USD", "Bill")
y.top_up_balance(10)
x.top_up_balance(y.top_down_balance(7))
x.info()
y.info()
