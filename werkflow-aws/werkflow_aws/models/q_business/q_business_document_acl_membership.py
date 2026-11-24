from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_document_acl_condition import QBusinessDocumentAclCondition


class QBusinessDocumentAclMembership(BaseModel):
    memberRelation: StrictStr | None = None
    conditions: list[QBusinessDocumentAclCondition] | None = None
