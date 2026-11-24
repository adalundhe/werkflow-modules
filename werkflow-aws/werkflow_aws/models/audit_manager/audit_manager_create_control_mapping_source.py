from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .audit_manager_source_keyword import AuditManagerSourceKeyword


class AuditManagerCreateControlMappingSource(BaseModel):
    sourceName: StrictStr | None = None
    sourceDescription: StrictStr | None = None
    sourceSetUpOption: Literal['System_Controls_Mapping', 'Procedural_Controls_Mapping'] | None = None
    sourceType: Literal['AWS_Cloudtrail', 'AWS_Config', 'AWS_Security_Hub', 'AWS_API_Call', 'MANUAL', 'Common_Control', 'Core_Control'] | None = None
    sourceKeyword: AuditManagerSourceKeyword | None = None
    sourceFrequency: Literal['DAILY', 'WEEKLY', 'MONTHLY'] | None = None
    troubleshootingText: StrictStr | None = None
