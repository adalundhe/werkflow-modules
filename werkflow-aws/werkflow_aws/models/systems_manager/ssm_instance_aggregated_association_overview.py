from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SSMInstanceAggregatedAssociationOverview(BaseModel):
    DetailedStatus: StrictStr | None = None
    InstanceAssociationStatusAggregatedCount: dict[StrictStr, StrictInt] | None = None
