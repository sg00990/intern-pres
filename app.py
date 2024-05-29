import streamlit as st

st.set_page_config(page_title='Intro to Streamlit', page_icon='random')

def home_page():
    st.subheader('What is Streamlit?')
    st.markdown('- A free and open-source Python framework')
    st.markdown('- Quickly build and share web apps')
    st.markdown('- No need to learn CSS, JavaScript, or HTML')
    st.markdown('- Can deploy app instantly from GitHub')
    st.markdown('- Used mostly for machine learning and data science')

def community_apps():
    st.subheader('My Favorite Apps from Streamlit Community Cloud')
    col1, col2 = st.columns([.5, 2])
    col1.write('#')
    col1.write('#')
    col1.write('#')
    col1.write('#')
    col1.write('#')
    col1.link_button('**Prettymapp**', url='https://prettymapp.streamlit.app/')
    col2.markdown("""
        <iframe
        src="https://prettymapp.streamlit.app/?embed=true"
        style="height: 450px; width: 100%;"
        ></iframe>
        """, unsafe_allow_html=True)
    col3, col4 = st.columns([2, .5])
    col4.write('#')
    col4.write('#')
    col4.write('#')
    col4.write('#')
    col4.write('#')
    col4.link_button('**Generate Tweets**', url='https://tweets.streamlit.app/')
    col3.markdown("""
        <iframe
        src="https://tweets.streamlit.app/?embed=true"
        style="height: 450px; width: 100%;"
        ></iframe>
        """, unsafe_allow_html=True)
    col5, col6 = st.columns([.5, 2])
    col5.write('#')
    col5.write('#')
    col5.write('#')
    col5.write('#')
    col5.write('#')
    col5.link_button('**CatGDP**', url='https://catgdp.streamlit.app/')
    col6.markdown("""
        <iframe
        src="https://catgdp.streamlit.app/?embed=true"
        style="height: 450px; width: 100%;"
        ></iframe>
        """, unsafe_allow_html=True)
    
def my_apps():
    st.subheader('**My Streamlit Apps**')
    st.markdown('1. [UNIFI](https://unifi-aba-app-service.azurewebsites.net/) - The megalodon of Streamlit apps 🦈')
    st.markdown('2. [DataViz TIG KPI Challenge](https://switch-games-kpi.streamlit.app/)')
    st.markdown('3. [My 2024 Bookshelf](https://my-2024-bookshelf.streamlit.app/)')
    st.markdown('4. [Intern Blog](https://internblog-8zqvnhap6d8gnsbxhbh6wz.streamlit.app/)')

def resources():
    st.subheader('Learning Resources')
    st.write('**Resources from Snowflake/Streamlit**')
    st.write('- [Snowflake Hands-On Essentials (Data Applications)](https://learn.snowflake.com/en/pages/hands-on-essentials-track/): This is great if you want to know more about Streamlit, REST API and SnowSQL')
    st.write('- [Streamlit Documentation](https://docs.streamlit.io/): I use this every day! It is an extremely helpful reference')
    st.write('- [Streamlit Forum](https://discuss.streamlit.io/): This forum is similar to Stack Overflow')
    st.write('- [Streamlit Roadmap](https://roadmap.streamlit.app/): This is where Streamlit lists past updates and future releases')
    st.write('**Resources from Streamlit Community Cloud**')
    st.write('- [Streamlit Cheat Sheet](https://cheat-sheet.streamlit.app/): Summary of the documentation')
    st.write('- [30 Days of Streamlit](https://30days.streamlit.app/): This app provides a breakdown of creating your first Streamlt app through daily challenges')
    st.write('- [Streamlit Component Hub](https://components.streamlit.app/): This app lists all Streamlit components that have been created')
    st.write('- [Streamlit Extras](https://extras.streamlit.app/): streamlit-extras is an additional Python library you can download that provides some other useful components')


def main():
    choice = st.selectbox('label', options=["What is Streamlit?", "Streamlit Community Cloud", "My Apps", "Resources"], label_visibility="collapsed", index=None)

    col1, col2 = st.columns([2, .5])

    col1.title('Introduction to Streamlit')
    col2.write('######')
    col2.image('img/logo.png', width=100)


    if choice == "What is Streamlit?":
        home_page()
    elif choice == "Streamlit Community Cloud":
        community_apps()
    elif choice == "My Apps":
        my_apps()
    elif choice == "Resources":
        resources()
    else:
        st.write(':gray[Please select an option above to display information]')      



if __name__ == "__main__":
    main()