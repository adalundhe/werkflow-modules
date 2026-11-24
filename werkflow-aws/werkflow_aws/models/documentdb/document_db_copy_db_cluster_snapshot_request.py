from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .document_db_tag import DocumentDBTag


class DocumentDBCopyDBClusterSnapshotRequest(BaseModel):
    SourceDBClusterSnapshotIdentifier: StrictStr
    TargetDBClusterSnapshotIdentifier: StrictStr
    KmsKeyId: StrictStr | None = None
    PreSignedUrl: StrictStr | None = None
    CopyTags: StrictBool | None = None
    Tags: list[DocumentDBTag] | None = None
    SourceRegion: StrictStr | None = None
