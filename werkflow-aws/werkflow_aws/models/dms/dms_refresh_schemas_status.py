from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DMSRefreshSchemasStatus(BaseModel):
    EndpointArn: StrictStr | None = None
    ReplicationInstanceArn: StrictStr | None = None
    Status: StrictStr | None = None
    LastRefreshDate: datetime.datetime | StrictStr | None = None
    LastFailureMessage: StrictStr | None = None
