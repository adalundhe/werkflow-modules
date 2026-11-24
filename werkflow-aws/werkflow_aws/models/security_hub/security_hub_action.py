from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_api_call_action import SecurityHubAwsApiCallAction
from .security_hub_dns_request_action import SecurityHubDnsRequestAction
from .security_hub_network_connection_action import SecurityHubNetworkConnectionAction
from .security_hub_port_probe_action import SecurityHubPortProbeAction


class SecurityHubAction(BaseModel):
    ActionType: StrictStr | None = None
    NetworkConnectionAction: SecurityHubNetworkConnectionAction | None = None
    AwsApiCallAction: SecurityHubAwsApiCallAction | None = None
    DnsRequestAction: SecurityHubDnsRequestAction | None = None
    PortProbeAction: SecurityHubPortProbeAction | None = None
