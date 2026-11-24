from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .textract_adapter_overview import TextractAdapterOverview


class TextractListAdaptersResponse(BaseModel):
    Adapters: list[TextractAdapterOverview] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
