import streamlit as st
from PIL import Image
import pickle
import numpy as np

model = pickle.load(open('../Model/ML_Model_Bigmart_Sales.pkl', 'rb'))

def run():
    img1 = Image.open('bank.png')
    img1 = img1.resize((156,145))
    st.image(img1,use_column_width=False)
    st.title("Bigmart Sales Prediction using ML Regression Model")

    ## 1) Item_Fat_Content
    fat_display = ('Low Fat','Regular')
    fat_options = list(range(len(fat_display)))
    fat = st.selectbox("Item_Fat_Content",fat_options, format_func=lambda x: fat_display[x])

    ## 2) Item_Type
    itype_display = ('Breakfast','Breads', 'Dairy', 'Fruits and Vegetables', 'Household' 'snack Foods', 'Soft Drinks')
    itype_options = list(range(len(itype_display)))
    itype = st.selectbox("Item_Type",itype_options, format_func=lambda x: itype_display[x])

    ## 3) Outlet_Identifier
    outlet_display = ('OUT017','OUT019', 'OUT35', 'OUT45', 'OUT49')
    outlet_options = list(range(len(outlet_display)))
    outlet = st.selectbox("Outlet_Identifier",outlet_options, format_func=lambda x: outlet_display[x])

    ## 4) Outlet_Size
    osize_display = ('Medium','Small')
    osize_options = list(range(len(osize_display)))
    osize = st.selectbox("Outlet_Size",osize_options, format_func=lambda x: osize_display[x])

    ## 5) Outlet_Location_Type
    oloc_display = ('Tier 1','Tier 2', 'Tier 3')
    oloc_options = list(range(len(oloc_display)))
    oloc = st.selectbox("Outlet_Location_Type",oloc_options, format_func=lambda x: oloc_display[x])

    ## 6) Outlet_Type
    otype_display = ('Supermarket_Type1','Supermarket_Type2')
    otype_options = list(range(len(otype_display)))
    otype = st.selectbox("Outlet_Type",otype_options, format_func=lambda x: otype_display[x])


    ## 7) Item_Weightlit 
    Item_Weight = st.number_input("Enter Item_Weight:",value=0.0)    
    
    ## 8) Item_Visibility
    Item_Visibility = st.number_input(" Enter Item_Visibility:" ,value=0.0)  

    ## 9) Item_MRP
    Item_MRP = st.number_input(" Enter Item_MRP:" ,value=0.0)  

    ## 10) Outlet_Establishment_Year
    Outlet_Establishment_Year = st.number_input("Enter any year (1999, 2002, 2004, 2007, 2009)",value=0)  

    
    if st.button("Submit"):
        
        features = [[fat, itype, outlet, osize, oloc, otype, Item_Weight, Item_Visibility, Item_MRP, Outlet_Establishment_Year]]
        print(features)
        
        bigmart_sales = model.predict(features)
        st.subheader('PREDICTED BIGMART SALES ARE :')
        st.subheader('Rupees'+':-'+str(np.round(bigmart_sales[0], 2)))

run()