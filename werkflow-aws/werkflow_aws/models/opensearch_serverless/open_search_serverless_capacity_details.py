from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class OpenSearchServerlessCapacityDetails(BaseModel):
    capacityInOcu: StrictFloat | StrictInt | None = None
    autoscalingStatus: StrictStr | None = None
