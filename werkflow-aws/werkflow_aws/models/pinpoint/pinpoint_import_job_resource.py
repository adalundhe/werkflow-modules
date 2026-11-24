from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class PinpointImportJobResource(BaseModel):
    DefineSegment: StrictBool | None = None
    ExternalId: StrictStr | None = None
    Format: StrictStr | None = None
    RegisterEndpoints: StrictBool | None = None
    RoleArn: StrictStr | None = None
    S3Url: StrictStr | None = None
    SegmentId: StrictStr | None = None
    SegmentName: StrictStr | None = None
