from pydantic import BaseModel, StrictStr


class NotificationConfiguration(BaseModel):
    TopicArn: StrictStr
    TopicStatus: StrictStr