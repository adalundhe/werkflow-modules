from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .auto_scaling_accelerator_count_request import AutoScalingAcceleratorCountRequest
from .auto_scaling_accelerator_total_memory_mi_b_request import AutoScalingAcceleratorTotalMemoryMiBRequest
from .auto_scaling_baseline_ebs_bandwidth_mbps_request import AutoScalingBaselineEbsBandwidthMbpsRequest
from .auto_scaling_baseline_performance_factors_request import AutoScalingBaselinePerformanceFactorsRequest
from .auto_scaling_memory_gi_b_per_v_cpu_request import AutoScalingMemoryGiBPerVCpuRequest
from .auto_scaling_memory_mi_b_request import AutoScalingMemoryMiBRequest
from .auto_scaling_network_bandwidth_gbps_request import AutoScalingNetworkBandwidthGbpsRequest
from .auto_scaling_network_interface_count_request import AutoScalingNetworkInterfaceCountRequest
from .auto_scaling_total_local_storage_gb_request import AutoScalingTotalLocalStorageGBRequest
from .auto_scaling_v_cpu_count_request import AutoScalingVCpuCountRequest


class AutoScalingInstanceRequirements(BaseModel):
    VCpuCount: AutoScalingVCpuCountRequest | None = None
    MemoryMiB: AutoScalingMemoryMiBRequest | None = None
    CpuManufacturers: list[StrictStr] | None = None
    MemoryGiBPerVCpu: AutoScalingMemoryGiBPerVCpuRequest | None = None
    ExcludedInstanceTypes: list[StrictStr] | None = None
    InstanceGenerations: list[StrictStr] | None = None
    SpotMaxPricePercentageOverLowestPrice: StrictInt | None = None
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: StrictInt | None = None
    OnDemandMaxPricePercentageOverLowestPrice: StrictInt | None = None
    BareMetal: StrictStr | None = None
    BurstablePerformance: StrictStr | None = None
    RequireHibernateSupport: StrictBool | None = None
    NetworkInterfaceCount: AutoScalingNetworkInterfaceCountRequest | None = None
    LocalStorage: StrictStr | None = None
    LocalStorageTypes: list[StrictStr] | None = None
    TotalLocalStorageGB: AutoScalingTotalLocalStorageGBRequest | None = None
    BaselineEbsBandwidthMbps: AutoScalingBaselineEbsBandwidthMbpsRequest | None = None
    AcceleratorTypes: list[StrictStr] | None = None
    AcceleratorCount: AutoScalingAcceleratorCountRequest | None = None
    AcceleratorManufacturers: list[StrictStr] | None = None
    AcceleratorNames: list[StrictStr] | None = None
    AcceleratorTotalMemoryMiB: AutoScalingAcceleratorTotalMemoryMiBRequest | None = None
    NetworkBandwidthGbps: AutoScalingNetworkBandwidthGbpsRequest | None = None
    AllowedInstanceTypes: list[StrictStr] | None = None
    BaselinePerformanceFactors: AutoScalingBaselinePerformanceFactorsRequest | None = None
