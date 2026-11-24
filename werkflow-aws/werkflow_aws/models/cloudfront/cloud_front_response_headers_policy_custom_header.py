from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFrontResponseHeadersPolicyCustomHeader(BaseModel):
    Header: StrictStr | None = None
    Value: StrictStr | None = None
    Override: StrictBool | None = None
