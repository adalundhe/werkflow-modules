from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .cloud_formation_physical_resource_id_context_key_value_pair import CloudFormationPhysicalResourceIdContextKeyValuePair
from .cloud_formation_property_difference import CloudFormationPropertyDifference


class CloudFormationStackInstanceResourceDriftsSummary(BaseModel):
    StackId: StrictStr | None = None
    LogicalResourceId: StrictStr | None = None
    PhysicalResourceId: StrictStr | None = None
    PhysicalResourceIdContext: list[CloudFormationPhysicalResourceIdContextKeyValuePair] | None = None
    ResourceType: StrictStr | None = None
    PropertyDifferences: list[CloudFormationPropertyDifference] | None = None
    StackResourceDriftStatus: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
