from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class HealthImagingCreateDatastoreRequest(BaseModel):
    clientToken: StrictStr
    datastoreName: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    kmsKeyArn: StrictStr | None = None
    lambdaAuthorizerArn: StrictStr | None = None
    losslessStorageFormat: Literal['HTJ2K', 'JPEG_2000_LOSSLESS'] | None = None
