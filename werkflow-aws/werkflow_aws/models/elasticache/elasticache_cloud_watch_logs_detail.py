from pydantic import BaseModel, StrictStr


class ElasticacheCloudWatchLogsDetail(BaseModel):
    LogGroup: StrictStr