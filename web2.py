#import sns as sns
import streamlit as st
import pandas as pd
import pickle
import numpy as np
import joblib
import seaborn as sns

model = joblib.load('./train_models/GNB9.sav')
#"click_id", "user_id", "store_id", "device_label_class", "platform_label_class" , "channel_label_class" ,"num_click_store"
def predict_click_store(click_id, user_id,  store_id,  device_label_class,  platform_label_class,channel_label_class ,num_click_store):
    features_name = [[click_id ,user_id,  store_id,  device_label_class,  platform_label_class,channel_label_class,num_click_store]]
    features_df = pd.DataFrame(features_name, columns= ['click_id', 'user_id', 'store_id' , 'device_label_class' ,'platform_label_class','channel_label_class','num_click_store'])
    y_pred=model.predict(features_df)
    merchant_id = store_id
    #print(features_df)
    return int(y_pred),int(merchant_id)
def main():
    # Side bar
    st.sidebar.title('Shopback ')
    st.sidebar.markdown('Next merchant Prediction :  ')
    df_2020 = pd.read_csv("./data_select_features/new_dataset_features2.csv")

    st.write('--------------------------------------------------------------File Uploader-----------------------------------------------------------------------')
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # store_id,new_device,new_platform,num_click_store
    st.write('-------------------------------------------------------------- Text Input ------------------------------------------------------------------------')
    click_id = st.text_input("click_id:")
    user_id = st.text_input("user_id:")
    store_id = st.text_input("store_id:")
    device_label_class = st.text_input("device_label_class:")
    platform_label_class = st.text_input("platform_label_class:")
    channel_label_class = st.text_input("channel_label_class :")
    num_click_store = st.text_input("num_click_store :")

    st.write('------------------------------------------------------------ Select Model Type -----------------------------------------------------------------')
    option = st.selectbox(
        'Select your model',
        ('decision tree', 'logistic regression', 'SVM', 'GNB'))
    st.write('You selected:', option)


    if st.checkbox("Get next prediction"):
        if st.button("Predict now"):
                output, id = predict_click_store(click_id, user_id,  store_id,  device_label_class,  platform_label_class,channel_label_class,num_click_store)
                print(output)
                if output == 1:
                    print(" prediction_value : ", output)
                    st.write('You prediction_value :', output)
                    st.markdown("From the **GNB** model,\nThis store is predicted to be a ** click ** :")
                elif output == 0:
                    print(" prediction_value : ", output)
                    st.write('You prediction_value :', output)
                    st.markdown("From the **KNN** model,\nThis store is predicted to be a **non-click**")

    st.write('------------------------------------------ Data Visualization : DataFrame----------------------------------------------------------------------')

    if st.button('Show Dataframe'):
        st.subheader('Data Frame')
        st.dataframe(df_2020.head())
        # st.line_chart(tracks_df)

    st.write('------------------------------------------ Data Visualization : Data Discovery-----------------------------------------------------------------')

    df_2020 = pd.read_csv("./data_select_features/new_dataset_features2.csv")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Visualise how balance our dataset is
    sns.countplot(x="click_label", data= df_2020, palette="muted")
    st.pyplot()



if __name__=="__main__":
    main()