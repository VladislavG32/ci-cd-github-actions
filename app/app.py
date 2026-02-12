import os
from flask import Flask, jsonify
import psycopg2
import redis

app = Flask(__name__)

def check_postgres():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "postgres"),
        port=int(os.getenv("POSTGRES_PORT", "5432")),
        dbname=os.getenv("POSTGRES_DB", "appdb"),
        user=os.getenv("POSTGRES_USER", "appuser"),
        password=os.getenv("POSTGRES_PASSWORD", "apppassword"),
    )
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    cur.fetchone()
    cur.close()
    conn.close()
    return True

def check_redis():
    r = redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=int(os.getenv("REDIS_PORT", "6379")),
        socket_connect_timeout=2,
        socket_timeout=2,
    )
    return r.ping() is True

@app.get("/")
def root():
    return "Hello from CI/CD demo app!\n"

@app.get("/live")
def live():
    return jsonify({"status": "alive"}), 200

@app.get("/ready")
def ready():
    try:
        check_postgres()
        check_redis()
        return jsonify({"status": "ready"}), 200
    except Exception as e:
        return jsonify({"status": "not_ready", "error": type(e).__name__}), 503

@app.get("/health")
def health():
    status = {"app": "ok", "postgres": "ok", "redis": "ok"}
    try:
        check_postgres()
    except Exception as e:
        status["postgres"] = f"fail: {type(e).__name__}"
    try:
        check_redis()
    except Exception as e:
        status["redis"] = f"fail: {type(e).__name__}"
    ok = all(v == "ok" for v in status.values())
    return jsonify(status), (200 if ok else 503)

if __name__ == "__main__":
    app.run(host=os.getenv("HOST", "0.0.0.0"), port=int(os.getenv("PORT", "8000")))
