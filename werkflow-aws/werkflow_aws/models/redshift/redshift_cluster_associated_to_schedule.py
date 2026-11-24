from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftClusterAssociatedToSchedule(BaseModel):
    ClusterIdentifier: StrictStr | None = None
    ScheduleAssociationState: StrictStr | None = None
