from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_file_cache_failure_details import FSxFileCacheFailureDetails
from .f_sx_file_cache_lustre_configuration import FSxFileCacheLustreConfiguration
from .f_sx_tag import FSxTag


class FSxFileCacheCreating(BaseModel):
    OwnerId: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    FileCacheId: StrictStr | None = None
    FileCacheType: StrictStr | None = None
    FileCacheTypeVersion: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    FailureDetails: FSxFileCacheFailureDetails | None = None
    StorageCapacity: StrictInt | None = None
    VpcId: StrictStr | None = None
    SubnetIds: list[StrictStr] | None = None
    NetworkInterfaceIds: list[StrictStr] | None = None
    DNSName: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    ResourceARN: StrictStr | None = None
    Tags: list[FSxTag] | None = None
    CopyTagsToDataRepositoryAssociations: StrictBool | None = None
    LustreConfiguration: FSxFileCacheLustreConfiguration | None = None
    DataRepositoryAssociationIds: list[StrictStr] | None = None
