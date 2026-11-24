from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class OrganizationsCreateOrganizationRequest(BaseModel):
    FeatureSet: Literal['ALL', 'CONSOLIDATED_BILLING'] | None = None
