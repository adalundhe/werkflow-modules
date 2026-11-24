from __future__ import annotations
from pydantic import BaseModel
from .q_business_member_group import QBusinessMemberGroup
from .q_business_member_user import QBusinessMemberUser
from .q_business_s3 import QBusinessS3


class QBusinessGroupMembers(BaseModel):
    memberGroups: list[QBusinessMemberGroup] | None = None
    memberUsers: list[QBusinessMemberUser] | None = None
    s3PathForGroupMembers: QBusinessS3 | None = None
