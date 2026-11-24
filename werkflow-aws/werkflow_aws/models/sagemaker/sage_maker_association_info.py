from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAssociationInfo(BaseModel):
    SourceArn: StrictStr | None = None
    DestinationArn: StrictStr | None = None
