Simple Tracking assignment
===========================================

A tracking pixel is commonly used to capture visitor activity on web sites, in order to later display statistics on page views, visits and advertising.
Currently the most frequently used tracking is Google Analytics, but it's common for web sites to use more than one solution in parallel.

The task in this assignment is to implement a rudimentary tracking solution.
Provide an implementation with suitable unit tests, that accepts http requests for tracking and a command line interface for reporting, that fulfills the following requirements.

Feature: Log Pageview
-------------------------------
  In order to gather statistics on each page view made by visitors to my web site
  As a webmaster
  I want to a plain image tag for a transparent 1x1 gif that can be placed on each page
  And a log of each request to the image including a timestamp, the url of the page, 
  and the unique cookie id of the visitor.
  
  Scenario: Basic Logging
  	Given all pages on my site contains an image tag referencing the tracking gif
  	And the next unused cookie id is 12345
  	And the time is "2013-09-01 09:00:00UTC"
  	When a new visitor "Per" views the page "/contact.html" on my site
  	Then a cookie with a new id 12345, should be placed in Per's browser
  	Then the visitor log should contain "2013-09-01 09:00:00UTC /contact.html 12345"
    
  Scenario: Repeat Visit
  	Given all pages on my site contains an image tag referencing the tracking gif
  	And the time is "2013-09-01 10:00:00UTC"
  	When a repeat visitor "Per" with cookie id 12345 views the page "/contact.html" 
  	Then the visitor log should contain "2013-09-01 10:00:00UTC /contact.html 12345"
    
Feature: Display Report
-------------------------------
  In order to understand how visitors use my web site
  As a webmaster
  I want a simple report that for each page displays the number of page views 
  and unique visitors for a given time range.

  Scenario: Basic Report
    Given a log of visits to my web site that contains:
      |timestamp              |url           |userid|
      |2013-09-01 09:00:00UTC |/contact.html |12345 |
      |2013-09-01 09:00:00UTC |/contact.html |12346 |
      |2013-09-01 10:00:00UTC |/contact.html |12345 |
      |2013-09-01 10:01:00UTC |/about.html   |12347 |
      |2013-09-01 11:00:00UTC |/contact.html |12347 |
    When I view the report for the time range 2013-09-01 09:00:00 - 10:59:59
    The the report should contain the data:
      |url           |page views |visitors|
      |/about.html   |1          |1       |
      |/contact.html |3          |2       |
    

Implementation
-------------------------------
The implementation should be made in Python, Ruby, Java, Javascript (ask if you want to use another language) and may use reasonable third party libraries (open source or libraries bundled with the relevant run-time). The delivery should contain a Readme file with information on how to build, test, and run your project. Use appropriate and commonly known build tools for your platform (no dependencies on a specific IDE). The build and instructions should be suitable for Ubuntu or OSX. 

This assignment is expected to require a few hours of work, but definitely not a full day. Please focus on clear, readable code and a well packaged delivery. If it seems like too much work you have likely misinterpreted something. Feel free to email questions.

Please submit your solution by email as a single zip file or as a link to a hosted file.

FAQ:
-------------------------------
Q: Is the format of timestamp, url, userid important?
A: No, use whatever makes sense to you

Q: Are userids supposed to be numeric and/or sequential?
A: No, you are free to use any type and strategy to get unique ids

Q: Should I use BDD/Cucumber?
A: No, the examples above are just my way of explaining. Unit tests are fine for the assignment.

Q: Should the command-line interface be interactive?
A: No, just accepting standard command-line parameters for the time-range is fine
