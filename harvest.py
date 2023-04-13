############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    # Fill in the rest
    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    cas.add_pairing('mint')
    cas.add_pairing('strawberries')
    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    cren.add_pairing('prosciutto')
    yw = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')

    return [musk, cas, cren, yw]


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for type in melon_types:
        print(f'{type.name} pairs with')
        for pairing in type.pairings:
            print(f'- {pairing}')
        print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_types_by_id = {}

    for type in melon_types:
        melon_types_by_id[type.code] = type

    return melon_types_by_id


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(self, code, shape_rating, color_rating, field, harvester):

        self.type = code
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = f'Harvested by {harvester}'

    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return 'CAN BE SOLD'
        else:
            return 'NOT SELLABLE'


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")  # sellable
    melon_2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")  # not sellable
    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")  # not sellable
    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")  # sellable
    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")  # sellable
    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")  # not sellable
    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")  # not sellable
    melon_8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")  # sellable
    melon_9 = Melon(melons_by_id["yw"], 7, 10, 3, "Michael")  # not sellable

    melons = [
        melon_1,
        melon_2,
        melon_3,
        melon_4,
        melon_5,
        melon_6,
        melon_7,
        melon_8,
        melon_9,
    ]

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    for melon in melons:
        print(f'{melon.harvester} from Field {melon.field} ({melon.is_sellable()})')


if __name__ == '__main__':
    melon_types = make_melon_types()
    melons = make_melons(melon_types)
    get_sellability_report(melons)
