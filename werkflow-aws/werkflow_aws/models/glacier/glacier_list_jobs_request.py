from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierListJobsRequest(BaseModel):
    accountId: StrictStr
    vaultName: StrictStr
    limit: StrictStr | None = None
    marker: StrictStr | None = None
    statuscode: StrictStr | None = None
    completed: StrictStr | None = None
