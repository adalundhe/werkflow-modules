from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CloudFrontResponseHeadersPolicyContentTypeOptions(BaseModel):
    Override: StrictBool | None = None
