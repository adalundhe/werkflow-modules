from __future__ import annotations
from pydantic import BaseModel
from .cost_explorer_ec2_instance_details import CostExplorerEC2InstanceDetails
from .cost_explorer_es_instance_details import CostExplorerESInstanceDetails
from .cost_explorer_elasti_cache_instance_details import CostExplorerElastiCacheInstanceDetails
from .cost_explorer_memory_db_instance_details import CostExplorerMemoryDBInstanceDetails
from .cost_explorer_rds_instance_details import CostExplorerRDSInstanceDetails
from .cost_explorer_redshift_instance_details import CostExplorerRedshiftInstanceDetails


class CostExplorerInstanceDetails(BaseModel):
    EC2InstanceDetails: CostExplorerEC2InstanceDetails | None = None
    RDSInstanceDetails: CostExplorerRDSInstanceDetails | None = None
    RedshiftInstanceDetails: CostExplorerRedshiftInstanceDetails | None = None
    ElastiCacheInstanceDetails: CostExplorerElastiCacheInstanceDetails | None = None
    ESInstanceDetails: CostExplorerESInstanceDetails | None = None
    MemoryDBInstanceDetails: CostExplorerMemoryDBInstanceDetails | None = None
