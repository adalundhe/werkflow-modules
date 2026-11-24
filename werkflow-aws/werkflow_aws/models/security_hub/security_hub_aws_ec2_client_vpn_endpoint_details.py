from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_aws_ec2_client_vpn_endpoint_authentication_options_details import SecurityHubAwsEc2ClientVpnEndpointAuthenticationOptionsDetails
from .security_hub_aws_ec2_client_vpn_endpoint_client_connect_options_details import SecurityHubAwsEc2ClientVpnEndpointClientConnectOptionsDetails
from .security_hub_aws_ec2_client_vpn_endpoint_client_login_banner_options_details import SecurityHubAwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails
from .security_hub_aws_ec2_client_vpn_endpoint_connection_log_options_details import SecurityHubAwsEc2ClientVpnEndpointConnectionLogOptionsDetails


class SecurityHubAwsEc2ClientVpnEndpointDetails(BaseModel):
    ClientVpnEndpointId: StrictStr | None = None
    Description: StrictStr | None = None
    ClientCidrBlock: StrictStr | None = None
    DnsServer: list[StrictStr] | None = None
    SplitTunnel: StrictBool | None = None
    TransportProtocol: StrictStr | None = None
    VpnPort: StrictInt | None = None
    ServerCertificateArn: StrictStr | None = None
    AuthenticationOptions: list[SecurityHubAwsEc2ClientVpnEndpointAuthenticationOptionsDetails] | None = None
    ConnectionLogOptions: SecurityHubAwsEc2ClientVpnEndpointConnectionLogOptionsDetails | None = None
    SecurityGroupIdSet: list[StrictStr] | None = None
    VpcId: StrictStr | None = None
    SelfServicePortalUrl: StrictStr | None = None
    ClientConnectOptions: SecurityHubAwsEc2ClientVpnEndpointClientConnectOptionsDetails | None = None
    SessionTimeoutHours: StrictInt | None = None
    ClientLoginBannerOptions: SecurityHubAwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails | None = None
