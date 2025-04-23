from flask import Flask, request

app = Flask(__name__)

@app.route('/onvif/device_service', methods=['POST'])
def endpoint():
    data =request.data.decode('utf-8', errors='ignore')
    print(f"[ONVIF] Request recieved: ")
    print(data[:300])
    with open("/logs/onvif.log", "a") as f:
        f.write(data + "\n+\n")
    respose = """<?xml version="1.0"?>
<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope">
    <s:Body>
        <tds:GetServicesResponse xmlns:tds="http://www.onvif.org/ver10/device/wsdl">
            <tds:Service>
                <tds:Namespace>http://www.onvif.org/ver10/media/wsdl</tds:Namespace>
                <tds:XAddr>http://172.19.17.46/onvif/media_service</tds:XAddr>
            </tds:Service>
        </tds:GetServicesResponse>
    </s:Body>
</s:Envelope>"""
    return respose, 200, {'Content-Type': 'application/soap+xml'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)