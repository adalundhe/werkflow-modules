from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteAssociationRequest(BaseModel):
    SourceArn: StrictStr
    DestinationArn: StrictStr
