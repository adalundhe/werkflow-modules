from __future__ import annotations
from pydantic import BaseModel
from .msk_jmx_exporter_model import MSKJmxExporterModel
from .msk_node_exporter_model import MSKNodeExporterModel


class MSKPrometheusModel(BaseModel):
    JmxExporter: MSKJmxExporterModel | None = None
    NodeExporter: MSKNodeExporterModel | None = None
