from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_predefined_attribute import ConnectPredefinedAttribute


class ConnectDescribePredefinedAttributeResponse(BaseModel):
    PredefinedAttribute: ConnectPredefinedAttribute | None = None
    ResponseMetadata: dict[str, Any] | None = None
