from urllib import response
import streamlit as st
import boto3

st.title('Face recogonising using AWS')
img_file=st.file_uploader('upload face image',type=['png','jpg','jpeg'])
if img_file is not None:
    # file_details={}
    # file_details['name']=img_file.name
    # file_details['type']=img_file.type
    # file_details['size']=img_file.size
    # st.write(file_details)

    with open('download(1).jpg','wb') as f:
        f.write(img_file.getbuffer())
    
    client=boto3.client('rekognition')
    imageSource=open('download(1).jpg','rb')
    
    response=client.recognize_celebrities(
        
        Image={'Bytes':imageSource.read()}
       )
    
    if (len(response['CelebrityFaces'])>0):
        st.write(response)
        st.success('It is a celebrity image')
    else:
        st.error('It is not a celebrity image')