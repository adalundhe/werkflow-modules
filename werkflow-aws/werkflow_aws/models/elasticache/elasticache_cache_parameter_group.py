from pydantic import BaseModel, StrictStr


class ElasticacheCacheParameterGroup(BaseModel):
    CacheParameterGroupName: StrictStr
    ParameterApplyStatus: StrictStr
    CacheNodeIdsToReboot: list[StrictStr]