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
    ELETRIC = "eletric"


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
    def __init__(
        self,
        builder,
        model,
        typeg,
        back_wood,
        top_wood,
    ) -> None:
        self.__builder: Builder = builder
        self.__model = model
        self.__typeg: TypeG = typeg
        self.__back_wood: Wood = back_wood
        self.__top_wood: Wood = top_wood

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


class Guitar:
    def __init__(
        self, builder, model, typeg, back_wood, top_wood, serial_number=None, price=None
    ):
        self.__serial_number = serial_number
        self.__price = price
        self.spec = GuitarSpec(builder, model, typeg, back_wood, top_wood)

    def get_serial_number(self):
        return self.__serial_number

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price


class Inventory:
    def __init__(self):
        self.guitars: List[Guitar] = []

    def add_guitar(
        self, builder, model, typeg, back_wood, top_wood, serial_number, price
    ) -> None:
        guitar = Guitar(
            builder,
            model,
            typeg,
            back_wood,
            top_wood,
            serial_number=serial_number,
            price=price,
        )
        self.guitars.append(guitar)

    def get_guitar(self, serial_number) -> Guitar | None:
        for guitar in self.guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar
        return None

    def search_guitar(self, search_guitar: Guitar) -> List[Guitar]:
        corresponding_guitars: List[Guitar] = []
        for guitar in self.guitars:
            if (
                search_guitar.spec.get_builder()
                and search_guitar.spec.get_builder().value.lower()
                != guitar.spec.get_builder().value.lower()
            ):
                continue
            model = search_guitar.spec.get_model()
            if (
                model
                and model != ""
                and model.lower() != guitar.spec.get_model().lower()
            ):
                continue
            if (
                search_guitar.spec.get_typeg()
                and search_guitar.spec.get_typeg().value.lower()
                != guitar.spec.get_typeg().value.lower()
            ):
                continue
            if (
                search_guitar.spec.get_back_wood()
                and search_guitar.spec.get_back_wood().value.lower()
                != guitar.spec.get_back_wood().value.lower()
            ):
                continue
            if (
                search_guitar.spec.get_top_wood()
                and search_guitar.spec.get_top_wood().value.lower()
                != guitar.spec.get_top_wood().value.lower()
            ):
                continue
            corresponding_guitars.append(guitar)
        return corresponding_guitars


inventory = Inventory()

inventory.add_guitar(
    Builder.FENDER,
    "Stratocastor",
    TypeG.ELETRIC,
    Wood.ALDER,
    Wood.ALDER,
    "V95693",
    1499.95,
)

inventory.add_guitar(
    Builder.OLSON,
    "Stratocastor",
    TypeG.ACOUSTIC,
    Wood.CEDAR,
    Wood.ALDER,
    "V91317",
    1700.95,
)


whatErinLikes = Guitar(None, "Stratocastor", None, None, Wood.ALDER)
guitars = inventory.search_guitar(whatErinLikes)
if len(guitars) == 0:
    print("Não foi encontrado nenhuma guitarra com o desejado")
elif len(guitars) == 1:
    guitar = guitars[0]
    print(
        f"""    Marca: {guitar.spec.get_builder()}
    Modelo: {guitar.spec.get_model()}
    Tipo: {'elétrica' if guitar.spec.get_typeg() == 'eletric' else 'acústica'}
    Madeira traseira e lateral: {guitar.spec.get_back_wood()}
    Madeira da frente: {guitar.spec.get_top_wood()}
    Preço: {guitar.get_price()}"""
    )
else:
    print("\n----- Lista de guitarras encontradas -----\n")
    for guitar in guitars:
        print(
            f"""    Marca: {guitar.spec.get_builder()}
    Modelo: {guitar.spec.get_model()}
    Tipo: {guitar.spec.get_typeg()}
    Madeira traseira e lateral: {guitar.spec.get_back_wood()}
    Madeira da frente: {guitar.spec.get_top_wood()}
    Preço: {guitar.get_price()}

        """
        )
    print("\n------------------------------------------\n")
