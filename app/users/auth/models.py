from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTableUUID

from app.infrastructure.database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    ...


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):
    ...
