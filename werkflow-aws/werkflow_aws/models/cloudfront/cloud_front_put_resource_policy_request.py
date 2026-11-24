from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontPutResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
    PolicyDocument: StrictStr
