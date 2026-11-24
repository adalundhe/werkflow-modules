from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_export_hidden_fields_option import QuickSightExportHiddenFieldsOption


class QuickSightDashboardVisualPublishOptions(BaseModel):
    ExportHiddenFieldsOption: QuickSightExportHiddenFieldsOption | None = None
