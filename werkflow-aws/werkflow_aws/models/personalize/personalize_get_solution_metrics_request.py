from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeGetSolutionMetricsRequest(BaseModel):
    solutionVersionArn: StrictStr
