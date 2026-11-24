from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .sage_maker_accelerator_partition_layout import SageMakerAcceleratorPartitionLayout
from .sage_maker_deployed_image import SageMakerDeployedImage
from .sage_maker_instance_pool_summary import SageMakerInstancePoolSummary
from .sage_maker_production_variant_capacity_reservation_summary import SageMakerProductionVariantCapacityReservationSummary
from .sage_maker_production_variant_managed_instance_scaling import SageMakerProductionVariantManagedInstanceScaling
from .sage_maker_production_variant_routing_config import SageMakerProductionVariantRoutingConfig
from .sage_maker_production_variant_serverless_config import SageMakerProductionVariantServerlessConfig
from .sage_maker_production_variant_status import SageMakerProductionVariantStatus


class SageMakerProductionVariantSummary(BaseModel):
    VariantName: StrictStr | None = None
    DeployedImages: list[SageMakerDeployedImage] | None = None
    CurrentWeight: StrictFloat | None = None
    DesiredWeight: StrictFloat | None = None
    CurrentInstanceCount: StrictInt | None = None
    DesiredInstanceCount: StrictInt | None = None
    InstancePools: list[SageMakerInstancePoolSummary] | None = None
    VariantStatus: list[SageMakerProductionVariantStatus] | None = None
    CurrentServerlessConfig: SageMakerProductionVariantServerlessConfig | None = None
    DesiredServerlessConfig: SageMakerProductionVariantServerlessConfig | None = None
    ManagedInstanceScaling: SageMakerProductionVariantManagedInstanceScaling | None = None
    RoutingConfig: SageMakerProductionVariantRoutingConfig | None = None
    CapacityReservationConfig: SageMakerProductionVariantCapacityReservationSummary | None = None
    AcceleratorPartitionLayouts: list[SageMakerAcceleratorPartitionLayout] | None = None
