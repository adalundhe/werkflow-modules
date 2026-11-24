from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudFrontResponseHeadersPolicyReferrerPolicy(BaseModel):
    Override: StrictBool | None = None
    ReferrerPolicy: StrictStr | None = None
