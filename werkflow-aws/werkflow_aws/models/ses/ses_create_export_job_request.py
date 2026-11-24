from __future__ import annotations
from pydantic import BaseModel
from .ses_export_data_source import SESExportDataSource
from .ses_export_destination import SESExportDestination


class SESCreateExportJobRequest(BaseModel):
    ExportDataSource: SESExportDataSource
    ExportDestination: SESExportDestination
