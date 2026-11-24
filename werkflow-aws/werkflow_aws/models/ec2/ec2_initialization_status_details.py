from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2InitializationStatusDetails(BaseModel):
    InitializationType: StrictStr | None = None
    Progress: StrictInt | None = None
    EstimatedTimeToCompleteInSeconds: StrictInt | None = None
