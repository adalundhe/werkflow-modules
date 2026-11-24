from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_sbom_validation_result_summary import IoTSbomValidationResultSummary


class IoTListSbomValidationResultsResponse(BaseModel):
    validationResultSummaries: list[IoTSbomValidationResultSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
