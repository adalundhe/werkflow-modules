from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_additional_detail import EC2AdditionalDetail
from .ec2_analysis_acl_rule import EC2AnalysisAclRule
from .ec2_analysis_component import EC2AnalysisComponent
from .ec2_analysis_packet_header import EC2AnalysisPacketHeader
from .ec2_analysis_route_table_route import EC2AnalysisRouteTableRoute
from .ec2_analysis_security_group_rule import EC2AnalysisSecurityGroupRule
from .ec2_analysis_transit_gateway_policy_table_entry import EC2AnalysisTransitGatewayPolicyTableEntry
from .ec2_explanation import EC2Explanation
from .ec2_firewall_stateful_rule import EC2FirewallStatefulRule
from .ec2_firewall_stateless_rule import EC2FirewallStatelessRule
from .ec2_transit_gateway_route_table_route import EC2TransitGatewayRouteTableRoute


class EC2PathComponent(BaseModel):
    SequenceNumber: StrictInt | None = None
    AclRule: EC2AnalysisAclRule | None = None
    AttachedTo: EC2AnalysisComponent | None = None
    Component: EC2AnalysisComponent | None = None
    DestinationVpc: EC2AnalysisComponent | None = None
    OutboundHeader: EC2AnalysisPacketHeader | None = None
    InboundHeader: EC2AnalysisPacketHeader | None = None
    RouteTableRoute: EC2AnalysisRouteTableRoute | None = None
    SecurityGroupRule: EC2AnalysisSecurityGroupRule | None = None
    SourceVpc: EC2AnalysisComponent | None = None
    Subnet: EC2AnalysisComponent | None = None
    Vpc: EC2AnalysisComponent | None = None
    AdditionalDetails: list[EC2AdditionalDetail] | None = None
    TransitGateway: EC2AnalysisComponent | None = None
    TransitGatewayRouteTableRoute: EC2TransitGatewayRouteTableRoute | None = None
    TransitGatewayPolicyTableEntry: EC2AnalysisTransitGatewayPolicyTableEntry | None = None
    Explanations: list[EC2Explanation] | None = None
    ElasticLoadBalancerListener: EC2AnalysisComponent | None = None
    FirewallStatelessRule: EC2FirewallStatelessRule | None = None
    FirewallStatefulRule: EC2FirewallStatefulRule | None = None
    ServiceName: StrictStr | None = None
