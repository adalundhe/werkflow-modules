from __future__ import annotations
from pydantic import BaseModel
from .f_sx_auto_export_policy import FSxAutoExportPolicy
from .f_sx_auto_import_policy import FSxAutoImportPolicy


class FSxS3DataRepositoryConfiguration(BaseModel):
    AutoImportPolicy: FSxAutoImportPolicy | None = None
    AutoExportPolicy: FSxAutoExportPolicy | None = None
