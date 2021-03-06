# Make an HTML document out of a spreadsheet of new books

![Screenshot of the application](img/screenshot.png?raw=True)

- This application was developed to solve a specific problem faced by our librarians: how to turn a spreadsheet of new books into an HTML document quickly and easily.
- Because our acquisitions librarian needed to be do this regularly, coding the HTML by hand was not a viable option.
- So the application we wrote automatically produces an HTML output from a CSV file. This HTML is suitable for cutting and pasting into a LibGuide.

## To set up the application

These instructions assume you already have the following installed: git, python 3, pipenv

To build the converter executable at the command line (you only need to do this part once):

    $ git clone https://github.com/markeeaton/new-books-desktop   # this will clone the github repository to your machine
    $ cd new-books-desktop   # go to the repository directory
    $ pipenv install   # to get the necessary packages
    
Then open up `build.spec` and replace `REPLACE_ME` with the name that you want to give your application.

Then, to build the application, run:

    $ pipenv run PyInstaller build.spec

The executable application will be in the `new-books-desktop/dist` directory. It will have the name that you gave it in the `build.spec` file.

If you need more detail about the build process, see the packaging instructions at the Gooey [page](https://github.com/chriskiehl/Gooey#packaging).


Once the application has been built, you can run it. You can navigate to your CSV file.

The CSV should be organized as follows:

|    A     |    B   |    C  |    D        |   E   |
|:--------:|:------:|:-----:|:-----------:|:-----:|
| LC Class | Author | Title | Call Number |  ISBN |
|   ...    |   ...  |  ...  |     ...     |  ...  |

- Be sure to include a row with column headers!
- You can run the application to process the CSV file. The output will be an `html` file in the same directory as the CSV.

## Want to run a command line version?

See the repository for the [command line application](https://github.com/markeeaton/new-books.git).

## Want to see more?

Presented as a poster "[Improving Workflows and Outreach with Python: Automating a New Books LibGuide](https://acrl2019-acrl.ipostersessions.com/default.aspx?s=37-56-DD-3C-35-98-74-74-B1-1A-26-90-E1-A6-31-35)" at ACRL 2019 in Cleveland, OH
