from pydantic import BaseModel
from .msk_jmx_exporter import MSKJmxExporter
from .msk_node_exporter import MSKNodeExporter


class MSKPrometheus(BaseModel):
    JmxExporter: MSKJmxExporter
    NodeExporter: MSKNodeExporter
