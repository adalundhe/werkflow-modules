from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .audit_record_bean import AuditRecordBean


class AuditRecords(BaseModel):
    limit: StrictInt | None = None
    offset: StrictInt | None = None
    records: list[AuditRecordBean] | None = None
    total: StrictInt | None = None
