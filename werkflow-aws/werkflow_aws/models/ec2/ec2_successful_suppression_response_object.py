from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2SuccessfulSuppressionResponseObject(BaseModel):
    InstanceId: StrictStr | None = None
    SuppressAt: datetime.datetime | StrictStr | None = None
    ResumeAt: datetime.datetime | StrictStr | None = None
