from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .timestream_write_batch_load_progress_report import TimestreamWriteBatchLoadProgressReport
from .timestream_write_data_model_configuration import TimestreamWriteDataModelConfiguration
from .timestream_write_data_source_configuration import TimestreamWriteDataSourceConfiguration
from .timestream_write_report_configuration import TimestreamWriteReportConfiguration


class TimestreamWriteBatchLoadTaskDescription(BaseModel):
    TaskId: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    DataSourceConfiguration: TimestreamWriteDataSourceConfiguration | None = None
    ProgressReport: TimestreamWriteBatchLoadProgressReport | None = None
    ReportConfiguration: TimestreamWriteReportConfiguration | None = None
    DataModelConfiguration: TimestreamWriteDataModelConfiguration | None = None
    TargetDatabaseName: StrictStr | None = None
    TargetTableName: StrictStr | None = None
    TaskStatus: StrictStr | None = None
    RecordVersion: StrictInt | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    ResumableUntil: datetime.datetime | StrictStr | None = None
