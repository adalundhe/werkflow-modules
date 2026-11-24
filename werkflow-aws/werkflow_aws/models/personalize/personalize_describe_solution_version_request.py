from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDescribeSolutionVersionRequest(BaseModel):
    solutionVersionArn: StrictStr
