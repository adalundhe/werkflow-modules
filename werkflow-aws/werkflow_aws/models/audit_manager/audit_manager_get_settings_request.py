from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class AuditManagerGetSettingsRequest(BaseModel):
    attribute: Literal['ALL', 'IS_AWS_ORG_ENABLED', 'SNS_TOPIC', 'DEFAULT_ASSESSMENT_REPORTS_DESTINATION', 'DEFAULT_PROCESS_OWNERS', 'EVIDENCE_FINDER_ENABLEMENT', 'DEREGISTRATION_POLICY', 'DEFAULT_EXPORT_DESTINATION']
