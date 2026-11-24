from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_compression_type import SageMakerCompressionType
from .sage_maker_data_source import SageMakerDataSource
from .sage_maker_record_wrapper import SageMakerRecordWrapper
from .sage_maker_shuffle_config import SageMakerShuffleConfig
from .sage_maker_training_input_mode import SageMakerTrainingInputMode


class SageMakerChannel(BaseModel):
    ChannelName: StrictStr | None = None
    DataSource: SageMakerDataSource | None = None
    ContentType: StrictStr | None = None
    CompressionType: SageMakerCompressionType | None = None
    RecordWrapperType: SageMakerRecordWrapper | None = None
    InputMode: SageMakerTrainingInputMode | None = None
    ShuffleConfig: SageMakerShuffleConfig | None = None
