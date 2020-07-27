from flask import Flask, request
import africastalking
import os
import requests 

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
    response = "CON Welcome to account aggregation services\n"
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
        response += "7. ગુજરતી\n" #gujrati
        response += "8. اردو\n" #urdu
        response += "9. ಕನ್ನಡ\n" #Kannada
        response += "10.ଓଡିଆ\n" #odia
        response += "11. മലയാളം\n" #malyalam
        response += "12. ਪੰਜਾਬੀ\n" #punjabi

    elif text =="1*1":

        #sub menu 1
        response = "CON You have selected English as your language\n"
        response += "To confirm press 1\n"
        

    elif text == "1*2*1":
        #sub menu 1
        response = "CON Select a service for Account Aggregation\n"
        response += "1. Login\n"
        response += "2. Register\n"

    elif text == "1*2*1*2":
        response = "CON Please enter your phone number\n"
    

    elif text == "1*2*1*2*8853056579":
        response = "CON Please enter the OTP\n"

    elif text == "1*2*1*2*8853056579*123456":
        response = "CON Please set a passcode\n"

    elif text == "1*2*1*2*8853056579*123456*123456":
        response = "CON Passcode set.\n"
        response += "CON Please login after some time.\n"

    elif text == "1*2*1*1":
        response = "CON Select your account aggregator platform:\n"
        response += "1. Onemoney\n"
        response += "2. Finvu\n"
        response += "3. Perfios\n"
        response += "2. Yodlee\n"
        
    elif text == "1*2*1*1*1":
        response = "CON Please enter your onemoney AA id (excluding @onemoney):\n"

    elif text == "1*2*1*1*1*8853056579":
        response = "CON Please enter your passcode\n"

    elif text == "1*2*1*1*1*8853056579*123456":
        response = "CON Logged in.\n"
        response += "Please select a service\n"
        response += "1. Consent management\n"
        response += "2. Account management\n"

    elif text == "1*2*1*1*1*8853056579*123456*1":
        response = "CON Please select the consent category \n"
        response += "1. Pending consent request\n"#pending request
        response += "2. Active consent request\n"#active consent
        
    elif text == "1*2*1*1*1*8853056579*123456*1*1":
        response = "CON Please select a consent artifact\n"
        response += "1. _FIUid_\n (_date_ - _date_)\n"
        response += "2. _FIUid_\n (_date_ - _date_)\n"

    elif text == "1*2*1*1*1*8853056579*123456*1*1*1":
        response = "CON FIU id: _FIUid_\n"
        response += "Period of data: (_date_ - _date_)\n"
        response += "Frequency: Once\n"
        response += "Data storage: View only\n"
        response += "Account: ACME-FIP-X9950"
        response += "To agree to the request, press 1.\n"
        response += "To deny the request, press 0.\n"
        

    elif text == "1*2*1*1*1*8853056579*123456*1*1*1*1":
        response = "CON Consent request accepted\n "
        response += "For more services, please dial in again."

    elif text == "1*2*1*1*1*8853056579*123456*1*1*1*0":
        response = "CON Consent request declined\n"
        response += "For more services, please dial in again."

        
        

    return response


if __name__=="__main__":
    app.run(host="0.0.0.0", port = os.environ.get("PORT"))
