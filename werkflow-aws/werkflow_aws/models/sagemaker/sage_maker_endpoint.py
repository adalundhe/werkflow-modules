from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_data_capture_config_summary_model import SageMakerDataCaptureConfigSummaryModel
from .sage_maker_monitoring_schedule import SageMakerMonitoringSchedule
from .sage_maker_production_variant_summary_model import SageMakerProductionVariantSummaryModel
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerEndpoint(BaseModel):
    EndpointName: StrictStr | None = None
    EndpointArn: StrictStr | None = None
    EndpointConfigName: StrictStr | None = None
    ProductionVariants: list[SageMakerProductionVariantSummaryModel] | None = None
    DataCaptureConfig: SageMakerDataCaptureConfigSummaryModel | None = None
    EndpointStatus: StrictStr | None = None
    FailureReason: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    MonitoringSchedules: list[SageMakerMonitoringSchedule] | None = None
    Tags: list[SageMakerTagModel] | None = None
    ShadowProductionVariants: list[SageMakerProductionVariantSummaryModel] | None = None
