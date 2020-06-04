"""
CP1404 Practical 10
A small program asking for a Wikipedia page title through user input
and return the Wikipedia page's summary, title and url
"""
import wikipedia


def main():
    """While input is not empty, print the page's summary, title and url"""
    page = input("Please enter a title: ")
    while page != "":
        try:
            wiki = wikipedia.page(page)     # store the page to load and access data
            print("Summary: {}\n".format(wikipedia.summary(page)))  # return the Wikipedia summary of the page
            print("Title: {}\n".format(wiki.title))    # return the Wikipedia title of the page
            print("URL: {}\n".format(wiki.url))      # return the Wikipedia url of the page
            print("-------------------------------------------------------------------------------")
        except wikipedia.exceptions.DisambiguationError as e:   # handle ambiguous error
            print("Please choose one clear title in the list below")
            print(e.options)
            print("-------------------------------------------------------------------------------")
        page = input("Please enter a title: ")
    return


main()
