from harvest import (
    make_melon_types,
    make_melon_type_lookup,
    Melon,
    get_sellability_report
)

melon_types = make_melon_types()
melon_types_dicts = make_melon_type_lookup(melon_types)


def make_melons():
    # melons_by_id = dicts
    with open('harvest_log.txt', 'r') as log_file:
        for line in log_file.readlines():
            line = line.split()
            print(line)


if __name__ == '__main__':
    make_melons()
