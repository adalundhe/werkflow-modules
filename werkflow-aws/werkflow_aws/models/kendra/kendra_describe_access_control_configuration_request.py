from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDescribeAccessControlConfigurationRequest(BaseModel):
    IndexId: StrictStr
    Id: StrictStr
