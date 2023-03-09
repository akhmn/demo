import streamlit as st
import math
import matplotlib.pyplot as plt
m = st.slider("Enter the value of slit width")
st.write(m)
o = st.slider("Enter the value of theta")
st.write(o)
p = math.sin(o)*m
st.write("path difference= ",p)
lambd =st.slider("Enter the value of lambd")
phase=(math.pi*2)/lambd
st.write("phase difference=",lambd)
# width of central maxima
f=st.slider("enter the value")
st.write("distnce between slit and screen=",f)
y=(2*f*lambd)/m
st.write("width of central maxima=",y)
aplha = (math.pi*p)/lambd
st.write("aplha=",aplha)
#using the theory of n harmonic vibration pf same amplitude (a) and having common phase differnce ,resultantant amplitude is
#na is no.of harmonic vibration multiplied by amplitude of each harmonic vibrator is represented by A
A=st.slider("let value of A be")
R =(A*math.sin(aplha))/aplha
st.write("Resultant Amplitude=",R)
I=(R**2)
st.write("Intensity=",I)
st.line_chart(I,aplha)