import pace.pace_math as pm


def format_table(given_paces: list[str], at_distance: str, new_distances: list[str]):
    # generate list of lists for new paces of each new_distance
    new_paces = list()
    for pace in given_paces:
        new_paces.append(pm.calculate_paces(pace, at_distance, new_distances))
    
    # set up col_width, find max width of calculated paces strings, or given paces
    col_width = len(max([pace for pace_list in new_paces for pace in pace_list] + given_paces, key=len))
    if (col_width % 2 == 0):
        col_width += 2
    else:
        col_width += 3
    
    # make table (each given pace is a new column)
        # header
    header_horizontal = ""
    header_content = ""
    given_paces.insert(0, " ")

    for pace in given_paces:
        padding = " "*((col_width - len(pace)) // 2)
        header_horizontal += "+" + "-"*(col_width - 1)
        header_content += "|" + padding + pace + padding
        if (len(pace) % 2 == 0):  header_horizontal += "-"

    header_horizontal += "+\n"
    header_content += "|\n"

    for pace in given_paces:
        pass
        # body - row by row
    for index, distance in enumerate(new_distances):
        pass

    table = header_horizontal + header_content + header_horizontal
    return table

def output(pace: list[str], at_distance: str, to_distances: list[str]):
    if (not at_distance):
        at_distance = "1mi"
    if (not to_distances):
        default_distances = ["200m", "400m", "800m", "1500m", "1mi", "2mi", "5km", "8km", "10km"]
        to_distances = default_distances

    table = format_table(pace, at_distance, to_distances)
    print(table)
    exit(0)