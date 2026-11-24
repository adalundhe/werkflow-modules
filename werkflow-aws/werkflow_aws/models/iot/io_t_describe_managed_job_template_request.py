from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeManagedJobTemplateRequest(BaseModel):
    templateName: StrictStr
    templateVersion: StrictStr | None = None
