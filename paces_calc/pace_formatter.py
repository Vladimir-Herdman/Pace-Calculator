import paces_calc.pace_math as pm


def format_table(given_paces: list[str], at_distance: str, new_distances: list[str]):
    # generate list of lists for new paces of each new_distance
    new_paces = list()
    for pace in given_paces:
        new_paces.append(pm.calculate_paces(pace, at_distance, new_distances))
    
    # set up col_width, find max width of calculated paces strings, or given paces
    # make col_width even
    col_width = len(max([pace for pace_list in new_paces for pace in pace_list] + given_paces, key=len))
    if (col_width % 2 == 0):
        col_width += 2
    else:
        col_width += 3
    
    # make table (each given pace is a new column) (highlight-bold header row)
        # header
    padding = " "*((col_width - len(at_distance) - 1) // 2)
    header_horizontal = "\033[1m" + "+" + "-"*(col_width - 1)
    header_content = "\033[1m" + "|" + "\033[103m" + padding + at_distance + padding + "\033[0m"
    if (len(at_distance) % 2 == 0):  header_content += "\033[103m \033[0m"

    for pace in given_paces:
        padding = " "*((col_width - len(pace)) // 2)
        header_horizontal += "+" + "-"*(col_width - 1)
        header_content += "|" + "\033[1;103m" + padding + pace + padding + "\033[0m"
        if (len(pace) % 2 == 1):  header_content += "\033[103m \033[0m"; header_horizontal += "-"
        if (len(pace) % 2 == 0):  header_horizontal += "-"

    header_horizontal += "+" + "\033[0m" + "\n"
    header_content += "|" + "\033[0m" + "\n"

        # body
    body = ""
    row_content = ""
    row_horizontal = ""

    for index, distance in enumerate(new_distances):
        # add the leftmost column holding new distance pace converted to
        dist_padding = " "*((col_width - len(distance)) // 2)
        
        row_content = "|" + dist_padding + distance + dist_padding
        row_horizontal = "|" + "-"*(col_width - 1)
        if (len(distance) % 2 == 0 and len(distance) % 2 != 0):  row_horizontal += "-"
        if (len(distance) % 2 == 0):  row_content = row_content[:-1]

        # add the new paces for the distance per column
        for pace_list in new_paces:
            new_pace = pace_list[index]
            pace_padding = " "*((col_width - len(new_pace)) // 2)

            row_content += "|" + pace_padding + new_pace + pace_padding
            row_horizontal += "|" + "-"*(col_width)
            if (len(new_pace) % 2 == 1):  row_content += " "
        
        row_content += "|\n"
        row_horizontal += "|\n"
        body += row_content + row_horizontal
    body = "+".join(body.rsplit("|", (2 + len(given_paces))))

    table = header_horizontal + header_content + header_horizontal + body
    return table

def output(pace: list[str], at_distance: str, to_distances: list[str]):
    if (not at_distance):
        at_distance = "1mi"
    if (not to_distances):
        default_distances = ["200m", "400m", "800m", "1500m", "1mi", "2mi", "5km", "8km", "10km"]
        to_distances = default_distances

    table = format_table(pace, at_distance, to_distances)
    print("\n" + table)
    exit(0)