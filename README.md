# Lyft Price Tracker

I commute to the same few locations with lyft and sometimes with my car. There were days and times where the price of a Lyft ride would be a decent price and other times the price would be really high or really low. I decided to create an application that would continously gather the price of a Lyft ride with a predetermined pickup and dropoff location. It would gather this data every couple hours from Lyft's website, and upload this data to a database where I could then observe the average price at a certain time of day, which days were the best to ride overall, etc.

# As of right now...

The program is configured to run on your computer and store the information in a csv and a database on MongoDB. I plan to change it so that it will run in a server on heroku, upload the data to a database, then upload that data to a csv file so that the numbers can be entered into different graphs and plots to depending on what the user wants to observe.

# ALSO

I am not sure how legal this all is, so I am working on this to make a cool project, but do not plan to actually continously run a bot on Lyft's website when this is all completed. 


