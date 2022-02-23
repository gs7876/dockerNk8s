from flask import Flask, request, render_template, jsonify
import socket
from datetime import datetime
from ifdp.logs.logger import Logger

app = Flask(__name__)

logger = Logger.get_logger('sample api')


@app.route('/getDetail', methods=['POST', 'GET'])
def getDetail():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    now = datetime.now()
    current_date_time = now.strftime("%d/%m/%Y - %H:%M:%S")
    api_version = "api/V3"

    api_response = [
        {
         'host_name': host_name
         },
        {
         'ip_address': ip_address
         },
        {
         'current_date_time': current_date_time
         },
        {
         'api_version': api_version,
         }
    ]

    logger.info(
        f'hostname={host_name} ip_address={ip_address}, current_date_time={current_date_time} api_version={api_version}')

    return jsonify({'api_response': api_response})


@app.route('/health/full', methods=['POST', 'GET'])
def health():
    health_check = "Health Check OK"

    logger.info(
        f'/health/full=OK')

    return render_template("health.html", health_check=health_check)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090, debug=True)
