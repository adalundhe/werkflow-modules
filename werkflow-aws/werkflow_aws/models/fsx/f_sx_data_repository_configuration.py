from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_data_repository_failure_details import FSxDataRepositoryFailureDetails


class FSxDataRepositoryConfiguration(BaseModel):
    Lifecycle: StrictStr | None = None
    ImportPath: StrictStr | None = None
    ExportPath: StrictStr | None = None
    ImportedFileChunkSize: StrictInt | None = None
    AutoImportPolicy: StrictStr | None = None
    FailureDetails: FSxDataRepositoryFailureDetails | None = None
