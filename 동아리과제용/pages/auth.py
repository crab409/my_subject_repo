import streamlit as st

# 사용자 정보를 저장할 딕셔너리 (학생 이름과 비밀번호)
user_info = {
    'student1': 'pass1',
    'student2': 'pass2',
    'student3': 'pass3',
    '이승민': '1234'
}

# 세션 상태 초기화
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# 인증 페이지
st.title("사용자 인증")

student_name = st.text_input("학생 이름을 입력하세요")
password = st.text_input("비밀번호를 입력하세요", type='password')

if st.button("로그인"):
    if student_name in user_info and password == user_info[student_name]:
        st.session_state.authenticated = True
        st.session_state.student_name = student_name
        st.success(f"{student_name}님, 인증에 성공했습니다!")
    else:
        st.session_state.authenticated = False
        st.error("학생 이름 또는 비밀번호가 잘못되었습니다.")