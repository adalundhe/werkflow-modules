from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDeleteSolutionRequest(BaseModel):
    solutionArn: StrictStr
