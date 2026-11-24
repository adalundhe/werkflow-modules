from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_predefined_attribute_summary import ConnectPredefinedAttributeSummary


class ConnectListPredefinedAttributesResponse(BaseModel):
    NextToken: StrictStr | None = None
    PredefinedAttributeSummaryList: list[ConnectPredefinedAttributeSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
