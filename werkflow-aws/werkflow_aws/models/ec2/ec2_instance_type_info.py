from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_ebs_info import EC2EbsInfo
from .ec2_fpga_info import EC2FpgaInfo
from .ec2_gpu_info import EC2GpuInfo
from .ec2_inference_accelerator_info import EC2InferenceAcceleratorInfo
from .ec2_instance_storage_info import EC2InstanceStorageInfo
from .ec2_media_accelerator_info import EC2MediaAcceleratorInfo
from .ec2_memory_info import EC2MemoryInfo
from .ec2_network_info import EC2NetworkInfo
from .ec2_neuron_info import EC2NeuronInfo
from .ec2_nitro_tpm_info import EC2NitroTpmInfo
from .ec2_placement_group_info import EC2PlacementGroupInfo
from .ec2_processor_info import EC2ProcessorInfo
from .ec2_v_cpu_info import EC2VCpuInfo


class EC2InstanceTypeInfo(BaseModel):
    InstanceType: StrictStr | None = None
    CurrentGeneration: StrictBool | None = None
    FreeTierEligible: StrictBool | None = None
    SupportedUsageClasses: list[StrictStr] | None = None
    SupportedRootDeviceTypes: list[StrictStr] | None = None
    SupportedVirtualizationTypes: list[StrictStr] | None = None
    BareMetal: StrictBool | None = None
    Hypervisor: StrictStr | None = None
    ProcessorInfo: EC2ProcessorInfo | None = None
    VCpuInfo: EC2VCpuInfo | None = None
    MemoryInfo: EC2MemoryInfo | None = None
    InstanceStorageSupported: StrictBool | None = None
    InstanceStorageInfo: EC2InstanceStorageInfo | None = None
    EbsInfo: EC2EbsInfo | None = None
    NetworkInfo: EC2NetworkInfo | None = None
    GpuInfo: EC2GpuInfo | None = None
    FpgaInfo: EC2FpgaInfo | None = None
    PlacementGroupInfo: EC2PlacementGroupInfo | None = None
    InferenceAcceleratorInfo: EC2InferenceAcceleratorInfo | None = None
    HibernationSupported: StrictBool | None = None
    BurstablePerformanceSupported: StrictBool | None = None
    DedicatedHostsSupported: StrictBool | None = None
    AutoRecoverySupported: StrictBool | None = None
    SupportedBootModes: list[StrictStr] | None = None
    NitroEnclavesSupport: StrictStr | None = None
    NitroTpmSupport: StrictStr | None = None
    NitroTpmInfo: EC2NitroTpmInfo | None = None
    MediaAcceleratorInfo: EC2MediaAcceleratorInfo | None = None
    NeuronInfo: EC2NeuronInfo | None = None
    PhcSupport: StrictStr | None = None
    RebootMigrationSupport: StrictStr | None = None
    SupportedInRegion: StrictBool | None = None
