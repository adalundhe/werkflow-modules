from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .neptune_tag import NeptuneTag


class NeptuneCopyDBClusterSnapshotRequest(BaseModel):
    SourceDBClusterSnapshotIdentifier: StrictStr
    TargetDBClusterSnapshotIdentifier: StrictStr
    KmsKeyId: StrictStr | None = None
    PreSignedUrl: StrictStr | None = None
    CopyTags: StrictBool | None = None
    Tags: list[NeptuneTag] | None = None
    SourceRegion: StrictStr | None = None
