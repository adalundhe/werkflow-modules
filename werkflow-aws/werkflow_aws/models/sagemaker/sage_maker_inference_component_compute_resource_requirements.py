from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class SageMakerInferenceComponentComputeResourceRequirements(BaseModel):
    NumberOfCpuCoresRequired: StrictFloat | StrictInt | None = None
    NumberOfAcceleratorDevicesRequired: StrictFloat | StrictInt | None = None
    MinMemoryRequiredInMb: StrictInt | None = None
    MaxMemoryRequiredInMb: StrictInt | None = None
    AcceleratorPartitionType: StrictStr | None = None
