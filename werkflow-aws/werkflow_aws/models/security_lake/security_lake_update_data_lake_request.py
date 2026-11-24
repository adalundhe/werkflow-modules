from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_lake_data_lake_configuration import SecurityLakeDataLakeConfiguration


class SecurityLakeUpdateDataLakeRequest(BaseModel):
    configurations: list[SecurityLakeDataLakeConfiguration]
    metaStoreManagerRoleArn: StrictStr | None = None
