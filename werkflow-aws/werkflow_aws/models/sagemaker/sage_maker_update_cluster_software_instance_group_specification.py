from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerUpdateClusterSoftwareInstanceGroupSpecification(BaseModel):
    InstanceGroupName: StrictStr
    ImageReleaseVersion: StrictStr | None = None
