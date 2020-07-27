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
        response += "7. বাংলা\n" #Bengali
        response += "8. اردو\n" #urdu
        response += "9. ಕನ್ನಡ\n" #Kannada
        response += "10.ଓଡିଆ\n" #odia
        response += "11. മലയാളം\n" #malyalam
        response += "12. ਪੰਜਾਬੀ\n" #punjabi

    elif text =="1*3":

        #sub menu 1
        response = "CON તમે ગુજરાતી ભાષાને તમારી ભાષા તરીકે પસંદ કરી છે\n"
        response += "પુષ્ટિ કરવા માટે દબાવો 1\n"
        

    elif text == "1*3*1":
        #sub menu 1
        response = "CON એકાઉન્ટ એકત્રીકરણ માટે કોઈ સેવા પસંદ કરો\n"
        response += "1. પ્રવેશ કરો\n"
        response += "2. નોંધણી\n"

    elif text == "1*3*1*2":
        response = "CON કૃપા કરીને તમારો ફોન નંબર દાખલ કરો\n"
    

    elif text == "1*3*1*2*8853056579":
        response = "CON કૃપા કરીને ઓટીપી દાખલ કરો\n"

    elif text == "1*3*1*2*8853056579*123456":
        response = "CON કૃપા કરીને પાસકોડ સેટ કરો\n"

    elif text == "1*3*1*2*8853056579*123456*123456":
        response = "CON પાસકોડ સેટ.\n"
        response += "CON કૃપા કરીને થોડા સમય પછી લગિન કરો.\n"

    elif text == "1*3*1*1":
        response = "CON તમારું એકાઉન્ટ એગ્રીગેટર પ્લેટફોર્મ પસંદ કરો:\n"
        response += "1. Onemoney\n"
        response += "2. Finvu\n"
        response += "3. Perfios\n"
        response += "2. Yodlee\n"
        
    elif text == "1*3*1*1*1":
        response = "CON કૃપા કરી તમારી એકમાની એએ ID દાખલ કરો(બાકાત @onemoney):\n"

    elif text == "1*3*1*1*1*8853056579":
        response = "CON કૃપા કરીને તમારો પાસકોડ દાખલ કરો\n"

    elif text == "1*3*1*1*1*8853056579*123456":
        response = "CON Logged in.\n"
        response += "કૃપા કરી કોઈ સેવા પસંદ કરો\n"
        response += "1. સંમતિ સંચાલન\n"
        response += "2. હિસાબી વય્વસ્થા\n"

    elif text == "1*3*1*1*1*8853056579*123456*1":
        response = "CON કૃપા કરીને સંમતિ કેટેગરી પસંદ કરો\n"
        response += "1. બાકી સંમતિ વિનંતી\n"#pending request
        response += "2. સક્રિય સંમતિ વિનંતી\n"#active consent
        
    elif text == "1*3*1*1*1*8853056579*123456*1*1":
        response = "CON કૃપા કરીને સંમતિ આર્ટિફેક્ટ પસંદ કરો\n"
        response += "1. _FIUid_\n (_date_ - _date_)\n"
        response += "2. _FIUid_\n (_date_ - _date_)\n"

    elif text == "1*3*1*1*1*8853056579*123456*1*1*1":
        response = "CON FIU id: _FIUid_\n"
        response += "ડેટાની અવધિ: (_date_ - _date_)\n"
        response += "આવર્તન: એકવાર\n"
        response += "માહિતી સંગ્રાહક: ફક્ત જોવાયોગ્ય\n"
        response += "ખાતું: ACME-FIP-X9950"
        response += "વિનંતી સાથે સંમત થવા માટે, 1 દબાવો.\n"
        response += "વિનંતીને નકારવા માટે, 0 દબાવો.\n"
        

    elif text == "1*3*1*1*1*8853056579*123456*1*1*1*1":
        response = "CON સંમતિ વિનંતી સ્વીકારી\n "
        response += "વધુ સેવાઓ માટે, કૃપા કરીને ફરીથી ડાયલ કરો."

    elif text == "1*3*1*1*1*8853056579*123456*1*1*1*0":
        response = "CON સંમતિ વિનંતી નકારી\n"
        response += "વધુ સેવાઓ માટે, કૃપા કરીને ફરીથી ડાયલ કરો."

    return response


if __name__=="__main__":
    app.run(host="0.0.0.0", port = os.environ.get("PORT"))
