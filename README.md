# Babel-Library-Book-Fetch
This python script fetches the selected book from the famous Online Babel Library (https://libraryofbabel.info/) (Don't know what the Babel Library is? https://en.wikipedia.org/wiki/The_Library_of_Babel) it lets the user input the hex, wall, shelf, and volume number of a book and it gives back the actual book as well as having a function to download separate pages with the search with bookmark function which lets you input a very short string and get access to 3200 characters (1 page)

This program was only tested on Windows although it should work on Linux and maybe MacOS


## This project was originally created for the B.L.U.E. project

### Why for the B.L.U.E. project?

Because B.L.U.E. will store huge quantities of data that will be impossible to backup as a whole, so my idea is to store short 10 character bookmarks instead of whole 3200 character pages
I added the functionality to get whole books by generated ID (which I am working on to shorten the ID) or to get books by manually typing in hex, wall, shelf and volume (as explained in previously) but this function is mainly for people who just want to play around with it


### About B.L.U.E.

### What does B.L.U.E. stand for?

The B.L.U.E. project stands for Broad Learning Universal Education project


### What is the B.L.U.E. project?

The B.L.U.E. project aims to develop a huge free, open-source, internationally recognized website that contains useful and accurate information about almost everything so anyone can learn anything in any field


### How can I help or contribute?

Only join if you will actively help the project, please do not purposefully slow down our progress
Just watch this introduction video https://youtu.be/qcRKmm3B25c?si=9VMqPcrBtKhbT38S and in the description, you will find a link to the discord server






## About the program

## Why should I use this?

Because it is an easy, lightweight solution in case you need to download whole books or single pages from the babel library.
Plus, it adds an option to just store bookmarks instead of whole books saving up a ton of space on long texts


## How to use

Open terminal and navigate to the directory where you have cloned/downloaded the repository
When you have reached the directory in Command Prompt type

```
python main.py
```

✅ It should work fine!

### Five options will appear:
1. Use bookmark link to get single page
2. Automatic mode
3. Manual mode
4. Convert Manual into Automatic query
5. Exit

#### Use bookmark link to get single page:
It opens up three options:
1. Get page with shortened bookmark (Recommended when storing bookmarks)
2. Get shortened bookmark from bookmark link (Recommended to store bookmarks)
3. Get page with bookmark link (Recommended for one time use only)
4. Exit

1: Type the shortened bookmark in the input field and the page will download in a file named BabelPageOut.txt in the current working directory

⚠️ Attention: If the entered bookmark is invalid, the output will just be a random babel page, which most of the time is just gibberish

2: Type in the bookmark link copied from the website into the input field and a shortened bookmark should be printed.

· How do I get the bookmark link?
Simple, you open the desired book at the correct page, you click on the button on the left named "Bookmarkable", you insert a name and click OK
You then go to the navigation bar and copy the current link (it should look something like https://libraryofbabel.info/bookmark.cgi?name_you_have_given_to_the_bookmark)
You then copy and paste it into the "2. Get shortened bookmark from bookmark link" module and you will get a shortened bookmark (which is basically just the part after "bookmark.cgi?")

3: Type in the link to the bookmark and it will download the page. This is only recommended if you will use it just one time. If your plan is to store bookmarks, refer to 2. Get shortened bookmark from bookmark link and 1. Get page with shortened bookmark


4: It is pretty self explanatory, it exits the program

#### Automatic mode:
Paste an Automatic query (generated with the fourth option) in the input field and press enter
The book should download automatically and store itself in a file named BabelBookOut.txt in the current working directory

#### Maual mode:
Paste the hex, wall, shelf, and volume
The book should download and store itself in a file named BabelBookOut.txt in the current working directory

#### Convert Manual into Automatic query mode:
Paste the hex, wall, shelf, and volume
The automatic query should display in a file named AutoQueryOut.txt, just open the file and copy the query ID

#### Exit:
It is pretty self explanatory, it exits the program



Any errors or questions you have, feel free to write an issue or contact me through e-mail

J1D1.7398@gmail.com
