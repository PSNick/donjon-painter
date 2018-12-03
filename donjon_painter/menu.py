import themes
import imgmap
import time
from pathlib import Path


# ==================== List of menu option functions ==================== #
def setTSV(args):
    print("Current TSV file:", args.MAPFILE)
    print("Enter in the location + name of your TSV file.")
    args.MAPFILE = str(Path(input()).expanduser())
    return args


def setTheme(args):
    print("Current theme:", args.tileset)
    print("Get inbuilt theme? (y/N)")

    getNative = input()
    if getNative == 'y' or getNative == 'Y':
        themes.printThemes()
        tmpTheme = themes.selTheme(args.tileset)
        if tmpTheme is not False:
            args.tileset = tmpTheme
    else:
        print("Enter in your theme directory.")
        args.tileset = input()

    return args


def setSave(args):
    print("Current save directory:", args.savetiles)
    print("Enter [name]/[location]/[location + name] to save your map image.")
    args.savetiles = input()
    return args


def setSize(args):
    print("Current tile size:", args.pixels)
    print("Enter in the new size of your tiles.")

    newSize = input()
    if newSize.isdigit():
        args.pixels = int(newSize)
        print("Size set to", newSize)
    else:
        print("Invalid input! (Press Enter to continue.)")
        input()

    return args


def togMetric(args):
    args.measure ^= True
    return args


def togRandom(args):
    args.randomise ^= True
    return args


def genTheme(args):
    if args.tileset is not None:
        print("Attempting theme generation at", args.tileset)
        start = time.time()
        if themes.writeTheme(args.tileset) is False:
            print("Insufficient resources found. (Press Enter to continue)")
        else:
            if args.measure:
                end = time.time()
                print("Done in", end - start, "seconds.")
    else:
        print("Specify tileset folder! (Press Enter to continue)")
        input()
    return args


def genMap(args):
    if args.MAPFILE is not None and args.tileset is not None:
        print("Attempting map generation to", args.output)
        start = time.time()
        if imgmap.writeMap(args) is False:
            print("Insufficient resources found. (Press Enter to continue)")
        else:
            if args.measure:
                end = time.time()
                print("Done in", end - start, "seconds.")
    else:
        print("Specify more details! (Press Enter to continue)")
        input()
    return args


def progExit():
    print("Exiting menu...")


choices = {
        "Select TSV File": setTSV,
        "Select Theme": setTheme,
        "Set Save Location": setSave,
        "Set Tile Size": setSize,
        "Toggle Savetime Metrics": togMetric,
        "Toggle Floor Shuffling": togRandom,
        "Generate Theme": genTheme,
        "Generate Map Image": genMap,
        "Exit Generator": progExit
    }
# ==================== End of map menu options ==================== #


def getSettings(args):
    optList = {
        "TSV Map File\t\t:": args.MAPFILE,
        "Tile Theme Folder\t:": args.tileset,
        "Save Location\t\t:": args.output,
        "Tile Size (Pixels)\t:": args.pixels,
        "Measure Save Time\t:": args.measure,
        "Shuffle Floor\t\t:": args.randomise
    }
    for i, val in optList.items():
        print(i, val)


def getOptions():
    for i, (key, val) in enumerate(choices.items()):
        print('[' + str(i) + ']', key)


def mainmenu(args):
    option = None
    while option != (len(choices) - 1):
        print("========== Current Settings ==========")
        getSettings(args)
        print()
        getOptions()
        print("Select option: ")

        tmpOpt = input()
        # Execute linked option
        if tmpOpt.isdigit():
            optList = list(choices.keys())
            option = int(tmpOpt)

            # No arguments for exiting
            if option < (len(optList) - 1):
                args = choices[optList[option]](args)
            elif option == (len(optList) - 1):
                choices[optList[option]]
    print("Exiting...")
