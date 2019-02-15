# Skill Demand - Scope Document
## Team members:
* Bruce Bookman
* BaSiL
* Nirmal Jayaraman  
* Frank Merla
## Short description
The skill demand application will use a set of defined domain specific skills to scrape job openings from popular sites such as indeed.com in order to produce data to help identify the most highly sought after skills for a given target job title in a given geography

## Scope of the project
The program will scrape publicly available job opening data from popular job search websites (such as indeed.com and monster.com).  The program will return a csv file(s), dataset(s) or graph(s) that show which skills are in demand for a given job title and domain skill set

* Indeed.com and other job websites will supply raw data.  Sites will be added as time permits
* Program will leverage scraping tools such as selenium, beautiful soup and scrapy to obtain / scrape job sites
* All job opening data is public and there are no privacy issues
## Deliverables
* The minimum deliverable (MVP) will include the python application open and available on github
* A readme.md file will be produced explaining the usage of the application
* The application itself will produce, at minimum, a human readable list of skills and the corresponding count of those skills for a given job title
* A table will be produced listing the skills and counts of each skill for a given job title
* A graph will be produced to easily visualize the counts for each skill
* The application will use pandas dataframe to identify the most sought after skill in a geographical area and an option to compare the skills in demand between geographical areas (states)
* For a given skill, the application will use pandas dataframe to get the highest/average salary offered in different geographical areas (states)
* Web front end
  * Allow user to input a target job title
  * Add titles the user deems “similar” to the target job title
  * User enters skill “keywords” that will be the basis for the count
  * The user will be presented with a bar graph displaying the keywords and counts (see end of this document for sample)
  * The user will be presented with a table listing the keywords and counts from highest to lowest

## Milestones
**Presentation date: March 21st**
**Presentation week is _30_ Days away**

### Milestone 1: Feb 15 2019
* A sitemap and/ or mock up containing the most important pages in our app
* Completed Scope Document *OVERDUE*
* Trello Board
* Code available on public github repo

### Milestone 2: March 1 2019
* Front End uses mock data and presents sample charts/graphs/tables
* Prototype will scrape data from indeed.com

### Milestone 3: March 15 2019
* Fully functional app
* Data from: indeed.com and one other job site TBD

### Stretch goals:
* Include data from linkedin.com, glassdoor.com, dice.com, careerbuilder.com and monster.com
* Project repository will include tests (pytest, unittest or whatever)
* User will be able to specify not only job title and zip code but also target salary and job posting age
* After user supplies a job title, a set of possible similar titles are presented.  These can be added to the users set of target titles
* After the user supplies an initial set of skills, a set of skills within the same domain will be presented and the user can add these indicating desire to include in results

## Document
This document was copied from [original google doc](https://docs.google.com/document/d/1z0yQyPqB6xyIo5EwPaph5A9CERkfgL8gPs7JxKRMhnY/edit?usp=sharing)
This will now be the living and official document

