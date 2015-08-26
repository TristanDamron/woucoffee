import sys

def main():
    f = open("src/data/conf", "w")
    for args in sys.argv[1:]:
        f.write(args)
        print args

main()
