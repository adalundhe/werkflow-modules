from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_completion_report import FSxCompletionReport
from .f_sx_release_configuration import FSxReleaseConfiguration
from .f_sx_tag import FSxTag


class FSxCreateDataRepositoryTaskRequest(BaseModel):
    Type: Literal['EXPORT_TO_REPOSITORY', 'IMPORT_METADATA_FROM_REPOSITORY', 'RELEASE_DATA_FROM_FILESYSTEM', 'AUTO_RELEASE_DATA']
    FileSystemId: StrictStr
    Report: FSxCompletionReport
    Paths: list[StrictStr] | None = None
    ClientRequestToken: StrictStr | None = None
    Tags: list[FSxTag] | None = None
    CapacityToRelease: StrictInt | None = None
    ReleaseConfiguration: FSxReleaseConfiguration | None = None
