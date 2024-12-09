from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/calculate', methods=['POST'])
def calculate_gpa():
    data = request.get_json()
    courses = data.get('courses', [])
    total_credits = sum(course['credit'] for course in courses)
    total_points = sum(course['credit'] * course['grade'] for course in courses)
    gpa = total_points / total_credits if total_credits else 0
    return jsonify({'gpa': round(gpa, 2)})

if __name__ == '__main__':
    app.run(debug=True)
