from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeGuruCodeArtifacts(BaseModel):
    SourceCodeArtifactsObjectKey: StrictStr | None = None
    BuildArtifactsObjectKey: StrictStr | None = None
