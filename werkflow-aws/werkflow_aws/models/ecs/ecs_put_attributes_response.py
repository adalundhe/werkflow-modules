from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecs_attribute import ECSAttribute


class ECSPutAttributesResponse(BaseModel):
    attributes: list[ECSAttribute] | None = None
    ResponseMetadata: dict[str, Any] | None = None
