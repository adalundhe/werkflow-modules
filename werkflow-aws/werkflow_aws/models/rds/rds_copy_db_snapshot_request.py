from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_tag_model import RDSTagModel
from .rds_tag_specification_model import RDSTagSpecificationModel


class RDSCopyDBSnapshotRequest(BaseModel):
    SourceDBSnapshotIdentifier: StrictStr
    TargetDBSnapshotIdentifier: StrictStr
    KmsKeyId: StrictStr | None = None
    Tags: list[RDSTagModel] | None = None
    CopyTags: StrictBool | None = None
    PreSignedUrl: StrictStr | None = None
    OptionGroupName: StrictStr | None = None
    TargetCustomAvailabilityZone: StrictStr | None = None
    SnapshotTarget: StrictStr | None = None
    CopyOptionGroup: StrictBool | None = None
    SnapshotAvailabilityZone: StrictStr | None = None
    TagSpecifications: list[RDSTagSpecificationModel] | None = None
    SourceRegion: StrictStr | None = None
