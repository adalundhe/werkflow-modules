from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSTargetResourceConfiguration(BaseModel):
    SourceArn: StrictStr
    TargetKmsKeyId: StrictStr | None = None
