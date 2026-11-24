from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftPutResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
    Policy: StrictStr
