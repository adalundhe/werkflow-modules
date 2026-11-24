from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_session_manager_output_url import SSMSessionManagerOutputUrl


class SSMSession(BaseModel):
    SessionId: StrictStr | None = None
    Target: StrictStr | None = None
    Status: StrictStr | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    DocumentName: StrictStr | None = None
    Owner: StrictStr | None = None
    Reason: StrictStr | None = None
    Details: StrictStr | None = None
    OutputUrl: SSMSessionManagerOutputUrl | None = None
    MaxSessionDuration: StrictStr | None = None
    AccessType: StrictStr | None = None
