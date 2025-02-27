def __init__(self, make: str, model: str, year: int, load_capacity: float) -> None:
    """
    Инициализирует объект Truck, расширяя конструктор Vehicle.

    Args:
        make (str): Производитель грузовика.
        model (str): Модель грузовика.
        year (int): Год выпуска грузовика.
        load_capacity (float): Грузоподъемность грузовика в тоннах.
    """
    super().__init__(make, model, year)
    self._load_capacity = load_capacity  # Инкапсуляция атрибута, чтобы предотвратить его изменение извне.


def __str__(self) -> str:
    """Возвращает строковое представление грузового автомобиля."""
    return f"{super().__str__()} with a load capacity of {self._load_capacity} tons"


def __repr__(self) -> str:
    """Возвращает формальное строковое представление грузового автомобиля."""
    return f"Truck(make='{self.make}', model='{self.model}', year={self.year}, load_capacity={self._load_capacity})"


def load(self, weight: float) -> str:
    """
    Загружает груз в грузовик, если вес меньше грузоподъемности.

    Args:
        weight (float): Вес груза в тоннах.

    Returns:
        str: Сообщение о результате загрузки.

    Raises:
        ValueError: Если вес груза превышает грузоподъемность.
    """
    if weight > self._load_capacity:
        raise ValueError(f"Cannot load {weight} tons. Exceeds capacity of {self._load_capacity} tons.")
    return f"Loaded {weight} tons into the truck."


if __name__ == "__main__":
    # Пример использования классов
    car = Car("Toyota", "Corolla", 2020, 4)
    print(car)
    print(car.drive())

    truck = Truck("Volvo", "FH", 2019, 18.0)
    print(truck)
    print(truck.load(15.0))