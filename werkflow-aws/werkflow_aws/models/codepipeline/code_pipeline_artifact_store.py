from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_encryption_key import CodePipelineEncryptionKey


class CodePipelineArtifactStore(BaseModel):
    type: StrictStr | None = None
    location: StrictStr | None = None
    encryptionKey: CodePipelineEncryptionKey | None = None
