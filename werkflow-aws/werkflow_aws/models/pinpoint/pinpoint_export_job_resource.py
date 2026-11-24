from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class PinpointExportJobResource(BaseModel):
    RoleArn: StrictStr | None = None
    S3UrlPrefix: StrictStr | None = None
    SegmentId: StrictStr | None = None
    SegmentVersion: StrictInt | None = None
