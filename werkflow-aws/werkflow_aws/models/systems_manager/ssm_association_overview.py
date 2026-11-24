from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SSMAssociationOverview(BaseModel):
    Status: StrictStr | None = None
    DetailedStatus: StrictStr | None = None
    AssociationStatusAggregatedCount: dict[StrictStr, StrictInt] | None = None
