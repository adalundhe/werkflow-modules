from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerHubContentDependency(BaseModel):
    DependencyOriginPath: StrictStr | None = None
    DependencyCopyPath: StrictStr | None = None
