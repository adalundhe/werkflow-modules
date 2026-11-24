from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeS3DataConfig(BaseModel):
    path: StrictStr | None = None
    kmsKeyArn: StrictStr | None = None
