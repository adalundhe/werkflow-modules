from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_security_finding_identifier import SecurityHubAwsSecurityFindingIdentifier
from .security_hub_finding_history_update import SecurityHubFindingHistoryUpdate
from .security_hub_finding_history_update_source import SecurityHubFindingHistoryUpdateSource


class SecurityHubFindingHistoryRecord(BaseModel):
    FindingIdentifier: SecurityHubAwsSecurityFindingIdentifier | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    FindingCreated: StrictBool | None = None
    UpdateSource: SecurityHubFindingHistoryUpdateSource | None = None
    Updates: list[SecurityHubFindingHistoryUpdate] | None = None
    NextToken: StrictStr | None = None
