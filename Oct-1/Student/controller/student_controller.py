from flask import Blueprint, request, jsonify

from service.student_service import StudentService


student_controller = Blueprint(
    "student_controller",
    __name__
)


# ==========================================
# CREATE STUDENT
# POST /api/students
# ==========================================

@student_controller.route(
    "/api/students",
    methods=["POST"]
)
def create_student():

    data = request.get_json()

    if not data:
        return jsonify({
            "message": "Request body is required"
        }), 400

    required_fields = [
        "name",
        "email",
        "course"
    ]

    for field in required_fields:

        if field not in data:
            return jsonify({
                "message": f"{field} is required"
            }), 400

    student = StudentService.create_student(data)

    return jsonify({
        "message": "Student created successfully",
        "student": student.to_dict()
    }), 201


# ==========================================
# GET ALL STUDENTS
# GET /api/students
# ==========================================

@student_controller.route(
    "/api/students",
    methods=["GET"]
)
def get_all_students():

    students = StudentService.get_all_students()

    result = [
        student.to_dict()
        for student in students
    ]

    return jsonify(result), 200


# ==========================================
# GET STUDENT BY ID
# GET /api/students/<id>
# ==========================================

@student_controller.route(
    "/api/students/<int:student_id>",
    methods=["GET"]
)
def get_student(student_id):

    student = StudentService.get_student_by_id(
        student_id
    )

    if student is None:
        return jsonify({
            "message": "Student not found"
        }), 404

    return jsonify(
        student.to_dict()
    ), 200


# ==========================================
# UPDATE STUDENT
# PUT /api/students/<id>
# ==========================================

@student_controller.route(
    "/api/students/<int:student_id>",
    methods=["PUT"]
)
def update_student(student_id):

    data = request.get_json()

    if not data:
        return jsonify({
            "message": "Request body is required"
        }), 400

    student = StudentService.update_student(
        student_id,
        data
    )

    if student is None:
        return jsonify({
            "message": "Student not found"
        }), 404

    return jsonify({
        "message": "Student updated successfully",
        "student": student.to_dict()
    }), 200


# ==========================================
# DELETE STUDENT
# DELETE /api/students/<id>
# ==========================================

@student_controller.route(
    "/api/students/<int:student_id>",
    methods=["DELETE"]
)
def delete_student(student_id):

    result = StudentService.delete_student(
        student_id
    )

    if not result:
        return jsonify({
            "message": "Student not found"
        }), 404

    return jsonify({
        "message": "Student deleted successfully"
    }), 200