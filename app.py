from multiprocessing import Process

from dotenv import load_dotenv
from flask import Flask, send_from_directory
from flask_cors import CORS

from backend.server import backend_app

load_dotenv()
CORS(backend_app)

def run_backend():
    backend_app.run(host='0.0.0.0', port=8000)

if __name__ == '__main__':
    backend_process = Process(target=run_backend)
    backend_process.start()

    backend_process.join()
