from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MacieResourceProfileArtifact(BaseModel):
    arn: StrictStr | None = None
    classificationResultStatus: StrictStr | None = None
    sensitive: StrictBool | None = None
