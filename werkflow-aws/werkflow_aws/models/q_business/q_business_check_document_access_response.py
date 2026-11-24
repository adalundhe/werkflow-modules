from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool
from .q_business_associated_group import QBusinessAssociatedGroup
from .q_business_associated_user import QBusinessAssociatedUser
from .q_business_document_acl import QBusinessDocumentAcl


class QBusinessCheckDocumentAccessResponse(BaseModel):
    userGroups: list[QBusinessAssociatedGroup] | None = None
    userAliases: list[QBusinessAssociatedUser] | None = None
    hasAccess: StrictBool | None = None
    documentAcl: QBusinessDocumentAcl | None = None
    ResponseMetadata: dict[str, Any] | None = None
