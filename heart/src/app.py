import streamlit as st
from streamlit import config
import data
import home
import heart

def write_page(page):  # pylint: disable=redefined-outer-name
    #if page == dash:
    #    return page.dash_write(name='MSFT', start='2019-06-03', stop='2021-06-03')
    return page.write()
PAGES={
    "Data Analysis" : data,
    "I want to predict my state!!" : heart
    }
    # , 'CryptoCurrency':crypto}

def main():
    choice=st.sidebar.radio("Drop to see what we offer",tuple(PAGES.keys()))


    if choice ==None:
        write_page(home) 
    else:
        page=PAGES[choice]
        write_page(page)


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()