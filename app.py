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
        response = "CON Select your account aggregator platform:\n"
        response += "1. Onemoney\n"
        response += "2. Finvu\n"
        response += "3. Perfios\n"
        response += "2. Yodlee\n"
        
    elif text == "1*1*1*1*1":
        response = "CON Please enter your onemoney AA id (excluding @onemoney):\n"

    elif text == "1*1*1*1*1*8853056579":
        response = "CON कृपया पासकोड दर्ज करें \n"

    elif text == "1*1*1*1*1*8853056579*123456":
        response = "CON सफलतापूर्ण प्रवेश \n"
        response += "कृपया एक सेवा चुनें \n"
        response += "1. सहमति प्रबंधन\n"
        response += "2. खाता प्रबंधन\n"

    elif text == "1*1*1*1*1*8853056579*123456*1":
        response = "CON कृपया एक क्रिया चुनें \n"
        response += "1. लंबित सहमति का अनुरोध"#pending request
        response += "2. सक्रिय सहमति सेवाएँ"#active consent
        
    elif text == "1*1*1*1*1*8853056579*123456*1*1":
        response = "CON एक सहमति अनुरोध चुनें\n"
        response += "1. _FIUid_\n (_date_ - _date_)\n"
        response += "2. _FIUid_\n (_date_ - _date_)\n"

    elif text == "1*1*1*1*1*8853056579*123456*1*1*1":
        response = "CON कंपनी: _FIUid_\n"
        resposne += "Period of data: (_date_ - _date_)\n"
        response += "Frequency: Once\n"
        response += "Data storage: View only\n"
        response += "Account: ACME-FIP-X9950"
        response += "अनुमोदन करने के लिए 1 दबाएँ और इनकार करने के लिए 0 दबाएँ\n"
        

    elif text == "1*1*1*1*1*8853056579*123456*1*1*1*1":
        response = "CON सहमति अनुरोध स्वीकृत \n "
        response += "अन्य सेवाओं के लिए कृपया कुछ समय बाद फिर से वापस आएं END "

    elif text == "1*1*1*1*1*8853056579*123456*1*1*1*2":
        response = "CON सहमति अनुरोध अस्वीकार कर दिया\n"
        response += "अन्य सेवाओं के लिए कृपया कुछ समय बाद फिर से वापस आएं END "

        
        

    return response


if __name__=="__main__":
    app.run(host="0.0.0.0", port = os.environ.get("PORT"))
