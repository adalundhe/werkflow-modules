from pydantic import BaseModel, StrictStr


class CloudWatchLogsDetail(BaseModel):
    LogGroup: StrictStr