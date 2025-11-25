# School Management System

A web-based software application designed to simplify and automate the administrative and academic activities of a basic school. The system helps manage student information, teacher operations, classes, communication, and exam records in an efficient and user-friendly way.

## Tech Stack
- Python  
- Django  
- Django REST Framework  
- HTML  
- CSS  
- JavaScript  

## Project Progress

### ✅ Day 1 – Planning & Setup
- Defined project scope and objectives.
- Prepared Software Requirements Document (SRD).
- Set up development environment and project structure.
- Created initial README file.

### ✅ Day 2 – User Management Module (In Progress)
- Implemented **CustomUser model** using `AbstractUser`.
- Added additional fields: role, gender, DOB, address, emergency contact, etc.
- Configured **automatic username generation** (Student/Teacher IDs).
- Implemented **automatic password generation** inside the model’s `save()` method.
- Created **Student** and **Teacher** models linked via `OneToOneField`.
- Registered all models in Django Admin for management.
- Added `AUTH_USER_MODEL = "users.CustomUser"` to project settings.
- Ran initial migrations successfully.

---

More updates will be added as development continues.
