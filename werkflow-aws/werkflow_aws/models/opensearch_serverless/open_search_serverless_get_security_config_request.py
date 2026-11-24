from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchServerlessGetSecurityConfigRequest(BaseModel):
    id: StrictStr
