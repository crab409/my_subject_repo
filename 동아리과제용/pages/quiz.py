import streamlit as st

# 세션 상태 초기화
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'score' not in st.session_state:
    st.session_state.score = 0

# 문제 풀기 페이지
if st.session_state.authenticated:
    st.title("객관식 문제")
    
    question_1 = st.radio("1. Streamlit은 어떤 언어로 작성되었나요?", 
                          ("Python", "Java", "C++", "JavaScript"))
    question_2 = st.radio("2. Streamlit에서 페이지를 나누는 데 사용되는 함수는?", 
                          ("st.page()", "st.sidebar()", "st.selectbox()", "st.write()"))
    question_3 = st.radio("3. Streamlit의 슬라이더 컴포넌트는?", 
                          ("st.slider()", "st.range()", "st.scrollbar()", "st.progress()"))
    question_4 = st.radio("4. Streamlit 앱을 실행하는 명령어는?", 
                          ("streamlit start", "streamlit run", "streamlit execute", "streamlit launch"))
    question_5 = st.radio("5. Streamlit의 캐싱 함수는?", 
                          ("st.cache()", "st.memo()", "st.save()", "st.remember()"))
    
    if st.button("제출"):
        score = 0
        if question_1 == "Python":
            score += 1
        if question_2 == "st.sidebar()":
            score += 1
        if question_3 == "st.slider()":
            score += 1
        if question_4 == "streamlit run":
            score += 1
        if question_5 == "st.cache()":
            score += 1
        st.session_state.score = score
        st.success("문제를 제출했습니다.")
else:
    st.warning("먼저 인증을 완료해주세요.")