from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_analysis_definition import QuickSightAnalysisDefinition
from .quick_sight_analysis_error import QuickSightAnalysisError


class QuickSightDescribeAnalysisDefinitionResponse(BaseModel):
    AnalysisId: StrictStr | None = None
    Name: StrictStr | None = None
    Errors: list[QuickSightAnalysisError] | None = None
    ResourceStatus: StrictStr | None = None
    ThemeArn: StrictStr | None = None
    Definition: QuickSightAnalysisDefinition | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
