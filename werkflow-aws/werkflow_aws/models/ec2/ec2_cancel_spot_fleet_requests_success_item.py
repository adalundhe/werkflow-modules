from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CancelSpotFleetRequestsSuccessItem(BaseModel):
    CurrentSpotFleetRequestState: StrictStr | None = None
    PreviousSpotFleetRequestState: StrictStr | None = None
    SpotFleetRequestId: StrictStr | None = None
