from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreateJobTemplateResponse(BaseModel):
    jobTemplateArn: StrictStr | None = None
    jobTemplateId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
