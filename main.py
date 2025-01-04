# Importing 
import streamlit as st
import pandas as pd
from csv import QUOTE_ALL

# Eol options definition
EOLS = {
    "LF": "\n",
    "CRLF": "\r\n"
}

# Intitalizing session state for the application buttons
if st.session_state.get("show_preview") is None:
    st.session_state["show_preview"] = False

if st.session_state.get("show_conversion") is None:
    st.session_state["show_conversion"] = False

# App title
st.title("Formatter for .csv files")

# File uploads
uploaded_file = st.file_uploader("Upload a .csv file", type=["csv"])

# File validation and reading
if uploaded_file is not None:
    try:

        # Reading options
        # Delimiter options to be used in the file reading
        delimiter = st.selectbox(
            "File delimiter", [",", ";", "|"], index=0 # Preselects comma (",") as default
        )
        
        # Encoding options to be used in the file reading
        encoding = st.selectbox(
            "File encoding", ["utf-8", "windows-1251", "windows-1252"], index=0 # Preselects utf-8 as default
        )

        # Providing the reading possibility 
        if st.button(label = "Read the given file"):
            st.session_state["show_preview"] = True # Altering "show_preview" to be fixed after interation

        # Validation of read and preview state
        if st.session_state["show_preview"]:

            # Reading the given file with the given parameters and saving it into a pandas DataFrame (df)
            df = pd.read_csv(uploaded_file, encoding=encoding, sep=delimiter)
            st.success("The uploaded file was read with succes!")

            # Displays the first rows of the read file (DataFrame)
            st.write("Preview of the uploaded file data:")
            st.dataframe(df.head(5))

            # Providing options for file formatting
            if st.button(label = "Convert the read file", ):
                st.session_state["show_conversion"] = True # Altering "show_conversion" to be fixed after interation
            
            # Validation of conversion state
            if st.session_state["show_conversion"]:
                
                st.subheader("Converting and saving a the data into a new file")

                # Conversion options
                
                # Delimiter options to be used in the conversion
                new_delimiter = st.selectbox(
                    "Chosse a new delimiter", [",", ";", "|"], index=0 # Preselects comma (",") as default
                )
                
                # Encoding options to be used in the conversion
                new_encoding = st.selectbox(
                    "Choose a new encoding", ["utf-8", "windows-1251", "windows-1252"], index=0 # Preselects utf-8 as default
                )
                
                # EoL options to be used in the conversion
                new_eol = st.selectbox(
                    "Choose a new line terminator",options = list(EOLS.keys())
                )

                # Chose lineterminator backend value retrieval
                chosen_eol = EOLS[new_eol]

                # Provinding the download possibility
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