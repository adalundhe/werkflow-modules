from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_task_template_metadata import ConnectTaskTemplateMetadata


class ConnectListTaskTemplatesResponse(BaseModel):
    TaskTemplates: list[ConnectTaskTemplateMetadata] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
