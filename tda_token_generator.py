from tda import auth

# Redirect uri from your TD Ameritrade Developer account
redirect_uri = 'https://localhost'

# Don't need to change token_path file name.
token_path = 'TDA_Auth_Token.json'

# Get consumer_key from user input
print("**************************************************************")
print("Token generator tda-api")
print("Link to get consumer key or register a new application: https://developer.tdameritrade.com")
consumer_key = input("Enter consumer_key: ")
redirect_uri = 'https://localhost'

# Don't change anything below
api_key = consumer_key + '@AMER.OAUTHAP'

# Validating existing token file or generate a new token file
try:
    print("Validating current token file")
    td_session = auth.client_from_token_file(
        token_path,
        api_key
    )
    print("Token file is still valid")
    print("Exiting program")

except:
    td_session = auth.client_from_manual_flow(
            api_key,
            redirect_uri,
            token_path
        )