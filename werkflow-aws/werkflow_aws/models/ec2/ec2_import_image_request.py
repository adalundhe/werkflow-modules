from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_client_data import EC2ClientData
from .ec2_image_disk_container import EC2ImageDiskContainer
from .ec2_import_image_license_configuration_request import EC2ImportImageLicenseConfigurationRequest
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2ImportImageRequest(BaseModel):
    Architecture: StrictStr | None = None
    ClientData: EC2ClientData | None = None
    ClientToken: StrictStr | None = None
    Description: StrictStr | None = None
    DiskContainers: list[EC2ImageDiskContainer] | None = None
    DryRun: StrictBool | None = None
    Encrypted: StrictBool | None = None
    Hypervisor: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    LicenseType: StrictStr | None = None
    Platform: StrictStr | None = None
    RoleName: StrictStr | None = None
    LicenseSpecifications: list[EC2ImportImageLicenseConfigurationRequest] | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    UsageOperation: StrictStr | None = None
    BootMode: Literal['legacy-bios', 'uefi', 'uefi-preferred'] | None = None
