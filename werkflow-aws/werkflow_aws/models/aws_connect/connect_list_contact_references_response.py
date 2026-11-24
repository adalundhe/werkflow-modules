from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_reference_summary import ConnectReferenceSummary


class ConnectListContactReferencesResponse(BaseModel):
    ReferenceSummaryList: list[ConnectReferenceSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
