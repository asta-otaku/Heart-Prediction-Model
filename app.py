import pickle
import streamlit as st
def main():
    model = load_model()
    #gender = {"male":1, "female":0}
    #query = {"yes":1, "no":0}
    
    st.title("Heart Failure Prediction :hospital:")
    st.header("An application designed to predict if a patient has a tendency of dying due to heart failure.")
    age = st.text_input("", key="age")
    st.write("Enter the patient's age")
    anaemia = st.text_input("", key="anaemia")
    st.write("Does the patient suffer from anaemia? (yes or no)")
    creatinine_ph = st.text_input("", key="creatinine phosphokinase")
    st.write("Enter the creatinine phosphokinase level")
    diabetes = st.text_input("", key="diabetic")
    st.write("Diabetic? (yes or no)")
    ejection_rate = st.text_input("", key="ejection rate")
    st.write("Enter the patient's ejection rate")
    hbp = st.text_input("", key= "high blood pressure")
    st.write("High blood pressure? (yes or no)")
    platelets = st.text_input("", key="platelets")
    st.write("Enter the patient's bloodplatelets")
    serum_creatinine = st.text_input("", key="serum creatinine")
    st.write("Enter serum creatinine level")
    serum_sodium = st.text_input("", key="serum sodium")
    st.write("Enter serum sodium level")
    sex = st.text_input("", key="sex")
    st.write("Gender? (male or female)")
    smoke = st.text_input("", key="smoke")
    st.write("Does the patient smoke? (yes or no)")
    time = st.text_input("", key="time")
    st.write("time")
    
    if st.button("predict"):
        try:
            if age: age = int(age)
            if anaemia:
                anaemia = 1 if anaemia == "yes" else 0
            if creatinine_ph: creatinine_ph = int(creatinine_ph)
            if diabetes:
                diabetes = 1 if diabetes == "yes" else 0
            if ejection_rate: ejection_rate = int(ejection_rate)
            if hbp:
                hbp = 1 if hbp == "yes" else 0
            if platelets: platelets = float(platelets)
            if serum_creatinine:
                serum_creatinine = 1 if serum_creatinine == "yes" else 0
            if serum_sodium:
                serum_sodium = 1 if serum_sodium == "yes" else 0
            if sex:
                sex = 1 if sex == "yes" else 0
            if smoke:
                smoke = 1 if smoke == "yes" else 0
            if time: time = float(time)
        except Exception as e:
            st.write(e)
            st.error("Ensure you give the correct inputs")
        else:
            pred = model.predict([
                [age,anaemia,creatinine_ph,diabetes,ejection_rate,hbp,platelets,serum_creatinine,
                 serum_sodium,sex,smoke,time]])
            if pred[0] ==1:
                st.success("High chance of dying of heart failure!!!")
            else:
                st.success("Patient is in good condition")
    
def load_model():
    with open("./model.pkl", "rb") as f:
        model = pickle.load(f)
    return model["classifier"]

if __name__ == "__main__":
    main()