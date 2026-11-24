from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ServiceCatalogCodeStarParameters(BaseModel):
    ConnectionArn: StrictStr | None = None
    Repository: StrictStr | None = None
    Branch: StrictStr | None = None
    ArtifactPath: StrictStr | None = None
