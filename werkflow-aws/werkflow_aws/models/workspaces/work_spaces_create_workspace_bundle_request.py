from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .work_spaces_compute_type import WorkSpacesComputeType
from .work_spaces_root_storage import WorkSpacesRootStorage
from .work_spaces_tag import WorkSpacesTag
from .work_spaces_user_storage import WorkSpacesUserStorage


class WorkSpacesCreateWorkspaceBundleRequest(BaseModel):
    BundleName: StrictStr
    BundleDescription: StrictStr
    ImageId: StrictStr
    ComputeType: WorkSpacesComputeType
    UserStorage: WorkSpacesUserStorage
    RootStorage: WorkSpacesRootStorage | None = None
    Tags: list[WorkSpacesTag] | None = None
