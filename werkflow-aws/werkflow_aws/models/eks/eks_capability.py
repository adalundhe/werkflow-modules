from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .eks_capability_configuration_response import EKSCapabilityConfigurationResponse
from .eks_capability_health import EKSCapabilityHealth


class EKSCapability(BaseModel):
    capabilityName: StrictStr | None = None
    arn: StrictStr | None = None
    clusterName: StrictStr | None = None
    type: StrictStr | None = None
    roleArn: StrictStr | None = None
    status: StrictStr | None = None
    version: StrictStr | None = None
    configuration: EKSCapabilityConfigurationResponse | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    health: EKSCapabilityHealth | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    modifiedAt: datetime.datetime | StrictStr | None = None
    deletePropagationPolicy: StrictStr | None = None
