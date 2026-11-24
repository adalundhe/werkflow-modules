from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .avatar_urls_bean import AvatarUrlsBean
from .updated_project_category import UpdatedProjectCategory


class ProjectDetails(BaseModel):
    avatarUrls: AvatarUrlsBean | None = None
    id: StrictStr | None = None
    key: StrictStr | None = None
    name: StrictStr | None = None
    projectCategory: UpdatedProjectCategory | None = None
    projectTypeKey: StrictStr | None = None
    self: StrictStr | None = None
    simplified: StrictBool | None = None
