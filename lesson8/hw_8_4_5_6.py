# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве
# единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например
# словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем
# данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать
# строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from abc import abstractmethod, ABC

class Technics(ABC):
    def __init__(self, model, serial_no):
        self.model = model
        self.serial_no = serial_no
        self.department = None

    def _set_department(self, department): #присвоить нашу технику какому-то департаменту
        self.department = department

    @abstractmethod
    def __call__(self, data):
        pass
    @abstractmethod
    def __str__(self): #для того, чтобы сделать красивый вывод по нашему экземпляру
        pass

class Printer(Technics):

    def print_smth(self, data: str):
        return f"Printer {self.model} s/n {self.serial_no} printed {data}"

    def __call__(self, data):
        self.print_smth(data)

    def __str__(self):
        return f"Printer model {self.model} s/n {self.serial_no}"

class Xerox(Technics):
    def copy_smth(self, data: str):
        return f"Xerox {self.model} s/n {self.serial_no} copied {data}"

    def __call__(self, data):
        self.copy_smth(data)

    def __str__(self):
        return f"Printer model {self.model} s/n {self.serial_no}"

class Scanner(Technics):
    def scan_smth(self, data):
        return f"Scanner {self.model} s/n {self.serial_no} scanned {data}"

    def __call__(self, data):
        self.scan_smth(data)

    def __str__(self):
        return f"Printer model {self.model} s/n {self.serial_no}"

class OverflowError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Warehouse:
    def __init__(self, max_volume):
        self.max_volume = max_volume
        self.storage = {
            "scanners": set(),
            "printers": set(),
            "xeroxes": set()
        }
        self.add_mapper = {Scanner: "scanners",
                           Printer: "printers",
                           Xerox: "xeroxes"}
        self.total = 0

    def get_several_tecs_to_warehouse(self, num: int, tech_list):
        if type(num) != int:
            raise ValueError("Невалидное число техники! Введите число!")
        for tech in tech_list[:num]:
            self.get_tech_to_warehouse(tech)

    def get_tech_to_warehouse(self, technics: Technics):
        if self.total == self.max_volume:
            raise OverflowError("Склад заполнен до отказа!")
        self.storage[self.add_mapper[type(technics)]].add(technics)
        technics._set_department("warehouse")
        self.total += 1
    def get_tech_to_department(self, tech_type, department):
        tech_to_dept = self.storage[tech_type].pop()
        tech_to_dept._set_department(department)
        self.total -= 1

    def __call__(self, *args, **kwargs):
        self.get_tech_to_warehouse(*args, **kwargs)
    def __str__(self):
        return f"Warehouse max capacity {self.max_volume} current {self.total}"

printer = Printer(1, 2)
printer_2 = Printer(1, 3)
scanner = Scanner(2, 3)
scanner_2 = Scanner(2, 5)
warehouse = Warehouse(10)
tech_list = [printer, printer_2, scanner, scanner_2]
warehouse.get_several_tecs_to_warehouse(3, tech_list)

