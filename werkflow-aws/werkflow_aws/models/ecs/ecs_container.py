from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_managed_agent import ECSManagedAgent
from .ecs_network_binding import ECSNetworkBinding
from .ecs_network_interface import ECSNetworkInterface
from .ecs_sharing_strategy import ECSSharingStrategy


class ECSContainer(BaseModel):
    containerArn: StrictStr | None = None
    taskArn: StrictStr | None = None
    name: StrictStr | None = None
    image: StrictStr | None = None
    imageDigest: StrictStr | None = None
    runtimeId: StrictStr | None = None
    lastStatus: StrictStr | None = None
    exitCode: StrictInt | None = None
    reason: StrictStr | None = None
    networkBindings: list[ECSNetworkBinding] | None = None
    networkInterfaces: list[ECSNetworkInterface] | None = None
    healthStatus: StrictStr | None = None
    managedAgents: list[ECSManagedAgent] | None = None
    cpu: StrictStr | None = None
    memory: StrictStr | None = None
    memoryReservation: StrictStr | None = None
    gpuIds: list[StrictStr] | None = None
    neuronDeviceIds: list[StrictStr] | None = None
    gpuSharingStrategy: ECSSharingStrategy | None = None
