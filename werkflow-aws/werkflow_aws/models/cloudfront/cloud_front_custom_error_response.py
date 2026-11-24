from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFrontCustomErrorResponse(BaseModel):
    ErrorCode: StrictInt | None = None
    ResponsePagePath: StrictStr | None = None
    ResponseCode: StrictStr | None = None
    ErrorCachingMinTTL: StrictInt | None = None
