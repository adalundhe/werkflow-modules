from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneSelfGrantStatusDetail(BaseModel):
    databaseName: StrictStr | None = None
    schemaName: StrictStr | None = None
    status: StrictStr | None = None
    failureCause: StrictStr | None = None
