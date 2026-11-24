from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QuickSightInboundConnectorApplicationAssociationSummary(BaseModel):
    AccessControlApplicationArn: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
