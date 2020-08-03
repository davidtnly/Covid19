### COVID-19

### Introduction

This was a personal project that I was interested in since it was a new dataset that was part of the health/medical area. I started working on late January 2020 and created the initial Tableau dashboard and published it on my [Tableau Public Gallery](https://public.tableau.com/profile/david.ly#!/vizhome/2019-nCoVGlobalCasesWuhan/Dashboard). This dashboard was updated on a daily basis up until April 10, 2020. From Jan - Apr 10, the dashboard has gained about 40,000 views.

### Background

The World Health Organization has declared the epidemic an international public health emergency, acknowledging that the virus outbreak caused by a novel (new) coronavirus (officially named COVID-19) that was first detected in Wuhan City a risk outside of China.

Coronaviruses are a large family of viruses that cause illness ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS). COVID-19 is a new strain of coronavirus that has not been previously identified in humans.

### Data and Methods

I am going to attempt to update the data on a weekly or monthly basis now after creating an automated process using Python. 

JHU CSSE
- https://github.com/CSSEGISandData/COVID-19

GISData/NextStrain
- https://nextstrain.org/ncov

_____________________________________________________________________________________________

### Current Setup

1. Git clone the data from JHU's [Github Repo Here](https://github.com/CSSEGISandData/COVID-19)

2. Create a "Merge" folder to store in all new data that will be combined together

3. Run ```py import_new_files.py``` to delete any old files and add new ones to the "Merge" folder  (For new users, need to update paths in the script based on user)

4. Run ```py merge_and_clean.py``` to automate the cleaning and merge process  (For new users, need to update paths in the script based on user)

5. Add the newly cleaned data to the master CSV file (2019_nCoV_data.csv)

6. Open up the Tableau workbook and update the data

### Previous Setup

When COVID-19 was newer and unknown, the data was a lot messier and inconclusive. I had to manually research for newer data like geolocations, confirmed cases, dates, country capitals to fill in any missing cities/provinces and more. This process has been simplified a lot thanks to JHU and their team. As of July 2020, I am using their data with some additions to my excel formulas to fill in blanks. 

Some other data gathering steps included:

1. Using Alteryx to create a view that would show how much the virus has spread throughout the world

2. Gathering additional information from public sources to supplment the dashboard like: other viruses' statistics, google trends, etc.
_____________________________________________________________________________________________

### Contact me!

I always welcome feedback and I enjoy connecting with individuals so feel free to drop by my [LinkedIn](https://www.linkedin.com/in/davidtly) and connect!
