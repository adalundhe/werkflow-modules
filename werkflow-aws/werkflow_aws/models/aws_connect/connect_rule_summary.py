from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_action_summary import ConnectActionSummary


class ConnectRuleSummary(BaseModel):
    Name: StrictStr | None = None
    RuleId: StrictStr | None = None
    RuleArn: StrictStr | None = None
    EventSourceName: StrictStr | None = None
    PublishStatus: StrictStr | None = None
    RuleCapabilityTiers: list[StrictStr] | None = None
    ActionSummaries: list[ConnectActionSummary] | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
