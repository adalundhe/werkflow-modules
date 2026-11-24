from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactAssociatedPackage(BaseModel):
    format: StrictStr | None = None
    namespace: StrictStr | None = None
    package: StrictStr | None = None
    associationType: StrictStr | None = None
