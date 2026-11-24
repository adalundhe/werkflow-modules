from __future__ import annotations
from pydantic import BaseModel
from .ses_import_data_source import SESImportDataSource
from .ses_import_destination import SESImportDestination


class SESCreateImportJobRequest(BaseModel):
    ImportDestination: SESImportDestination
    ImportDataSource: SESImportDataSource
