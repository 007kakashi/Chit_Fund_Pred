import pandas as pd
import numpy as np
import streamlit as st
#import pickle as pk
import joblib as jb
from xgboost import Booster 
from xgboost import DMatrix
from sklearn.preprocessing import LabelEncoder

#import pickle

model = Booster(model_file='LoanPredictor.bin')
# model=jb.load('LoanPredictor.pkl')

data=pd.read_csv('Loan_Req.csv')
#data.columns

st.title('Welcome To the Laxmi Chit Funds')

def none(var):
    if var==0.0:
       var=None
    return var

u_income=st.number_input('Enter Applicant Salary')
u_income=none(u_income)
    
co_income=st.number_input('Enter Co-Applicant Income')
co_income=none(co_income)

l_amount=st.number_input('Loan Amount')
l_amount=none(l_amount)

duration=st.number_input('Duration of Loan')
duration=none(duration)

c_history=st.selectbox('Credit History',['None','No','Yes'])

if c_history=='None':
   c_history=None
elif c_history=='No':
   c_history=0
else:
   c_history=1
        

  
#def n():
     
df={'ApplicantIncome':u_income,'CoapplicantIncome':co_income,' LoanAmount':l_amount,' Loan_Amount_Term':duration,' Credit_History':c_history}
    
df1=pd.DataFrame(df,index=[1])
#le=LabelEncoder()
#df1['Credit History']=le.fit_transform(df1['Credit History'])
# df1
    
# df3=DMatrix(data=df1.values)
  
# model.predict(df1)


if st.button('Check Eligibilty of Loan'):
    
    if  df1.isnull().values.any():
        st.error('Fill The Required Field')
    else:  
        df3=DMatrix(data=df1.values)
        pred=model.predict(df3)
        if pred>=0.5:
            st.success('Congrtulation You Are Eligible For Scheme Which Gives you\n 21 din main paisa double')
            # pred
        else:
            st.error('Sorry, But You Are Not Eligible For Loan')
            # pred
       
        
    
    

    
   
    
   
    
    
    

   
        



 #print('Congrtulation You Are Eligible For Loan ')
#else :
#    print('Sorry, But You Are Not Eligible For Loan')
    
  #  out<=0.5