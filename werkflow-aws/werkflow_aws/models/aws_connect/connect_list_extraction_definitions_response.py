from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_extraction_definition_summary import ConnectExtractionDefinitionSummary


class ConnectListExtractionDefinitionsResponse(BaseModel):
    ExtractionDefinitionSummaryList: list[ConnectExtractionDefinitionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
