from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFrontResponseHeadersPolicyXSSProtection(BaseModel):
    Override: StrictBool | None = None
    Protection: StrictBool | None = None
    ModeBlock: StrictBool | None = None
    ReportUri: StrictStr | None = None
