from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_db_subnet import DocumentDBSubnet


class DocumentDBDBSubnetGroup(BaseModel):
    DBSubnetGroupName: StrictStr | None = None
    DBSubnetGroupDescription: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetGroupStatus: StrictStr | None = None
    Subnets: list[DocumentDBSubnet] | None = None
    DBSubnetGroupArn: StrictStr | None = None
    SupportedNetworkTypes: list[StrictStr] | None = None
