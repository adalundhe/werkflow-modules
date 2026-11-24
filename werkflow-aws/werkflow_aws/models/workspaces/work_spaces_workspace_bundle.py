from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .work_spaces_compute_type import WorkSpacesComputeType
from .work_spaces_root_storage import WorkSpacesRootStorage
from .work_spaces_user_storage import WorkSpacesUserStorage


class WorkSpacesWorkspaceBundle(BaseModel):
    BundleId: StrictStr | None = None
    Name: StrictStr | None = None
    Owner: StrictStr | None = None
    Description: StrictStr | None = None
    ImageId: StrictStr | None = None
    RootStorage: WorkSpacesRootStorage | None = None
    UserStorage: WorkSpacesUserStorage | None = None
    ComputeType: WorkSpacesComputeType | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    BundleType: StrictStr | None = None
