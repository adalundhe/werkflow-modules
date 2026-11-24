from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_block_device_mapping import EC2BlockDeviceMapping
from .ec2_image_watermark import EC2ImageWatermark
from .ec2_instance_type_specification import EC2InstanceTypeSpecification
from .ec2_product_code import EC2ProductCode
from .ec2_scan_results import EC2ScanResults
from .ec2_state_reason import EC2StateReason
from .ec2_tag_model import EC2TagModel


class EC2Image(BaseModel):
    PlatformDetails: StrictStr | None = None
    UsageOperation: StrictStr | None = None
    BlockDeviceMappings: list[EC2BlockDeviceMapping] | None = None
    Description: StrictStr | None = None
    EnaSupport: StrictBool | None = None
    Hypervisor: StrictStr | None = None
    ImageOwnerAlias: StrictStr | None = None
    Name: StrictStr | None = None
    RootDeviceName: StrictStr | None = None
    RootDeviceType: StrictStr | None = None
    SriovNetSupport: StrictStr | None = None
    StateReason: EC2StateReason | None = None
    Tags: list[EC2TagModel] | None = None
    VirtualizationType: StrictStr | None = None
    BootMode: StrictStr | None = None
    TpmSupport: StrictStr | None = None
    DeprecationTime: StrictStr | None = None
    ImdsSupport: StrictStr | None = None
    SourceInstanceId: StrictStr | None = None
    DeregistrationProtection: StrictStr | None = None
    LastLaunchedTime: StrictStr | None = None
    ImageAllowed: StrictBool | None = None
    SourceImageId: StrictStr | None = None
    SourceImageRegion: StrictStr | None = None
    FreeTierEligible: StrictBool | None = None
    PublicSsmParameterName: StrictStr | None = None
    ImageWatermarks: list[EC2ImageWatermark] | None = None
    ScanResults: EC2ScanResults | None = None
    InstanceTypeSpecification: EC2InstanceTypeSpecification | None = None
    ImageId: StrictStr | None = None
    ImageLocation: StrictStr | None = None
    State: StrictStr | None = None
    OwnerId: StrictStr | None = None
    CreationDate: StrictStr | None = None
    Public: StrictBool | None = None
    ProductCodes: list[EC2ProductCode] | None = None
    Architecture: StrictStr | None = None
    ImageType: StrictStr | None = None
    KernelId: StrictStr | None = None
    RamdiskId: StrictStr | None = None
    Platform: StrictStr | None = None
