from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationDeregisterResourceRequest(BaseModel):
    ResourceArn: StrictStr
