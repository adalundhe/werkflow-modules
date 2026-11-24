from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_accelerator_count_request import EC2AcceleratorCountRequest
from .ec2_accelerator_total_memory_mi_b_request import EC2AcceleratorTotalMemoryMiBRequest
from .ec2_baseline_ebs_bandwidth_mbps_request import EC2BaselineEbsBandwidthMbpsRequest
from .ec2_baseline_performance_factors_request import EC2BaselinePerformanceFactorsRequest
from .ec2_memory_gi_b_per_v_cpu_request import EC2MemoryGiBPerVCpuRequest
from .ec2_memory_mi_b_request import EC2MemoryMiBRequest
from .ec2_network_bandwidth_gbps_request import EC2NetworkBandwidthGbpsRequest
from .ec2_network_interface_count_request import EC2NetworkInterfaceCountRequest
from .ec2_total_local_storage_gb_request import EC2TotalLocalStorageGBRequest
from .ec2_v_cpu_count_range_request import EC2VCpuCountRangeRequest


class EC2InstanceRequirementsRequest(BaseModel):
    VCpuCount: EC2VCpuCountRangeRequest | None = None
    MemoryMiB: EC2MemoryMiBRequest | None = None
    CpuManufacturers: list[StrictStr] | None = None
    MemoryGiBPerVCpu: EC2MemoryGiBPerVCpuRequest | None = None
    ExcludedInstanceTypes: list[StrictStr] | None = None
    InstanceGenerations: list[StrictStr] | None = None
    SpotMaxPricePercentageOverLowestPrice: StrictInt | None = None
    OnDemandMaxPricePercentageOverLowestPrice: StrictInt | None = None
    BareMetal: StrictStr | None = None
    BurstablePerformance: StrictStr | None = None
    RequireHibernateSupport: StrictBool | None = None
    NetworkInterfaceCount: EC2NetworkInterfaceCountRequest | None = None
    LocalStorage: StrictStr | None = None
    LocalStorageTypes: list[StrictStr] | None = None
    TotalLocalStorageGB: EC2TotalLocalStorageGBRequest | None = None
    BaselineEbsBandwidthMbps: EC2BaselineEbsBandwidthMbpsRequest | None = None
    AcceleratorTypes: list[StrictStr] | None = None
    AcceleratorCount: EC2AcceleratorCountRequest | None = None
    AcceleratorManufacturers: list[StrictStr] | None = None
    AcceleratorNames: list[StrictStr] | None = None
    AcceleratorTotalMemoryMiB: EC2AcceleratorTotalMemoryMiBRequest | None = None
    NetworkBandwidthGbps: EC2NetworkBandwidthGbpsRequest | None = None
    AllowedInstanceTypes: list[StrictStr] | None = None
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: StrictInt | None = None
    BaselinePerformanceFactors: EC2BaselinePerformanceFactorsRequest | None = None
    RequireEncryptionInTransit: StrictBool | None = None
