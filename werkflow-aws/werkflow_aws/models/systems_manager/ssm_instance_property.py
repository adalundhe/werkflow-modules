from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_instance_aggregated_association_overview import SSMInstanceAggregatedAssociationOverview


class SSMInstanceProperty(BaseModel):
    Name: StrictStr | None = None
    InstanceId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    InstanceRole: StrictStr | None = None
    KeyName: StrictStr | None = None
    InstanceState: StrictStr | None = None
    Architecture: StrictStr | None = None
    IPAddress: StrictStr | None = None
    LaunchTime: datetime.datetime | StrictStr | None = None
    PingStatus: StrictStr | None = None
    LastPingDateTime: datetime.datetime | StrictStr | None = None
    AgentVersion: StrictStr | None = None
    PlatformType: StrictStr | None = None
    PlatformName: StrictStr | None = None
    PlatformVersion: StrictStr | None = None
    ActivationId: StrictStr | None = None
    IamRole: StrictStr | None = None
    RegistrationDate: datetime.datetime | StrictStr | None = None
    ResourceType: StrictStr | None = None
    ComputerName: StrictStr | None = None
    AssociationStatus: StrictStr | None = None
    LastAssociationExecutionDate: datetime.datetime | StrictStr | None = None
    LastSuccessfulAssociationExecutionDate: datetime.datetime | StrictStr | None = None
    AssociationOverview: SSMInstanceAggregatedAssociationOverview | None = None
    SourceId: StrictStr | None = None
    SourceType: StrictStr | None = None
    SourceLocation: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
