import pace.pace_math as pm


def format_table(given_paces: list[str], at_distance: str, new_distances: list[str]):
    new_paces = list()
    for pace in given_paces:
        new_paces.append(pm.calculate_paces(pace, at_distance, new_distances))
    
    table = new_paces
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