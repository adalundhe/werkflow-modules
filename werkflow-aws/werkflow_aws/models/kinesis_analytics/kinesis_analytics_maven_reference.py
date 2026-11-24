from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsMavenReference(BaseModel):
    GroupId: StrictStr | None = None
    ArtifactId: StrictStr | None = None
    Version: StrictStr | None = None
