from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .sage_maker_accelerator_partition_config import SageMakerAcceleratorPartitionConfig


class SageMakerComputeQuotaResourceConfig(BaseModel):
    InstanceType: StrictStr | None = None
    Count: StrictInt | None = None
    Accelerators: StrictInt | None = None
    VCpu: StrictFloat | StrictInt | None = None
    MemoryInGiB: StrictFloat | StrictInt | None = None
    AcceleratorPartition: SageMakerAcceleratorPartitionConfig | None = None
