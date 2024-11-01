import uuid
from uuid import UUID
from sqlalchemy.orm import declarative_base, declarative_mixin, declared_attr

Base = declarative_base()


@declarative_mixin
class BaseMixin:
    """
    Class defining common attributes for all models.
    All models should inherit from this class.
    """

    uuid = UUID(
        as_uuid=True,
        primary_key=True,
        index=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()