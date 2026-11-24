from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .directory_service_tag import DirectoryServiceTag


class DirectoryServiceCreateHybridADRequest(BaseModel):
    SecretArn: StrictStr
    AssessmentId: StrictStr
    Tags: list[DirectoryServiceTag] | None = None
