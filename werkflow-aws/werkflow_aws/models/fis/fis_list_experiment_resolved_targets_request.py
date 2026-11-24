from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FISListExperimentResolvedTargetsRequest(BaseModel):
    experimentId: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    targetName: StrictStr | None = None
