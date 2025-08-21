
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "fabrics.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS fabrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            color TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            image_base64 TEXT NOT NULL
        )
        '''
    )
    conn.commit()
    conn.close()

app = Flask(__name__)
CORS(app)

@app.route("/fabrics", methods=["GET"])
def get_fabrics():
    conn = get_db()
    rows = conn.execute("SELECT id, name, color, quantity, image_base64 FROM fabrics ORDER BY id DESC").fetchall()
    conn.close()
    data = [
        {"id": r["id"], "name": r["name"], "color": r["color"], "quantity": r["quantity"], "image": r["image_base64"]}
        for r in rows
    ]
    return jsonify(data), 200

@app.route("/fabrics", methods=["POST"])
def add_fabric():
    data = request.get_json(force=True)
    name = (data.get("name") or "").strip()
    color = (data.get("color") or "").strip()
    quantity = int(data.get("quantity") or 0)
    image = data.get("image") or ""

    if not name or not color or not image or quantity <= 0:
        return jsonify({"message": "بيانات ناقصة"}), 400

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO fabrics (name, color, quantity, image_base64) VALUES (?, ?, ?, ?)",
        (name, color, quantity, image),
    )
    conn.commit()
    new_id = cur.lastrowid
    conn.close()

    return jsonify({"message": "تمت إضافة القماش", "fabric": {"id": new_id, "name": name, "color": color, "quantity": quantity, "image": image}}), 201

@app.route("/fabrics/<int:fabric_id>", methods=["DELETE"])
def delete_fabric(fabric_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM fabrics WHERE id = ?", (fabric_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "تم حذف القماش"}), 200

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
