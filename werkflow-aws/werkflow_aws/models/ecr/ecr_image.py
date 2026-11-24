from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_image_identifier import ECRImageIdentifier


class ECRImage(BaseModel):
    registryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    imageId: ECRImageIdentifier | None = None
    imageManifest: StrictStr | None = None
    imageManifestMediaType: StrictStr | None = None
