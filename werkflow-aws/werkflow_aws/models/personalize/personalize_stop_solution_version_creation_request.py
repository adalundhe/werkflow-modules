from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeStopSolutionVersionCreationRequest(BaseModel):
    solutionVersionArn: StrictStr
