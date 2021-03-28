from flask import Flask, jsonify, request
from Data import final_list_Dwarf
from Data import final_list_Star
from Data import final_list

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({
        "data": final_list,
        "message": "success"
    }), 200


@app.route("/Dwarf")
def Dwarf():
    name = request.args.get("name")
    planet_data = next(
        item for item in final_list_Dwarf if item["Brown_Dwarf_Name"] == name)
    return jsonify({
        "data": planet_data,
        "message": "success"
    }), 200


@app.route("/Star")
def Star():
    name = request.args.get("name")
    planet_data = next(
        item for item in final_list_Star if item["Star_name"] == name)
    return jsonify({
        "data": planet_data,
        "message": "success"
    }), 200


if __name__ == "__main__":
    app.run()
