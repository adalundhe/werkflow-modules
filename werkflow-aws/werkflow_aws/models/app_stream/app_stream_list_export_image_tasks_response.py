from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_stream_export_image_task import AppStreamExportImageTask


class AppStreamListExportImageTasksResponse(BaseModel):
    ExportImageTasks: list[AppStreamExportImageTask] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
