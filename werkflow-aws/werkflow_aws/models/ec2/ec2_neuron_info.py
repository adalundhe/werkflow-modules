from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .ec2_neuron_device_info import EC2NeuronDeviceInfo


class EC2NeuronInfo(BaseModel):
    NeuronDevices: list[EC2NeuronDeviceInfo] | None = None
    TotalNeuronDeviceMemoryInMiB: StrictInt | None = None
