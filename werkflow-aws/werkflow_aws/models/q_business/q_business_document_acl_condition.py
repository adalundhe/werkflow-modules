from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_document_acl_group import QBusinessDocumentAclGroup
from .q_business_document_acl_user import QBusinessDocumentAclUser


class QBusinessDocumentAclCondition(BaseModel):
    memberRelation: StrictStr | None = None
    users: list[QBusinessDocumentAclUser] | None = None
    groups: list[QBusinessDocumentAclGroup] | None = None
