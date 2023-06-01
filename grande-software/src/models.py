from enum import Enum
from typing import List


class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"


class TypeG(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "electric"


class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "ococobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"


class GuitarSpec:
    def __init__(self, builder, model, typeg, back_wood, top_wood, num_strings) -> None:
        self.__builder: Builder = builder
        self.__model = model
        self.__typeg: TypeG = typeg
        self.__back_wood: Wood = back_wood
        self.__top_wood: Wood = top_wood
        self.__num_strings = num_strings

    def get_builder(self) -> Builder:
        return self.__builder

    def get_typeg(self) -> TypeG:
        return self.__typeg

    def get_model(self) -> str:
        return self.__model

    def get_back_wood(self) -> Wood:
        return self.__back_wood

    def get_top_wood(self) -> Wood:
        return self.__top_wood

    def get_num_strings(self) -> str:
        return self.__num_strings

    def matches(self, other_spec) -> bool:
        if self.__builder != other_spec.get_builder():
            return False
        if self.__model and self.__model.lower() != other_spec.get_model().lower():
            return False
        if self.__typeg != other_spec.get_typeg():
            return False
        if self.__back_wood != other_spec.get_back_wood():
            return False
        if self.__top_wood != other_spec.get_top_wood():
            return False
        if self.__num_strings != other_spec.get_num_strings():
            return False
        return True


class Guitar:
    def __init__(self, serial_number, price, spec):
        self.__serial_number = serial_number
        self.__price = price
        self.__spec = spec

    def get_serial_number(self):
        return self.__serial_number

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def get_spec(self):
        return self.__spec


class Inventory:
    def __init__(self):
        self.guitars: List[Guitar] = []

    def add_guitar(self, serial_number, price, spec) -> None:
        guitar = Guitar(
            serial_number=serial_number,
            price=price,
            spec=spec,
        )
        self.guitars.append(guitar)

    def get_guitar(self, serial_number) -> Guitar | None:
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search(self, search_guitar: GuitarSpec) -> List[Guitar]:
        matching_guitars: List[Guitar] = []
        for guitar in self.guitars:
            if guitar.get_spec().matches(search_guitar):
                matching_guitars.append(guitar)
        return matching_guitars


def initialize_inventory(inventory: Inventory):
    spec1 = GuitarSpec(
        Builder.FENDER, "stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6
    )
    inventory.add_guitar("V95693", 1499.95, spec1)
    inventory.add_guitar("V99999", 1599.95, spec1)


def main():
    inventory = Inventory()
    initialize_inventory(inventory)
    what_erin_likes = GuitarSpec(
        Builder.FENDER, "Stratocastor", TypeG.ELECTRIC, Wood.ALDER, Wood.ALDER, 6
    )
    matching_guitars = inventory.search(what_erin_likes)

    if len(matching_guitars) == 0:
        print("Não foi encontrado nenhuma guitarra com o desejado")
    else:
        print("Erin, talvez você goste desta(s): ")
        print("\n----- Lista de guitarra(s) encontrada(s) -----\n")
        for guitar in matching_guitars:
            guitar_spec = guitar.get_spec()
            print(
                f"""        Marca: {guitar_spec.get_builder().value}
        Modelo: {guitar_spec.get_model()}
        Tipo: {guitar_spec.get_typeg().value}
        Madeira traseira e lateral: {guitar_spec.get_back_wood().value}
        Madeira da frente: {guitar_spec.get_top_wood().value}
        Preço: {guitar.get_price()}
            """
            )
        print("\n------------------------------------------\n")


if __name__ == "__main__":
    main()
