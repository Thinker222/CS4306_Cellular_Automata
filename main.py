# Internal Libraries

from Automata import Automata
from Rules import wolfram, wolframgetindex, conway, apply_conway, setup_conway
from Creatures import creatures
# External Libraries
# https://stackoverflow.com/questions/4480075/argparse-optional-positional-arguments
import argparse


def update_with_commentary(aut, num):
    step = num // 100
    total = num
    count = 0
    while count != 99:
        if(count % 5 == 0):
            print(str(count) + '% Complete')
        aut.update_automata(step)
        total = total - step
        count += 1
    aut.update_automata(total)
    count+= 1
    print(str(count) + '% Complete')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--Type", help="Use conway or wolfram", nargs='?', default="wolfram")
    parser.add_argument("--Par", help="For wolfram, type in a number betweeen 0 and 255 inclusive. For," +
    "Conway type in the survive numbers a forward slash, and the birth numbers with no spaces", nargs='?', default=30)
    parser.add_argument("--Size", help="Sets the dimensions of the automata; the horizontal will be twice the size of the input", nargs='?', default=100)
    parser.add_argument("--Cheat", help="Only for wolfram; creates faster output but does not follow the algorithm perfectly", nargs='?', default=False)
    parser.add_argument("--SaveFile", help="Save file name; don't add .jpg or .gif; the file extensions will be appended automatically", nargs='?', default="out")
    parser.add_argument("--Times", help="Number of iterations in the automata", nargs='?', default=1)
    parser.add_argument("--Speed", help="Rate of video for conway", default=.2)
    parser.add_argument("--Creature", help="For conway only, type in the name of a creature. Here are all the creatures\n" + str(creatures.keys()), nargs='?',default='square')
    args = parser.parse_args()
    args.Type = args.Type.lower()
    args.Size = int(args.Size)
    if args.Type == "conway":
        aut = Automata(x_size = args.Size, y_size = args.Size, par = args.Par, rule= conway,
                       setup = setup_conway, setup_params=creatures[args.Creature])
        aut.setup()
        update_with_commentary(aut, int(args.Times))
        print('Creating movie')
        aut.print_movie(args.Speed, args.SaveFile + '.gif')
        print('Done!')
    elif args.Type == "wolfram":
        aut = Automata(x_size=args.Size, y_size=args.Size * 2, par = (int(args.Par), bool(args.Cheat)), rule = wolfram)
        print(args.Cheat)
        aut.setup()
        if (args.Cheat == False):
            update_with_commentary(aut, int(args.Times))
        else:
            aut.update_automata(times = 1)
        print('Creating image')
        aut.print(args.SaveFile + '.jpg')
        print('Done!')
    else:
        print(args.Type)
        print("The type must be either wolfram or conway")

if __name__ == "__main__":
    main()