from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerFileSystemDataSourceModel(BaseModel):
    FileSystemId: StrictStr | None = None
    FileSystemAccessMode: StrictStr | None = None
    FileSystemType: StrictStr | None = None
    DirectoryPath: StrictStr | None = None
