from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ecs_accelerator_count_request import ECSAcceleratorCountRequest
from .ecs_accelerator_total_memory_mi_b_request import ECSAcceleratorTotalMemoryMiBRequest
from .ecs_baseline_ebs_bandwidth_mbps_request import ECSBaselineEbsBandwidthMbpsRequest
from .ecs_memory_gi_b_per_v_cpu_request import ECSMemoryGiBPerVCpuRequest
from .ecs_memory_mi_b_request import ECSMemoryMiBRequest
from .ecs_network_bandwidth_gbps_request import ECSNetworkBandwidthGbpsRequest
from .ecs_network_interface_count_request import ECSNetworkInterfaceCountRequest
from .ecs_total_local_storage_gb_request import ECSTotalLocalStorageGBRequest
from .ecsv_cpu_count_range_request import ECSVCpuCountRangeRequest


class ECSInstanceRequirementsRequest(BaseModel):
    vCpuCount: ECSVCpuCountRangeRequest | None = None
    memoryMiB: ECSMemoryMiBRequest | None = None
    cpuManufacturers: list[StrictStr] | None = None
    memoryGiBPerVCpu: ECSMemoryGiBPerVCpuRequest | None = None
    excludedInstanceTypes: list[StrictStr] | None = None
    instanceGenerations: list[StrictStr] | None = None
    spotMaxPricePercentageOverLowestPrice: StrictInt | None = None
    onDemandMaxPricePercentageOverLowestPrice: StrictInt | None = None
    bareMetal: StrictStr | None = None
    burstablePerformance: StrictStr | None = None
    requireHibernateSupport: StrictBool | None = None
    networkInterfaceCount: ECSNetworkInterfaceCountRequest | None = None
    localStorage: StrictStr | None = None
    localStorageTypes: list[StrictStr] | None = None
    totalLocalStorageGB: ECSTotalLocalStorageGBRequest | None = None
    baselineEbsBandwidthMbps: ECSBaselineEbsBandwidthMbpsRequest | None = None
    acceleratorTypes: list[StrictStr] | None = None
    acceleratorCount: ECSAcceleratorCountRequest | None = None
    acceleratorManufacturers: list[StrictStr] | None = None
    acceleratorNames: list[StrictStr] | None = None
    acceleratorTotalMemoryMiB: ECSAcceleratorTotalMemoryMiBRequest | None = None
    networkBandwidthGbps: ECSNetworkBandwidthGbpsRequest | None = None
    allowedInstanceTypes: list[StrictStr] | None = None
    maxSpotPriceAsPercentageOfOptimalOnDemandPrice: StrictInt | None = None
