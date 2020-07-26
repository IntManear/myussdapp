import requests

url_initiate_session = "https://api-sandbox.onemoney.in/user/initsession"
Content_Type = "application/json"
organisationId = "FIN0176"
client_id = "fp_test_9c84a33600449fa0c572dff3bae82b0ce337e2cc"
client_secret = "cbf4cb1a14be02885e0285d737bae683d4351be745cd5e19617ca6f584b4224035cbeeb2"
appIdentifier = "Consentmanager"
header = {"Content-Type":Content_Type,"organisationId":organisationId, "client_id":client_id, "client_secret":client_secret, "appIdentifier":appIdentifier}
body = '{"vua":"7016400304@onemoney"}'

response = requests.post(url_initiate_session, data = body, headers = header)
response_json = response.json()
print("Status code:", response.status_code)
aa_session_id =  response_json['sessionId']
print(aa_session_id)