from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .glue_kafka_streaming_source_options import GlueKafkaStreamingSourceOptions
from .glue_streaming_data_preview_options import GlueStreamingDataPreviewOptions


class GlueCatalogKafkaSource(BaseModel):
    Name: StrictStr | None = None
    WindowSize: StrictInt | None = None
    DetectSchema: StrictBool | None = None
    Table: StrictStr | None = None
    Database: StrictStr | None = None
    StreamingOptions: GlueKafkaStreamingSourceOptions | None = None
    DataPreviewOptions: GlueStreamingDataPreviewOptions | None = None
