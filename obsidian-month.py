import argparse
def main():
    parser = argparse.ArgumentParser(description= 'new')
    
    parser.add_argument('input', tupe = str, help = 'вход')
    parser.add_argument('output', tupe = str, help = 'выход')
    
    parser.add_argument('vervose', narsgs = '?', const = True, default = False, help = 'подробный режим') 
    
    args = parser.parse_args()
    number = args.one
    month = args.two
    yaer = args.three
if __name__ == "__main__":
    main()