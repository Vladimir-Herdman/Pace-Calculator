def output(pace, km_convert, at_distance, to_distances):
    if not (at_distance and to_distances): # print out table of values from pace at different distances (assuming mile pace), no distances given
        pass
    elif (at_distance and not to_distances): # print out table of values, assuming pace at given distance
        pass
    elif (not at_distance and to_distances): # print out table of values at distances assuming mile pace
        pass
    else: # convert pace at distance to new distance pace (pace 4:19 --at 1600 --to 400)
        pass
    exit(0)