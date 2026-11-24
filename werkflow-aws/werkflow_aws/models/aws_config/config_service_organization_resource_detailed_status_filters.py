from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConfigServiceOrganizationResourceDetailedStatusFilters(BaseModel):
    AccountId: StrictStr | None = None
    Status: Literal['CREATE_SUCCESSFUL', 'CREATE_IN_PROGRESS', 'CREATE_FAILED', 'DELETE_SUCCESSFUL', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_SUCCESSFUL', 'UPDATE_IN_PROGRESS', 'UPDATE_FAILED'] | None = None
