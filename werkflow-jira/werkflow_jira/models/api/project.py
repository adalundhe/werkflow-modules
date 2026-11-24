from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .avatar_urls_bean import AvatarUrlsBean
from .hierarchy import Hierarchy
from .issue_type_details import IssueTypeDetails
from .project_category import ProjectCategory
from .project_component import ProjectComponent
from .project_insight import ProjectInsight
from .project_landing_page_info import ProjectLandingPageInfo
from .project_permissions import ProjectPermissions
from .user import User
from .version import Version


class Project(BaseModel):
    archived: StrictBool | None = None
    archivedBy: User | None = None
    archivedDate: StrictStr | None = None
    assigneeType: StrictStr | None = None
    avatarUrls: AvatarUrlsBean | None = None
    components: list[ProjectComponent] | None = None
    deleted: StrictBool | None = None
    deletedBy: User | None = None
    deletedDate: StrictStr | None = None
    description: StrictStr | None = None
    email: StrictStr | None = None
    expand: StrictStr | None = None
    favourite: StrictBool | None = None
    id: StrictStr | None = None
    insight: ProjectInsight | None = None
    isPrivate: StrictBool | None = None
    issueTypeHierarchy: Hierarchy | None = None
    issueTypes: list[IssueTypeDetails] | None = None
    key: StrictStr | None = None
    landingPageInfo: ProjectLandingPageInfo | None = None
    lead: User | None = None
    name: StrictStr | None = None
    permissions: ProjectPermissions | None = None
    projectCategory: ProjectCategory | None = None
    projectTypeKey: StrictStr | None = None
    properties: dict[StrictStr, Any] | None = None
    retentionTillDate: StrictStr | None = None
    roles: dict[StrictStr, StrictStr] | None = None
    self: StrictStr | None = None
    simplified: StrictBool | None = None
    style: StrictStr | None = None
    url: StrictStr | None = None
    uuid: StrictStr | None = None
    versions: list[Version] | None = None
