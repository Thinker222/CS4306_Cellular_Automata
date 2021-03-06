# Internal Libraries

from Automata import Automata
from Rules import wolfram, wolframgetindex, conway, apply_conway, setup_conway
from Creatures import creatures
# External Libraries
# https://stackoverflow.com/questions/4480075/argparse-optional-positional-arguments
import argparse

# This is for detailed output
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
    # How to use argparse: https://www.pythonforbeginners.com/argparse/argparse-tutorial
    parser = argparse.ArgumentParser()
    parser.add_argument("--Type", help="Use conway or wolfram", nargs='?', default="none")
    parser.add_argument("--Par", help="For wolfram, type in a number betweeen 0 and 255 inclusive. For," +
    "Conway type in the survive numbers a forward slash, and the birth numbers with no spaces e.g. 23/3", nargs='?', default=30)
    parser.add_argument("--Size", help="Sets the dimensions of the automata; the horizontal will be twice the size of the input", nargs='?', default=100)
    parser.add_argument("--Cheat", help="Only for wolfram; creates faster output but does not follow the algorithm perfectly", nargs='?', default=False)
    parser.add_argument("--SaveFile", help="Save file name; don't add .jpg or .gif; the file extensions will be appended automatically", nargs='?', default="out")
    parser.add_argument("--Times", help="Number of iterations in the automata", nargs='?', default=0)
    parser.add_argument("--Speed", help="Rate of video for conway", default=.2)
    parser.add_argument("--Creature", help="For conway only, type in the name of a creature. Here are all the creatures\n" + str(creatures.keys()), nargs='?',default='square')
    args = parser.parse_args()
    args.Type = args.Type.lower()
    args.Size = int(args.Size)
    if args.Type == "conway":
        if(type(args.Par) == int):
            args.Par = '23/3'
        if(args.Times == 0):
            args.Times = 50
        aut = Automata(x_size = args.Size, y_size = args.Size, par = args.Par, rule= conway,
                       setup = setup_conway, setup_params=creatures[args.Creature])
        aut.setup()
        update_with_commentary(aut, int(args.Times))
        print('Creating movie')
        aut.print_movie(args.Speed, args.SaveFile + '.gif')
        print('Done!')
    elif args.Type == "wolfram":
        aut = Automata(x_size=args.Size, y_size=args.Size * 2, par = (int(args.Par), bool(args.Cheat)), rule = wolfram)
        if(args.Times == 0):
            args.Times = 50
        aut.setup()
        if (args.Cheat == False):
            update_with_commentary(aut, int(args.Times))
        else:
            aut.update_automata(times = 1)
        print('Creating image')
        aut.print(args.SaveFile + '.jpg')
        print('Done!')
    else:
        args.Size = 100
        x = input('Invalid input; would you like to get some samples? y or n?')
        x = x.lower()
        if x == 'y' or x == 'yes':
            print('Doing wolfram rule 90')
            aut = Automata(x_size=args.Size, y_size=args.Size * 2, par = (90,True), rule = wolfram)
            aut.setup()
            aut.update_automata()
            aut.print('Rule_ninety.jpg')
            print('Saving to Rule_ninety.jpg')
            print('Doing wolfram rule 45')
            aut = Automata(x_size=args.Size, y_size=args.Size * 2, par=(45, True), rule=wolfram)
            aut.setup()
            aut.update_automata()
            aut.print('Rule_forty-five.jpg')
            print('Saving to Rule_forty-five.jpg')
            print('Doing rule 23/3 glider')
            aut = Automata(x_size=args.Size, y_size=args.Size, par='23/3', rule=conway,
                           setup=setup_conway, setup_params=creatures['glider'])
            aut.setup()
            update_with_commentary(aut, 30)
            aut.print_movie(speed = .2, name='glider.gif')
            print('Saving to glider.gif')
            print('Doing rule 23/36 replicator')
            aut = Automata(x_size=args.Size, y_size=args.Size, par='23/36', rule=conway,
                           setup=setup_conway, setup_params=creatures['replicator'])
            aut.setup()
            update_with_commentary(aut, 100)
            aut.print_movie(speed=.2, name='replicator.gif')
            print('Saving to replicator.gif')


if __name__ == "__main__":
    main()