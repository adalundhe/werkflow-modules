from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .sage_maker_accelerator_partition_layout_model import SageMakerAcceleratorPartitionLayoutModel
from .sage_maker_deployed_image_model import SageMakerDeployedImageModel
from .sage_maker_instance_pool_summary_model import SageMakerInstancePoolSummaryModel
from .sage_maker_production_variant_capacity_reservation_summary_model import SageMakerProductionVariantCapacityReservationSummaryModel
from .sage_maker_production_variant_managed_instance_scaling_model import SageMakerProductionVariantManagedInstanceScalingModel
from .sage_maker_production_variant_routing_config_model import SageMakerProductionVariantRoutingConfigModel
from .sage_maker_production_variant_serverless_config_model import SageMakerProductionVariantServerlessConfigModel
from .sage_maker_production_variant_status_model import SageMakerProductionVariantStatusModel


class SageMakerProductionVariantSummaryModel(BaseModel):
    VariantName: StrictStr | None = None
    DeployedImages: list[SageMakerDeployedImageModel] | None = None
    CurrentWeight: StrictFloat | StrictInt | None = None
    DesiredWeight: StrictFloat | StrictInt | None = None
    CurrentInstanceCount: StrictInt | None = None
    DesiredInstanceCount: StrictInt | None = None
    InstancePools: list[SageMakerInstancePoolSummaryModel] | None = None
    VariantStatus: list[SageMakerProductionVariantStatusModel] | None = None
    CurrentServerlessConfig: SageMakerProductionVariantServerlessConfigModel | None = None
    DesiredServerlessConfig: SageMakerProductionVariantServerlessConfigModel | None = None
    ManagedInstanceScaling: SageMakerProductionVariantManagedInstanceScalingModel | None = None
    RoutingConfig: SageMakerProductionVariantRoutingConfigModel | None = None
    CapacityReservationConfig: SageMakerProductionVariantCapacityReservationSummaryModel | None = None
    AcceleratorPartitionLayouts: list[SageMakerAcceleratorPartitionLayoutModel] | None = None
