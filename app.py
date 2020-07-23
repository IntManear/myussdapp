from flask import Flask, request
import africastalking
import os

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
    response = "CON Welcome to account aggregation services Pandey and Dhruv\n"
    response += "Enter 1 to select desired language"

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
        response = "CON कृपया अपना ए.ए. आईडी या फोन नंबर दर्ज करें\n"
    elif text == "1*1*1*1*987654":
        response = "CON कृपया पासकोड दर्ज करें \n"
    elif text == "1*1*1*1*987654*123456":
        response = "CON सफलतापूर्ण प्रवेश \n"
        response += "कृपया एक सेवा चुनें \n";
        response += "1. सहमति प्रबंधन\n";
        response += "2. खाता प्रबंधन\n";
    elif text == "1*1*1*1*987654*123456*1":
       response = "CON आपके पास कोई सहमति अनुरोध नहीं है \n"

    elif text == "1*1*1*1*987654*123456*2":
       response = "CON आपने खाता प्रबंधन चुना है \n "
       response += "पुष्टि करने के लिए 1 दर्ज करें \n"
       
    elif text == "1*1*1*1*987654*123456*2*1":
     response = "CON खाते की खोज शुरू हो गई है। कृपया कुछ समय बाद सेवा में वापस आएं\n "             
        
        

    return response


if __name__=="__main__":
    app.run(host="0.0.0.0", port = os.environ.get("PORT"))
