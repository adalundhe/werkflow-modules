from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_s3_model_data_source import SageMakerS3ModelDataSource


class SageMakerAdditionalModelDataSource(BaseModel):
    ChannelName: StrictStr | None = None
    S3DataSource: SageMakerS3ModelDataSource | None = None
