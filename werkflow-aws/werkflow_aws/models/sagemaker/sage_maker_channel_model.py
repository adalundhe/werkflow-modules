from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_data_source_model import SageMakerDataSourceModel
from .sage_maker_shuffle_config_model import SageMakerShuffleConfigModel


class SageMakerChannelModel(BaseModel):
    ChannelName: StrictStr | None = None
    DataSource: SageMakerDataSourceModel | None = None
    ContentType: StrictStr | None = None
    CompressionType: StrictStr | None = None
    RecordWrapperType: StrictStr | None = None
    InputMode: StrictStr | None = None
    ShuffleConfig: SageMakerShuffleConfigModel | None = None
