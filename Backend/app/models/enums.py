import enum


class UserRole(str, enum.Enum):
    CUSTOMER = "customer"
    CONTRACTOR = "contractor"
    ADMINISTRATOR = "administrator"
    MODERATOR = "moderator"


class UserStatus(str, enum.Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"


class ProjectStatus(str, enum.Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    CONTRACTOR_SELECTED = "contractor_selected"
    PLAN_APPROVAL = "plan_approval"
    IN_PROGRESS = "in_progress"
    AWAITING_FINAL_ACCEPTANCE = "awaiting_final_acceptance"
    COMPLETED = "completed"
    HIDDEN = "hidden"


class ResponseStatus(str, enum.Enum):
    PENDING = "pending"
    SELECTED = "selected"
    NOT_SELECTED = "not_selected"


class PlanStatus(str, enum.Enum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    APPROVED = "approved"
    REVISION_REQUESTED = "revision_requested"
    SUPERSEDED = "superseded"


class StageStatus(str, enum.Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    SUBMITTED = "submitted"
    ACCEPTED = "accepted"
    REVISION_REQUESTED = "revision_requested"


class ReportStatus(str, enum.Enum):
    SUBMITTED = "submitted"
    ACCEPTED = "accepted"
    REVISION_REQUESTED = "revision_requested"


class PlanChangeStatus(str, enum.Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"
