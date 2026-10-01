import streamlit as st
from langchain.chat_models import init_chat_model

st.set_page_config(
    page_title="챗봇",
    page_icon="😂",
    layout="wide"
)
@st.cache_resource
def get_model():
    return init_chat_model("openai:gpt-6-luna", 
                           reasoning_effort="none",
                           api_key=st.secrets["OPENAI_API_KEY"])

model = get_model()

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
        with st.spinner("답변을 생성하고 있습니다."):
            response = model.invoke(user_input)
        st.write(f"입력한 메시지: {response.content}")