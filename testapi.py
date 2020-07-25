import requests
#comment
url_session_init = "https://api-sandbox.onemoney.in/user/initsession"
Content_type = "application/json"
organisationId = "FIN0176"
client_id = "fp_test_9c84a33600449fa0c572dff3bae82b0ce337e2cc"
client_secret= "cbf4cb1a14be02885e0285d737bae683d4351be745cd5e19617ca6f584b4224035cbeeb2"
appIdentifier = "Consentmanage"

vua = "7016400304@onemoney"
header = {"Content_type":Content_type, 'organisationId' : organisationId,'client_id' : client_id, 'client_secret': client_secret,'appIdentifier' : appIdentifier}
body = {"vua" : vua}

request = requests.post('https://api-sandbox.onemoney.in/app/loginwithotp/send',data = body, headers=header)
apiresponse = request.json()

session_id = apiresponse['sessionId']

print(session_id)