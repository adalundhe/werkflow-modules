from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_application_status_detail import EC2ApplicationStatusDetail


class EC2ApplicationStatus(BaseModel):
    Status: StrictStr | None = None
    StatusTimeStamp: datetime.datetime | StrictStr | None = None
    StatusSince: datetime.datetime | StrictStr | None = None
    ResumeAt: datetime.datetime | StrictStr | None = None
    Details: list[EC2ApplicationStatusDetail] | None = None
