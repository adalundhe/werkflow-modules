from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_ec2_client_vpn_endpoint_client_connect_options_status_details import SecurityHubAwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails


class SecurityHubAwsEc2ClientVpnEndpointClientConnectOptionsDetails(BaseModel):
    Enabled: StrictBool | None = None
    LambdaFunctionArn: StrictStr | None = None
    Status: SecurityHubAwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails | None = None
