from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_security_finding_identifier import SecurityHubAwsSecurityFindingIdentifier


class SecurityHubGetFindingHistoryRequest(BaseModel):
    FindingIdentifier: SecurityHubAwsSecurityFindingIdentifier
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
