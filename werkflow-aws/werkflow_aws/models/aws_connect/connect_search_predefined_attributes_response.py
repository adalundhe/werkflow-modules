from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_predefined_attribute import ConnectPredefinedAttribute


class ConnectSearchPredefinedAttributesResponse(BaseModel):
    PredefinedAttributes: list[ConnectPredefinedAttribute] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
