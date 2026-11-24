from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_attribute_boolean_value import EC2AttributeBooleanValue
from .ec2_attribute_value import EC2AttributeValue
from .ec2_enclave_options import EC2EnclaveOptions
from .ec2_group_identifier_model import EC2GroupIdentifierModel
from .ec2_instance_block_device_mapping import EC2InstanceBlockDeviceMapping
from .ec2_product_code import EC2ProductCode


class EC2DescribeInstanceAttributeResponse(BaseModel):
    BlockDeviceMappings: list[EC2InstanceBlockDeviceMapping] | None = None
    DisableApiTermination: EC2AttributeBooleanValue | None = None
    EnaSupport: EC2AttributeBooleanValue | None = None
    EnclaveOptions: EC2EnclaveOptions | None = None
    EbsOptimized: EC2AttributeBooleanValue | None = None
    InstanceId: StrictStr | None = None
    InstanceInitiatedShutdownBehavior: EC2AttributeValue | None = None
    InstanceType: EC2AttributeValue | None = None
    KernelId: EC2AttributeValue | None = None
    ProductCodes: list[EC2ProductCode] | None = None
    RamdiskId: EC2AttributeValue | None = None
    RootDeviceName: EC2AttributeValue | None = None
    SourceDestCheck: EC2AttributeBooleanValue | None = None
    SriovNetSupport: EC2AttributeValue | None = None
    UserData: EC2AttributeValue | None = None
    DisableApiStop: EC2AttributeBooleanValue | None = None
    Groups: list[EC2GroupIdentifierModel] | None = None
    ResponseMetadata: dict[str, Any] | None = None
