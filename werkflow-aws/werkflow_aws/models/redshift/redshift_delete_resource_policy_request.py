from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
