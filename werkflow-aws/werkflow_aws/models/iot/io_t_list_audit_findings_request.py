from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .io_t_resource_identifier import IoTResourceIdentifier


class IoTListAuditFindingsRequest(BaseModel):
    taskId: StrictStr | None = None
    checkName: StrictStr | None = None
    resourceIdentifier: IoTResourceIdentifier | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    listSuppressedFindings: StrictBool | None = None
