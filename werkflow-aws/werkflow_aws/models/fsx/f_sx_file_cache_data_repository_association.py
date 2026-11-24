from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_file_cache_nfs_configuration import FSxFileCacheNFSConfiguration


class FSxFileCacheDataRepositoryAssociation(BaseModel):
    FileCachePath: StrictStr
    DataRepositoryPath: StrictStr
    DataRepositorySubdirectories: list[StrictStr] | None = None
    NFS: FSxFileCacheNFSConfiguration | None = None
