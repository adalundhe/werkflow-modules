from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DMSDescribeApplicableIndividualAssessmentsResponse(BaseModel):
    IndividualAssessmentNames: list[StrictStr] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
