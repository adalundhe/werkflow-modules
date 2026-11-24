from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_associated_target_network import EC2AssociatedTargetNetwork
from .ec2_client_connect_response_options import EC2ClientConnectResponseOptions
from .ec2_client_login_banner_response_options import EC2ClientLoginBannerResponseOptions
from .ec2_client_route_enforcement_response_options import EC2ClientRouteEnforcementResponseOptions
from .ec2_client_vpn_authentication import EC2ClientVpnAuthentication
from .ec2_client_vpn_endpoint_status import EC2ClientVpnEndpointStatus
from .ec2_connection_log_response_options import EC2ConnectionLogResponseOptions
from .ec2_device_posture_response_options import EC2DevicePostureResponseOptions
from .ec2_tag_model import EC2TagModel
from .ec2_transit_gateway_configuration_describe_endpoint_structure import EC2TransitGatewayConfigurationDescribeEndpointStructure


class EC2ClientVpnEndpoint(BaseModel):
    ClientVpnEndpointId: StrictStr | None = None
    Description: StrictStr | None = None
    Status: EC2ClientVpnEndpointStatus | None = None
    CreationTime: StrictStr | None = None
    DeletionTime: StrictStr | None = None
    DnsName: StrictStr | None = None
    ClientCidrBlock: StrictStr | None = None
    DnsServers: list[StrictStr] | None = None
    SplitTunnel: StrictBool | None = None
    VpnProtocol: StrictStr | None = None
    TransportProtocol: StrictStr | None = None
    VpnPort: StrictInt | None = None
    AssociatedTargetNetworks: list[EC2AssociatedTargetNetwork] | None = None
    ServerCertificateArn: StrictStr | None = None
    AuthenticationOptions: list[EC2ClientVpnAuthentication] | None = None
    ConnectionLogOptions: EC2ConnectionLogResponseOptions | None = None
    Tags: list[EC2TagModel] | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    VpcId: StrictStr | None = None
    SelfServicePortalUrl: StrictStr | None = None
    ClientConnectOptions: EC2ClientConnectResponseOptions | None = None
    SessionTimeoutHours: StrictInt | None = None
    ClientLoginBannerOptions: EC2ClientLoginBannerResponseOptions | None = None
    ClientRouteEnforcementOptions: EC2ClientRouteEnforcementResponseOptions | None = None
    DisconnectOnSessionTimeout: StrictBool | None = None
    EndpointIpAddressType: StrictStr | None = None
    TrafficIpAddressType: StrictStr | None = None
    TransitGatewayConfiguration: EC2TransitGatewayConfigurationDescribeEndpointStructure | None = None
    DevicePostureOptions: EC2DevicePostureResponseOptions | None = None
