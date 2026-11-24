from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDeleteTemplateAliasResponse(BaseModel):
    Status: StrictInt | None = None
    TemplateId: StrictStr | None = None
    AliasName: StrictStr | None = None
    Arn: StrictStr | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
