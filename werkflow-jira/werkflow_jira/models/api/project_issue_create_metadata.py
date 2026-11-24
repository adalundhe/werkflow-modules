from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .avatar_urls_bean import AvatarUrlsBean
from .issue_type_issue_create_metadata import IssueTypeIssueCreateMetadata


class ProjectIssueCreateMetadata(BaseModel):
    avatarUrls: AvatarUrlsBean | None = None
    expand: StrictStr | None = None
    id: StrictStr | None = None
    issuetypes: list[IssueTypeIssueCreateMetadata] | None = None
    key: StrictStr | None = None
    name: StrictStr | None = None
    self: StrictStr | None = None
