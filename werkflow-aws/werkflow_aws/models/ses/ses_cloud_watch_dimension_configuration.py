from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SESCloudWatchDimensionConfiguration(BaseModel):
    DimensionName: StrictStr | None = None
    DimensionValueSource: StrictStr | None = None
    DefaultDimensionValue: StrictStr | None = None
