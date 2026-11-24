from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_monitoring_csv_dataset_format import SageMakerMonitoringCsvDatasetFormat
from .sage_maker_monitoring_json_dataset_format import SageMakerMonitoringJsonDatasetFormat
from .sage_maker_monitoring_parquet_dataset_format import SageMakerMonitoringParquetDatasetFormat


class SageMakerMonitoringDatasetFormat(BaseModel):
    Csv: SageMakerMonitoringCsvDatasetFormat | None = None
    Json: SageMakerMonitoringJsonDatasetFormat | None = None
    Parquet: SageMakerMonitoringParquetDatasetFormat | None = None
