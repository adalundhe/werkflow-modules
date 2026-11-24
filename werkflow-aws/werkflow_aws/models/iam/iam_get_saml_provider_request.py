from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMGetSAMLProviderRequest(BaseModel):
    SAMLProviderArn: StrictStr
