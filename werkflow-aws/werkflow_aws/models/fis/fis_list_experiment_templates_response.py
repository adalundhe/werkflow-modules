from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .fis_experiment_template_summary import FISExperimentTemplateSummary


class FISListExperimentTemplatesResponse(BaseModel):
    experimentTemplates: list[FISExperimentTemplateSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
