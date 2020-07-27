from flask import Flask, request
import africastalking
import os
import requests 
url_login_sendotp= "https://api-sandbox.onemoney.in/app/loginwithotp/send"
Content_type = "application/json"
organisationId = "FIN0176"
client_id = "fp_test_9c84a33600449fa0c572dff3bae82b0ce337e2cc"
client_secret= "cbf4cb1a14be02885e0285d737bae683d4351be745cd5e19617ca6f584b4224035cbeeb2"
appIdentifier = "Consentmanage"
app = Flask(__name__)
username = "sandbox"
api_key = "0a94d47d47c2a97dedd2b973b40a5ce4291d27ca3587764443bd3b5fd6c960f3"
africastalking.initialize(username, api_key)
sms = africastalking.SMS


    


@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionID", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text","default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)
    response = "CON Welcome to account aggregation services by aryan \n"
    response += "Enter 1 to select desired language\n"

    #ussd_logic
    if text == "1":

        #main menu
        response = "CON Select a language\n"
        response += "1. हिन्दी \n" #hindi
        response += "2. English\n" #english
        response += "3. বাংলা \n" #bengali
        response += "4. मराठी\n" #marathi
        response += "5. తెలుగు\n" #telgu
        response += "6. தமிழ்\n" #tamil
        response += "7. પાસ\n" #gujrati
        response += "8. اردو\n" #urdu
        response += "9. ಕನ್ನಡ\n" #Kannada
        response += "10.ଓଡିଆ\n" #odia
        response += "11. മലയാളം\n" #malyalam
        response += "12. ਪੰਜਾਬੀ\n" #punjabi

    elif text =="1*1":

        #sub menu 1
        response = "CON आपने अपनी पसंद की भाषा के रूप में हिंदी को चुना है\n"
        response += "पुष्टि करने के लिए 1 दर्ज करें\n"
        

    elif text == "1*1*1":
        #sub menu 1
        response = "CON कृपया एक सेवा चुनें\n"
        response += "1. लॉग इन करें \n"
        response += "2. रजिस्टर करें\n"

    elif text == "1*1*1*2":
        response = "CON कृपया अपना फोन नंबर दर्ज करें\n"
    

    elif text == "1*1*1*2*8853056579":
        response = "CON कृपया ओटीपी दर्ज करें\n"

    elif text == "1*1*1*2*8853056579*369258":
        response = "CON पंजीकरण सफल, कृपया कुछ मिनटों में लॉगिन करें\n"

    elif text == "1*1*1*1":
        response = "CON अपना AA प्लेटफ़ॉर्म चुनें\n"
        response += "1. Onemoney"
        response += "2. Finvu"
        

    elif text == "1*1*1*1*1*1":
        response = "CON कृपया पासकोड दर्ज करें \n"
    elif text == "1*1*1*1*1*123456":
        response = "CON सफलतापूर्ण प्रवेश \n"
        response += "कृपया एक सेवा चुनें \n"
        response += "1. सहमति प्रबंधन\n"
        response += "2. खाता प्रबंधन\n"

    elif text == "1*1*1*1*1*123456*1":
        response = "CON Session initialised.\n Press 1 to continue \n"
        
       
    elif text == "1*1*1*1*1*123456*1*1":
        response = "CON Select consent request category:\n"
        response += "1. Pending"
        response += "2. Active (under development)"
        response += "3. Paused (under development)"
        response += "4. Inactive (under development)"
        response += "5. Rejected (under development)"

    elif text == "1*1*1*1*1*123456*1*1*1":
        response = "CON Pending consent requests:\n"
        url_dashboard = "https://api-sandbox.onemoney.in/app/dashboard"
        Content_Type = "application/json"
        PARAMS = {'Content_Type':Content_Type, 'sessionId':aa_session_id}

        request = requests.get(url = url_dashboard, params = PARAMS)
        request_json = request.json()
        print("Status code:", response.status_code)
        

    elif text == "1*1*1*1*1*123456*2":
        response = "CON आपने खाता प्रबंधन चुना है \n "
        response += "पुष्टि करने के लिए 1 दर्ज करें \n"

    elif text == "1*1*1*1*1*123456*2*1":
        response = "CON खाते की खोज शुरू हो गई है। कृपया कुछ समय बाद सेवा में वापस आएं\n"             
        
        

    return response


if __name__=="__main__":
    app.run(host="0.0.0.0", port = os.environ.get("PORT"))
