import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import ARRAY, UUID
from sqlalchemy.orm import relationship

from app.db.session import Base
from app.models.enums import ProjectStatus, ResponseStatus


class Project(Base):
    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    contractor_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)

    title = Column(String(160), nullable=False)
    description = Column(Text, nullable=False)
    object_details = Column(Text, nullable=False)
    status = Column(
        Enum(ProjectStatus, name="project_status", native_enum=False),
        default=ProjectStatus.DRAFT,
        nullable=False,
    )
    photo_media_ids = Column(ARRAY(UUID(as_uuid=True)), default=list)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    published_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)

    customer = relationship(
        "User", foreign_keys=[customer_id], back_populates="projects_as_customer"
    )
    contractor = relationship(
        "User", foreign_keys=[contractor_id], back_populates="projects_as_contractor"
    )
    responses = relationship(
        "ProjectResponse", back_populates="project", cascade="all, delete-orphan"
    )
    plans = relationship("WorkPlan", back_populates="project", cascade="all, delete-orphan")
    plan_changes = relationship(
        "PlanChange", back_populates="project", cascade="all, delete-orphan"
    )
    review = relationship("Review", back_populates="project", uselist=False)


class ProjectResponse(Base):
    __tablename__ = "project_responses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    contractor_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    message = Column(Text, nullable=False)
    status = Column(
        Enum(ResponseStatus, name="response_status", native_enum=False),
        default=ResponseStatus.PENDING,
        nullable=False,
    )
    created_at = Column(DateTime, default=datetime.utcnow)

    project = relationship("Project", back_populates="responses")
    contractor = relationship("User", back_populates="responses")
