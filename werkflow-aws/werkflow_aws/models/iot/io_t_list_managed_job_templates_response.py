from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_managed_job_template_summary import IoTManagedJobTemplateSummary


class IoTListManagedJobTemplatesResponse(BaseModel):
    managedJobTemplates: list[IoTManagedJobTemplateSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
