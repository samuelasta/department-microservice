

class department_repository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, department):
        self.db.add(department)
        self.db.commit()
        self.db.refresh(department)
        return department

    def get_by_id(self, id):
        return self.db.query(Department).filter(Department.id == id).first()

    def get_all(self):
        return self.db.query(Department).all()