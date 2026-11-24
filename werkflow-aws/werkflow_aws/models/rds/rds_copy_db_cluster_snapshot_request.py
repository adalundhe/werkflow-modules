from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCopyDBClusterSnapshotRequest(BaseModel):
    SourceDBClusterSnapshotIdentifier: StrictStr
    TargetDBClusterSnapshotIdentifier: StrictStr
    KmsKeyId: StrictStr | None = None
    PreSignedUrl: StrictStr | None = None
    CopyTags: StrictBool | None = None
    Tags: list[RDSTagModel] | None = None
    SourceRegion: StrictStr | None = None
