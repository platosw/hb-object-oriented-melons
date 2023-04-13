from harvest import (
    make_melon_types,
    make_melon_type_lookup,
    Melon,
    get_sellability_report
)

melon_types = make_melon_types()
melon_types_dicts = make_melon_type_lookup(melon_types)


def make_melons():
    melons_by_id = melon_types_dicts
    melons = []
    with open('harvest_log.txt', 'r') as log_file:
        for line in log_file.readlines():
            melon = line.split()
            # code, shape_rating, color_rating, field, harvester
            melons.append(
                Melon(melons_by_id[melon[5]], int(melon[1]), int(melon[3]), int(melon[-1]), melon[-4]))

    return melons


if __name__ == '__main__':
    get_sellability_report(make_melons())
