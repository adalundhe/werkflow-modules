from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECRPublicImageIdentifier(BaseModel):
    imageDigest: StrictStr | None = None
    imageTag: StrictStr | None = None
