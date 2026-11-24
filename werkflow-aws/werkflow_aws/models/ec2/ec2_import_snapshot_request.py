from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_client_data import EC2ClientData
from .ec2_snapshot_disk_container import EC2SnapshotDiskContainer
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2ImportSnapshotRequest(BaseModel):
    ClientData: EC2ClientData | None = None
    ClientToken: StrictStr | None = None
    Description: StrictStr | None = None
    DiskContainer: EC2SnapshotDiskContainer | None = None
    DryRun: StrictBool | None = None
    Encrypted: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    RoleName: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
