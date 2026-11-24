from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoIDPS3ConfigurationType(BaseModel):
    BucketArn: StrictStr | None = None
