from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RDSDownloadDBLogFilePortionRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    LogFileName: StrictStr
    Marker: StrictStr | None = None
    NumberOfLines: StrictInt | None = None
