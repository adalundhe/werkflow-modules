from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactPackageGroupReference(BaseModel):
    arn: StrictStr | None = None
    pattern: StrictStr | None = None
