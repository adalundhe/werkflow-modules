from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .batch_capacity_reservation_request import BatchCapacityReservationRequest
from .batch_instance_requirements_request import BatchInstanceRequirementsRequest
from .batch_managed_instances_local_storage_configuration import BatchManagedInstancesLocalStorageConfiguration
from .batch_managed_instances_network_configuration import BatchManagedInstancesNetworkConfiguration
from .batch_managed_instances_storage_configuration import BatchManagedInstancesStorageConfiguration


class BatchInstanceLaunchTemplateUpdate(BaseModel):
    ec2InstanceProfileArn: StrictStr | None = None
    networkConfiguration: BatchManagedInstancesNetworkConfiguration | None = None
    instanceRequirements: BatchInstanceRequirementsRequest | None = None
    storageConfiguration: BatchManagedInstancesStorageConfiguration | None = None
    monitoring: StrictStr | None = None
    capacityReservations: BatchCapacityReservationRequest | None = None
    instanceMetadataTagsPropagation: StrictBool | None = None
    localStorageConfiguration: BatchManagedInstancesLocalStorageConfiguration | None = None
