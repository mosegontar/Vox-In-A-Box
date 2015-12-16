import re
import urllib2
import webbrowser

def sanitize_headlines(headlines):
    for index, pair in enumerate(headlines):
        if '&nbsp;' in pair[1]:
            converted = list(pair)
            converted[1] = converted[1].replace('&nbsp;', ' ')
            convert_back = tuple(converted)
            headlines[index] = convert_back
    return headlines


def get_headlines():

    vox = urllib2.urlopen('http://www.vox.com')
    data = vox.read()

    urls_and_headlines = re.findall(r'<a data-analytics-link="(?:beat|group|latest-news)" href="(\w+.+)">(\w+.+)</a>', data)
    unique_headlines = list(set(urls_and_headlines))
    
    return sanitize_headlines(unique_headlines)


if __name__ == "__main__":
    headlines = get_headlines()

    print "\nCurrent Vox Headlines:\n"

    for index, headline in enumerate(headlines):
        print ("[%d]" % (index+1)), headline[1]

    print '-' * 100

    while True:
        print "Enter [#] to read article in your browser."
        print "Enter Q to quit"

        choice = raw_input("> ")

        if choice.lower() == 'q':
            break
        else:
            try:
                if int(choice) > len(headlines):
                    print "* That number isn't in the list *"
                elif int(choice) > 0 and int(choice) <= len(headlines):
                    webbrowser.open(headlines[int(choice)-1][0])
            except ValueError:
                print
                print "* Couldn't understand! Enter an article number to read or 'Q' to quit. *"
                print