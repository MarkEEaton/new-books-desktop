""" turns a csv of new books into html """
import argparse
import csv
from titlecase import titlecase
from gooey import Gooey, GooeyParser


def make_tuples(input_data):
    """ make tuples out of the csv data """
    data_list = []

    # iterate through the lines of the csv file. Leave out the headers.
    for line in input_data[1:]:

        # make the HTML for the title. Use the titlecase library for better capitalization
        bib_info1 = "<strong>" + titlecase(line[2]) + "</strong>"

        # make the HTML for the author. Leave out the word 'author'.
        if line[1]:
            if line[1][-9:] == ", author.":
                author = line[1][:-9]
            elif line[1][-9:] == "- author.":
                author = line[1][:-8]
            else:
                author = line[1]
            bib_info2 = "<li><em>Author: </em>" + author + "</li>"
        else:
            # if there is no author, assign an empty string
            bib_info2 = ""

        # make the HTML for the call number
        if line[6]:
            bib_info3 = "<li><em>Call number: </em>" + line[6] + "</li>"
        else:
            # if there is no call number, assign an empty string
            bib_info3 = ""

        # make the format (print or ebook)
        if line[5].lower().strip() == "print":
            bib_info5 = "<li><em>Format: </em>Print book</li>"
        elif line[5]:
            bib_info5 = "<li><em>Format: </em>" + line[5] + "</li>"
        else:
            bib_info5 = ""

        # make the URL based on the ISBN
        # failing that make the URL based on the title
        # failing that make no link
        if line[3]:
            url = (
                "https://cuny-kb.primo.exlibrisgroup.com/discovery/search?query=isbn,exact,"
                + line[3]
                + "&tab=Everything&search_scope=IZ_CI_AW&sortby=rank&vid=01CUNY_KB:CUNY_KB&lang=en&offset=0"
            )
            bib_info4 = '<li><a href="' + url + '">Search the catalog</a></li>'
        elif line[2]:
            url = (
                "https://cuny-kb.primo.exlibrisgroup.com/discovery/search?query=title,contains,"
                + line[2]
                + "&tab=Everything&search_scope=MyInst_and_CI&sortby=rank&vid=01CUNY_KB:CUNY_KB&lang=en&offset=0"
            )
            bib_info4 = '<li><a href="' + url + '">Search the catalog</a></li>'
        else:
            bib_info4 = ""

        # assemble all the HTML for the item
        bib_info = (
            "<li>"
            + bib_info1
            + "<ul>"
            + bib_info2
            + bib_info3
            + bib_info5
            + bib_info4
            + "</ul></li>"
        )

        # make a tuple for the item. The first item is LC Class, the second is the HTML.
        lc_class = line[0]
        collection = line[4]
        item_tuple = (lc_class, collection, bib_info)
        if line[2]:
            data_list.append(item_tuple)

    # return the list of tuples
    return data_list


def make_html(input_tuples, args):
    """ makes html out of the tuples """

    # open a file for the HTML
    with open(args.infile[:-3] + "html", "w", encoding="utf-16") as file_2:

        # start a big unordered list
        file_2.write("<ul>")

        # keep track of what LC class/collection is the current one, iterate through the tuples
        current_lc_class = ""
        current_collection = ""
        for item in input_tuples:

            # if it's a new LC class, or a new header, create a new header
            if item[1] == "Juvenile Collection" and item[1] != current_collection:
                file_2.write("</ul><h3>" + item[1] + "</h3><ul>")
            elif item[1] == "Leisure Collection" and item[1] != current_collection:
                file_2.write("</ul><h3>" + item[1] + "</h3><ul>")
            if item[0] != current_lc_class:
                file_2.write("</ul><h3>" + item[0] + "</h3><ul>")

            # then write the item, then reassign the current LC class and collection
            file_2.write(item[2])
            current_lc_class = item[0]
            current_collection = item[1]

        # close the big list
        file_2.write("</ul>")


@Gooey(program_name="Convert a CSV of new books to HTML")
def main():
    """ run it! """

    # make the GUI application using Gooey
    parser = GooeyParser(
        description="Parses a csv of new books to produce an html file."
        "\nThe resulting html output file will be in the same folder as the csv."
    )
    search_group = parser.add_argument_group(
        "Specify files", gooey_options={"columns": 1}
    )
    search_group.add_argument(
        "infile", metavar="Infile", type=str, help="a csv file", widget="FileChooser"
    )
    args = parser.parse_args()

    # do all the work! Make the tuples and then turn them into HTML
    with open(args.infile, "r", encoding="latin-1") as file_1:
        data = list(csv.reader(file_1))
        tuples = make_tuples(data)
    make_html(tuples, args)


if __name__ == "__main__":
    main()
