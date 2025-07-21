# Importing 
import streamlit as st
import pandas as pd
from csv import QUOTE_ALL

# Eol options
EOLS = {
    "LF": "\n",
    "CRLF": "\r\n"
}

# initializing session state for the application buttons
if st.session_state.get("show_preview") is None:
    st.session_state["show_preview"] = False

if st.session_state.get("show_conversion") is None:
    st.session_state["show_conversion"] = False

st.title("Formatter for .csv files")

uploaded_file = st.file_uploader("Upload a .csv file", type=["csv"])

# file validation and reading
if uploaded_file is not None:
    try:

        # delimiter options to be used in the file reading
        delimiter = st.selectbox(
            "File delimiter", [",", ";", "|"], index=0 # preselects comma (",") as default
        )
        
        # encoding options to be used in the file reading
        encoding = st.selectbox(
            "File encoding", ["utf-8", "cp1251", "cp1252"], index=0 # preselects utf-8 as default
        )

        if st.button(label = "Read the given file"):
            st.session_state["show_preview"] = True

        # validation of read and preview state
        if st.session_state["show_preview"]:

            df = pd.read_csv(uploaded_file, encoding=encoding, sep=delimiter)
            st.success("The uploaded file was read with succes!")
            st.write("Preview of the uploaded file data:")
            st.dataframe(df.head(5))

            # providing options for file formatting
            if st.button(label = "Convert the read file", ):
                st.session_state["show_conversion"] = True
            
            # validation of conversion state
            if st.session_state["show_conversion"]:
                
                st.subheader("Converting and saving a the data into a new file")

                # conversion options
                new_delimiter = st.selectbox(
                    "Chosse a new delimiter", [",", ";", "|"], index=0 # preselects comma (",") as default
                )
                
                new_encoding = st.selectbox(
                    "Choose a new encoding", ["utf-8", "cp1251", "cp1252"], index=0 # preselects utf-8 as default
                )
                
                new_eol = st.selectbox(
                    "Choose a new line terminator",options = list(EOLS.keys())
                )

                chosen_eol = EOLS[new_eol]

                st.download_button(
                    label = "Donwload converted file",
                    data = df.to_csv(encoding=new_encoding, sep=new_delimiter, lineterminator=chosen_eol, quoting=QUOTE_ALL, index=False),
                    file_name = "converted.csv",
                    mime="text/csv"
                )

        else:
            st.error("To be able to convert the file the button: **Read the given file** needs to be pressed!")

    except Exception as error:
        st.error(f'An error occured!\n Error: {error}')
else:
    st.info("To be able to convert a file, a file needs to be uploaded in the first place!")