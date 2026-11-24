from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaSourceAccessConfigurationModel(BaseModel):
    Type: StrictStr | None = None
    URI: StrictStr | None = None
