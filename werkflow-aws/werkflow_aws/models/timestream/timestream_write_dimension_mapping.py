from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamWriteDimensionMapping(BaseModel):
    SourceColumn: StrictStr | None = None
    DestinationColumn: StrictStr | None = None
