import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.session import Base
from app.models.enums import UserRole, UserStatus


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    display_name = Column(String(120), nullable=False)
    role = Column(
        Enum(UserRole, name="user_role", native_enum=False),
        default=UserRole.CUSTOMER,
        nullable=False,
    )
    status = Column(
        Enum(UserStatus, name="user_status", native_enum=False),
        default=UserStatus.ACTIVE,
        nullable=False,
    )

    suspended_at = Column(DateTime, nullable=True)
    suspension_reason = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    projects_as_customer = relationship(
        "Project", foreign_keys="[Project.customer_id]", back_populates="customer"
    )
    projects_as_contractor = relationship(
        "Project", foreign_keys="[Project.contractor_id]", back_populates="contractor"
    )
    responses = relationship("ProjectResponse", back_populates="contractor")
    reviews_received = relationship(
        "Review", foreign_keys="[Review.contractor_id]", back_populates="contractor"
    )
