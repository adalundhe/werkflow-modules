from __future__ import annotations
from pydantic import BaseModel
from .transfer_update_connector_vpc_lattice_egress_config import TransferUpdateConnectorVpcLatticeEgressConfig


class TransferUpdateConnectorEgressConfig(BaseModel):
    VpcLattice: TransferUpdateConnectorVpcLatticeEgressConfig | None = None
