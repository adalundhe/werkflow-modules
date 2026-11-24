from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudFormationUpdateGeneratedTemplateResponse(BaseModel):
    GeneratedTemplateId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
