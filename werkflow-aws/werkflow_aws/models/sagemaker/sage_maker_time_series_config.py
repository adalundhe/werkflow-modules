from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTimeSeriesConfig(BaseModel):
    TargetAttributeName: StrictStr | None = None
    TimestampAttributeName: StrictStr | None = None
    ItemIdentifierAttributeName: StrictStr | None = None
    GroupingAttributeNames: list[StrictStr] | None = None
