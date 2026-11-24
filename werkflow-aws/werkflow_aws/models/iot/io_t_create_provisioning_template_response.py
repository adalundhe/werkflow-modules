from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class IoTCreateProvisioningTemplateResponse(BaseModel):
    templateArn: StrictStr | None = None
    templateName: StrictStr | None = None
    defaultVersionId: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
