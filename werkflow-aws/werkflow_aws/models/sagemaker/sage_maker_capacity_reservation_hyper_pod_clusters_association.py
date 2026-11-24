from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SageMakerCapacityReservationHyperPodClustersAssociation(BaseModel):
    Status: StrictStr | None = None
    FailureReason: StrictStr | None = None
    AssociatedTime: datetime.datetime | StrictStr | None = None
