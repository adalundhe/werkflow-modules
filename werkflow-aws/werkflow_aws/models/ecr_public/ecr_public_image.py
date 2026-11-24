from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_public_image_identifier import ECRPublicImageIdentifier


class ECRPublicImage(BaseModel):
    registryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    imageId: ECRPublicImageIdentifier | None = None
    imageManifest: StrictStr | None = None
    imageManifestMediaType: StrictStr | None = None
