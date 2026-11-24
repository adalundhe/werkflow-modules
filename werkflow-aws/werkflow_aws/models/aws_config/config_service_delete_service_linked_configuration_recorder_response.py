from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConfigServiceDeleteServiceLinkedConfigurationRecorderResponse(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
