from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store: a list of cars, each car is a dict {plate, model, year}
cars = [
    {"plate": "AA-12-34", "model": "Toyota Corolla", "year": 2010},
    {"plate": "BB-56-78", "model": "Honda Civic", "year": 2015},
]

# GET /cars - list all cars
@app.route("/cars", methods=["GET"])
def list_cars():
    return jsonify(cars), 200

# POST /cars - add a new car
@app.route("/cars", methods=["POST"])
def add_car():
    data = request.get_json()
    if not data or "plate" not in data or "model" not in data or "year" not in data:
        return jsonify({"error": "Invalid data"}), 400
    # Check if plate already exists
    for c in cars:
        if c["plate"] == data["plate"]:
            return jsonify({"error": "Car with this plate already exists"}), 409
    
    cars.append({
        "plate": data["plate"],
        "model": data["model"],
        "year": data["year"]
    })
    return jsonify({"message": "Car added"}), 201

# PUT /cars/<plate> - update car info
@app.route("/cars/<plate>", methods=["PUT"])
def update_car(plate):
    data = request.get_json()
    for c in cars:
        if c["plate"] == plate:
            c["model"] = data.get("model", c["model"])
            c["year"] = data.get("year", c["year"])
            return jsonify({"message": "Car updated"}), 200
    return jsonify({"error": "Car not found"}), 404

# DELETE /cars/<plate> - remove a car
@app.route("/cars/<plate>", methods=["DELETE"])
def delete_car(plate):
    for i, c in enumerate(cars):
        if c["plate"] == plate:
            cars.pop(i)
            return jsonify({"message": "Car deleted"}), 200
    return jsonify({"error": "Car not found"}), 404


if __name__ == "__main__":
    # Running the app in a more "production" style
    app.run(host="0.0.0.0", port=5000, debug=False)
