""" turns a csv of new books into html """
import argparse
import csv


def make_tuples(input_data):
    """ make tuples out of the csv data """
    data_list = []

    for line in input_data:
        bib_info1 = '<li><strong>' + line[2].title() + '</strong>'
        if line[1]:
            bib_info2 = '<li><em>Author: </em>' + line[1] + '</li>'
        else:
            bib_info2 = ''
        if line[3]:
            bib_info3 = '<li><em>Call number: </em>' + line[3] + '</li>'
        else:
            bib_info3 = ''
        bib_info4 = '</li>'
        bib_info = bib_info1 + '<ul>' + bib_info2 + bib_info3 + '</ul>' + bib_info4
        line_tup = (line[0], bib_info)
        data_list.append(line_tup)
    return data_list

def make_html(input_tuples, outfile):
    """ makes html out of the tuples """
    with open(outfile, 'a', encoding='utf-16') as file_2:
        file_2.write('<ul>')
        item_counter = ''
        for item in input_tuples:
            if item[0] != item_counter:
                file_2.write('</ul><h3>' + item[0] + '</h3><ul>')
            file_2.write(item[1])
            item_counter = item[0]
        file_2.write('</ul>')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parses a csv of new books')
    parser.add_argument('infile', metavar='[infile]', type=str,
                        help='a csv file')
    parser.add_argument('outfile', metavar='[outfile]', type=str,
                        help='an html file')
    args = parser.parse_args()
    with open(args.infile, 'r', encoding='cp437') as file_1:
        DATA = csv.reader(file_1)
        TUPLES = make_tuples(DATA)
    make_html(TUPLES, args.outfile)
