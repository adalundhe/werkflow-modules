from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PinpointExportJobRequest(BaseModel):
    RoleArn: StrictStr
    S3UrlPrefix: StrictStr
    SegmentId: StrictStr | None = None
    SegmentVersion: StrictInt | None = None
