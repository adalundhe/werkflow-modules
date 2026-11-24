from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_public_image_identifier import ECRPublicImageIdentifier


class ECRPublicImageFailure(BaseModel):
    imageId: ECRPublicImageIdentifier | None = None
    failureCode: StrictStr | None = None
    failureReason: StrictStr | None = None
