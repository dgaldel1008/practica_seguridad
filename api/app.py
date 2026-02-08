from flask import Flask, jsonify
import redis
import time

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def slow_process():
    time.sleep(2)

    cached_result = r.get('my_data')
    if cached_result:
        return jsonify({"message": "Cache hit", "data": cached_result.decode('utf-8')})

    result = "Resultado generado en: " + time.ctime()

    r.set('my_data', result, ex=60)

    return jsonify({"message": "Cache miss", "data": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
