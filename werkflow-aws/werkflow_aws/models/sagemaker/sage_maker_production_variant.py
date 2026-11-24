from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .sage_maker_accelerator_partition_layout import SageMakerAcceleratorPartitionLayout
from .sage_maker_instance_pool import SageMakerInstancePool
from .sage_maker_production_variant_accelerator_type import SageMakerProductionVariantAcceleratorType
from .sage_maker_production_variant_capacity_reservation_config import SageMakerProductionVariantCapacityReservationConfig
from .sage_maker_production_variant_core_dump_config import SageMakerProductionVariantCoreDumpConfig
from .sage_maker_production_variant_inference_ami_version import SageMakerProductionVariantInferenceAmiVersion
from .sage_maker_production_variant_instance_type import SageMakerProductionVariantInstanceType
from .sage_maker_production_variant_managed_instance_scaling import SageMakerProductionVariantManagedInstanceScaling
from .sage_maker_production_variant_routing_config import SageMakerProductionVariantRoutingConfig
from .sage_maker_production_variant_serverless_config import SageMakerProductionVariantServerlessConfig


class SageMakerProductionVariant(BaseModel):
    VariantName: StrictStr | None = None
    ModelName: StrictStr | None = None
    InitialInstanceCount: StrictInt | None = None
    InstanceType: SageMakerProductionVariantInstanceType | None = None
    InstancePools: list[SageMakerInstancePool] | None = None
    VariantInstanceProvisionTimeoutInSeconds: StrictInt | None = None
    InitialVariantWeight: StrictFloat | None = None
    AcceleratorType: SageMakerProductionVariantAcceleratorType | None = None
    CoreDumpConfig: SageMakerProductionVariantCoreDumpConfig | None = None
    ServerlessConfig: SageMakerProductionVariantServerlessConfig | None = None
    VolumeSizeInGB: StrictInt | None = None
    ModelDataDownloadTimeoutInSeconds: StrictInt | None = None
    ContainerStartupHealthCheckTimeoutInSeconds: StrictInt | None = None
    EnableSSMAccess: StrictBool | None = None
    ManagedInstanceScaling: SageMakerProductionVariantManagedInstanceScaling | None = None
    RoutingConfig: SageMakerProductionVariantRoutingConfig | None = None
    InferenceAmiVersion: SageMakerProductionVariantInferenceAmiVersion | None = None
    CapacityReservationConfig: SageMakerProductionVariantCapacityReservationConfig | None = None
    AcceleratorPartitionLayouts: list[SageMakerAcceleratorPartitionLayout] | None = None
