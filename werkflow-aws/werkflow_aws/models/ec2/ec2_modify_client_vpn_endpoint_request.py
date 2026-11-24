from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_client_connect_options import EC2ClientConnectOptions
from .ec2_client_login_banner_options import EC2ClientLoginBannerOptions
from .ec2_client_route_enforcement_options import EC2ClientRouteEnforcementOptions
from .ec2_connection_log_options import EC2ConnectionLogOptions
from .ec2_device_posture_options import EC2DevicePostureOptions
from .ec2_dns_servers_options_modify_structure import EC2DnsServersOptionsModifyStructure
from .ec2_transit_gateway_configuration_input_structure import EC2TransitGatewayConfigurationInputStructure


class EC2ModifyClientVpnEndpointRequest(BaseModel):
    ClientVpnEndpointId: StrictStr
    ServerCertificateArn: StrictStr | None = None
    ConnectionLogOptions: EC2ConnectionLogOptions | None = None
    DnsServers: EC2DnsServersOptionsModifyStructure | None = None
    VpnPort: StrictInt | None = None
    Description: StrictStr | None = None
    SplitTunnel: StrictBool | None = None
    DryRun: StrictBool | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    VpcId: StrictStr | None = None
    SelfServicePortal: Literal['enabled', 'disabled'] | None = None
    ClientConnectOptions: EC2ClientConnectOptions | None = None
    SessionTimeoutHours: StrictInt | None = None
    ClientLoginBannerOptions: EC2ClientLoginBannerOptions | None = None
    ClientRouteEnforcementOptions: EC2ClientRouteEnforcementOptions | None = None
    DisconnectOnSessionTimeout: StrictBool | None = None
    TransitGatewayConfiguration: EC2TransitGatewayConfigurationInputStructure | None = None
    DevicePostureOptions: EC2DevicePostureOptions | None = None
