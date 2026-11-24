from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .ssm_runbook import SSMRunbook
from .ssm_tag import SSMTag


class SSMStartChangeRequestExecutionRequest(BaseModel):
    DocumentName: StrictStr
    Runbooks: list[SSMRunbook]
    ScheduledTime: datetime.datetime | StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    Parameters: dict[StrictStr, list[StrictStr]] | None = None
    ChangeRequestName: StrictStr | None = None
    ClientToken: StrictStr | None = None
    AutoApprove: StrictBool | None = None
    Tags: list[SSMTag] | None = None
    ScheduledEndTime: datetime.datetime | StrictStr | None = None
    ChangeDetails: StrictStr | None = None
