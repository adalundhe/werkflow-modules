from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_auto_ml_data_source import SageMakerAutoMLDataSource


class SageMakerAutoMLChannel(BaseModel):
    DataSource: SageMakerAutoMLDataSource | None = None
    CompressionType: StrictStr | None = None
    TargetAttributeName: StrictStr | None = None
    ContentType: StrictStr | None = None
    ChannelType: StrictStr | None = None
    SampleWeightAttributeName: StrictStr | None = None
