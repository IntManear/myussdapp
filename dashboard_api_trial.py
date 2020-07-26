import requests

url_dashboard = "https://api-sandbox.onemoney.in/app/dashboard"
Content_Type = "application/json"
PARAMS = {'Content_Type':'application/json','sessionId':"95029fc002b5b6ef87fe211844be2a26:d27398aa97a585699dadc3a9b8edf7c09af38a260a128943c61ea230167b81476cf186fac6e1ec7e2788420b3f621e54ddedd7e4f5068e9119b5f936b7e244ab"}
request = requests.get(url = url_dashboard, params = PARAMS)
request_json = request.text
print(request_json)
#print("Status code:", request.status_code)