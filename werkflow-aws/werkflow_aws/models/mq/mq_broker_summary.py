from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class MQBrokerSummary(BaseModel):
    BrokerArn: StrictStr | None = None
    BrokerId: StrictStr | None = None
    BrokerName: StrictStr | None = None
    BrokerState: StrictStr | None = None
    Created: datetime.datetime | StrictStr | None = None
    DeploymentMode: StrictStr | None = None
    EngineType: StrictStr | None = None
    HostInstanceType: StrictStr | None = None
