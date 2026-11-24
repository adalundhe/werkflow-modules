from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEdge(BaseModel):
    SourceArn: StrictStr | None = None
    DestinationArn: StrictStr | None = None
    AssociationType: StrictStr | None = None
