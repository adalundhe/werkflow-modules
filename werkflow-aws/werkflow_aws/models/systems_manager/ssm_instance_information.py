from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .ssm_instance_aggregated_association_overview import SSMInstanceAggregatedAssociationOverview


class SSMInstanceInformation(BaseModel):
    InstanceId: StrictStr | None = None
    PingStatus: StrictStr | None = None
    LastPingDateTime: datetime.datetime | StrictStr | None = None
    AgentVersion: StrictStr | None = None
    IsLatestVersion: StrictBool | None = None
    PlatformType: StrictStr | None = None
    PlatformName: StrictStr | None = None
    PlatformVersion: StrictStr | None = None
    ActivationId: StrictStr | None = None
    IamRole: StrictStr | None = None
    RegistrationDate: datetime.datetime | StrictStr | None = None
    ResourceType: StrictStr | None = None
    Name: StrictStr | None = None
    IPAddress: StrictStr | None = None
    ComputerName: StrictStr | None = None
    AssociationStatus: StrictStr | None = None
    LastAssociationExecutionDate: datetime.datetime | StrictStr | None = None
    LastSuccessfulAssociationExecutionDate: datetime.datetime | StrictStr | None = None
    AssociationOverview: SSMInstanceAggregatedAssociationOverview | None = None
    SourceId: StrictStr | None = None
    SourceType: StrictStr | None = None
    SourceLocation: StrictStr | None = None
