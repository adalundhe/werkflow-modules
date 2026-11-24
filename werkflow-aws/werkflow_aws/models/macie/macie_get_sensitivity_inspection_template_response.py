from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_sensitivity_inspection_template_excludes import MacieSensitivityInspectionTemplateExcludes
from .macie_sensitivity_inspection_template_includes import MacieSensitivityInspectionTemplateIncludes


class MacieGetSensitivityInspectionTemplateResponse(BaseModel):
    description: StrictStr | None = None
    excludes: MacieSensitivityInspectionTemplateExcludes | None = None
    includes: MacieSensitivityInspectionTemplateIncludes | None = None
    name: StrictStr | None = None
    sensitivityInspectionTemplateId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
