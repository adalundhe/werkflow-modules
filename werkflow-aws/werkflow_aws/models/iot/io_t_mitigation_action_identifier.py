from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IoTMitigationActionIdentifier(BaseModel):
    actionName: StrictStr | None = None
    actionArn: StrictStr | None = None
    creationDate: datetime.datetime | StrictStr | None = None
