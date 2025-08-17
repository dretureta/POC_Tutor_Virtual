import json
import random
import datetime
from faker import Faker
import uuid

# Initialize Faker for Spanish (Uruguay)
fake = Faker('es_ES')

# --- Data for generation ---
FIRST_NAMES_MALE = ['Juan', 'Carlos', 'Luis', 'Jorge', 'Diego', 'Andrés', 'Pablo', 'Martín', 'Santiago', 'Sebastián']
FIRST_NAMES_FEMALE = ['María', 'Ana', 'Sofía', 'Lucía', 'Valentina', 'Camila', 'Florencia', 'Natalia', 'Verónica', 'Paola']
LAST_NAMES = ['Rodríguez', 'González', 'Martínez', 'Fernández', 'Pérez', 'García', 'López', 'Silva', 'Romero', 'Sosa']
SCHOOLS = [
    'Liceo N°1 "José Enrique Rodó"',
    'Liceo N°2 "Héctor Miranda"',
    'Liceo N°3 "Dámaso Antonio Larrañaga" (IAVA)',
    'Liceo N°7 "Joaquín Suárez"',
    'Liceo N°8 "Juan Zorrilla de San Martín"',
    'Liceo N°35 "Instituto Alfredo Vásquez Acevedo" (IAVA)',
    'Colegio y Liceo "José Pedro Varela"',
    'Colegio y Liceo "Sagrada Familia"',
    'Liceo Francés "Jules Supervielle"',
    'Scuola Italiana di Montevideo'
]
SUBJECTS = ['Matemáticas', 'Lengua y Literatura', 'Historia', 'Geografía', 'Biología', 'Física', 'Química', 'Inglés', 'Educación Física']

# --- Generation functions ---

def generate_students(num_students=100):
    """Generates a list of student records."""
    students = []
    for _ in range(num_students):
        gender = random.choice(['male', 'female'])
        first_name = random.choice(FIRST_NAMES_MALE) if gender == 'male' else random.choice(FIRST_NAMES_FEMALE)
        student = {
            "id": str(uuid.uuid4()),
            "first_name": first_name,
            "last_name": random.choice(LAST_NAMES),
            "school": random.choice(SCHOOLS),
        }
        students.append(student)
    return students

def generate_evaluations(students, subjects):
    """Generates a list of evaluation records for the given students."""
    evaluations = []
    today = datetime.date.today()
    for student in students:
        num_evals = random.randint(5, 20)
        for _ in range(num_evals):
            evaluation_date = today - datetime.timedelta(days=random.randint(10, 365 * 2))
            evaluation = {
                "student_id": student['id'],
                "subject": random.choice(subjects),
                "score": random.randint(1, 12),
                "date": evaluation_date.isoformat()
            }
            evaluations.append(evaluation)
    return evaluations

# --- Main script execution ---

if __name__ == "__main__":
    print("Generating mock data...")

    # Generate students and evaluations
    students_data = generate_students(100)
    evaluations_data = generate_evaluations(students_data, SUBJECTS)

    # Save data to JSON files
    with open('students.json', 'w', encoding='utf-8') as f:
        json.dump(students_data, f, indent=2, ensure_ascii=False)

    with open('evaluations.json', 'w', encoding='utf-8') as f:
        json.dump(evaluations_data, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated {len(students_data)} students and {len(evaluations_data)} evaluations.")
    print("Files 'students.json' and 'evaluations.json' have been created.")
