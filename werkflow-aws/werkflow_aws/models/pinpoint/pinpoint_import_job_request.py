from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class PinpointImportJobRequest(BaseModel):
    Format: Literal['CSV', 'JSON']
    RoleArn: StrictStr
    S3Url: StrictStr
    DefineSegment: StrictBool | None = None
    ExternalId: StrictStr | None = None
    RegisterEndpoints: StrictBool | None = None
    SegmentId: StrictStr | None = None
    SegmentName: StrictStr | None = None
