# import re

# def check_password_strength(password):
#     score = 0
    
#     # Length Check
#     if len(password) >= 8:
#         score += 1
#     else:
#         print("❌ Password should be at least 8 characters long.")
    
#     # Upper & Lowercase Check
#     if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
#         score += 1
#     else:
#         print("❌ Include both uppercase and lowercase letters.")
    
#     # Digit Check
#     if re.search(r"\d", password):
#         score += 1
#     else:
#         print("❌ Add at least one number (0-9).")
    
#     # Special Character Check
#     if re.search(r"[!@#$%^&*]", password):
#         score += 1
#     else:
#         print("❌ Include at least one special character (!@#$%^&*).")
    
#     # Strength Rating
#     if score == 4:
#         print("✅ Strong Password!")
#     elif score == 3:
#         print("⚠️ Moderate Password - Consider adding more security features.")
#     else:
#         print("❌ Weak Password - Improve it using the suggestions above.")

# # Get user input
# password = input("Enter your password: ")
# check_password_strength(password)
























# import re
# import random
# import string
# import streamlit as st

# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits + "!@#$%^&*"
#     return "".join(random.choice(characters) for _ in range(length))

# def check_password_strength(password, weights={'length': 1, 'case': 1, 'digit': 1, 'special': 1}):
#     score = 0
#     common_passwords = {"password123", "123456", "qwerty", "letmein", "admin"}
    
#     if password in common_passwords:
#         return "❌ Weak Password - Commonly used password detected."
    
#     if len(password) >= 8:
#         score += weights['length']
#     if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
#         score += weights['case']
#     if re.search(r"\d", password):
#         score += weights['digit']
#     if re.search(r"[!@#$%^&*]", password):
#         score += weights['special']
    
#     if score >= sum(weights.values()):
#         return "✅ Strong Password!"
#     elif score >= sum(weights.values()) / 2:
#         return "⚠️ Moderate Password - Consider improving it."
#     else:
#         return "❌ Weak Password - Improve it using suggestions."

# def main():
#     st.title("Password Strength Checker & Generator")
    
#     password = st.text_input("Enter a password to check strength:", type="password")
#     if st.button("Check Strength") and password:
#         result = check_password_strength(password)
#         st.write(result)
    
#     if st.button("Generate Strong Password"):
#         strong_password = generate_password()
#         st.write(f"Generated Password: `{strong_password}`")

# if __name__ == "__main__":
#     main()
























# import re
# import streamlit as st

# def check_password_strength(password):
#     score = 0
#     messages = []

#     if len(password) >= 8:
#         score += 1
#     else:
#         messages.append("❌ Password should be at least 8 characters long.")

#     if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
#         score += 1
#     else:
#         messages.append("❌ Include both uppercase and lowercase letters.")

#     if re.search(r"\d", password):
#         score += 1
#     else:
#         messages.append("❌ Add at least one number (0-9).")

#     if re.search(r"[!@#$%^&*]", password):
#         score += 1
#     else:
#         messages.append("❌ Include at least one special character (!@#$%^&*).")

#     if messages:
#         for msg in messages:
#             st.write(msg)

#     if score == 4:
#         st.success("✅ Strong Password!")
#     elif score == 3:
#         st.warning("⚠️ Moderate Password - Consider adding more security features.")
#     else:
#         st.error("❌ Weak Password - Improve it using the suggestions above.")

# def main():
#     st.title("🔒 Password Strength Checker")
    
#     password = st.text_input("Enter your password:", type="password")
    
#     if st.button("Check Strength"):
#         if password:
#             check_password_strength(password)
#         else:
#             st.warning("⚠️ Please enter a password!")

# if __name__ == "__main__":
#     main()






























import re
import streamlit as st

def set_theme(theme):
    if theme == "Dark":
        st.markdown(
            """
            <style>
            body, .stApp { background-color: #0e1117; color: white; }
            .stTextInput input, .stButton button { background-color: #1e1e1e; color: white; border: 1px solid white; }
            .stAlert { background-color: #333; color: white; }
            .theme-toggle { background-color: #1e1e1e; color: white; padding: 10px 20px; border-radius: 10px; transition: 0.3s; }
            .theme-toggle:hover { background-color: #444; }
            /* Fix for hidden deploy button and three-dot menu */
            header { background-color: #0e1117 !important; }
            .viewerBadge_container__1QSob, .stDeployButton { display: block !important; }
            </style>
            """, 
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
            body, .stApp { background-color: white; color: black; }
            .stTextInput input, .stButton button { background-color: white; color: black; border: 1px solid black; }
            .stAlert { background-color: #f0f0f0; color: black; }
            .theme-toggle { background-color: #ddd; color: black; padding: 10px 20px; border-radius: 10px; transition: 0.3s; }
            .theme-toggle:hover { background-color: #bbb; }
            /* Fix for hidden deploy button and three-dot menu */
            header { background-color: white !important; }
            .viewerBadge_container__1QSob, .stDeployButton { display: block !important; }
            </style>
            """, 
            unsafe_allow_html=True
        )

# Custom scoring weights
weights = {'length': 2, 'case': 1, 'digit': 1, 'special': 2}

def check_password_strength(password):
    score = 0
    messages = []

    if len(password) >= 8:
        score += weights['length']
    else:
        messages.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += weights['case']
    else:
        messages.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += weights['digit']
    else:
        messages.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += weights['special']
    else:
        messages.append("❌ Include at least one special character (!@#$%^&*).")

    if messages:
        for msg in messages:
            st.write(msg)

    total_weight = sum(weights.values())

    if score >= total_weight:
        st.success("✅ Strong Password!")
    elif score >= total_weight / 2:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions above.")

def main():
    st.set_page_config(page_title="Password Strength Checker", layout="centered")
    
    if "theme" not in st.session_state:
        st.session_state["theme"] = "Light"
    
    if st.button("🌙 Toggle Theme", key="theme-toggle", help="Switch between Light and Dark mode"):
        st.session_state["theme"] = "Dark" if st.session_state["theme"] == "Light" else "Light"
    
    set_theme(st.session_state["theme"])
    
    st.title("🔒 Password Strength Checker")
    
    password = st.text_input("Enter your password:", type="password")
    
    if st.button("Check Strength"):
        if password:
            check_password_strength(password)
        else:
            st.warning("⚠️ Please enter a password!")

if __name__ == "__main__":
    main()
