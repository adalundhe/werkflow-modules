from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDeleteAccessControlConfigurationRequest(BaseModel):
    IndexId: StrictStr
    Id: StrictStr
