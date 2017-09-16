import urllib.request
import logging
import datetime
import sys

from bs4 import BeautifulSoup

logging.basicConfig(filename='log.txt',level=logging.DEBUG)

def my_handler(type, value, tb):
    logging.debug("Uncaught exception: {0}".format(str(value)))
sys.excepthook = my_handler

YOURSHOT_URL = "http://yourshot.nationalgeographic.com/assignments-stories/"


# new in variable names refers to data gathered in this iteration of the script
# old in variable names refers to data pulled from old_titles.txt
def main():
    r = urllib.request.urlopen(YOURSHOT_URL).read()
    soup = BeautifulSoup(r, "html.parser")

    try:
        with open("./old_titles.txt", "r") as f:
            old_titles = set(f.read().split('\n'))

    # If first time running script, ./old_titles.txt will be created at the end.
    except FileNotFoundError:
        old_titles = set()

    # Assignments are chunked by a div with class assignment-block,
    # Go through each assignment and grab the title.
    new_assignments = soup.findAll("div", {"class": "assignment-block"})
    new_titles = set()
    for assignment in new_assignments:
        title = assignment.findAll("h3")[0].get_text()
        status = assignment.findAll("a", {"class": "gold"})[0].get_text().strip()
        new_titles.add(title)

    # Report if any titles have changed.
    changed_titles = new_titles - old_titles
    if changed_titles:
        today = datetime.date.today()
        logging.info("{}: {}".format(today, changed_titles))

    # Save current titles to be checked against later.
    with open("./old_titles.txt", "w+") as f:
        for title in new_titles:
            f.write(title + "\n")

    # time.sleep(60 * 60 * 24)


if __name__ == "__main__":
    main()