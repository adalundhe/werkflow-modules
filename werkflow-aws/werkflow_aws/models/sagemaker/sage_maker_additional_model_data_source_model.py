from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_s3_model_data_source_model import SageMakerS3ModelDataSourceModel


class SageMakerAdditionalModelDataSourceModel(BaseModel):
    ChannelName: StrictStr | None = None
    S3DataSource: SageMakerS3ModelDataSourceModel | None = None
