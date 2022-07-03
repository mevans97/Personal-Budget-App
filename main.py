'''
So here is my attempt at making a personal finance calculator using python streamlit :

I wrote all my notes as i went along for learning purposes as well as explaining the project on my youtube channel which can be found
here : https://www.youtube.com/channel/UC5HXUbZ98xCalomnkPfZVGA

First thing i had to figure out was how to utilize python packages; more specifically streamlit .

My original attempt went like this :
    I went on streamlit.io and tried to install the packages using the windows command prompt terminal.
    I installed streamlit however, when i tried to import streamlit into my python script, the followiing error occured :
        'Import "plotly.graph_objects" could not be resolved'

I looked online and found a solution here : https://github.com/streamlit/streamlit/wiki/Installing-in-a-virtual-environment

Apparently streamlit has an officially-supported environment manager on Windows known as Anaconda Navigator :
    The Navigator can be downloaded here : https://docs.anaconda.com/anaconda/install/

So i was confused, I thought the Python IDLE(Integrated development learning enviornment) was enough to utilize all aspects of python
So to clear up this misunderstanding I looked up the difference between an IDLE and an Enviornment Manager such as Anaconda. 
Here is the explanation i found : https://qr.ae/pvPgCy

So i looked at the anaconda documentation showing all the python packages pre installed and ready to use. 
streamlit was not there so i decided to install it using the terminal found in the anaconda navigation app.
IT WORKED ! The first part of the journey is now a success and I can begin coding

Streamlit Documentation : https://docs.streamlit.io/library/api-reference

'''

import streamlit as st 

st.set_page_config( page_title='Personal Budget Calculator')
st.title('Personal Budget Calculator')

explanation = st.container()
with explanation:
    st.write('This calculator is meant to review your current spending and create a budget using the 50/30/20 rule. Senator Elizabeth Warren popularized the so-called "50/20/30 budget rule" (sometimes labeled "50-30-20") in her book, All Your Worth: The Ultimate Lifetime Money Plan. The basic rule is to divide up after-tax income and allocate it to spend: 50% on needs, 30% on wants, and socking away 20% to savings. Here, we evaluate your current spending, create a reccomended budget using your post tax income and comparing the reccomended budget to your current monthly spending. I hope this helps !')

st.header('**Income**')
st.caption('Here we will evaluate your monthly income and calculate your income after taxes')
st.subheader('Monthly Income')
colIncome, colTax = st.columns(2)

with colIncome:
        monthlyIncome = st.number_input('Enter Your Monthly Income Before Taxes : ',min_value=0.0)

with colTax:
        monthlyTax = st.number_input('Enter Percentage Taxed On Income : ', min_value=0.0, max_value=100.0)

taxes = monthlyTax / 100
monthlyTakeHome = monthlyIncome - (taxes * monthlyIncome)

st.header('**Expenses**')
st.caption('Here we will evaluate your monthly expenses')
colExpenses1, colExpenses2 = st.columns(2)

with colExpenses1 :
    st.subheader('Monthly Housing')
    monthlyHousing = st.number_input('Enter Monthly Housing Expenses')

    st.subheader('Monthly Utilities')
    monthlyUtilities = st.number_input('Enter Monthly Housing Utility Expenses')

    st.subheader('Monthly Entertainment')
    monthlyEntertainment = st.number_input('Enter Monthly Entertainment Expenses')



with colExpenses2 :
    st.subheader('Monthly Transportation')
    monthlyTransport = st.number_input('Enter Monthly Transportation')

    st.subheader('Monthly Food')
    monthlyFood = st.number_input('Enter Monthly Food Expenses')

expenses = monthlyHousing + monthlyEntertainment + monthlyFood + monthlyTransport + monthlyUtilities
savings = monthlyTakeHome - expenses

st.header('Totals')
st.subheader('Monthly Income After Taxes : $' + str(round(monthlyTakeHome))) 
st.subheader('Monthly Expenses : $' + str(round(expenses)))
st.subheader('Amount Left To Save And Invest : $' + str(round(savings)))


recommendedCol,currentCol = st.columns(2)

reccomendedNeeds = monthlyTakeHome * 0.5
reccomendedWants = monthlyTakeHome * 0.3
reccomendedSavings = monthlyTakeHome * 0.2

currentNeeds = monthlyHousing + monthlyFood + monthlyTransport + monthlyUtilities
currentWants = monthlyEntertainment
currentSavings = savings

with recommendedCol:

    st.header('Recommended Budget')
    st.caption('Here is an ideal budget using the 50/30/20 rule with your post tax income')
    st.subheader('Needs (50%) : $' + str(round(reccomendedNeeds)))
    st.subheader('Wants (30%) : $' + str(round(reccomendedWants)))
    st.subheader('Savings (20%) : $' + str(round(reccomendedSavings)))

with currentCol:
    st.header('Current Budget')
    st.caption('Here is your actual expenses on your needs, wants and savings')
    st.subheader('Needs : $' + str(round(currentNeeds)))
    st.subheader('Wants : $' + str(round(currentWants)))
    st.subheader('Savings : $' + str(round(currentSavings)))