from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_image_identifier import ECRImageIdentifier


class ECRImageFailure(BaseModel):
    imageId: ECRImageIdentifier | None = None
    failureCode: StrictStr | None = None
    failureReason: StrictStr | None = None
