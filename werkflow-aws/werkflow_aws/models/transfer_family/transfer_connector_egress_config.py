from __future__ import annotations
from pydantic import BaseModel
from .transfer_connector_vpc_lattice_egress_config import TransferConnectorVpcLatticeEgressConfig


class TransferConnectorEgressConfig(BaseModel):
    VpcLattice: TransferConnectorVpcLatticeEgressConfig | None = None
