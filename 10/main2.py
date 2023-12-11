def dir_calc(pipe_type, last_dir):
    if (pipe_type == "|"):
        return last_dir
    elif (pipe_type == "-"):
        return (0)
    elif (pipe_type == "L"):
        if (last_dir == 0):
            return (-1)
        else:
            return (0)
    elif (pipe_type == "J"):
        if (last_dir == 0):
            return (-1)
        else:
            return (0)
    elif (pipe_type == "7"):
        if (last_dir == 0):
            return (1)
        else:
            return (0)
    elif (pipe_type == "F"):
        if (last_dir == 0):
            return (1)
        else:
            return (0)
    else:
        return (0)

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
    border_maps = [[]] * 4
    for line in file:
        pipe_map.append(list(line))
        for border_map in border_maps:
            border_map.append(["."] * len(line))
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
    winning_border_map = []
    location = {"X" : start["X"] + 1, "Y" : start["Y"]}
    prev_location = {"X" : start["X"], "Y" : start["Y"]}
    cnt = 0
    dir = 0
    general_dir = 0
    while (not done):
        cnt += 1
        temp = {"X" : location["X"], "Y" : location["Y"]}
        if (pipe_map[location["Y"]][location["X"]] == "-" or pipe_map[location["Y"]][location["X"]] == "S"):
            border_maps[0][location["Y"]][location["X"]] = "0"
        elif (pipe_map[location["Y"]][location["X"]] == "|"):
            border_maps[0][location["Y"]][location["X"]] = "X"
        else:
            dir = dir_calc(pipe_map[location["Y"]][location["X"]], dir)
            if (dir != 0 and (dir == general_dir or general_dir == 0)):
                border_maps[0][location["Y"]][location["X"]] = "X"
            else:
                border_maps[0][location["Y"]][location["X"]] = "0"
            if (dir != 0):
                general_dir = dir    
        location = piping(pipe_map[location["Y"]][location["X"]], location, prev_location)
        if (location == 1):
            done = True
            winning_border_map = border_maps[0]
            break
        elif (location == -1):
            break
        prev_location = {"X" : temp["X"], "Y" : temp["Y"]}

    location = {"X" : start["X"] - 1, "Y" : start["Y"]}
    prev_location = {"X" : start["X"], "Y" : start["Y"]}
    cnt = 0
    dir = 0
    general_dir = 0
    while (not done):
        cnt += 1
        temp = {"X" : location["X"], "Y" : location["Y"]}
        if (pipe_map[location["Y"]][location["X"]] == "-" or pipe_map[location["Y"]][location["X"]] == "S"):
            border_maps[1][location["Y"]][location["X"]] = "0"
        elif (pipe_map[location["Y"]][location["X"]] == "|"):
            border_maps[1][location["Y"]][location["X"]] = "X"
        else:
            dir = dir_calc(pipe_map[location["Y"]][location["X"]], dir)
            if (dir != 0 and (dir == general_dir or general_dir == 0)):
                border_maps[1][location["Y"]][location["X"]] = "X"
            else:
                border_maps[1][location["Y"]][location["X"]] = "0"
            if (dir != 0):
                general_dir = dir   

        location = piping(pipe_map[location["Y"]][location["X"]], location, prev_location)
        if (location == 1):
            done = True
            winning_border_map = border_maps[1]
            break
        elif (location == -1):
            break
        prev_location = {"X" : temp["X"], "Y" : temp["Y"]}

    location = {"X" : start["X"], "Y" : start["Y"] + 1}
    prev_location = {"X" : start["X"], "Y" : start["Y"]}
    cnt = 0
    dir = 1
    general_dir = 1
    while (not done):
        cnt += 1
        temp = {"X" : location["X"], "Y" : location["Y"]}
        if (pipe_map[location["Y"]][location["X"]] == "-"):
            border_maps[2][location["Y"]][location["X"]] = "0"
        elif (pipe_map[location["Y"]][location["X"]] == "|"):
            border_maps[2][location["Y"]][location["X"]] = "X"
        else:
            if (pipe_map[location["Y"]][location["X"]] == "S"):
                dir = 1
            else:
                dir = dir_calc(pipe_map[location["Y"]][location["X"]], dir)
            if (dir != 0 and (dir == general_dir or general_dir == 0)):
                border_maps[0][location["Y"]][location["X"]] = "X"
            else:
                border_maps[0][location["Y"]][location["X"]] = "0"
            if (dir != 0):
                general_dir = dir   
        location = piping(pipe_map[location["Y"]][location["X"]], location, prev_location)
        if (location == 1):
            done = True
            winning_border_map = border_maps[2]
            break
        elif (location == -1):
            break
        prev_location = {"X" : temp["X"], "Y" : temp["Y"]}

    location = {"X" : start["X"], "Y" : start["Y"] - 1}
    prev_location = {"X" : start["X"], "Y" : start["Y"]}
    cnt = 0
    dir = -1
    general_dir = -1
    while (not done):
        cnt += 1
        temp = {"X" : location["X"], "Y" : location["Y"]}
        if (pipe_map[location["Y"]][location["X"]] == "-"):
            border_maps[3][location["Y"]][location["X"]] = "0"
        elif (pipe_map[location["Y"]][location["X"]] == "|"):
            border_maps[3][location["Y"]][location["X"]] = "X"
        else:
            if (pipe_map[location["Y"]][location["X"]] == "S"):
                dir = -1
            else:
                dir = dir_calc(pipe_map[location["Y"]][location["X"]], dir)
            if (dir != 0 and (dir == general_dir or general_dir == 0)):
                border_maps[0][location["Y"]][location["X"]] = "X"
            else:
                border_maps[0][location["Y"]][location["X"]] = "0"
            if (dir != 0):
                general_dir = dir   
        location = piping(pipe_map[location["Y"]][location["X"]], location, prev_location)
        if (location == 1):
            done = True
            winning_border_map = border_maps[3]
            break
        elif (location == -1):
            break
        prev_location = {"X" : temp["X"], "Y" : temp["Y"]}
    
    result = 0
    for line in winning_border_map:
        check = False
        for place in line:
            if (place == "X"):
                check = True
                break
        if (check):
            for place, i in zip(line, range(len(line))):
                if ((place != "X") and (place != "0")):
                    cnt = 0
                    for j in range(i + 1, len(line)):
                        if (line[j] == "X"):
                            cnt += 1
                    if ((cnt % 2) == 1):
                        result += 1
    print ("Result: " + str(result))
                    
if (__name__ == "__main__"):
    main("./10/input1.txt")