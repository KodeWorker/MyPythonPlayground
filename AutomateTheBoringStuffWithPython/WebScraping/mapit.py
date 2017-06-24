import argparse
import webbrowser

def search_googlemap():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', help='The address for google map to search', type=str)
    args = parser.parse_args()
    
    webbrowser.open('https://www.google.com/maps/place/' + args.addr)
    
if __name__ == '__main__':
    search_googlemap()