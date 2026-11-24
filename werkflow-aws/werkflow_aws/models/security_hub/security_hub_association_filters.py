from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SecurityHubAssociationFilters(BaseModel):
    ConfigurationPolicyId: StrictStr | None = None
    AssociationType: Literal['INHERITED', 'APPLIED'] | None = None
    AssociationStatus: Literal['PENDING', 'SUCCESS', 'FAILED', 'DISABLED'] | None = None
