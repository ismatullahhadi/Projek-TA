import streamlit as st
import pickle



lin_model=pickle.load(open('lin_model.pkl','rb'))
log_model=pickle.load(open('log_model.pkl','rb'))
svm=pickle.load(open('svm.pkl','rb'))

def classify(num):
    if num<0.5:
        return 'Setosa'
    elif num <1.5:
        return 'Versicolor'
    else:
        return 'Sangat Buruk'
def main():
    st.title("Website")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Air Pollution Classification</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    activities=['Linear Regression','Logistic Regression','SVM']
    option=st.sidebar.selectbox('Pilih model yang akan digunakan?',activities)
    st.subheader(option)
    sl=st.slider('Select PM10', 0.0, 10.0)
    sw=st.slider('Select so2', 0.0, 10.0)
    pl=st.slider('Select CO', 0.0, 10.0)
    pw=st.slider('Select O3', 0.0, 10.0)
    pw=st.slider('Select NO2', 0.0, 10.0)
    inputs=[[sl,sw,pl,pw]]
    if st.button('Classify'):
        if option=='Linear Regression':
            st.success(classify(lin_model.predict(inputs)))
        elif option=='Logistic Regression':
            st.success(classify(log_model.predict(inputs)))
        else:
           st.success(classify(svm.predict(inputs)))


if __name__=='__main__':
    main()
