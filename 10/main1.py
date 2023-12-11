def piping(pipe_type, pipe_loc, prev_loc):
    out = {"X": 0, "Y": 0}
    if (pipe_type == "|"):
        out["X"] = pipe_loc["X"]
        if ((pipe_loc["X"] == prev_loc["X"]) and (pipe_loc["Y"] < prev_loc["Y"])):
            out["Y"] = pipe_loc["Y"] - 1
        elif ((pipe_loc["X"] == prev_loc["X"]) and (pipe_loc["Y"] > prev_loc["Y"])):
            out["Y"] = pipe_loc["Y"] + 1
        else:
            return (-1)
    elif (pipe_type == "-"):
        out["Y"] = pipe_loc["Y"]
        if ((pipe_loc["Y"] == prev_loc["Y"]) and (pipe_loc["X"] < prev_loc["X"])):
            out["X"] = pipe_loc["X"] - 1
        elif ((pipe_loc["Y"] == prev_loc["Y"]) and (pipe_loc["X"] > prev_loc["X"])):
            out["X"] = pipe_loc["X"] + 1
        else:
            return (-1)
    elif (pipe_type == "L"):
        if ((pipe_loc["X"] == prev_loc["X"]) and (pipe_loc["Y"] > prev_loc["Y"])):
            out["Y"] = pipe_loc["Y"]
            out["X"] = pipe_loc["X"] + 1
        elif ((pipe_loc["Y"] == prev_loc["Y"]) and (pipe_loc["X"] < prev_loc["X"])):
            out["X"] = pipe_loc["X"]
            out["Y"] = pipe_loc["Y"] - 1
        else:
            return (-1)
    elif (pipe_type == "J"):
        if ((pipe_loc["X"] == prev_loc["X"]) and (pipe_loc["Y"] > prev_loc["Y"])):
            out["Y"] = pipe_loc["Y"]
            out["X"] = pipe_loc["X"] - 1
        elif ((pipe_loc["Y"] == prev_loc["Y"]) and (pipe_loc["X"] > prev_loc["X"])):
            out["X"] = pipe_loc["X"]
            out["Y"] = pipe_loc["Y"] - 1
        else:
            return (-1)
    elif (pipe_type == "7"):
        if ((pipe_loc["X"] == prev_loc["X"]) and (pipe_loc["Y"] < prev_loc["Y"])):
            out["Y"] = pipe_loc["Y"]
            out["X"] = pipe_loc["X"] - 1
        elif ((pipe_loc["Y"] == prev_loc["Y"]) and (pipe_loc["X"] > prev_loc["X"])):
            out["X"] = pipe_loc["X"]
            out["Y"] = pipe_loc["Y"] + 1
        else:
            return (-1)
    elif (pipe_type == "F"):
        if ((pipe_loc["X"] == prev_loc["X"]) and (pipe_loc["Y"] < prev_loc["Y"])):
            out["Y"] = pipe_loc["Y"]
            out["X"] = pipe_loc["X"] + 1
        elif ((pipe_loc["Y"] == prev_loc["Y"]) and (pipe_loc["X"] < prev_loc["X"])):
            out["X"] = pipe_loc["X"]
            out["Y"] = pipe_loc["Y"] + 1
        else:
            return (-1)
    elif (pipe_type == "S"):
        return (1)
    else:
        return (-1)
    return (out)

def main(filepath):
    file = open(filepath, "r")
    result = 0
    pipe_map = []
    for line in file:
        pipe_map.append(list(line))
    start = []
    done = False
    for line, i in zip(pipe_map, range(len(pipe_map))):
        for place, j in zip(line, range(len(line))):
            if (place == "S"):
                start = {"X" : j, "Y" : i}
                done = True
                break
        if (done):
            break
    done = False
    location = {"X" : start["X"] + 1, "Y" : start["Y"]}
    prev_location = {"X" : start["X"], "Y" : start["Y"]}
    cnt = 0
    while (not done):
        cnt += 1
        temp = {"X" : location["X"], "Y" : location["Y"]}
        location = piping(pipe_map[location["Y"]][location["X"]], location, prev_location)
        if (location == 1):
            done = True
            result = (cnt / 2)
            break
        elif (location == -1):
            break
        prev_location = {"X" : temp["X"], "Y" : temp["Y"]}

    location = {"X" : start["X"] - 1, "Y" : start["Y"]}
    prev_location = {"X" : start["X"], "Y" : start["Y"]}
    cnt = 0
    while (not done):
        cnt += 1
        temp = {"X" : location["X"], "Y" : location["Y"]}
        location = piping(pipe_map[location["Y"]][location["X"]], location, prev_location)
        if (location == 1):
            done = True
            result = (cnt / 2)
            break
        elif (location == -1):
            break
        prev_location = {"X" : temp["X"], "Y" : temp["Y"]}

    location = {"X" : start["X"], "Y" : start["Y"] + 1}
    prev_location = {"X" : start["X"], "Y" : start["Y"]}
    cnt = 0
    while (not done):
        cnt += 1
        temp = {"X" : location["X"], "Y" : location["Y"]}
        location = piping(pipe_map[location["Y"]][location["X"]], location, prev_location)
        if (location == 1):
            done = True
            result = (cnt / 2)
            break
        elif (location == -1):
            break
        prev_location = {"X" : temp["X"], "Y" : temp["Y"]}

    location = {"X" : start["X"], "Y" : start["Y"] - 1}
    prev_location = {"X" : start["X"], "Y" : start["Y"]}
    cnt = 0
    while (not done):
        cnt += 1
        temp = {"X" : location["X"], "Y" : location["Y"]}
        location = piping(pipe_map[location["Y"]][location["X"]], location, prev_location)
        if (location == 1):
            done = True
            result = (cnt / 2)
            break
        elif (location == -1):
            break
        prev_location = {"X" : temp["X"], "Y" : temp["Y"]}
    print("Result: " + str(int(result)))

if (__name__ == "__main__"):
    main("./10/input1.txt")