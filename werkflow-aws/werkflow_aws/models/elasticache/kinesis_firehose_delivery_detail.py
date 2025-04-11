from pydantic import BaseModel, StrictStr


class KinesisFirehoseDetail(BaseModel):
    DeliveryStream: StrictStr