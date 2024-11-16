import sys
import argparse
def main():
        parser = argparse.ArgumentParser(description= 'Generate file')
            
        parser.add_argument('number_of_file', type = int, help = 'Number file')
        parser.add_argument('month', type = str, help = 'Any one of the 12 months')
        parser.add_argument('year', type = str, help = 'Any year')

        args = parser.parse_args()
        number_of_file = args.number_of_file
        month = args.month
        year = args.year
    
        if len(sys.argv)==1:
            parser.print_help(sys.stderr)
            sys.exit(1)
        
        for i in range(30):
            i+=1
            with open(f'{i} keyword2 keyword2.md', '+a'):
                pass

if __name__ == "__main__":
    main()