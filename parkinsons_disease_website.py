import streamlit as s
import pandas as pd
import pickle as p

s.title("Parkinson's disease prediction")
average = s.number_input('enter Average vocal fundamental frequency (MDVPFo)')	
minimum = s.number_input('enter Minimum vocal fundamental frequency (MDVPFlo)')
shimmer = s.number_input(' enter measure of variation in amplitude (MDVPShimmer)')
apq = s.number_input('enter measure of variation in amplitude (MDVPAPQ)')
hnr = s.number_input('enter measure of ratio of noise (HNR)')
spread1 = s.number_input('enter nonlinear measure of fundamental frequency variation(spread1)')
spread2 = s.number_input('enter nonlinear measure of fundamental frequency variation(spread2)')
ppe = s.number_input('enter nonlinear measure of fundamental frequency variation(PPE)')

if s.button('predict'):
    in_pickle = open("parkinsons.pkl", 'rb')
    pipe = p.load(in_pickle)
    result = pd.DataFrame(
        [[average, minimum, shimmer, apq, hnr, spread1, spread2, ppe]],columns = ['MDVP:Fo(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Shimmer',                                    'MDVP:APQ', 'HNR', 'spread1', 'spread2', 'PPE'])

    r = pipe.predict(result)
    if r==1:
        s.success("Patient is daignosed with Parkinson's disease")
    else:
        s.success('Patient is Healthy')