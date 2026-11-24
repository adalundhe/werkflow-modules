from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_analysis_acl_rule import EC2AnalysisAclRule
from .ec2_analysis_component import EC2AnalysisComponent
from .ec2_analysis_load_balancer_listener import EC2AnalysisLoadBalancerListener
from .ec2_analysis_load_balancer_target import EC2AnalysisLoadBalancerTarget
from .ec2_analysis_route_table_route import EC2AnalysisRouteTableRoute
from .ec2_analysis_security_group_rule import EC2AnalysisSecurityGroupRule
from .ec2_analysis_transit_gateway_policy_table_entry import EC2AnalysisTransitGatewayPolicyTableEntry
from .ec2_firewall_stateful_rule import EC2FirewallStatefulRule
from .ec2_firewall_stateless_rule import EC2FirewallStatelessRule
from .ec2_port_range import EC2PortRange
from .ec2_transit_gateway_route_table_route import EC2TransitGatewayRouteTableRoute


class EC2Explanation(BaseModel):
    Acl: EC2AnalysisComponent | None = None
    AclRule: EC2AnalysisAclRule | None = None
    Address: StrictStr | None = None
    Addresses: list[StrictStr] | None = None
    AttachedTo: EC2AnalysisComponent | None = None
    AvailabilityZones: list[StrictStr] | None = None
    AvailabilityZoneIds: list[StrictStr] | None = None
    Cidrs: list[StrictStr] | None = None
    Component: EC2AnalysisComponent | None = None
    CustomerGateway: EC2AnalysisComponent | None = None
    Destination: EC2AnalysisComponent | None = None
    DestinationVpc: EC2AnalysisComponent | None = None
    Direction: StrictStr | None = None
    ExplanationCode: StrictStr | None = None
    IngressRouteTable: EC2AnalysisComponent | None = None
    InternetGateway: EC2AnalysisComponent | None = None
    LoadBalancerArn: StrictStr | None = None
    ClassicLoadBalancerListener: EC2AnalysisLoadBalancerListener | None = None
    LoadBalancerListenerPort: StrictInt | None = None
    LoadBalancerTarget: EC2AnalysisLoadBalancerTarget | None = None
    LoadBalancerTargetGroup: EC2AnalysisComponent | None = None
    LoadBalancerTargetGroups: list[EC2AnalysisComponent] | None = None
    LoadBalancerTargetPort: StrictInt | None = None
    ElasticLoadBalancerListener: EC2AnalysisComponent | None = None
    MissingComponent: StrictStr | None = None
    NatGateway: EC2AnalysisComponent | None = None
    NetworkInterface: EC2AnalysisComponent | None = None
    PacketField: StrictStr | None = None
    VpcPeeringConnection: EC2AnalysisComponent | None = None
    Port: StrictInt | None = None
    PortRanges: list[EC2PortRange] | None = None
    PrefixList: EC2AnalysisComponent | None = None
    Protocols: list[StrictStr] | None = None
    RouteTableRoute: EC2AnalysisRouteTableRoute | None = None
    RouteTable: EC2AnalysisComponent | None = None
    SecurityGroup: EC2AnalysisComponent | None = None
    SecurityGroupRule: EC2AnalysisSecurityGroupRule | None = None
    SecurityGroups: list[EC2AnalysisComponent] | None = None
    SourceVpc: EC2AnalysisComponent | None = None
    State: StrictStr | None = None
    Subnet: EC2AnalysisComponent | None = None
    SubnetRouteTable: EC2AnalysisComponent | None = None
    Vpc: EC2AnalysisComponent | None = None
    VpcEndpoint: EC2AnalysisComponent | None = None
    VpnConnection: EC2AnalysisComponent | None = None
    VpnGateway: EC2AnalysisComponent | None = None
    TransitGateway: EC2AnalysisComponent | None = None
    TransitGatewayRouteTable: EC2AnalysisComponent | None = None
    TransitGatewayRouteTableRoute: EC2TransitGatewayRouteTableRoute | None = None
    TransitGatewayPolicyTable: EC2AnalysisComponent | None = None
    TransitGatewayPolicyTableEntry: EC2AnalysisTransitGatewayPolicyTableEntry | None = None
    TransitGatewayAttachment: EC2AnalysisComponent | None = None
    ComponentAccount: StrictStr | None = None
    ComponentRegion: StrictStr | None = None
    FirewallStatelessRule: EC2FirewallStatelessRule | None = None
    FirewallStatefulRule: EC2FirewallStatefulRule | None = None
