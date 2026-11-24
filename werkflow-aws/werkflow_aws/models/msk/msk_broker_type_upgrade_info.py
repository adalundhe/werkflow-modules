from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKBrokerTypeUpgradeInfo(BaseModel):
    TopicReassignmentMode: StrictStr | None = None
    TopicReassignmentOperationArn: StrictStr | None = None
