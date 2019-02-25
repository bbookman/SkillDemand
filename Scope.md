# Skill Demand - Scope Document
## Team members:
* Bruce Bookman
* Nirmal Jayaraman  
## Short description
The skill demand application will use a set of defined domain specific skills to scrape job openings from popular sites such as indeed.com in order to produce data to help identify the most highly sought after skills for a set of pre-determined job titles in a given geography

## Scope of the project
The program will scrape publicly available job opening data from popular job search websites (such as indeed.com and monster.com).  The program will produce a files that can be ingested in Notebooks to produce graphical results

* Indeed.com and other job websites will supply raw data.  Sites will be added as time permits
* Program will leverage scraping tools such as selenium, beautiful soup and scrapy to obtain / scrape job sites
* All job opening data is public and there are no privacy issues
## Deliverables
* The minimum deliverable (MVP) will include the python application open and available on github
* A readme.md file will be produced explaining the usage of the application
* The application itself will produce, at minimum, a human readable list of skills and the corresponding count of those skills for a given job title and geo
* A graph in Jupyter Notebooks will be produced to easily visualize the counts for each skill
* The application will use pandas dataframes or other methods to identify the most sought after skill in a geographical areas, and by salary
* For a given skill, the application will use pandas dataframe to get the highest/average salary offered in different geographical areas (states)

**Presentation date: March 21st**
**Presentation week is _30_ Days away**

### Milestone 1: Feb 15 2019
* Code available on public github repo

### Milestone 2: March 15 2019
* Prototype will scrape data from indeed.com
* Prototype Notebook will display a graph showing skills in demand for a predefined job title

### Milestone 3: March 15 2019
* Fully functional app
* Data from: indeed.com and one other job site TBD

### Stretch goals:
* Include data from linkedin.com, glassdoor.com, dice.com, careerbuilder.com, monster.com and/or other major job sites


## Document
This document was copied from [original google doc](https://docs.google.com/document/d/1z0yQyPqB6xyIo5EwPaph5A9CERkfgL8gPs7JxKRMhnY/edit?usp=sharing)
This will now be the living and official document

