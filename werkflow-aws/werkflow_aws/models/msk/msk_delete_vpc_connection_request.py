from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKDeleteVpcConnectionRequest(BaseModel):
    Arn: StrictStr
