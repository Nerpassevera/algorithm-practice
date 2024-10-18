# Add your clarifying questions here

def skyline(building_list):
    bottom_line = 0
    buildings_we_see = []
    for i in building_list:
        if i > bottom_line:
            buildings_we_see.append(i)
            bottom_line = i
    return buildings_we_see

print(skyline([-1, 1, 3, 7, 7, 3]))

assert skyline([-1, 1, 3, 7, 7, 3]) == [1, 3, 7]