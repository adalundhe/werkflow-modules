from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_application_status_reason import EC2ApplicationStatusReason


class EC2ApplicationStatusDetail(BaseModel):
    ApplicationStatusCheckId: StrictStr | None = None
    CheckUpdateTime: datetime.datetime | StrictStr | None = None
    Aggregation: StrictStr | None = None
    Status: StrictStr | None = None
    StatusTimeStamp: datetime.datetime | StrictStr | None = None
    StatusSince: datetime.datetime | StrictStr | None = None
    Reason: EC2ApplicationStatusReason | None = None
