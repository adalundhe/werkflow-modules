from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontWebAclCustomization(BaseModel):
    Action: StrictStr | None = None
    Arn: StrictStr | None = None
