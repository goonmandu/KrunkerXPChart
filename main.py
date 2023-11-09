import matplotlib.pyplot as plt


colors = {
    "AK": "dimgray",
    "Sniper": "peru",
    "SMG": "lightskyblue",
    "LMG": "mediumseagreen",
    "Shotgun": "steelblue",
    "Revolver": "burlywood",
    "Semi Auto": "forestgreen",
    "RPG": "darkseagreen",
    "Akimbos": "black",
    "Runner": "bisque",
    "Crossbow": "yellow",
    "FAMAS": "darkgoldenrod",
    "Blaster": "aqua",
    "Charge Rifle": "pink"
}


class ClassXP:
    def __init__(self, name, level, curr):
        self.name = name
        self.xp = get_xp_earned(level, curr)
        self.level = level
        self.curr = curr
        if name not in colors.keys():
            self.color = ""
        else:
            self.color = colors[name]


def get_xp_earned(level, curr):
    if level <= 1:
        return curr
    else:
        ret = 1111
        for i in range(level - 1):
            ret += 2222 * i
        return ret + curr


classes = ["AK", "Sniper", "SMG", "LMG", "Shotgun", "Revolver", "Semi Auto",
           "RPG", "Akimbos", "Runner", "Crossbow", "FAMAS", "Blaster", "Charge Rifle"]

'''
temp = [[65, 127066], [134, 255422], [43, 7298], [20, 14643], [21, 42269], [44, 10313], [13, 9955],
       [13, 128], [8, 14131], [21, 11803], [22, 42762], [14, 688], [11, 22817], [3, 2458]]
data = [ClassXP(classes[i], temp[i][0], temp[i][1]) for i in range(len(classes))]
'''

data = [ClassXP(to_enter, int(input(f"{to_enter} XP Level: ")), int(input(f"{to_enter} XP Now: "))) for to_enter in classes]
data.sort(key=lambda x: x.xp, reverse=True)

fig, ax = plt.subplots()
ax.pie([entry.xp for entry in data], labels=[f"{entry.name}: {entry.xp} (Lv. {entry.level})" for entry in data],
       autopct='%1.1f%%', radius=1.2, labeldistance=1.05, colors=[entry.color for entry in data])
plt.show()