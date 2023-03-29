import os   
import streamlit as st 
app_name="Streamlit-GCP-Cloud-Run"

PAGE_CONFIG ={"page_title":app_name,"layout":"wide"}
st.set_page_config(**PAGE_CONFIG) 

def main():
    st.write(f'{os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")=}')
    st.write(f'{os.environ.get("SECRET_KEY")=}')
    st.write(f'{os.environ.get("PROJECT_ID")=}')
    st.write(f'{os.environ.get("GOOGLE_CLOUD_PROJECT")=}')
    
    try:
        with open("$HOME/.config/gcloud/application_default_credentials.json") as f:
                st.write(f.read())
    except:
        pass
    
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    try:
        credentials = service_account.Credentials.from_service_account_file(
        '$HOME/.config/gcloud/application_default_credentials.json'
        )

        service = build('gmail', 'v1', credentials=credentials)

        st.write(f'{service=}')
    except:
        pass

if __name__=="__main__":
    main()


