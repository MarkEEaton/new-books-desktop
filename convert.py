""" turns a csv of new books into html """
import csv


def make_tuples(input_data):
    """ make tuples out of the csv data """
    data_list = []

    for line in input_data:
        bib_info1 = '<li><strong>' + line[2] + '</strong>'
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

def make_html(input_tuples):
    """ makes html out of the tuples """
    with open('output.html', 'a') as f2:
        f2.write('<ul>')
        for item in input_tuples:
            f2.write(item[1])
        f2.write('</ul>')

if __name__ == "__main__":
    with open('March2018.csv', 'r') as f1:
        DATA = csv.reader(f1)
        tuples = make_tuples(DATA)
    make_html(tuples)
