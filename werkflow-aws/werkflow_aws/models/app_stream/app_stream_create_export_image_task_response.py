from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_stream_export_image_task import AppStreamExportImageTask


class AppStreamCreateExportImageTaskResponse(BaseModel):
    ExportImageTask: AppStreamExportImageTask | None = None
    ResponseMetadata: dict[str, Any] | None = None
