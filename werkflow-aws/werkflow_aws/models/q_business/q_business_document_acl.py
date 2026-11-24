from __future__ import annotations
from pydantic import BaseModel
from .q_business_document_acl_membership import QBusinessDocumentAclMembership


class QBusinessDocumentAcl(BaseModel):
    allowlist: QBusinessDocumentAclMembership | None = None
    denyList: QBusinessDocumentAclMembership | None = None
