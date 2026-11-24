from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUntagSAMLProviderRequest(BaseModel):
    SAMLProviderArn: StrictStr
    TagKeys: list[StrictStr]
