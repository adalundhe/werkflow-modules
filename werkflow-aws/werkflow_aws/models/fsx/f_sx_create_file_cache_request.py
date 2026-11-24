from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_create_file_cache_lustre_configuration import FSxCreateFileCacheLustreConfiguration
from .f_sx_file_cache_data_repository_association import FSxFileCacheDataRepositoryAssociation
from .f_sx_tag import FSxTag


class FSxCreateFileCacheRequest(BaseModel):
    FileCacheType: Literal['LUSTRE']
    FileCacheTypeVersion: StrictStr
    StorageCapacity: StrictInt
    SubnetIds: list[StrictStr]
    ClientRequestToken: StrictStr | None = None
    SecurityGroupIds: list[StrictStr] | None = None
    Tags: list[FSxTag] | None = None
    CopyTagsToDataRepositoryAssociations: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    LustreConfiguration: FSxCreateFileCacheLustreConfiguration | None = None
    DataRepositoryAssociations: list[FSxFileCacheDataRepositoryAssociation] | None = None
