from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_association_overview import SSMAssociationOverview
from .ssm_target import SSMTarget


class SSMAssociation(BaseModel):
    Name: StrictStr | None = None
    InstanceId: StrictStr | None = None
    AssociationId: StrictStr | None = None
    AssociationVersion: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    Targets: list[SSMTarget] | None = None
    LastExecutionDate: datetime.datetime | StrictStr | None = None
    Overview: SSMAssociationOverview | None = None
    ScheduleExpression: StrictStr | None = None
    AssociationName: StrictStr | None = None
    ScheduleOffset: StrictInt | None = None
    Duration: StrictInt | None = None
    TargetMaps: list[dict[StrictStr, list[StrictStr]]] | None = None
