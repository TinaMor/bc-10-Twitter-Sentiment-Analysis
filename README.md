# Twitter Sentiment Analysis

## Introduction

![sentiment definition](sentiment.png)

This a console application that helps you get a glimpse of sentiments that can deduced from your twitter status updates.

The application grabs your status updates, checks the frequency of important words in the tweets and also uses the IBM Alchemy API to deduce sentiments.

### Sentiments

Google dictionary defines 'sentiment' as 
> a view of or attitude toward a situation or event; an opinion.
> a feeling or emotion.

The scope to of this application is constrained to doing two things:
* Deducing emotions expressed in the tweets. By emotions, I mean feelings such as anger, fear, joy and so on. Ordinarily, one expects a mixture of emotions to be expressed. Thus, you will be presented by a list of five different emotions with a percentage score for each.
* Overall sentiment -- whether your tweets express positive view, negative view or neutral view. Again, a percentage score for each sentiment is also displayed.

NOTE: This analysis is done using artificial intelligence by the awesome folks at [IBM Alchemy API](http://www.alchemyapi.com/). 
**THE RESULTS DISPLAYED BY THIS APPLICATION SHOULD NEVER BE USED AS A BASIS FOR ANY PERSONAL OR BUSINESS DECISIONS; ANY SENTIMENTS DISPLAYED ARE PURELY FOR ENTERTAINMENT VALUE AND PROGRAMMING PLEASURE.**

## Installation and Setup

**Twitter Sentiment Analysis currently works in Python 3 only. It will be ported to Python
 2 soon, so please, bear with it for now.**

To get up and running:

Clone this repo using the url:

     https://github.com/michaelkamau/bc-10-Twitter-Sentiment-Analysis
      
Navigate to the Twitter Sentiment Analysis folder and install dependencies:

      pip3 install -r requirements.txt

If the pip3 is not installed, please install it from your Package Manager. It is generally called 
      
        python3-pip

To run the application:
    
        python3 main.py

If **Python3 is default in your setup**:

        python main.py
    

_THAT'S it!_


You will be greeted by this screen 
![main screen](screen.png)

### ToDo List

They say data is the new oil. A lot more can be done to enhance the functionality of this application. Below is a list of feature I intend to add to the application:

* Give user more control over which sentiments to analyse
* Add ability to analyse many accounts at the same time; and compare sentiment results.
* Create a Python 2 port

If you have any suggestions, comments, requests, complains or gifts, feel free to [contact me](mailto:tokamau@gmail.com) 

## Why am I doing this?

This project is part of the Andela boot-camp set of activities, which am currently participating in.

Feel free to comment on the code or ask any questions about the boot-camp.
