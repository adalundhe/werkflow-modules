from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudFormationGetGeneratedTemplateResponse(BaseModel):
    Status: StrictStr | None = None
    TemplateBody: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
