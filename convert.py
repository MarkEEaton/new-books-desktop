""" turns a csv of new books into html """
import argparse
import csv
from titlecase import titlecase


def make_tuples(input_data):
    """ make tuples out of the csv data """
    data_list = []

    # iterate through the lines of the csv file. Leave out the headers.
    for line in input_data[1:]:

        # make the HTML for the title. Use the titlecase library for better capitalization
        bib_info1 = '<li><strong>' + titlecase(line[2]) + '</strong>'

        # make the HTML for the author. Leave out the word 'author'.
        if line[1]:
            if line[1][-9:] == ', author.':
                author = line[1][:-9]
            elif line[1][-9:] == '- author.':
                author = line[1][:-8]
            else:
                author = line[1]
            bib_info2 = '<li><em>Author: </em>' + author + '</li>'
        else:
            # if there is no author, return an empty string
            bib_info2 = ''

        # make the HTML for the call number
        if line[3]:
            bib_info3 = '<li><em>Call number: </em>' + line[3] + '</li>'
        else:
            # if there is no call number, return an empty string
            bib_info3 = ''

        # make the HTML for the catalog link
        url = 'http://onesearch.cuny.edu/primo-explore/search?query=any,contains,' + \
              line[2] + '&tab=default_tab&search_scope=everything&vid=kb&lang=en_US&offset=0'
        bib_info4 = '<li><a href=\"' + url + '\">Search the catalog</a></li>'

        # assemble all the HTML for the item
        bib_info = bib_info1 + '<ul>' + bib_info2 + bib_info3 + bib_info4 + '</ul></li>'

        # make a tuple for the item. The first item is LC Class, the second is the HTML.
        line_tup = (line[0], bib_info)
        data_list.append(line_tup)

    # return the list of tuples
    return data_list

def make_html(input_tuples, outfile):
    """ makes html out of the tuples """

    # make a file for the HTML
    with open('data/' + outfile, 'a', encoding='utf-16') as file_2:

        # start a big unordered list
        file_2.write('<ul>')

        # keep track of what LC class is the current one, iterate through the tuples
        current_lc_class = ''
        for item in input_tuples:

            # if it's a new LC class, create a new header
            if item[0] != current_lc_class:
                file_2.write('</ul><h3>' + item[0] + '</h3><ul>')

            # then write the item, then reassign the current LC class
            file_2.write(item[1])
            current_lc_class = item[0]

        # close the big list
        file_2.write('</ul>')

def main():
    """ run it! """

    # handle the command line input
    parser = argparse.ArgumentParser(description='Parses a csv of new books')
    parser.add_argument('infile', metavar='[infile]', type=str,
                        help='a csv file')
    parser.add_argument('outfile', metavar='[outfile]', type=str,
                        help='an html file')
    args = parser.parse_args()

    # do all the work! Make the tuples and then turn them into HTML
    with open('data/' + args.infile, 'r', encoding='cp1252') as file_1:
        data = list(csv.reader(file_1))
        tuples = make_tuples(data)
    make_html(tuples, args.outfile)

if __name__ == "__main__":
    main()
