from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_space_settings import SageMakerSpaceSettings


class SageMakerUpdateSpaceRequest(BaseModel):
    DomainId: StrictStr
    SpaceName: StrictStr
    SpaceSettings: SageMakerSpaceSettings | None = None
    SpaceDisplayName: StrictStr | None = None
