from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsRollbackApplicationRequest(BaseModel):
    ApplicationName: StrictStr
    CurrentApplicationVersionId: StrictInt
