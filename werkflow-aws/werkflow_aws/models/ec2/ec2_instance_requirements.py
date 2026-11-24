from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_accelerator_count import EC2AcceleratorCount
from .ec2_accelerator_total_memory_mi_b import EC2AcceleratorTotalMemoryMiB
from .ec2_baseline_ebs_bandwidth_mbps import EC2BaselineEbsBandwidthMbps
from .ec2_baseline_performance_factors import EC2BaselinePerformanceFactors
from .ec2_memory_gi_b_per_v_cpu import EC2MemoryGiBPerVCpu
from .ec2_memory_mi_b import EC2MemoryMiB
from .ec2_network_bandwidth_gbps import EC2NetworkBandwidthGbps
from .ec2_network_interface_count import EC2NetworkInterfaceCount
from .ec2_total_local_storage_gb import EC2TotalLocalStorageGB
from .ec2_v_cpu_count_range import EC2VCpuCountRange


class EC2InstanceRequirements(BaseModel):
    VCpuCount: EC2VCpuCountRange | None = None
    MemoryMiB: EC2MemoryMiB | None = None
    CpuManufacturers: list[StrictStr] | None = None
    MemoryGiBPerVCpu: EC2MemoryGiBPerVCpu | None = None
    ExcludedInstanceTypes: list[StrictStr] | None = None
    InstanceGenerations: list[StrictStr] | None = None
    SpotMaxPricePercentageOverLowestPrice: StrictInt | None = None
    OnDemandMaxPricePercentageOverLowestPrice: StrictInt | None = None
    BareMetal: StrictStr | None = None
    BurstablePerformance: StrictStr | None = None
    RequireHibernateSupport: StrictBool | None = None
    NetworkInterfaceCount: EC2NetworkInterfaceCount | None = None
    LocalStorage: StrictStr | None = None
    LocalStorageTypes: list[StrictStr] | None = None
    TotalLocalStorageGB: EC2TotalLocalStorageGB | None = None
    BaselineEbsBandwidthMbps: EC2BaselineEbsBandwidthMbps | None = None
    AcceleratorTypes: list[StrictStr] | None = None
    AcceleratorCount: EC2AcceleratorCount | None = None
    AcceleratorManufacturers: list[StrictStr] | None = None
    AcceleratorNames: list[StrictStr] | None = None
    AcceleratorTotalMemoryMiB: EC2AcceleratorTotalMemoryMiB | None = None
    NetworkBandwidthGbps: EC2NetworkBandwidthGbps | None = None
    AllowedInstanceTypes: list[StrictStr] | None = None
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: StrictInt | None = None
    BaselinePerformanceFactors: EC2BaselinePerformanceFactors | None = None
    RequireEncryptionInTransit: StrictBool | None = None
