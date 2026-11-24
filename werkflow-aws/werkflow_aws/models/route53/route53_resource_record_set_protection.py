from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ResourceRecordSetProtection(BaseModel):
    RecordName: StrictStr | None = None
    RecordType: StrictStr | None = None
    Comment: StrictStr | None = None
