from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ECRCvssScore(BaseModel):
    baseScore: StrictFloat | StrictInt | None = None
    scoringVector: StrictStr | None = None
    source: StrictStr | None = None
    version: StrictStr | None = None
