from pydantic import BaseModel, StrictStr


class CacheParameterGroup(BaseModel):
    CacheParameterGroupName: StrictStr
    ParameterApplyStatus: StrictStr
    CacheNodeIdsToReboot: list[StrictStr]