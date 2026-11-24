from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_ownership_settings_summary import SageMakerOwnershipSettingsSummary
from .sage_maker_space_settings_summary import SageMakerSpaceSettingsSummary
from .sage_maker_space_sharing_settings_summary import SageMakerSpaceSharingSettingsSummary


class SageMakerSpaceDetails(BaseModel):
    DomainId: StrictStr | None = None
    SpaceName: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    SpaceSettingsSummary: SageMakerSpaceSettingsSummary | None = None
    SpaceSharingSettingsSummary: SageMakerSpaceSharingSettingsSummary | None = None
    OwnershipSettingsSummary: SageMakerOwnershipSettingsSummary | None = None
    SpaceDisplayName: StrictStr | None = None
