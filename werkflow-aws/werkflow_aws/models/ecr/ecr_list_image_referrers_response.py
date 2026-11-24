from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_image_referrer import ECRImageReferrer


class ECRListImageReferrersResponse(BaseModel):
    referrers: list[ECRImageReferrer] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
