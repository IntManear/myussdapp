import requests
def initsession(vua):
    vua = vua+"@onemoney"
    body = '{"vua": vua}'
    url_initsesssion = "https://api-sandbox.onemoney.in/user/initsession"
    Content_Type = "application/json"
    header = {'Content-Type':'application/json','organisationId':'FIN0176','client_id':'fp_test_9c84a33600449fa0c572dff3bae82b0ce337e2cc','client_secret':'cbf4cb1a14be02885e0285d737bae683d4351be745cd5e19617ca6f584b4224035cbeeb2','appIdentifier':'Consentmanager'}
    request = requests.post(url = url_initsesssion,data = body, headers = header)
    request_json = request.json()
    apisession_id=request_json["sessionId"]
    return apisession_id

def user_dashboard(apisession_id):
    url_dashboard = "https://api-sandbox.onemoney.in/app/dashboard"
    Content_Type = "application/json"
    header = {'Content_Type':'application/json','sessionId':apisession_id}
    request = requests.get(url = url_dashboard, headers = header)
    request_json = request.json()
    return request_json

def initsession_reg(uname,uphno,tc):
    url_reg = "https://api-sandbox.onemoney.in/user/signupwithsdk"
    Content_Type = "application/json"
    header = {'Content-Type':'application/json','organisationId':'FIN0176','client_id':'fp_test_9c84a33600449fa0c572dff3bae82b0ce337e2cc','client_secret':'cbf4cb1a14be02885e0285d737bae683d4351be745cd5e19617ca6f584b4224035cbeeb2','appIdentifier':'Consentmanager'}
    body ='{"name":uname ,"phone_number": uphno ,"terms_and_conditions": tc }'
    request = request.post (url = url_reg, headers= header, data = body)
    request_json = request.json()
    username =request_json["username"]
    return username



