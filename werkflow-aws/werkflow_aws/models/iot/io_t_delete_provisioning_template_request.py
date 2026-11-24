from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDeleteProvisioningTemplateRequest(BaseModel):
    templateName: StrictStr
