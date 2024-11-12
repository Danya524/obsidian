import sys
import argparse
def main():
    parser = argparse.ArgumentParser(description= 'new')
    
    parser.add_argument('number_of_file', type = int, help = 'вход')
    parser.add_argument('month', type = str, help = 'выход')
    parser.add_argument('year', type = str, help = 'da')

    args = parser.parse_args()
    number_of_file = args.number_of_file
    month = args.month
    year = args.year

    for i in range(30):
        i+=1
        with open(f"{i} keyword2 keyword2.md", "+a"):
            pass
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
if __name__ == "__main__":
    main()