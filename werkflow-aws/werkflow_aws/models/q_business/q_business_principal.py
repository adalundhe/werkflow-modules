from __future__ import annotations
from pydantic import BaseModel
from .q_business_principal_group import QBusinessPrincipalGroup
from .q_business_principal_user import QBusinessPrincipalUser


class QBusinessPrincipal(BaseModel):
    user: QBusinessPrincipalUser | None = None
    group: QBusinessPrincipalGroup | None = None
