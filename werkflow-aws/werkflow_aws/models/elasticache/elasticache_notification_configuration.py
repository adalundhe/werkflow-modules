from pydantic import BaseModel, StrictStr


class ElasticacheNotificationConfiguration(BaseModel):
    TopicArn: StrictStr
    TopicStatus: StrictStr