import os   
import streamlit as st 
app_name="Streamlit-GCP-Cloud-Run"

PAGE_CONFIG ={"page_title":app_name,"layout":"wide"}
st.set_page_config(**PAGE_CONFIG) 

def main():
    st.header('Check Environment Variables')
    st.write(f'{os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")=}')
    st.write(f'{os.environ.get("SECRET_KEY")=}')
    st.write(f'{os.environ.get("PROJECT_ID")=}')
    st.write(f'{os.environ.get("GOOGLE_CLOUD_PROJECT")=}')
    
    try:
        with open("/.config/gcloud/application_default_credentials.json") as f:
                st.write(f.read())
    except:
        pass
    
    st.header('Check /.config/gcloud/application_default_credentials.json')
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    try:
        credentials = service_account.Credentials.from_service_account_file(
        '/.config/gcloud/application_default_credentials.json'
        )

        service = build('gmail', 'v1', credentials=credentials)

        st.write(f'{service=}')
    except:
        pass

    st.header('Check Application Default Credential via google.auth')
    try:
        import google.auth
        credentials, project_id = google.auth.default()
        st.code('credentials, project_id = google.auth.default()')
        st.text(f'{credentials=} \n{project_id=}')
        st.caption('credentials.__dict__')
        st.text(f'{credentials.__dict__}')
    except:
        pass

    from google.cloud import datacatalog_v1
    
    client = datacatalog_v1.DataCatalogClient(credentials=credentials)

    st.code('client = datacatalog_v1.DataCatalogClient(credentials=credentials)')
    st.write(f'{client=}')

    dc_scope = datacatalog_v1.SearchCatalogRequest.Scope()
    dc_scope.include_project_ids.append('ocb-data-gov-poc')
    
    search_term = 'customer'

    query_en="".join(
        [
            f"displayname:'{search_term}'", 
            f", type={'business_glossary'}",  # system=data_catalog tag:hierarchy
        ]
    )

    results_en = client.search_catalog(
        scope=dc_scope,
        query=query_en,
    )

    st.code(
'''query_en="".join(
    [
        f"displayname:'{search_term}'", 
        f", type={'business_glossary'}",  # system=data_catalog tag:hierarchy
    ]
)
    
results_en = (
    client.search_catalog(scope=dc_scope,query=query_en)
        ._response
        .results[0]
)
''')
    st.write(results_en._response.results[0])

if __name__=="__main__":
    main()


