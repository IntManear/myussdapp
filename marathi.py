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
        response += "3. ગુજરાતી \n" #Gujrati
        response += "4. मराठी\n" #marathi
        response += "5. తెలుగు\n" #telgu
        response += "6. தமிழ்\n" #tamil
        response += "7. বাংলা\n" #bengali
        response += "8. اردو\n" #urdu
        response += "9. ಕನ್ನಡ\n" #Kannada
        response += "10.ଓଡିଆ\n" #odia
        response += "11. മലയാളം\n" #malyalam
        response += "12. ਪੰਜਾਬੀ\n" #punjabi

    elif text =="1*4":

        #sub menu 1
        response = "CON आपण आपली भाषा मराठी निवडली आहे\n"
        response += "पुष्टी करण्यासाठी 1 दाबा\n"
        

    elif text == "1*4*1":
        #sub menu 1
        response = "CON खाते एकत्रिकरणासाठी सेवा निवडा\n"
        response += "1. लॉगिन\n"
        response += "2. नोंदणी करा\n"

    elif text == "1*4*1*2":
        response = "CON कृपया आपला फोन नंबर प्रविष्ट करा\n"
    

    elif text == "1*4*1*2*8853056579":
        response = "CON कृपया ओटीपी प्रविष्ट करा\n"

    elif text == "1*4*1*2*8853056579*123456":
        response = "CON कृपया पासकोड सेट करा\n"

    elif text == "1*4*1*2*8853056579*123456*123456":
        response = "CON पासकोड सेट.\n"
        response += "CON कृपया काही काळानंतर लॉगिन करा.\n"

    elif text == "1*4*1*1":
        response = "CON आपले खाते एकत्रित प्लॅटफॉर्म निवडा:\n"
        response += "1. Onemoney\n"
        response += "2. Finvu\n"
        response += "3. Perfios\n"
        response += "4. Yodlee\n"
        
    elif text == "1*4*1*1*1":
        response = "CON कृपया आपला एकमुनी एए आयडी प्रविष्ट करा( वगळता @onemoney):\n"

    elif text == "1*4*1*1*1*8853056579":
        response = "CON कृपया आपला पासकोड प्रविष्ट करा\n"

    elif text == "1*4*1*1*1*8853056579*123456":
        response = "CON लॉग इन\n"
        response += "कृपया एक सेवा निवडा\n"
        response += "1. संमती व्यवस्थापन\n"
        response += "2. खाते व्यवस्थापन\n"

    elif text == "1*4*1*1*1*8853056579*123456*1":
        response = "CON कृपया संमती श्रेणी निवडा \n"
        response += "1. प्रलंबित संमती विनंती\n"#pending request
        response += "2. सक्रिय संमती विनंती\n"#active consent
        
    elif text == "1*4*1*1*1*8853056579*123456*1*1":
        response = "CON कृपया एक संमती कृत्रिम वस्तू निवडा\n"
        response += "1. _FIUid_\n (_date_ - _date_)\n"
        response += "2. _FIUid_\n (_date_ - _date_)\n"

    elif text == "1*4*1*1*1*8853056579*123456*1*1*1":
        response = "CON एफआययू आयडी: _FIUid_\n"
        response += "डेटा कालावधी: (_date_ - _date_)\n"
        response += "वारंवारता: एकदा\n"
        response += "डेटा संचयन: केवळ पहा\n"
        response += "खाते: ACME-FIP-X9950"
        response += "विनंतीस सहमती देण्यासाठी 1 दाबा.\n"
        response += "विनंती नाकारण्यासाठी 0 दाबा.\n"
        

    elif text == "1*4*1*1*1*8853056579*123456*1*1*1*1":
        response = "CON संमती विनंती स्वीकारली\n "
        response += "अधिक सेवांसाठी कृपया पुन्हा डायल करा."

    elif text == "1*4*1*1*1*8853056579*123456*1*1*1*0":
        response = "CON संमती विनंती नाकारली\n"
        response += "अधिक सेवांसाठी कृपया पुन्हा डायल करा."

        
        

    return response


if __name__=="__main__":
    app.run(host="0.0.0.0", port = os.environ.get("PORT"))
