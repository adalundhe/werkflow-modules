from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_data_repository_failure_details import FSxDataRepositoryFailureDetails
from .f_sx_nfs_data_repository_configuration import FSxNFSDataRepositoryConfiguration
from .f_sx_s3_data_repository_configuration import FSxS3DataRepositoryConfiguration
from .f_sx_tag import FSxTag


class FSxDataRepositoryAssociation(BaseModel):
    AssociationId: StrictStr | None = None
    ResourceARN: StrictStr | None = None
    FileSystemId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    FailureDetails: FSxDataRepositoryFailureDetails | None = None
    FileSystemPath: StrictStr | None = None
    DataRepositoryPath: StrictStr | None = None
    BatchImportMetaDataOnCreate: StrictBool | None = None
    ImportedFileChunkSize: StrictInt | None = None
    S3: FSxS3DataRepositoryConfiguration | None = None
    Tags: list[FSxTag] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    FileCacheId: StrictStr | None = None
    FileCachePath: StrictStr | None = None
    DataRepositorySubdirectories: list[StrictStr] | None = None
    NFS: FSxNFSDataRepositoryConfiguration | None = None
