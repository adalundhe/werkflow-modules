from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_ownership_settings import SageMakerOwnershipSettings
from .sage_maker_space_settings import SageMakerSpaceSettings
from .sage_maker_space_sharing_settings import SageMakerSpaceSharingSettings


class SageMakerDescribeSpaceResponse(BaseModel):
    DomainId: StrictStr | None = None
    SpaceArn: StrictStr | None = None
    SpaceName: StrictStr | None = None
    HomeEfsFileSystemUid: StrictStr | None = None
    Status: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    SpaceSettings: SageMakerSpaceSettings | None = None
    OwnershipSettings: SageMakerOwnershipSettings | None = None
    SpaceSharingSettings: SageMakerSpaceSharingSettings | None = None
    SpaceDisplayName: StrictStr | None = None
    Url: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
