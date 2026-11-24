from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .security_hub_aws_security_finding_filters import SecurityHubAwsSecurityFindingFilters
from .security_hub_note_update import SecurityHubNoteUpdate


class SecurityHubUpdateFindingsRequest(BaseModel):
    Filters: SecurityHubAwsSecurityFindingFilters
    Note: SecurityHubNoteUpdate | None = None
    RecordState: Literal['ACTIVE', 'ARCHIVED'] | None = None
