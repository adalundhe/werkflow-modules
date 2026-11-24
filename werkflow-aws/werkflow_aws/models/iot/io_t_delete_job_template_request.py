from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDeleteJobTemplateRequest(BaseModel):
    jobTemplateId: StrictStr
