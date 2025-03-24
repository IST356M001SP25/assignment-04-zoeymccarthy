'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

#build a fiter on the dataframe based on a text column 
#and one of the values in the column

#dataframe with column / row filters applied

#statistics for the numerical columns

st.title("UniBrow")
st.caption("The Universal data browser")

#file uploader
file = st.file_uploader("Upload a file:")
if file is not None:
    ext = pl.get_file_extension(file.name)
    df = pl.load_file(file.name, ext)
    #column selector
    colSelector = st.multiselect("Select which columns to display: ", pl.get_column_names(df), default = columns)
    if st.toggle("Filter data"):
        stcols = st.columns(3)
        text_cols = pl.get_columns_of_type(df, 'object')
        filter_col = stcols[0].selectbox("Select column to filter", text_cols)
        if filter_col:
            vals = pl.get_unique_values(df, filter_col)
            val = stcols[1].selectbox("Select value to filter on", vals)
            df_show = df[df[filter_col] == val][selected_cols]
    else:
        df_show = df[selected_cols]
    
    st.dataframe(df_show)
    st.dataframe(df_show.describe())

