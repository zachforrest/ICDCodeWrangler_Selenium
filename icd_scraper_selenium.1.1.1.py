# Required packages: selenium, chromedriver

import webbrowser

query_list = []

def show_help(): #COMPLETE
    print("\nseparate each item with a comma.")
    print("Type DONE to quit, SHOW to see the current list, and HELP to get this message.")


def show_list(): #COMPLETE
    count = 1
    for item in query_list:
        print("{}: {}:".format(count, item))
        count += 1

#def search_query():  #IN Progress
    #webbrowser.open('http://www.findacode.com/search/search.php')
def search_query(): ## Looks Complete
    from selenium import webdriver
    import requests
    search_box = {'search_box': 'value1'}
    webpage = r"http://www.findacode.com/search/search.php" # edit me
    searchterm = query_list

    r = requests.get(webpage, params=search_box)

    r.raise_for_status()


def build_list(): ## COMPLETE
    print("What would youl ICD 10 groupings would you like to extract today?")
    show_help()

    while True:
        new_stuff = input("> ")

        if new_stuff == "DONE":
            print("\nHere's your list:")
            show_list()
            break
        elif new_stuff == "HELP":
            show_help()
            continue
        elif new_stuff == "SHOW":
            show_list()
            continue
        else:
          new_list = new_stuff.split(",")
          index = input("Add this at a certain spot? Press enter for the end of the list,"
                        "or give me a number, Currently {} items in the list.".format(
                len(query_list)))
          if index:
            spot = int(index) - 1
            for item in new_list:
                    query_list.insert(spot, item.strip())
                    spot += 1
          else:
            for item in new_list:
              query_list.append(item.strip())



# Save results to drive

def save_results():

    playFile = open('icd_results.txt', 'wb')
    for chunk in r.iter_content(100000):
        playFile.write(chunk)

# Parse HTML with BS4
def parse_html():
    exampleFile = open('icd_results.txt')

    exampleSoup = bs4.BeautifulSoup(exampleFile)

    type(exampleSoup)
# transfer and save to excel

build_list()
search_query()

#for len.queries in query_list:
    #search_query()




#Search query and get results

#select next page and get more results
#nextLink = soup.select('a[rel="prev"]')[0]
    #url = 'http://xkcd.com' + nextLink.get('href')
