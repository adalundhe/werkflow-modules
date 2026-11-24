from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .paged_list_user_details_application_user import PagedListUserDetailsApplicationUser


class Group(BaseModel):
    expand: StrictStr | None = None
    groupId: StrictStr | None = None
    name: StrictStr | None = None
    self: StrictStr | None = None
    users: PagedListUserDetailsApplicationUser | None = None
