from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SageMakerAddAssociationRequest(BaseModel):
    SourceArn: StrictStr
    DestinationArn: StrictStr
    AssociationType: Literal['ContributedTo', 'AssociatedWith', 'DerivedFrom', 'Produced', 'SameAs'] | None = None
