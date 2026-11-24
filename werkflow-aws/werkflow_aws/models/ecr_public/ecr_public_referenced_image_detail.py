from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ECRPublicReferencedImageDetail(BaseModel):
    imageDigest: StrictStr | None = None
    imageSizeInBytes: StrictInt | None = None
    imagePushedAt: datetime.datetime | StrictStr | None = None
    imageManifestMediaType: StrictStr | None = None
    artifactMediaType: StrictStr | None = None
