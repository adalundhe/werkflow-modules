from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerCapacityReservationEndpointsAssociation(BaseModel):
    MlReservationId: StrictStr | None = None
    Status: StrictStr | None = None
    MatchCriteria: StrictStr | None = None
    EndpointSharing: StrictStr | None = None
    MlReservationArn: StrictStr | None = None
    FailureReason: StrictStr | None = None
    AssociatedTime: datetime.datetime | StrictStr | None = None
