from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ImageReference(BaseModel):
    ImageId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Arn: StrictStr | None = None
