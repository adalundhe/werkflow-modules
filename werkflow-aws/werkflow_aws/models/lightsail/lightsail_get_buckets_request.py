from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailGetBucketsRequest(BaseModel):
    bucketName: StrictStr | None = None
    pageToken: StrictStr | None = None
    includeConnectedResources: StrictBool | None = None
    includeCors: StrictBool | None = None
