from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTCreateProvisioningTemplateVersionRequest(BaseModel):
    templateName: StrictStr
    templateBody: StrictStr
    setAsDefault: StrictBool | None = None
