from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTCreateProvisioningTemplateVersionResponse(BaseModel):
    templateArn: StrictStr | None = None
    templateName: StrictStr | None = None
    versionId: StrictInt | None = None
    isDefaultVersion: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
