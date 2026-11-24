from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KinesisAnalyticsDeleteApplicationInputProcessingConfigurationRequest(BaseModel):
    ApplicationName: StrictStr
    CurrentApplicationVersionId: StrictInt
    InputId: StrictStr
