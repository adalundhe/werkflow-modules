import datetime
from pydantic import BaseModel, StrictStr


class Credentials(BaseModel):
    AccessKeyId: StrictStr
    SecretAccessKey: StrictStr
    SessionToken: StrictStr
    Expiration: datetime.datetime