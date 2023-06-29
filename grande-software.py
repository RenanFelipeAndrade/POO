from enum import Enum
from typing import TypedDict, NotRequired, List


class Builder(Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collings"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "prs"
    ANY = "any"


class InstrumentType(Enum):
    GUITAR = "Guitar"
    BANJO = "Banjo"
    DOBRO = "Dobro"
    FIDDLE = "Fiddle"
    BASS = "Bass"
    MANDOLIN = "Mandolin"
    SAX = "Sax"
    UNSPECIFIED = "Unspecified"


class Style(Enum):
    A = "a"
    F = "f"


class Type(Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "electric"


class Wood(Enum):
    INDIAN_ROSEWOOD = "indian_rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian_rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "cocobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"


# just to be used as a type
class Properties(TypedDict):
    instrument_type: NotRequired[InstrumentType]
    builder: NotRequired[Builder]
    model: NotRequired[str]
    type: NotRequired[Type]
    num_strings: NotRequired[int]
    top_wood: NotRequired[Wood]
    back_wood: NotRequired[Wood]
    style: NotRequired[Style]


class InstrumentSpec:
    def __init__(self, properties: None | Properties = None):
        if properties is None:
            self.properties: Properties = {}
        else:
            self.properties = properties.copy()

    def get_property(self, property_name):
        return self.properties.get(property_name)

    def get_properties(self) -> Properties:
        return self.properties

    def matches(self, other_spec) -> bool:
        for property_name in other_spec.get_properties():
            if (
                self.properties.get(property_name).value
                != other_spec.get_property(property_name).value
            ):
                return False
        return True


class Instrument:
    def __init__(self, serial_number: str, price: float | int, spec: InstrumentSpec):
        self.serial_number = serial_number
        self.__price = price
        self.spec = spec

    def get_serial_number(self) -> str:
        return self.serial_number

    def get_price(self) -> float | int:
        return self.__price

    def set_price(self, new_price) -> None:
        self.__price = new_price

    def get_spec(self) -> InstrumentSpec:
        return self.spec


class Inventory:
    def __init__(self):
        self.inventory: List[Instrument] = []

    def add_instrument(
        self, serial_number: str, price: int | float, spec: InstrumentSpec
    ):
        instrument = Instrument(serial_number, price, spec)
        self.inventory.append(instrument)

    def get_instrument(self, serial_number: str):
        for instrument in self.inventory:
            if instrument.get_serial_number() == serial_number:
                return instrument
        return None

    def search(self, search_spec: InstrumentSpec) -> List[Instrument]:
        matching_instruments: List[Instrument] = []
        for instrument in self.inventory:
            if instrument.get_spec().matches(search_spec):
                matching_instruments.append(instrument)
        return matching_instruments


def initialize_inventory(inventory):
    properties: Properties = Properties(
        instrument_type=InstrumentType.GUITAR,
        builder=Builder.COLLINGS,
        model="CJ",
        type=Type.ACOUSTIC,
        num_strings=6,
        top_wood=Wood.INDIAN_ROSEWOOD,
        back_wood=Wood.SITKA,
    )
    inventory.add_instrument("11277", 3999.95, InstrumentSpec(properties))

    properties = Properties(
        instrument_type=InstrumentType.GUITAR,
        builder=Builder.GIBSON,
        model="Les Paul",
        type=Type.ELECTRIC,
        num_strings=6,
        top_wood=Wood.MAPLE,
        back_wood=Wood.MAPLE,
    )
    inventory.add_instrument("70108276", 2295.95, InstrumentSpec(properties))

    properties = Properties(
        instrument_type=InstrumentType.MANDOLIN,
        builder=Builder.GIBSON,
        model="F5-G",
        type=Type.ACOUSTIC,
        top_wood=Wood.MAPLE,
        back_wood=Wood.MAPLE,
        style=Style.A,
    )
    inventory.add_instrument("9019920", 5495.99, InstrumentSpec(properties))

    properties = Properties(
        instrument_type=InstrumentType.BANJO,
        builder=Builder.GIBSON,
        model="RB-3",
        type=Type.ACOUSTIC,
        num_strings=5,
        back_wood=Wood.MAPLE,
    )
    inventory.add_instrument("8900231", 2945.95, InstrumentSpec(properties))


def main():
    inventory = Inventory()
    initialize_inventory(inventory)

    properties = Properties(builder=Builder.GIBSON, back_wood=Wood.MAPLE)
    client_spec = InstrumentSpec(properties)
    matching_instruments = inventory.search(client_spec)
    if matching_instruments:
        print("Erin, talvez você goste desta(s): ")
        print("\n----- Lista de instrumentos encontradas -----\n")
        for instrument in matching_instruments:
            instrument_spec = instrument.get_spec()
            for property in instrument_spec.get_properties():
                if property == "instrumentType":
                    continue
                print(property.capitalize() + ":", property)
            print("Ele pode ser seu por apenas $", instrument.get_price(), "\n")
        return
    print("Não foi encontrado nenhuma guitarra com o desejado")


if __name__ == "__main__":
    main()
