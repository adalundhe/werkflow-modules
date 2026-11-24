from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListProvisioningTemplateVersionsRequest(BaseModel):
    templateName: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
