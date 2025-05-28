from pydantic import BaseModel, StrictStr


class ElasticacheKinesisFirehoseDetail(BaseModel):
    DeliveryStream: StrictStr