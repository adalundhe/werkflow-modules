from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_elb_load_balancer_attributes import SecurityHubAwsElbLoadBalancerAttributes
from .security_hub_aws_elb_load_balancer_backend_server_description import SecurityHubAwsElbLoadBalancerBackendServerDescription
from .security_hub_aws_elb_load_balancer_health_check import SecurityHubAwsElbLoadBalancerHealthCheck
from .security_hub_aws_elb_load_balancer_instance import SecurityHubAwsElbLoadBalancerInstance
from .security_hub_aws_elb_load_balancer_listener_description import SecurityHubAwsElbLoadBalancerListenerDescription
from .security_hub_aws_elb_load_balancer_policies import SecurityHubAwsElbLoadBalancerPolicies
from .security_hub_aws_elb_load_balancer_source_security_group import SecurityHubAwsElbLoadBalancerSourceSecurityGroup


class SecurityHubAwsElbLoadBalancerDetails(BaseModel):
    AvailabilityZones: list[StrictStr] | None = None
    BackendServerDescriptions: list[SecurityHubAwsElbLoadBalancerBackendServerDescription] | None = None
    CanonicalHostedZoneName: StrictStr | None = None
    CanonicalHostedZoneNameID: StrictStr | None = None
    CreatedTime: StrictStr | None = None
    DnsName: StrictStr | None = None
    HealthCheck: SecurityHubAwsElbLoadBalancerHealthCheck | None = None
    Instances: list[SecurityHubAwsElbLoadBalancerInstance] | None = None
    ListenerDescriptions: list[SecurityHubAwsElbLoadBalancerListenerDescription] | None = None
    LoadBalancerAttributes: SecurityHubAwsElbLoadBalancerAttributes | None = None
    LoadBalancerName: StrictStr | None = None
    Policies: SecurityHubAwsElbLoadBalancerPolicies | None = None
    Scheme: StrictStr | None = None
    SecurityGroups: list[StrictStr] | None = None
    SourceSecurityGroup: SecurityHubAwsElbLoadBalancerSourceSecurityGroup | None = None
    Subnets: list[StrictStr] | None = None
    VpcId: StrictStr | None = None
