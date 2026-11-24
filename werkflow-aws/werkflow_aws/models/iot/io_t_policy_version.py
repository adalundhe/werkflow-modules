from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class IoTPolicyVersion(BaseModel):
    versionId: StrictStr | None = None
    isDefaultVersion: StrictBool | None = None
    createDate: datetime.datetime | StrictStr | None = None
