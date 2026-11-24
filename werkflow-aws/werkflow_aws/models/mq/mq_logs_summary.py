from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .mq_pending_logs import MQPendingLogs


class MQLogsSummary(BaseModel):
    Audit: StrictBool | None = None
    AuditLogGroup: StrictStr | None = None
    General: StrictBool | None = None
    GeneralLogGroup: StrictStr | None = None
    Pending: MQPendingLogs | None = None
