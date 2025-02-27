class Vehicle:
    """
    Базовый класс для всех транспортных средств.

    Attributes:
        make (str): Производитель транспортного средства.
        model (str): Модель транспортного средства.
        year (int): Год выпуска транспортного средства.
    """

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Инициализирует объект Vehicle.

        Args:
            make (str): Производитель транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска транспортного средства.
        """
        self.make = make
        self.model = model
        self.year = year

    def __str__(self) -> str:
        """Возвращает строковое представление транспортного средства."""
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление транспортного средства."""
        return f"Vehicle(make='{self.make}', model='{self.model}', year={self.year})"


class Car(Vehicle):
    """
    Класс для легковых автомобилей, наследуется от Vehicle.

    Attributes:
        num_doors (int): Количество дверей в автомобиле.
    """

    def __init__(self, make: str, model: str, year: int, num_doors: int) -> None:
        """
        Инициализирует объект Car, расширяя конструктор Vehicle.

        Args:
            make (str): Производитель автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.
            num_doors (int): Количество дверей в автомобиле.
        """
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def __str__(self) -> str:
        """Возвращает строковое представление легкового автомобиля."""
        return f"{super().__str__()} with {self.num_doors} doors"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление легкового автомобиля."""
        return f"Car(make='{self.make}', model='{self.model}', year={self.year}, num_doors={self.num_doors})"

    def drive(self) -> str:
        """
        Симулирует движение автомобиля.

        Returns:
            str: Сообщение о том, что автомобиль движется.
        """
        return f"{self.make} {self.model} is driving."


class Truck(Vehicle):
    """
    Класс для грузовых автомобилей, наследуется от Vehicle.

    Attributes:
        load_capacity (float): Грузоподъемность грузовика в тоннах.
    """