from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_commit_blob_metadata import CodeCommitBlobMetadata


class CodeCommitDifference(BaseModel):
    beforeBlob: CodeCommitBlobMetadata | None = None
    afterBlob: CodeCommitBlobMetadata | None = None
    changeType: StrictStr | None = None
