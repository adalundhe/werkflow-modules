from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_ops_item_identity import SSMOpsItemIdentity


class SSMOpsItemEventSummary(BaseModel):
    OpsItemId: StrictStr | None = None
    EventId: StrictStr | None = None
    Source: StrictStr | None = None
    DetailType: StrictStr | None = None
    Detail: StrictStr | None = None
    CreatedBy: SSMOpsItemIdentity | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
