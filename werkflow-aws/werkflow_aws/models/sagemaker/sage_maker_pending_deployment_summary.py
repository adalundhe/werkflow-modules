from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .sage_maker_pending_production_variant_summary import SageMakerPendingProductionVariantSummary


class SageMakerPendingDeploymentSummary(BaseModel):
    EndpointConfigName: StrictStr | None = None
    ProductionVariants: list[SageMakerPendingProductionVariantSummary] | None = None
    StartTime: datetime.datetime | None = None
    ShadowProductionVariants: list[SageMakerPendingProductionVariantSummary] | None = None
