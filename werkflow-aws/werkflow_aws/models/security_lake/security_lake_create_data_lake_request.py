from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_lake_data_lake_configuration import SecurityLakeDataLakeConfiguration
from .security_lake_tag import SecurityLakeTag


class SecurityLakeCreateDataLakeRequest(BaseModel):
    configurations: list[SecurityLakeDataLakeConfiguration]
    metaStoreManagerRoleArn: StrictStr
    tags: list[SecurityLakeTag] | None = None
