from __future__ import annotations
from pydantic import BaseModel
from .msk_jmx_exporter_info import MSKJmxExporterInfo
from .msk_node_exporter_info import MSKNodeExporterInfo


class MSKPrometheusInfo(BaseModel):
    JmxExporter: MSKJmxExporterInfo | None = None
    NodeExporter: MSKNodeExporterInfo | None = None
