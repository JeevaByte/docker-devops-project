from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

# Database connection details from environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "mydatabase")
DB_USER = os.getenv("DB_USER", "myuser")
DB_PASS = os.getenv("DB_PASS", "mypassword")

# Redis connection details from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/health")
def health():
    return "OK", 200

@app.route("/health/db")
def health_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        conn.close()
        return "Database is running!", 200
    except Exception as e:
        return f"Database connection failed: {e}", 500

@app.route("/health/cache")
def health_cache():
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        r.ping()
        return "Cache is running!", 200
    except Exception as e:
        return f"Cache connection failed: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)