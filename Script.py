  from google.oauth2 import service_account
    from apiclient.discovery import build
    
    # TODO: read in the credentials from a JSON file, converyt to dict and assign to 'credentials_dict'
    
    try:
        credentials = service_account.Credentials.from_service_account_info(credentials_dict)
    except Exception as e:
         print(e) 
         return   
    # Get list of reviews using googleapiclient.discovery
    try:      
        service = googleapiclient.discovery.build('androidpublisher', 'v3', credentials=credentials)
        response = service.reviews().list(packageName='uk.organisation.appname.production').execute()
    except Exception as e:
         print(e) 
         return
  
    if not 'reviews' in response or len(response['reviews']) == 0:
        print('No reviews available')
    else:
        print('Reviews detected.')
        # Save or process the response, e.g. save the json.dumps(response) to a JSON file
    save_reviews(all_review_data, define_csv_file_name())
