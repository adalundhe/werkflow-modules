from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TimestreamQueryQueryTemporalRangeMax(BaseModel):
    Value: StrictInt | None = None
    TableArn: StrictStr | None = None
