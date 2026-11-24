from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_disk_resource_utilization import CostExplorerDiskResourceUtilization
from .cost_explorer_ebs_resource_utilization import CostExplorerEBSResourceUtilization
from .cost_explorer_network_resource_utilization import CostExplorerNetworkResourceUtilization


class CostExplorerEC2ResourceUtilization(BaseModel):
    MaxCpuUtilizationPercentage: StrictStr | None = None
    MaxMemoryUtilizationPercentage: StrictStr | None = None
    MaxStorageUtilizationPercentage: StrictStr | None = None
    EBSResourceUtilization: CostExplorerEBSResourceUtilization | None = None
    DiskResourceUtilization: CostExplorerDiskResourceUtilization | None = None
    NetworkResourceUtilization: CostExplorerNetworkResourceUtilization | None = None
