""" turns a csv of new books into html """
import argparse
import csv
from titlecase import titlecase


def make_tuples(input_data):
    """ make tuples out of the csv data """
    data_list = []

    for line in input_data[1:]:
        bib_info1 = '<li><strong>' + titlecase(line[2]) + '</strong>'
        if line[1]:
            if line[1][-9:] == ', author.':
                author = line[1][:-9]
            elif line[1][-9:] == '- author.':
                author = line[1][:-8]
            else:
                author = line[1]
            bib_info2 = '<li><em>Author: </em>' + author + '</li>'
        else:
            bib_info2 = ''
        if line[3]:
            bib_info3 = '<li><em>Call number: </em>' + line[3] + '</li>'
        else:
            bib_info3 = ''
        url = line[5].replace(' ', '%20')
        bib_info4 = '<li><a href=' + url + '>Search the catalog</a></li>'
        bib_info5 = '</li>'
        bib_info = bib_info1 + '<ul>' + bib_info2 + bib_info3 + bib_info4 + '</ul>' + bib_info5
        line_tup = (line[0], bib_info)
        data_list.append(line_tup)
    return data_list

def make_html(input_tuples, outfile):
    """ makes html out of the tuples """
    with open('data/' + outfile, 'a', encoding='utf-16') as file_2:
        file_2.write('<ul>')
        item_counter = ''
        for item in input_tuples:
            if item[0] != item_counter:
                file_2.write('</ul><h3>' + item[0] + '</h3><ul>')
            file_2.write(item[1])
            item_counter = item[0]
        file_2.write('</ul>')

def main():
    """ run it! """
    parser = argparse.ArgumentParser(description='Parses a csv of new books')
    parser.add_argument('infile', metavar='[infile]', type=str,
                        help='a csv file')
    parser.add_argument('outfile', metavar='[outfile]', type=str,
                        help='an html file')
    args = parser.parse_args()
    with open('data/' + args.infile, 'r', encoding='cp1252') as file_1:
        data = list(csv.reader(file_1))
        tuples = make_tuples(data)
    make_html(tuples, args.outfile)

if __name__ == "__main__":
    main()
