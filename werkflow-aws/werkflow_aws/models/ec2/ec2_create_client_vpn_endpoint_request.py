from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_client_connect_options import EC2ClientConnectOptions
from .ec2_client_login_banner_options import EC2ClientLoginBannerOptions
from .ec2_client_route_enforcement_options import EC2ClientRouteEnforcementOptions
from .ec2_client_vpn_authentication_request import EC2ClientVpnAuthenticationRequest
from .ec2_connection_log_options import EC2ConnectionLogOptions
from .ec2_device_posture_options import EC2DevicePostureOptions
from .ec2_tag_specification_model import EC2TagSpecificationModel
from .ec2_transit_gateway_configuration_input_structure import EC2TransitGatewayConfigurationInputStructure


class EC2CreateClientVpnEndpointRequest(BaseModel):
    ServerCertificateArn: StrictStr
    AuthenticationOptions: list[EC2ClientVpnAuthenticationRequest]
    ConnectionLogOptions: EC2ConnectionLogOptions
    ClientCidrBlock: StrictStr | None = None
    DnsServers: list[StrictStr] | None = None
    TransportProtocol: Literal['tcp', 'udp'] | None = None
    VpnPort: StrictInt | None = None
    Description: StrictStr | None = None
    SplitTunnel: StrictBool | None = None
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    VpcId: StrictStr | None = None
    SelfServicePortal: Literal['enabled', 'disabled'] | None = None
    ClientConnectOptions: EC2ClientConnectOptions | None = None
    SessionTimeoutHours: StrictInt | None = None
    ClientLoginBannerOptions: EC2ClientLoginBannerOptions | None = None
    ClientRouteEnforcementOptions: EC2ClientRouteEnforcementOptions | None = None
    DisconnectOnSessionTimeout: StrictBool | None = None
    EndpointIpAddressType: Literal['ipv4', 'ipv6', 'dual-stack'] | None = None
    TrafficIpAddressType: Literal['ipv4', 'ipv6', 'dual-stack'] | None = None
    TransitGatewayConfiguration: EC2TransitGatewayConfigurationInputStructure | None = None
    DevicePostureOptions: EC2DevicePostureOptions | None = None
