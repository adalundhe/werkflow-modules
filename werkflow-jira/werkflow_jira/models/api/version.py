from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .simple_link import SimpleLink
from .version_approver import VersionApprover
from .version_issues_status import VersionIssuesStatus


class Version(BaseModel):
    approvers: list[VersionApprover] | None = None
    archived: StrictBool | None = None
    description: StrictStr | None = None
    driver: StrictStr | None = None
    expand: StrictStr | None = None
    id: StrictStr | None = None
    issuesStatusForFixVersion: VersionIssuesStatus | None = None
    moveUnfixedIssuesTo: StrictStr | None = None
    name: StrictStr | None = None
    operations: list[SimpleLink] | None = None
    overdue: StrictBool | None = None
    project: StrictStr | None = None
    projectId: StrictInt | None = None
    releaseDate: StrictStr | None = None
    released: StrictBool | None = None
    self: StrictStr | None = None
    startDate: StrictStr | None = None
    userReleaseDate: StrictStr | None = None
    userStartDate: StrictStr | None = None
