from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample student data
students = [
    {"id": 1, "name": "John Doe", "total_marks": 85},
    {"id": 2, "name": "Jane Smith", "total_marks": 92},
    {"id": 3, "name": "David Johnson", "total_marks": 78},
    # Add more student data...
]

@app.route('/students', methods=['GET'])
def get_students():
    # Pagination parameters
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))

    # Calculate start and end indices for pagination
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    # Get paginated student data
    paginated_students = students[start_index:end_index]

    return jsonify(paginated_students)

@app.route('/students/filter', methods=['POST'])
def filter_students():
    # Get filter criteria from request body
    filters = request.json

    filtered_students = []

    # Apply filters to student data
    for student in students:
        if matches_filters(student, filters):
            filtered_students.append(student)

    return jsonify(filtered_students)

def matches_filters(student, filters):
    # Apply filter criteria to student data
    for key, value in filters.items():
        if key not in student or student[key] != value:
            return False
    return True

if __name__ == '__main__':
    app.run()
