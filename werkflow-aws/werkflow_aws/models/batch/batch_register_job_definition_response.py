from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class BatchRegisterJobDefinitionResponse(BaseModel):
    jobDefinitionName: StrictStr | None = None
    jobDefinitionArn: StrictStr | None = None
    revision: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
