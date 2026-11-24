from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_mac_system_integrity_protection_configuration_request import EC2MacSystemIntegrityProtectionConfigurationRequest
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateMacSystemIntegrityProtectionModificationTaskRequest(BaseModel):
    InstanceId: StrictStr
    MacSystemIntegrityProtectionStatus: Literal['enabled', 'disabled']
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    MacCredentials: StrictStr | None = None
    MacSystemIntegrityProtectionConfiguration: EC2MacSystemIntegrityProtectionConfigurationRequest | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
