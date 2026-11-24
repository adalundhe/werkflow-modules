from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayCloudWatchLogsConfiguration(BaseModel):
    SpansLogGroupKmsKeyId: StrictStr | None = None
