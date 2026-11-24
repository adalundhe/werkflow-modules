from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeJobTemplateRequest(BaseModel):
    jobTemplateId: StrictStr
