# CS50-Introduction-to-Computer-Science
Contains final project done for CS50's Introduction to Computer Science


## OptiRoute

Video Demo: https://youtu.be/WaBTM_Di_EM

Description:

OptiRoute is a route planning web application, that gives the user the optimal route for their journey. The user has to provide the locations they need to go to, and OptiRoute will return them the best route on Google Maps where they can immediately set off.

OptiRoute has 2 options of inputting addresses of locations:

Through an Excel Template that can be downloaded, where the user will provide a list of addresses and upload the completed Excel Sheet onto OptiRoute web application.
Manually input the addresses into each column on the web application.
The user will have to enter the start point and end point of their journey, then provide the addresses.

I got inspiration for this project when I was doing an internship at Insect Feed Technologies Pte Ltd, where I had to do some deliveries for the company. We had to plan out our route before we headed off, and I wanted to find a way to automate and optiimise this process. Hence, I decided to use CS50's Final Project as a platform for me to test out creating this idea.

app.py: This is the main application where the flask application is written. Within app.py, there are the following app routes: /preupload - the user will enter their start/end point before uploading the excel sheet /upload - the user will upload their excel sheet of addresses, and the addresses will be processed. The addresses put into a list and passed to the google maps api to optimise waypoints /download - the user can download the excel template /preentry - the user will input their start/end point for manual entry /entry - does the same thing as /upload, but the addresses will be entered manually rather than passed through the excel sheet

helper.py: This a file of helper functions written to deal with the list of addresses. These functions are called in the app.py file.

styles.css: This contains some CSS that were used to style the webpage. Bootstrap was also used.

templates: This file contains all the HTML pages written and used. index - the homepage of OptiRoute, helps user navigate the web app download - to download the excel template preupload - page to take start/end point upload - take excel and get directions preentry - take start/end points entry - take entries and get directions failure - this page is returned when there is an error i.e. invalid addresses

When I was designing this webpage, I had to decide what was the best way for users to input the addresses of the locations they were heading to. As I had already created an Excel Sheet to track the delivery locations I had to go to, it felt like a logical option to include the Upload Excel method. The user can simply copy the column of addresses from their own Excel sheet and paste it into the Excel template, making the Upload Excel method to be more user-friendly in this case. However, when I was testing the website out, it became quite a hassle when I had to edit the excel sheet every time I wanted a new location. This prompted me to design a different method of submission, where the user could directly input the locations they wanted to go to on the web app itself. I designed the manual entry method, where users will get to enter the addresses they would like to go to, and use the information received from the HTML page directly. This required a lot of work, where I had to learn new ways to take information between the front end and back end of the web page. I also had to consult some friends in order to implement the Javascript function.
