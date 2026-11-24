from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftGetResourcePolicyRequest(BaseModel):
    ResourceArn: StrictStr
