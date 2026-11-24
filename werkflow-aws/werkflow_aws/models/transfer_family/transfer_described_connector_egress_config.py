from __future__ import annotations
from pydantic import BaseModel
from .transfer_described_connector_vpc_lattice_egress_config import TransferDescribedConnectorVpcLatticeEgressConfig


class TransferDescribedConnectorEgressConfig(BaseModel):
    VpcLattice: TransferDescribedConnectorVpcLatticeEgressConfig | None = None
