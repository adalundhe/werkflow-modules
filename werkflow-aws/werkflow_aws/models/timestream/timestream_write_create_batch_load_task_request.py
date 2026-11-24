from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .timestream_write_data_model_configuration import TimestreamWriteDataModelConfiguration
from .timestream_write_data_source_configuration import TimestreamWriteDataSourceConfiguration
from .timestream_write_report_configuration import TimestreamWriteReportConfiguration


class TimestreamWriteCreateBatchLoadTaskRequest(BaseModel):
    DataSourceConfiguration: TimestreamWriteDataSourceConfiguration
    ReportConfiguration: TimestreamWriteReportConfiguration
    TargetDatabaseName: StrictStr
    TargetTableName: StrictStr
    ClientToken: StrictStr | None = None
    DataModelConfiguration: TimestreamWriteDataModelConfiguration | None = None
    RecordVersion: StrictInt | None = None
