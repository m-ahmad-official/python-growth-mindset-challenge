# Imports
import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up our App
st.set_page_config(page_icon="📀", page_title="Data Sweeper", layout="wide")

# Sidebar configuration
with st.sidebar:
    st.header("🎮 Data Sweeper Controls")
    st.write("Configure your data processing options here")
    st.markdown("---")

# Main content
st.markdown(
    "<h1 style='text-align: center;'>Growth Mindset Challenge 🚀</h1>",
    unsafe_allow_html=True,
)
st.markdown("---")
st.header("📀 Data Sweeper")
st.write(
    "Transform your files between CSV and Excel formats with built-in data cleaning and visualization!"
)

# File uploader in sidebar
with st.sidebar:
    uploaded_files = st.file_uploader(
        "📂 Upload your files (CSV or Excel):",
        type=["csv", "xlsx"],
        accept_multiple_files=True,
    )

# Process uploaded files
if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read file based on extension
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"❌ Unsupported file type: {file_ext}")
            continue

        # Display info about the file
        st.write(f"📋 **File Name:** {file.name}")
        st.write(f"💾 **File Size:** {round(file.size/1024, 2)} KB")

        # Show 5 rows of our df
        st.write("Preview the head of the Dataframe")
        st.dataframe(df.head())

        # Options for data cleaning
        st.subheader("🛠️ Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicate from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicate Removed!")

            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing Values have been Filled!")

            # Choose Specific Columns to Keep or Convert
            st.subheader("🎯 Select Columns")
            columns = st.multiselect(
                f"Choose Columns for {file.name}",
                df.columns,
                default=list(df.columns),
                key=f"cols_{file.name}",
            )
            df = df[columns]

            # Create Some Visualizations
            st.subheader("📊 Data Visualization")
            if st.checkbox(
                f"Show Visualization for {file.name}", key=f"viz_{file.name}"
            ):
                num_cols = df.select_dtypes(include='number').columns
                if len(num_cols) >= 2:
                    st.bar_chart(df[num_cols[:2]])
                elif len(num_cols) == 1:
                    st.bar_chart(df[num_cols[0]])
                else:
                    st.warning("⚠️ No numeric columns available for visualization")

            # Convert the File -> CSV to Excel
            st.subheader("🔄 Conversion Options")
            conversion_type = st.radio(
                f"Convert {file.name} to:", ["CSV", "Excel"], key=f"conv_{file.name}"
            )
            if st.button(f"🔄 Convert {file.name}", key=f"convert_{file.name}"):
                buffer = BytesIO()
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".csv")
                    mime_type = "text/csv"
                else:  # Excel
                    df.to_excel(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                buffer.seek(0)

                # Download Button
                st.download_button(
                    label=f"⬇️ Download {file.name} as {conversion_type}",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type,
                )

    st.success("All Files Processed! 🎉")
else:
    st.info("ℹ️ Please upload files using the sidebar to begin processing.")
