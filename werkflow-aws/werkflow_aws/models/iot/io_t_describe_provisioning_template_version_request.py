from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTDescribeProvisioningTemplateVersionRequest(BaseModel):
    templateName: StrictStr
    versionId: StrictInt
