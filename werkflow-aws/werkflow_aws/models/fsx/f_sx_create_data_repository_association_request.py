from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_s3_data_repository_configuration import FSxS3DataRepositoryConfiguration
from .f_sx_tag import FSxTag


class FSxCreateDataRepositoryAssociationRequest(BaseModel):
    FileSystemId: StrictStr
    DataRepositoryPath: StrictStr
    FileSystemPath: StrictStr | None = None
    BatchImportMetaDataOnCreate: StrictBool | None = None
    ImportedFileChunkSize: StrictInt | None = None
    S3: FSxS3DataRepositoryConfiguration | None = None
    ClientRequestToken: StrictStr | None = None
    Tags: list[FSxTag] | None = None
