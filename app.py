import streamlit as st
st.title("🏦 Bank Management System")
from hello import Bank
user = Bank()

menu = ["Create Account", "Deposit", "Withdraw", "Show Details", "Update Details", "Delete Account"]
choice = st.sidebar.selectbox("Choose Action", menu)

if choice == "Create Account":
    st.header("Create New Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=10, max_value=100)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")
    if st.button("Create Account"):
        if pin.isdigit() and len(pin) == 4:
            acc = user.Createaccount(name, age, email, int(pin))
            if acc:
                st.success("✅ Account created successfully!")
                st.write(acc)
            else:
                st.error("❌ Age must be 18+ and PIN must be 4 digits.")
        else:
            st.error("❌ Invalid PIN")


elif choice == "Deposit":
    st.header("Deposit Money")
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1, max_value=10000)
    if st.button("Deposit"):
        res = user.depositmoney(acc, int(pin), amount)
        if res:
            st.success("✅ Amount deposited successfully")
            st.write(res)
        else:
            st.error("❌ Invalid account or amount")
            

elif choice == "Withdraw":
    st.header("Withdraw Money")
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)
    if st.button("Withdraw"):
        res = user.withdrawmoney(acc, int(pin), amount)
        if res:
            st.success("✅ Amount withdrawn successfully")
            st.write(res)
        else:
            st.error("❌ Insufficient balance or wrong credentials")

elif choice == "Show Details":
    st.header("Account Details")
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    if st.button("Show"):
        res = user.showdetail(acc, int(pin))
        if res:
            st.json(res)
        else:
            st.error("❌ No account found")

elif choice == "Update Details":
    st.header("Update Account Details")
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    newname = st.text_input("New Name")
    # newemailwedrfg
            

elif choice == "Delete Account":
    st.header("Delete Account")
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    if st.button("Delete"):
        res = user.Delete(acc, int(pin))
        if res:
            st.success("✅ Account deleted successfully")
        else:
            st.error("❌ No account found")