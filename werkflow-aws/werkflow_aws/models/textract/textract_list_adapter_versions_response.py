from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .textract_adapter_version_overview import TextractAdapterVersionOverview


class TextractListAdapterVersionsResponse(BaseModel):
    AdapterVersions: list[TextractAdapterVersionOverview] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
