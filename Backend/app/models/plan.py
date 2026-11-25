import uuid
from datetime import datetime

from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.dialects.postgresql import ARRAY, JSONB, UUID
from sqlalchemy.orm import relationship

from app.db.session import Base
from app.models.enums import PlanChangeStatus, PlanStatus, ReportStatus, StageStatus


class WorkPlan(Base):
    __tablename__ = "work_plans"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    version = Column(Integer, nullable=False, default=1)

    works_description = Column(Text, nullable=False)
    planned_start_date = Column(Date, nullable=False)
    planned_end_date = Column(Date, nullable=False)
    estimated_cost_amount = Column(Numeric(12, 2), nullable=False)
    estimated_cost_currency = Column(String(3), default="RUB", nullable=False)
    status = Column(
        Enum(PlanStatus, name="plan_status", native_enum=False),
        default=PlanStatus.DRAFT,
        nullable=False,
    )

    submitted_at = Column(DateTime, nullable=True)
    decided_at = Column(DateTime, nullable=True)
    decision_comment = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    project = relationship("Project", back_populates="plans")
    stages = relationship("WorkStage", back_populates="plan", cascade="all, delete-orphan")


class WorkStage(Base):
    __tablename__ = "work_stages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    plan_id = Column(UUID(as_uuid=True), ForeignKey("work_plans.id"), nullable=False)

    title = Column(String(160), nullable=False)
    description = Column(Text, nullable=False)
    planned_start_date = Column(Date, nullable=False)
    planned_end_date = Column(Date, nullable=False)
    estimated_cost_amount = Column(Numeric(12, 2), nullable=False)
    estimated_cost_currency = Column(String(3), default="RUB", nullable=False)
    actual_cost_amount = Column(Numeric(12, 2), nullable=True)
    actual_cost_currency = Column(String(3), nullable=True)
    status = Column(
        Enum(StageStatus, name="stage_status", native_enum=False),
        default=StageStatus.NOT_STARTED,
        nullable=False,
    )

    plan = relationship("WorkPlan", back_populates="stages")
    reports = relationship("WorkReport", back_populates="stage", cascade="all, delete-orphan")


class WorkReport(Base):
    __tablename__ = "work_reports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    stage_id = Column(UUID(as_uuid=True), ForeignKey("work_stages.id"), nullable=False)
    description = Column(Text, nullable=False)
    actual_cost_amount = Column(Numeric(12, 2), nullable=False)
    actual_cost_currency = Column(String(3), default="RUB", nullable=False)
    photo_media_ids = Column(ARRAY(UUID(as_uuid=True)), default=list)
    status = Column(
        Enum(ReportStatus, name="report_status", native_enum=False),
        default=ReportStatus.SUBMITTED,
        nullable=False,
    )
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    stage = relationship("WorkStage", back_populates="reports")


class PlanChange(Base):
    __tablename__ = "plan_changes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    reason = Column(Text, nullable=False)
    proposed_changes = Column(JSONB, nullable=False)
    status = Column(
        Enum(PlanChangeStatus, name="plan_change_status", native_enum=False),
        default=PlanChangeStatus.PENDING,
        nullable=False,
    )
    decision_comment = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    project = relationship("Project", back_populates="plan_changes")
