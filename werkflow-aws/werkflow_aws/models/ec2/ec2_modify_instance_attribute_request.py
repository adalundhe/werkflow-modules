from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_attribute_boolean_value import EC2AttributeBooleanValue
from .ec2_attribute_value import EC2AttributeValue
from .ec2_enclave_options_request import EC2EnclaveOptionsRequest
from .ec2_instance_block_device_mapping_specification import EC2InstanceBlockDeviceMappingSpecification
from .ec2_secure_blob_attribute_value import EC2SecureBlobAttributeValue


class EC2ModifyInstanceAttributeRequest(BaseModel):
    InstanceId: StrictStr
    SourceDestCheck: EC2AttributeBooleanValue | None = None
    EnclaveOptions: EC2EnclaveOptionsRequest | None = None
    DisableApiStop: EC2AttributeBooleanValue | None = None
    DryRun: StrictBool | None = None
    Attribute: Literal['instanceType', 'kernel', 'ramdisk', 'userData', 'disableApiTermination', 'instanceInitiatedShutdownBehavior', 'rootDeviceName', 'blockDeviceMapping', 'productCodes', 'sourceDestCheck', 'groupSet', 'ebsOptimized', 'sriovNetSupport', 'enaSupport', 'enclaveOptions', 'disableApiStop'] | None = None
    Value: StrictStr | None = None
    BlockDeviceMappings: list[EC2InstanceBlockDeviceMappingSpecification] | None = None
    DisableApiTermination: EC2AttributeBooleanValue | None = None
    InstanceType: EC2AttributeValue | None = None
    Kernel: EC2AttributeValue | None = None
    Ramdisk: EC2AttributeValue | None = None
    UserData: EC2SecureBlobAttributeValue | None = None
    InstanceInitiatedShutdownBehavior: EC2AttributeValue | None = None
    Groups: list[StrictStr] | None = None
    EbsOptimized: EC2AttributeBooleanValue | None = None
    SriovNetSupport: EC2AttributeValue | None = None
    EnaSupport: EC2AttributeBooleanValue | None = None
