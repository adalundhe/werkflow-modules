from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsDeleteApplicationReferenceDataSourceRequest(BaseModel):
    ApplicationName: StrictStr
    CurrentApplicationVersionId: StrictInt
    ReferenceId: StrictStr
