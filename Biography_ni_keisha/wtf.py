import streamlit as st
import datetime 

st.set_page_config(page_title="keisha's Biography", page_icon="🤡", layout="wide")

if 'toggle_state' not in st.session_state:
    st.session_state.toggle_state = False

# Define a function to toggle the state
def Drawing_button():
    st.session_state.toggle_state = not st.session_state.toggle_state
    
import streamlit as st



# Display the name dynamically
st.markdown(
    f"""
    <div style="text-align: center; font-size: 40px;">
        <strong>😲 Keisha's Biography 😲</strong>  
    </div>
    """,
    unsafe_allow_html=True,
)

    
with st.container(): 
     st.write("---") 
     left_column, right_column = st.columns(2) 
     
     with left_column: #left column
        

        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>Get to know me</strong>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("I hope this biography will help you know this person more")

        
        st.text_input("My Name", "Keisha Terece D. Gibertas")
        
        st.write("---") 
        
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>What I do</strong>
            </div>
        """, unsafe_allow_html=True)
         
        
        
        st.text_area("","""-Watching movies
-Dancing routine
-Sleep
-Study
-Household chores""", height=125 )
        st.write("---")
        
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>My ahievements</strong>
                </di
            
        """, unsafe_allow_html=True)
        st.text_area("discription", """I've been in a lot of competitions and activities that molded me to what I am now. I've always known what I am passionate about and that's mostly dancing. Dancing  has given me opportunities that I never knew that it could give me different type of happiness. It makes me feel alive in stage and can understand the flow of music in my ears. Beside dancing, I also compete in academic activities such as writing, patimpalak, quizzes, and many more school competitions. I once stopped everything, being the competent woman I am. But everything has it ways to go back and move forward.
           """, height = 330)
        

        
        st.write("   ")
        st.write("   ")
        if st.button("click here to see all my achievents "):
            Drawing_button()
        
        if st.session_state.toggle_state == True:
            st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>My dancing carrier</strong>
            </div>
            """, unsafe_allow_html=True)
            st.write("---")
            inner_col1, inner_col2 = st.columns(2)
            with inner_col1:
                st.image('1.jpg', width=150)
                st.image('5.jpg', width=150)
            
                st.image('3.jpg', width=150)
                

            with inner_col2:
                st.image('2.jpg', width=150)
                st.image('4.jpg', width=150)
                st.image('6.jpg', width=150)
                
            st.write("---")   
            
            
            
        st.write("---")  
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>Social Media Accounts</strong>
            </div>
        """, unsafe_allow_html=True)
        st.write("[Facebook](https://www.facebook.com/profile.php?id=100090975026071)")
        st.write("[Instagram](https://www.instagram.com/mjay.cabahug/?igsh=NWVnMmNiOWg3MTBx&fbclid=IwY2xjawGv2dVleHRuA2FlbQIxMAABHRyufPcsJO5y5NMdKJqTXz9K82xrwQKedo1uJnRQbz94zBAZQPNv_r1UtQ_aem_wZg6nnp58nuCFK6NA74R7Q)")         
            
            
            
     with right_column: #right column
        st.markdown("""
            <div style="text-align: center; font-size: 25px;">
               <strong>ABOUT ME</strong>
            </div>
        """, unsafe_allow_html=True)
        
        st.text_area("", """Hi, I'm Keisha Terece D. Gibertas, and I'm passionate about dancing and in my academic. I believe that I can survive every obstacle that comes my way, that everything has a hard path while going on a journey. Everything happens for a reason, and I am glad I have everyone that I can be with through this beautiful but harsh life.

Professionally, I am a student in Surigao Del Norte State University, and I’m always looking for ways to achieve what I always wanted in life. My skills include hardwork and dedication to fullfil what I've been longing for.

In my free time, I enjoy listening to music, dancing, watching movies and many more that I can think that will help me cope with stress. I also believe in being positive even if everything goes hard, that I really can do it no matter what.

I’m always open to connect with others, explore new opportunities, learning, etc. Feel free to reach out if you'd like to chat about life interests.""", height = 330)
        
      
        
        st.radio("Gender", ["Male", "Female"])
        st.subheader("Family Background")  
        mother = st.text_input("Mother's name", "Ma. Elena G. Ensomo")
        mbday = st.date_input("Mother's Birthday", datetime.date(1970, 1, 7))
        father = st.text_input("Father's Name", "Marlon L. Cabahug")
        mbday = st.date_input("Mother's Birthday", datetime.date(1969, 6, 30)) 
        st.subheader("Educational Attainment")

        hs = st.text_input("High School", "Surigao City National Highschool")
        shs = st.text_input("Senior High School", "Surigao del Norte National highschool")
        college = st.text_input("College", "Surigao del Norte State University")
        st.write("---")