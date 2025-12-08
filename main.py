
"""
@author: aaronmateljan
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def poly(x,a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0,k=0):
    y = []
    for i in x:
        y.append(a*x + b)

    return a*x**10 + b*x**9 + c*x**8 + d*x**7 + e*x**6 + f*x**5 + g*x**4 + h*x**3 + i*x**2 + j*x + k

def quad(x, a=1,b=0, c=0):
    y = []
    for i in x:
        y.append(a*x**2 + b*x + c)

    return (a*x**2 + b*x + c)

def cubic(x,a=1,b=0,c=0,d=0):
    y = []
    for i in x:
        y.append(a*x**3 + b*x**2 + c*x + d)
    return a*x**3 + b*x**2 + c*x + d

def expo(x,a=1,h=1,d=0,c=0):
    return a*np.exp((h*(x-d))) + c

def sine(x,a,h,d,c):
    return a*np.sin(h*(x-d)) + c


contents = None

st.title('welcome to the ⋆｡°✩ curve fitter ☾⋆⁺₊⋆ ')

text = st.text_input(label='Enter some text')

if st.button(label='Show text'):
    st.write(text)

CSV = st.file_uploader(label='Upload a CSV to graph', key='something')



if CSV is not None:
    strCSV = str(CSV)
    if '.csv' in strCSV:
        contents = pd.read_csv(CSV, names = ['x', 'y'], header=0, dtype=float, skip_blank_lines = True, on_bad_lines = 'skip', sep = ',')
    else:
        st.write('duuude, this needs to be a CSV :/')
        st.write(strCSV)


list_of_opt = ['poly', 'exponential', 'sine']


style = st.selectbox('what did you want to map your data to? (poly, exponential, sine)', list_of_opt)
if style and contents is not None:
    style = style.lower()
    if False:
        pass
    elif style == 'quadratic':
        coeffs = curve_fit(quad, xdata=contents.x, ydata=contents.y, p0=(1,0,0))
    elif style == 'cubic':
        coeffs = curve_fit(cubic, xdata=contents.x, ydata=contents.y, p0=(1,0,0,0))
    elif style =='exponential':
        st.write(contents.x)
        st.write(contents.y)
        coeffs = curve_fit(expo, xdata=contents.x, ydata=contents.y, p0=(1,1,0,0))

fig, ax = plt.subplots()
st.write('the style is', style)
style = style.lower()

if contents is not None:
    if style == 'poly':
        st.write(contents)
        st.write('choose a degree')
        degree = st.slider(label='Degree', min_value=1, max_value=10)
        coeffs = np.polyfit(contents.x, contents.y, degree)
        ax.scatter(contents.x,contents.y, c='r', alpha=0.25)
        #for i in range(degree+1):
            #fittedy = -(coeffs[-i]*contents.x**(i))
        #i didn't write this entire thing by hand
        #I wrote 1 line and kept copy pasting, modifying them a little each time and using ctrl R a lot
        #This is still pretty stupid, but in my defence I was very tired when programming this part.
        #Couldn't focus enough to make a functional for loop
        if degree == 1:
            fittedy = (coeffs[0]*contents.x + coeffs[1])
        elif degree == 2:
            fittedy = (coeffs[0]*contents.x**2 + coeffs[1]*contents.x + coeffs[2])
        elif degree == 3:
            fittedy = (coeffs[0]*contents.x**3 + coeffs[1]*contents.x**2 + coeffs[2]*contents.x + coeffs[3])
        elif degree == 4:
            fittedy = (coeffs[0]*contents.x**4 + coeffs[1]*contents.x**3 + coeffs[2]*contents.x**2 + coeffs[3]*contents.x + coeffs[4])
        elif degree == 5:
            fittedy = (coeffs[0]*contents.x**5 + coeffs[1]*contents.x**4 + coeffs[2]*contents.x**3 + coeffs[3]*contents.x**2 + coeffs[4]*contents.x + coeffs[5])
        elif degree == 6:
            fittedy = (coeffs[0]*contents.x**6 + coeffs[1]*contents.x**5 + coeffs[2]*contents.x**4 + coeffs[3]*contents.x**3 + coeffs[4]*contents.x**2 + coeffs[5]*contents.x + coeffs[6])
        elif degree == 7:
            fittedy = (coeffs[0]*contents.x**7 + coeffs[1]*contents.x**6 + coeffs[2]*contents.x**5 + coeffs[3]*contents.x**4 + coeffs[4]*contents.x**3 + coeffs[5]*contents.x**2 + coeffs[6]*contents.x + coeffs[7])
        elif degree == 8:
            fittedy = (coeffs[0]*contents.x**8 + coeffs[1]*contents.x**7 + coeffs[2]*contents.x**6 + coeffs[3]*contents.x**5 + coeffs[4]*contents.x**4 + coeffs[5]*contents.x**3 + coeffs[6]*contents.x**2 + coeffs[7]*contents.x + coeffs[8])
        elif degree == 9:
            fittedy = (coeffs[0]*contents.x**9 + coeffs[1]*contents.x**8 + coeffs[2]*contents.x**7 + coeffs[3]*contents.x**6 + coeffs[4]*contents.x**5 + coeffs[5]*contents.x**4 + coeffs[6]*contents.x**3 + coeffs[7]*contents.x**2 + coeffs[8]*contents.x + coeffs[9])
        else:
            fittedy = (coeffs[0]*contents.x**10 + coeffs[1]*contents.x**9 + coeffs[2]*contents.x**8 + coeffs[3]*contents.x**7 + coeffs[4]*contents.x**6 + coeffs[5]*contents.x**5 + coeffs[6]*contents.x**4 + coeffs[7]*contents.x**3 + coeffs[8]*contents.x**2 + coeffs[9]*contents.x + coeffs[10])    
        ax.plot(contents.x, fittedy)
        st.write(fig)
        

    elif style == 'exponential':
        st.write(contents)
        coeffs = curve_fit(expo, xdata=contents.x, ydata=contents.y, p0=(1,1,0,0))
        ax.scatter(contents.x, contents.y, c='r', alpha=0.5)
        fittedy = coeffs[0][0]*np.exp((coeffs[0][1])*(contents.x + coeffs[0][2])) + coeffs[0][3]
        ax.plot(contents.x, fittedy)
        st.write(fig)

    elif style == 'sine':
        st.write(contents)
        coeffs = curve_fit(sine, xdata=contents.x, ydata=contents.y, p0=(1,1,0,0))
        ax.scatter(contents.x, contents.y, c='r', alpha=0.5)
        fittedy = coeffs[0][0]*np.sin(coeffs[0][1]*(contents.x + coeffs[0][2]) + coeffs[0][3])
        ax.plot(contents.x, fittedy)
        st.write(fig)

    else:
        st.write('I\'m sure that\'s a beautiful type of curve but I didn\'t code it')
        st.write('you can enter any of the curves listed')
        st.write('How did you trigger this message anyway?')

if contents is not None:
    st.write('the best fitting function is')
    if style == 'poly':
        if degree == 1:
            st.write(coeffs[0], 'x + ', coeffs[1])
        elif degree == 2:
            st.write(coeffs[0], 'x^2 + ', coeffs[1], 'x + ', coeffs[2])
        elif degree == 3:
            st.write(coeffs[0], 'x^3 + ', coeffs[1], 'x^2 + ', coeffs[2], 'x + ', coeffs[3])
        elif degree == 4:
            st.write(coeffs[0], 'x^4 + ', coeffs[1], 'x^3 + ', coeffs[2], 'x^2 + ', coeffs[3], 'x + ', coeffs[4])
        elif degree == 5:
            st.write(coeffs[0], 'x^5 + ', coeffs[1], 'x^4 + ', coeffs[2], 'x^3 + ', coeffs[3], 'x^2 + ', coeffs[4], 'x + ', coeffs[5])
        elif degree == 6:
            st.write(coeffs[0], 'x^6 + ', coeffs[1], 'x^5 + ', coeffs[2], 'x^4 + ', coeffs[3], 'x^3 + ', coeffs[4], 'x^2 + ', coeffs[5], 'x + ', coeffs[6])
        elif degree == 7:
            st.write(coeffs[0], 'x^7 + ', coeffs[1], 'x^6 + ', coeffs[2], 'x^5 + ', coeffs[3], 'x^4 + ', coeffs[4], 'x^3 + ', coeffs[5], 'x^2 + ', coeffs[6], 'x + ', coeffs[7])
        elif degree == 8:
            st.write(coeffs[0], 'x^8 + ', coeffs[1], 'x^7+ ', coeffs[2], 'x^6 + ', coeffs[3], 'x^5 + ', coeffs[4], 'x^4 + ', coeffs[5], 'x^3 + ', coeffs[6], 'x^2 + ', coeffs[7], 'x + ', coeffs[8])
        elif degree == 9:
            st.write(coeffs[0], 'x^9 + ', coeffs[1], 'x^8 + ', coeffs[2], 'x^7 + ', coeffs[3], 'x^6 + ', coeffs[4], 'x^5 + ', coeffs[5], 'x^4 + ', coeffs[6], 'x^3 + ', coeffs[7], 'x^2 +' , coeffs[8], 'x + ', coeffs[9])
        else:
            st.write(coeffs[0], 'x^10 + ', coeffs[1], 'x^9 + ', coeffs[2], 'x^8 + ', coeffs[3], 'x^7 + ', coeffs[4], 'x^6 + ', coeffs[5], 'x^5 + ', coeffs[6], 'x^4 + ', coeffs[7], 'x^3 + ', coeffs[8], 'x^2 + ', coeffs[9], 'x + ', coeffs[10])

    if style == 'exponential':
        st.write('the best fitting function is')
        st.write(coeffs[0][0], '*2^(', coeffs[0][1], '(x + ', coeffs[0][2], '))', '+ ', coeffs[0][3])

    if style == 'sine':
        st.write('the best fitting function is')
        st.write(coeffs[0][0], '*sin(', coeffs[0][1], '(x - ', coeffs[0][2], ')) + ', coeffs[0][3])

    errors = coeffs[1]
    st.write('the average error is', np.mean(errors))


st.write('Hey you')
st.write('yeah you')
st.write("I wanted to add something fun at the last minute to my site so here are some videos and articles I enjoyed.")
st.write("Try refreshing the site and seeing what you get")
st.write('(I hope) a random link will be generated each time')
st.write('if you really wanna, you can just find all the links at the end of my code')
st.write('you gotta upload a file first')
if contents is not None:
    advice = np.random.randint(1,9)
    if advice == 1:
        st.write('Here\'s a tone deafness test!')
        #Music test
        st.write('https://www.themusiclab.org/quizzes/td')
    elif advice == 2:
        st.write('Check out this crazy article!')
        #Every 60 seconds in Africa, a byte of data passes.
        st.write('https://phys.org/news/2009-09-carrier-pigeon-faster-broadband-internet.html')
    elif advice == 3:
        st.write('check out this cool video! (It\'s funny I swear)')
        #spiders on drugs
        st.write('https://www.youtube.com/watch?v=sHzdsFiBbFc')
    elif advice == 4:
        st.write('Harry Potter... with a twist!')
        #harry potter w guns
        st.write('https://www.youtube.com/watch?v=8sz5NbI-CPs')
    elif advice == 5:
        st.write('here\'s a monty python sketch I love')
        #Dennis Moore
        st.write('https://www.youtube.com/watch?v=qLkhx0eqK5w&t=5s')
    elif advice == 6:
        st.write('here\'s an amazing geometery video')
        #Outside in
        st.write('https://www.youtube.com/watch?v=wO61D9x6lNY&t=902s')
    elif advice == 7:
        st.write('Check out this_website_will_self_destruct')
        #RIP this_website_will_self_destruct
        st.write('Unfortunately, after 3 years of service, as promised, the site did self destruct.')
        st.write('You can see what it looked like using the Internet Archive')
        st.write('https://web.archive.org/web/20230308185510/https://www.thiswebsitewillselfdestruct.com/')
    elif advice == 8:
        st.write('I HIGHLY recommend the Magnus Archives on Youtube')
        #Magnus archives
        st.write('It\'s a podcast style story where each episode reviews a file from the \'supernatural\' archive')
        st.write('When I say story, I mean it. There\'s a deep and very well written overarching story to these cases')
        st.write('If you\'re cleaning the house or just need a break from work, give it a listen!')
        st.write('Episode 1: https://www.youtube.com/watch?v=AdiUHYacaRI')


    st.write("thank you. Come again :)")