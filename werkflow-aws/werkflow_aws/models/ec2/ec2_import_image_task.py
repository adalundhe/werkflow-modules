from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_import_image_license_configuration_response import EC2ImportImageLicenseConfigurationResponse
from .ec2_snapshot_detail import EC2SnapshotDetail
from .ec2_tag_model import EC2TagModel


class EC2ImportImageTask(BaseModel):
    Architecture: StrictStr | None = None
    Description: StrictStr | None = None
    Encrypted: StrictBool | None = None
    Hypervisor: StrictStr | None = None
    ImageId: StrictStr | None = None
    ImportTaskId: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    LicenseType: StrictStr | None = None
    Platform: StrictStr | None = None
    Progress: StrictStr | None = None
    SnapshotDetails: list[EC2SnapshotDetail] | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    LicenseSpecifications: list[EC2ImportImageLicenseConfigurationResponse] | None = None
    UsageOperation: StrictStr | None = None
    BootMode: StrictStr | None = None
