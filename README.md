# About
This app takes an input of a name as a string. 
Using a model trained on data set from student's well-being checkin application called Skodel,
It makes predictions on the user's mood, why they are feeling that and what their next check in might be. 
The data is processed using Pandas inside a Flask sever. 
This app uses React, React-Bootstrap and Font-Awesome to efficently build an eye-catching user interface. 

# Privacy
Original Data isn't uploaded for privacy of users. 
Processed data exludes last names and other data that could be used to identify users. 

# Note
For names not in the data set, the model will still make a prediction based on the sample data set, but will have reduced accuracy. 
