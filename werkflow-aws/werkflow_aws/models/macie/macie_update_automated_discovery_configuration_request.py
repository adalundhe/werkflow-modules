from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class MacieUpdateAutomatedDiscoveryConfigurationRequest(BaseModel):
    status: Literal['ENABLED', 'DISABLED']
    autoEnableOrganizationMembers: Literal['ALL', 'NEW', 'NONE'] | None = None
