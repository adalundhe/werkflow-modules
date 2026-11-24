from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ecs_capacity_reservation_request import ECSCapacityReservationRequest
from .ecs_instance_requirements_request import ECSInstanceRequirementsRequest
from .ecs_managed_instances_local_storage_configuration import ECSManagedInstancesLocalStorageConfiguration
from .ecs_managed_instances_network_configuration import ECSManagedInstancesNetworkConfiguration
from .ecs_managed_instances_storage_configuration import ECSManagedInstancesStorageConfiguration


class ECSInstanceLaunchTemplateUpdate(BaseModel):
    ec2InstanceProfileArn: StrictStr | None = None
    networkConfiguration: ECSManagedInstancesNetworkConfiguration | None = None
    storageConfiguration: ECSManagedInstancesStorageConfiguration | None = None
    instanceMetadataTagsPropagation: StrictBool | None = None
    localStorageConfiguration: ECSManagedInstancesLocalStorageConfiguration | None = None
    monitoring: Literal['BASIC', 'DETAILED'] | None = None
    instanceRequirements: ECSInstanceRequirementsRequest | None = None
    capacityReservations: ECSCapacityReservationRequest | None = None
