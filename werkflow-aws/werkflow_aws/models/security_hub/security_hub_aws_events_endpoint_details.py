from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_events_endpoint_event_buses_details import SecurityHubAwsEventsEndpointEventBusesDetails
from .security_hub_aws_events_endpoint_replication_config_details import SecurityHubAwsEventsEndpointReplicationConfigDetails
from .security_hub_aws_events_endpoint_routing_config_details import SecurityHubAwsEventsEndpointRoutingConfigDetails


class SecurityHubAwsEventsEndpointDetails(BaseModel):
    Arn: StrictStr | None = None
    Description: StrictStr | None = None
    EndpointId: StrictStr | None = None
    EndpointUrl: StrictStr | None = None
    EventBuses: list[SecurityHubAwsEventsEndpointEventBusesDetails] | None = None
    Name: StrictStr | None = None
    ReplicationConfig: SecurityHubAwsEventsEndpointReplicationConfigDetails | None = None
    RoleArn: StrictStr | None = None
    RoutingConfig: SecurityHubAwsEventsEndpointRoutingConfigDetails | None = None
    State: StrictStr | None = None
    StateReason: StrictStr | None = None
