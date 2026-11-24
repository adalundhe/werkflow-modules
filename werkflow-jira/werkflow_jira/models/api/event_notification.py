from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .field_details import FieldDetails
from .group_name import GroupName
from .project_role import ProjectRole
from .user_details import UserDetails


class EventNotification(BaseModel):
    emailAddress: StrictStr | None = None
    expand: StrictStr | None = None
    field: FieldDetails | None = None
    group: GroupName | None = None
    id: StrictInt | None = None
    notificationType: StrictStr | None = None
    parameter: StrictStr | None = None
    projectRole: ProjectRole | None = None
    recipient: StrictStr | None = None
    user: UserDetails | None = None
