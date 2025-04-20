from ..models_db.user import Users
from sqlmodel import Session, select

def get_user_by_username(username: str, session: Session) -> Users:
    statement = select(Users).where(Users.username == username)
    results = session.exec(statement)
    return results.first()


def create_user(name: str, username: str, email: str, password: str, 
                session: Session) -> Users:
    db_user = Users(name=name, username=username, email=email, password=password)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

