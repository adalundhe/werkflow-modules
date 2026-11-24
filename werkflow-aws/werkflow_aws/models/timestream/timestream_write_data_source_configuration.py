from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .timestream_write_csv_configuration import TimestreamWriteCsvConfiguration
from .timestream_write_data_source_s3_configuration import TimestreamWriteDataSourceS3Configuration


class TimestreamWriteDataSourceConfiguration(BaseModel):
    DataSourceS3Configuration: TimestreamWriteDataSourceS3Configuration | None = None
    CsvConfiguration: TimestreamWriteCsvConfiguration | None = None
    DataFormat: StrictStr | None = None
