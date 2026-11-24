from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_neuron_device_core_info import EC2NeuronDeviceCoreInfo
from .ec2_neuron_device_memory_info import EC2NeuronDeviceMemoryInfo


class EC2NeuronDeviceInfo(BaseModel):
    Count: StrictInt | None = None
    Name: StrictStr | None = None
    CoreInfo: EC2NeuronDeviceCoreInfo | None = None
    MemoryInfo: EC2NeuronDeviceMemoryInfo | None = None
