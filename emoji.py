import demoji
import streamlit as st 

st.title("Emoji reader ")
st.caption("Developed by SOUMENDU DAS")
st.write("You input an emoji, and this application tells you what kind of emoji it is")
emoji=st.text_area("input emoji ")
if(st.button('Get')):
    ans=demoji.findall(emoji)
    st.success(ans)