from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class PersonalizeGetSolutionMetricsResponse(BaseModel):
    solutionVersionArn: StrictStr | None = None
    metrics: dict[StrictStr, StrictFloat | StrictInt] | None = None
    ResponseMetadata: dict[str, Any] | None = None
