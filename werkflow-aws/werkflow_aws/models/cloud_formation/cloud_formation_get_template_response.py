from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudFormationGetTemplateResponse(BaseModel):
    TemplateBody: StrictStr | None = None
    StagesAvailable: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
