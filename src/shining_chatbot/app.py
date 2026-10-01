import streamlit as st

st.set_page_config(
    page_title="챗봇",
    page_icon="😂",
    layout="wide"
)

# 페이지만 만들고 -> 깃허브에 올려봅시다 
# 10분 정도 드릴테니 

st.title("😂 나의 첫 번째 챗봇")
st.write("Streamlit으로 만든 챗봇 페이지입니다.")
st.write("업데이트가 될까요?")

# 입력창과 응답 화면 테스트
user_input = st.chat_input("메시지를 입력하세요.")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        st.write(f"입력한 메시지: {user_input}")