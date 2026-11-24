from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_user_settings import SageMakerUserSettings


class SageMakerDescribeUserProfileResponse(BaseModel):
    DomainId: StrictStr | None = None
    UserProfileArn: StrictStr | None = None
    UserProfileName: StrictStr | None = None
    HomeEfsFileSystemUid: StrictStr | None = None
    Status: StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    FailureReason: StrictStr | None = None
    SingleSignOnUserIdentifier: StrictStr | None = None
    SingleSignOnUserValue: StrictStr | None = None
    UserSettings: SageMakerUserSettings | None = None
    ResponseMetadata: dict[str, Any] | None = None
