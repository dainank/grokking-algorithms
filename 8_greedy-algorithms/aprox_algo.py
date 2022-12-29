# sets can't have duplicates
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}  # available stations
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()  # solution
while states_needed:
    best_station = None
    states_covered = set()  # collection of new states covered by station
    for station, states_for_station in stations.items():    # finding best station
        # return set containing overlap items
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered  # some states can be removed from the needed list
    final_stations.add(best_station)  # current best station added

print(final_stations)