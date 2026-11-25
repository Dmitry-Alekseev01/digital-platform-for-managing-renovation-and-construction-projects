import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.session import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), unique=True, nullable=False)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    contractor_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    rating = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    is_hidden = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    project = relationship("Project", back_populates="review")
    contractor = relationship(
        "User", foreign_keys=[contractor_id], back_populates="reviews_received"
    )
