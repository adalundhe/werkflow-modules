from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontResponseHeadersPolicyRemoveHeader(BaseModel):
    Header: StrictStr | None = None
