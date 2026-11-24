from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_job_template_summary import IoTJobTemplateSummary


class IoTListJobTemplatesResponse(BaseModel):
    jobTemplates: list[IoTJobTemplateSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
