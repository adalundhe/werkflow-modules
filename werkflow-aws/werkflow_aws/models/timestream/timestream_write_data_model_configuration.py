from __future__ import annotations
from pydantic import BaseModel
from .timestream_write_data_model import TimestreamWriteDataModel
from .timestream_write_data_model_s3_configuration import TimestreamWriteDataModelS3Configuration


class TimestreamWriteDataModelConfiguration(BaseModel):
    DataModel: TimestreamWriteDataModel | None = None
    DataModelS3Configuration: TimestreamWriteDataModelS3Configuration | None = None
