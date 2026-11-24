from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_hsm_tag import CloudHSMTag


class CloudHSMTagResourceRequest(BaseModel):
    ResourceId: StrictStr
    TagList: list[CloudHSMTag]
