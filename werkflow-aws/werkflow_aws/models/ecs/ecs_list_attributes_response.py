from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecs_attribute import ECSAttribute


class ECSListAttributesResponse(BaseModel):
    attributes: list[ECSAttribute] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
