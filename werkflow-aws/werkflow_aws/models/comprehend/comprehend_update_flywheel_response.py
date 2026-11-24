from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .comprehend_flywheel_properties import ComprehendFlywheelProperties


class ComprehendUpdateFlywheelResponse(BaseModel):
    FlywheelProperties: ComprehendFlywheelProperties | None = None
    ResponseMetadata: dict[str, Any] | None = None
