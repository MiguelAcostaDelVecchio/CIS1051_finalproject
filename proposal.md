# Proposal

## What will (likely) be the title of your project?

Stock Suggestions Based on Monte Carlo and Machine Learning Simulations

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

The purpose of the project is to create a program that will perform Monte Carlo and Machine Learning simulations of a
given stock's historical data. Based on the results of the Monte Carlo and Machine Learning simulations, if there is 
enough upside or downside that can be exploited (this will be specified through a certain threshold), the program will 
suggest buying or shorting the given stock. Otherwise

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

In theory, the user would be able to enter the ticker symbol of a stock in the S&P500 and the program should
automatically perform a Monte Carlo and Machine Learning simulation on the historical data of the stock. If both the 
Monte Carlo and Machine Learning simulations determine that the stock has an upside or downside greater than a specific
threshold, then it would suggest to the user to either buy or short the stock. On the other hand, if the program
determines that the stock does not have sufficient upside or downside, then it would suggest the user to not buy the
stock. 

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

N/A

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

N/A

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

The program will only analyze a pre-defined stock and suggest whether it is a buy/short opportunity or not a good
opportunity using only the results of a Monte Carlo simulation.

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

The program will only analyze a pre-defined stock and suggest whether it is a buy/short opportunity or not a good 
opportunity using the results of both the Monte Carlo and Machine Learning simulation.

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

The user will be able to input the ticker symbol of any stock in the S&P500 into the program and the program will 
determine whether the stock is a buy/short opportunity or not a good opportunity using the results of both the Monte 
Carlo and Machine Learning simulation. 

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

What APIs can I use to get historical information about stocks?
    a) Is there a limit to how many APIs I can use in a day/week/month?
    b) Can I get information about all the stocks in the S&P500?

How to determine stock price using Monte Carlo simulation?
    a) Are there any libraries available that I can use?

How to create a Machine Learning algorithm that will predict stock price?
    a) Are there any libraries available that I can use?
