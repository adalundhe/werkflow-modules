from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_association_info import SageMakerAssociationInfo


class SageMakerLineageMetadata(BaseModel):
    ActionArns: dict[StrictStr, StrictStr] | None = None
    ArtifactArns: dict[StrictStr, StrictStr] | None = None
    ContextArns: dict[StrictStr, StrictStr] | None = None
    Associations: list[SageMakerAssociationInfo] | None = None
