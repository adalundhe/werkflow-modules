from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_file_system_access_mode import SageMakerFileSystemAccessMode
from .sage_maker_file_system_type import SageMakerFileSystemType


class SageMakerFileSystemDataSource(BaseModel):
    FileSystemId: StrictStr | None = None
    FileSystemAccessMode: SageMakerFileSystemAccessMode | None = None
    FileSystemType: SageMakerFileSystemType | None = None
    DirectoryPath: StrictStr | None = None
