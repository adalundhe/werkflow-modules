from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAmazonQSettings(BaseModel):
    Status: StrictStr | None = None
    QProfileArn: StrictStr | None = None
