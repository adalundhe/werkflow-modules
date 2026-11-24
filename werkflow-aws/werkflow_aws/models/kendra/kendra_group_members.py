from __future__ import annotations
from pydantic import BaseModel
from .kendra_member_group import KendraMemberGroup
from .kendra_member_user import KendraMemberUser
from .kendra_s3_path import KendraS3Path


class KendraGroupMembers(BaseModel):
    MemberGroups: list[KendraMemberGroup] | None = None
    MemberUsers: list[KendraMemberUser] | None = None
    S3PathforGroupMembers: KendraS3Path | None = None
