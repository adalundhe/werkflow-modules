from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .macie_sensitivity_inspection_template_excludes import MacieSensitivityInspectionTemplateExcludes
from .macie_sensitivity_inspection_template_includes import MacieSensitivityInspectionTemplateIncludes


class MacieUpdateSensitivityInspectionTemplateRequest(BaseModel):
    id: StrictStr
    description: StrictStr | None = None
    excludes: MacieSensitivityInspectionTemplateExcludes | None = None
    includes: MacieSensitivityInspectionTemplateIncludes | None = None
