from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sessoa_record import SESSOARecord


class SESVerificationInfo(BaseModel):
    LastCheckedTimestamp: datetime.datetime | StrictStr | None = None
    LastSuccessTimestamp: datetime.datetime | StrictStr | None = None
    ErrorType: StrictStr | None = None
    SOARecord: SESSOARecord | None = None
