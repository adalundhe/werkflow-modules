from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECRImageReferrer(BaseModel):
    digest: StrictStr | None = None
    mediaType: StrictStr | None = None
    artifactType: StrictStr | None = None
    size: StrictInt | None = None
    annotations: dict[StrictStr, StrictStr] | None = None
    artifactStatus: StrictStr | None = None
