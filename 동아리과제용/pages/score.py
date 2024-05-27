import streamlit as st

# 세션 상태 초기화
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'score' not in st.session_state:
    st.session_state.score = 0

# 점수 확인 페이지
if st.session_state.authenticated:
    st.title("점수 확인")
    if st.session_state.score > 0:
        st.write(f"{st.session_state.student_name}님의 점수는 {st.session_state.score}점 입니다.")
    else:
        st.warning("먼저 문제를 풀어주세요.")
else:
    st.warning("먼저 인증을 완료해주세요.")