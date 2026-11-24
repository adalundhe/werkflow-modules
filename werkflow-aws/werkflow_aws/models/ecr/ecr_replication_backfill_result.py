from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecr_image_identifier import ECRImageIdentifier


class ECRReplicationBackfillResult(BaseModel):
    repositoryName: StrictStr | None = None
    imageId: ECRImageIdentifier | None = None
    status: StrictStr | None = None
    failureCode: StrictStr | None = None
    subImageFailureCodes: list[StrictStr] | None = None
