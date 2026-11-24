from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_action_remote_ip_details import SecurityHubActionRemoteIpDetails
from .security_hub_aws_api_call_action_domain_details import SecurityHubAwsApiCallActionDomainDetails


class SecurityHubAwsApiCallAction(BaseModel):
    Api: StrictStr | None = None
    ServiceName: StrictStr | None = None
    CallerType: StrictStr | None = None
    RemoteIpDetails: SecurityHubActionRemoteIpDetails | None = None
    DomainDetails: SecurityHubAwsApiCallActionDomainDetails | None = None
    AffectedResources: dict[StrictStr, StrictStr] | None = None
    FirstSeen: StrictStr | None = None
    LastSeen: StrictStr | None = None
