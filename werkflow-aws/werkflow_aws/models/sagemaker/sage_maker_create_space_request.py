from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_ownership_settings import SageMakerOwnershipSettings
from .sage_maker_space_settings import SageMakerSpaceSettings
from .sage_maker_space_sharing_settings import SageMakerSpaceSharingSettings
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreateSpaceRequest(BaseModel):
    DomainId: StrictStr
    SpaceName: StrictStr
    Tags: list[SageMakerTagModel] | None = None
    SpaceSettings: SageMakerSpaceSettings | None = None
    OwnershipSettings: SageMakerOwnershipSettings | None = None
    SpaceSharingSettings: SageMakerSpaceSharingSettings | None = None
    SpaceDisplayName: StrictStr | None = None
