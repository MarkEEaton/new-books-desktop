# Make an HTML document out of a spreadsheet of new books

- This script was developed to solve a specific problem faced by our librarians: how to turn a spreadsheet of new books into an HTML document quickly and easily.
- Because our acquisitions librarian needed to be do this regularly, coding the HTML by hand was not a viable option.
- So the script we wrote automatically produces an HTML output from a CSV file. This HTML is suitable for cutting and pasting into a LibGuide.

## To use the script

These instructions assume you already have the following installed: git, python 3, pipenv

To set up the converter at the command line (you only need to do this part once):

    $ git clone https://github.com/markeeaton/new-books   # this will clone the github repository to your machine
    $ cd new-books   # go to the repository directory
    $ pipenv install   # to get the necessary packages

Then you should have your input spreadsheet organized as follows:

|    A     |    B   |    C  |    D        |
|:--------:|:------:|:-----:|:-----------:|
| LC Class | Author | Title | Call Number |
|   ...    |   ...  |  ...  |     ...     |

- Be sure to include a row with column headers!
- The data goes below. 
- Save it as a CSV file. Place it in the `new-books/data/` directory.

Once that's set up, you can use the convert script by replacing `input.csv` and `output.html` in this command with your own filenames:

`$ pipenv run python convert.py input.csv output.html`

The output file will be in the `data/` directory.

## Want to run a desktop version?

Use the `gooey` branch of this repository. Run `pipenv install pyinstaller` to get the packaging library, and then follow the packaging instructions at the Gooey [page](https://github.com/chriskiehl/Gooey#packaging).

## Want to see more?

Presented as a poster "[Improving Workflows and Outreach with Python: Automating a New Books LibGuide](https://acrl2019-acrl.ipostersessions.com/default.aspx?s=37-56-DD-3C-35-98-74-74-B1-1A-26-90-E1-A6-31-35)" at ACRL 2019 in Cleveland, OH
