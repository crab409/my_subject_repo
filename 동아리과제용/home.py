import streamlit 
import myfunction

id_in = input("아이디를 입력해주세요 : ")
password_in = input("비밀번호를 입력해줘요 : ")
myfunction.is_user(id_in, password_in)