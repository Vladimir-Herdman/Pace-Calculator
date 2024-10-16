meters_conversion = {
    "m": 1,
    "mi": 1609.34,
    "km": 1000
}

def convert_to_meters(distance: str):
    """Take a distance str value (i.e. 400m, 3mi, 4km, 200...), convert the distance
    to its representation in meters, return ditance value (float).
    """
    # convert old distance to meters for easier comparison and calculations
    if (distance[-1].isnumeric()):  # no unit given, assume meters
        old_distance = distance
        old_unit = "m"
    elif (distance[-1] == "m" and distance[-2:] != "km"):
        old_distance = distance[:-1]
        old_unit = "m"
    elif (distance[-1] == "k"):  # k instead of km
        old_distance = distance[:-1]
        old_unit = "km"
    else:
        old_distance = distance[:-2]  # mi or km left
        old_unit = distance[-2:]

    return float(old_distance) * meters_conversion[old_unit]

def convert_to_seconds(pace: str):
    """Take an str pace value H:M:S (i.e. 1:12:42, 4:19, 19...) and convert it to its
    representation in seconds (float).
    """
    if (":" in pace):
        pace = pace.split(":")
        if (len(pace) == 3):
            pace = int(pace[0])*60*60 + int(pace[1])*60 + float(pace[2])
        else:
            pace = int(pace[0])*60 + float(pace[1])
    else:
        pace = float(pace)

    return pace

def convert_to_time_format(pace: float):
    """Take a pace value in terms of seconds (float) and convert to str representation
    in H:M:S or M:S format (i.e. 67 -> 1:07, 3664 -> 1:01:04, 12 -> 0:12...)
    """
    hour = str(int(pace // 3600))
    min = str(int((pace % 3600) // 60))
    seconds = str(round(pace % 60, 2))

    if (len(min) == 1):  min = "0" + min
    if (len(seconds) == 1):  seconds = "0" + seconds
    if ("." in seconds):
        if (len(seconds.split(".")[0]) == 1):  seconds = "0" + seconds
        if (seconds.split(".")[1] == "0"):  seconds = seconds.split(".")[0]

    if (hour == "0"):  return min + ":" + seconds
    
    return hour + ":" + min + ":" + seconds

def calculate_paces(pace:str, at_distance:str, new_distances:list[str]):
    """Take a given pace at a distance and convert to the paces at each given new
    distance.

    Returns:
        A list of converted paces to the new distance values
    """
    old_distance_in_meters = convert_to_meters(at_distance)
    old_pace_in_seconds = convert_to_seconds(pace)

    # convert pace to paces for new distances
    new_paces = list()
    for new_distance in new_distances:
        new_distance_in_meters = convert_to_meters(new_distance)
        conversion_rate = (new_distance_in_meters / old_distance_in_meters)
        new_pace = (old_pace_in_seconds * conversion_rate)
        new_pace = convert_to_time_format(new_pace)
        new_paces.append(new_pace)

    return new_paces