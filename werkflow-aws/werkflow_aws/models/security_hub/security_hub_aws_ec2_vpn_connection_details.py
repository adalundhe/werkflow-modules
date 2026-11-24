from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_ec2_vpn_connection_options_details import SecurityHubAwsEc2VpnConnectionOptionsDetails
from .security_hub_aws_ec2_vpn_connection_routes_details import SecurityHubAwsEc2VpnConnectionRoutesDetails
from .security_hub_aws_ec2_vpn_connection_vgw_telemetry_details import SecurityHubAwsEc2VpnConnectionVgwTelemetryDetails


class SecurityHubAwsEc2VpnConnectionDetails(BaseModel):
    VpnConnectionId: StrictStr | None = None
    State: StrictStr | None = None
    CustomerGatewayId: StrictStr | None = None
    CustomerGatewayConfiguration: StrictStr | None = None
    Type: StrictStr | None = None
    VpnGatewayId: StrictStr | None = None
    Category: StrictStr | None = None
    VgwTelemetry: list[SecurityHubAwsEc2VpnConnectionVgwTelemetryDetails] | None = None
    Options: SecurityHubAwsEc2VpnConnectionOptionsDetails | None = None
    Routes: list[SecurityHubAwsEc2VpnConnectionRoutesDetails] | None = None
    TransitGatewayId: StrictStr | None = None
