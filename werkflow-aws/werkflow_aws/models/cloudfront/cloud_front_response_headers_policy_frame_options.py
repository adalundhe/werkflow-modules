from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFrontResponseHeadersPolicyFrameOptions(BaseModel):
    Override: StrictBool | None = None
    FrameOption: StrictStr | None = None
