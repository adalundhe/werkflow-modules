from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeArtifactPackageDependency(BaseModel):
    namespace: StrictStr | None = None
    package: StrictStr | None = None
    dependencyType: StrictStr | None = None
    versionRequirement: StrictStr | None = None
