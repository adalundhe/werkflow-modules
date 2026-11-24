from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ses_suppressed_destination_attributes import SESSuppressedDestinationAttributes


class SESSuppressedDestination(BaseModel):
    EmailAddress: StrictStr | None = None
    Reason: StrictStr | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
    Attributes: SESSuppressedDestinationAttributes | None = None
    TenantName: StrictStr | None = None
