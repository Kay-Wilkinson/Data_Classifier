# Data Classifier
Parse out infomation from a CSV as part of the data processing stage of Data Science/Analysis
<!--
  Title: Data Classifier
  Description: Data Science, Data Analysis, Python, Regex, Classifier, Classifiy, Clustering
  Author: Kay-Wilkinson
  -->
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="">
    <img src="https://github.com/Kay-Wilkinson/Data_Classifier/blob/master/PhotoFunia-1571655487.jpg" alt="This would have shown a cool vapourwave logo :/" width="700" height="420">
  </a>

  <h3 align="center">Data Classifier for Pre-Processing Stage</h3>

  <p align="center">
    Have a CSV file full of dense data? Strip it out to find the good stuff... 
    <br/>
  </p>
</p>

## About the project

This project is intended for the pre-processing stage of data analysis, whereby raw data must be converted into more meaningful representations.

Note: This project is still in it's WIP status.
<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Virtual Env](#virtualenv)
  * [Installing Dependencies](#running-the-container)
* [Run the Script](#token-and-password-set-up)
* [Roadmap](#Reusing-the-Docker-container)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
### Built With
I have intentionally kept the dependencies of this project to a bare minimum and therefore the only 3rd party packages needed (at this point), is BeautifulSoup and urllib. 
Note that these are only required should you want to use the IAB Deep Search
* [bs4][a link](https://pypi.org/project/beautifulsoup4/)

## Getting Started

Simply create a virtualenv for your project and run the script. Ensure that any CSV you wish to parse is in the same directory level as the script.

### Virtual Env
The first step was to create a virtualenv:
```
$ mkvirtualenv classifier
```

You can be sure that you are working inside your virtualenv because the env name: 'classifier' will now appear at the beginning of the terminal line (prior to the $). 

### Install Dependencies
```
$ pip install -r requirements.txt
```

### Run the Script
Update the `read_and_parse_target()` function inside of main to point to the correct file name. 
Then:
```
$ python classy.py
```
Output will be a CSV file within the same directory level

## Roadmap

* Fix iteration issues on keys() within edge_case function
* Optimise writing to CSV to be quicker.
* Take in user input of filename 
* Write to database Table
    * Option for Hadoop Table
    * Option for MySQL Table
* Read from DB Table, instead of CSV file
* Expand classification functions to include groupings (e.g. Age Groupings) and to search for more options.

## Contibutors
If you would like to contribute to this project, please make a pull request. 

## Licence
This project operates under an MIT licence. Feel free to use and update this code to fit your needs, just credit my work with a comment in your code. 

## Contact
