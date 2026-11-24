from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTDeleteProvisioningTemplateVersionRequest(BaseModel):
    templateName: StrictStr
    versionId: StrictInt
