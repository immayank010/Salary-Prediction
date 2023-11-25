import streamlit as st
from PIL import Image

def show_explore_page1():
    st.title("Explore Software Engineer Salaries")

    st.write(
        """
    ### Stack Overflow Developer Survey 2022
    """
    )

    image = Image.open('plot1.jpg')
    st.image(image, caption='Number of Data from different Countries', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.title("""#### Number of Data from different countries""")

    st.write(
        """#### Mean Salary Based On Country
    """
    )
    image = Image.open('line.jpg')
    st.image(image, caption='Salary vs Country', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.write(
        """
    #### Mean Salary Based On Experience
    """
    )

    image = Image.open('bar.jpg')
    st.image(image, caption='Salary vs Experience', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


