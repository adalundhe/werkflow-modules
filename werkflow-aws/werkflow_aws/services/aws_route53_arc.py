from werkflow_aws.models.route53_arc import (
    Route53ARCCreateClusterRequest,
    Route53ARCCreateClusterResponse,
    Route53ARCCreateControlPanelRequest,
    Route53ARCCreateControlPanelResponse,
    Route53ARCCreateRoutingControlRequest,
    Route53ARCCreateRoutingControlResponse,
    Route53ARCCreateSafetyRuleRequest,
    Route53ARCCreateSafetyRuleResponse,
    Route53ARCDeleteClusterRequest,
    Route53ARCDeleteClusterResponse,
    Route53ARCDeleteControlPanelRequest,
    Route53ARCDeleteControlPanelResponse,
    Route53ARCDeleteRoutingControlRequest,
    Route53ARCDeleteRoutingControlResponse,
    Route53ARCDeleteSafetyRuleRequest,
    Route53ARCDeleteSafetyRuleResponse,
    Route53ARCDescribeClusterRequest,
    Route53ARCDescribeClusterResponse,
    Route53ARCDescribeControlPanelRequest,
    Route53ARCDescribeControlPanelResponse,
    Route53ARCDescribeRoutingControlRequest,
    Route53ARCDescribeRoutingControlResponse,
    Route53ARCDescribeSafetyRuleRequest,
    Route53ARCDescribeSafetyRuleResponse,
    Route53ARCGetResourcePolicyRequest,
    Route53ARCGetResourcePolicyResponse,
    Route53ARCListAssociatedRoute53HealthChecksRequest,
    Route53ARCListAssociatedRoute53HealthChecksResponse,
    Route53ARCListClustersRequest,
    Route53ARCListClustersResponse,
    Route53ARCListControlPanelsRequest,
    Route53ARCListControlPanelsResponse,
    Route53ARCListRoutingControlsRequest,
    Route53ARCListRoutingControlsResponse,
    Route53ARCListSafetyRulesRequest,
    Route53ARCListSafetyRulesResponse,
    Route53ARCListTagsForResourceRequest,
    Route53ARCListTagsForResourceResponse,
    Route53ARCTagResourceRequest,
    Route53ARCTagResourceResponse,
    Route53ARCUntagResourceRequest,
    Route53ARCUntagResourceResponse,
    Route53ARCUpdateClusterRequest,
    Route53ARCUpdateClusterResponse,
    Route53ARCUpdateControlPanelRequest,
    Route53ARCUpdateControlPanelResponse,
    Route53ARCUpdateRoutingControlRequest,
    Route53ARCUpdateRoutingControlResponse,
    Route53ARCUpdateSafetyRuleRequest,
    Route53ARCUpdateSafetyRuleResponse,
)
from werkflow_aws.types.route53_arc_client import Route53ARCClient
from .base import AWSBaseService


class AWSRoute53ARC(AWSBaseService[Route53ARCClient]):
    service_name = 'route53-arc'
    boto3_service_name = 'route53-recovery-control-config'

    def __init__(self) -> None:
        super().__init__(service_name='route53-arc', boto3_service_name='route53-recovery-control-config')

    async def create_cluster(
        self,
        request: Route53ARCCreateClusterRequest,
    ) -> Route53ARCCreateClusterResponse:
        client = self._require_client()
        return await self._execute(client.create_cluster, request, Route53ARCCreateClusterResponse)

    async def create_control_panel(
        self,
        request: Route53ARCCreateControlPanelRequest,
    ) -> Route53ARCCreateControlPanelResponse:
        client = self._require_client()
        return await self._execute(client.create_control_panel, request, Route53ARCCreateControlPanelResponse)

    async def create_routing_control(
        self,
        request: Route53ARCCreateRoutingControlRequest,
    ) -> Route53ARCCreateRoutingControlResponse:
        client = self._require_client()
        return await self._execute(client.create_routing_control, request, Route53ARCCreateRoutingControlResponse)

    async def create_safety_rule(
        self,
        request: Route53ARCCreateSafetyRuleRequest | None = None,
    ) -> Route53ARCCreateSafetyRuleResponse:
        client = self._require_client()
        return await self._execute(client.create_safety_rule, request, Route53ARCCreateSafetyRuleResponse)

    async def delete_cluster(
        self,
        request: Route53ARCDeleteClusterRequest,
    ) -> Route53ARCDeleteClusterResponse:
        client = self._require_client()
        return await self._execute(client.delete_cluster, request, Route53ARCDeleteClusterResponse)

    async def delete_control_panel(
        self,
        request: Route53ARCDeleteControlPanelRequest,
    ) -> Route53ARCDeleteControlPanelResponse:
        client = self._require_client()
        return await self._execute(client.delete_control_panel, request, Route53ARCDeleteControlPanelResponse)

    async def delete_routing_control(
        self,
        request: Route53ARCDeleteRoutingControlRequest,
    ) -> Route53ARCDeleteRoutingControlResponse:
        client = self._require_client()
        return await self._execute(client.delete_routing_control, request, Route53ARCDeleteRoutingControlResponse)

    async def delete_safety_rule(
        self,
        request: Route53ARCDeleteSafetyRuleRequest,
    ) -> Route53ARCDeleteSafetyRuleResponse:
        client = self._require_client()
        return await self._execute(client.delete_safety_rule, request, Route53ARCDeleteSafetyRuleResponse)

    async def describe_cluster(
        self,
        request: Route53ARCDescribeClusterRequest,
    ) -> Route53ARCDescribeClusterResponse:
        client = self._require_client()
        return await self._execute(client.describe_cluster, request, Route53ARCDescribeClusterResponse)

    async def describe_control_panel(
        self,
        request: Route53ARCDescribeControlPanelRequest,
    ) -> Route53ARCDescribeControlPanelResponse:
        client = self._require_client()
        return await self._execute(client.describe_control_panel, request, Route53ARCDescribeControlPanelResponse)

    async def describe_routing_control(
        self,
        request: Route53ARCDescribeRoutingControlRequest,
    ) -> Route53ARCDescribeRoutingControlResponse:
        client = self._require_client()
        return await self._execute(client.describe_routing_control, request, Route53ARCDescribeRoutingControlResponse)

    async def describe_safety_rule(
        self,
        request: Route53ARCDescribeSafetyRuleRequest,
    ) -> Route53ARCDescribeSafetyRuleResponse:
        client = self._require_client()
        return await self._execute(client.describe_safety_rule, request, Route53ARCDescribeSafetyRuleResponse)

    async def get_resource_policy(
        self,
        request: Route53ARCGetResourcePolicyRequest,
    ) -> Route53ARCGetResourcePolicyResponse:
        client = self._require_client()
        return await self._execute(client.get_resource_policy, request, Route53ARCGetResourcePolicyResponse)

    async def list_associated_route53_health_checks(
        self,
        request: Route53ARCListAssociatedRoute53HealthChecksRequest,
    ) -> Route53ARCListAssociatedRoute53HealthChecksResponse:
        client = self._require_client()
        return await self._execute(client.list_associated_route53_health_checks, request, Route53ARCListAssociatedRoute53HealthChecksResponse)

    async def list_associated_route53_health_checks_paginated(
        self,
        request: Route53ARCListAssociatedRoute53HealthChecksRequest,
    ) -> list[Route53ARCListAssociatedRoute53HealthChecksResponse]:
        return await self._paginate('list_associated_route53_health_checks', request, Route53ARCListAssociatedRoute53HealthChecksResponse)

    async def list_clusters(
        self,
        request: Route53ARCListClustersRequest | None = None,
    ) -> Route53ARCListClustersResponse:
        client = self._require_client()
        return await self._execute(client.list_clusters, request, Route53ARCListClustersResponse)

    async def list_clusters_paginated(
        self,
        request: Route53ARCListClustersRequest | None = None,
    ) -> list[Route53ARCListClustersResponse]:
        return await self._paginate('list_clusters', request, Route53ARCListClustersResponse)

    async def list_control_panels(
        self,
        request: Route53ARCListControlPanelsRequest | None = None,
    ) -> Route53ARCListControlPanelsResponse:
        client = self._require_client()
        return await self._execute(client.list_control_panels, request, Route53ARCListControlPanelsResponse)

    async def list_control_panels_paginated(
        self,
        request: Route53ARCListControlPanelsRequest | None = None,
    ) -> list[Route53ARCListControlPanelsResponse]:
        return await self._paginate('list_control_panels', request, Route53ARCListControlPanelsResponse)

    async def list_routing_controls(
        self,
        request: Route53ARCListRoutingControlsRequest,
    ) -> Route53ARCListRoutingControlsResponse:
        client = self._require_client()
        return await self._execute(client.list_routing_controls, request, Route53ARCListRoutingControlsResponse)

    async def list_routing_controls_paginated(
        self,
        request: Route53ARCListRoutingControlsRequest,
    ) -> list[Route53ARCListRoutingControlsResponse]:
        return await self._paginate('list_routing_controls', request, Route53ARCListRoutingControlsResponse)

    async def list_safety_rules(
        self,
        request: Route53ARCListSafetyRulesRequest,
    ) -> Route53ARCListSafetyRulesResponse:
        client = self._require_client()
        return await self._execute(client.list_safety_rules, request, Route53ARCListSafetyRulesResponse)

    async def list_safety_rules_paginated(
        self,
        request: Route53ARCListSafetyRulesRequest,
    ) -> list[Route53ARCListSafetyRulesResponse]:
        return await self._paginate('list_safety_rules', request, Route53ARCListSafetyRulesResponse)

    async def list_tags_for_resource(
        self,
        request: Route53ARCListTagsForResourceRequest,
    ) -> Route53ARCListTagsForResourceResponse:
        client = self._require_client()
        return await self._execute(client.list_tags_for_resource, request, Route53ARCListTagsForResourceResponse)

    async def tag_resource(
        self,
        request: Route53ARCTagResourceRequest,
    ) -> Route53ARCTagResourceResponse:
        client = self._require_client()
        return await self._execute(client.tag_resource, request, Route53ARCTagResourceResponse)

    async def untag_resource(
        self,
        request: Route53ARCUntagResourceRequest,
    ) -> Route53ARCUntagResourceResponse:
        client = self._require_client()
        return await self._execute(client.untag_resource, request, Route53ARCUntagResourceResponse)

    async def update_cluster(
        self,
        request: Route53ARCUpdateClusterRequest,
    ) -> Route53ARCUpdateClusterResponse:
        client = self._require_client()
        return await self._execute(client.update_cluster, request, Route53ARCUpdateClusterResponse)

    async def update_control_panel(
        self,
        request: Route53ARCUpdateControlPanelRequest,
    ) -> Route53ARCUpdateControlPanelResponse:
        client = self._require_client()
        return await self._execute(client.update_control_panel, request, Route53ARCUpdateControlPanelResponse)

    async def update_routing_control(
        self,
        request: Route53ARCUpdateRoutingControlRequest,
    ) -> Route53ARCUpdateRoutingControlResponse:
        client = self._require_client()
        return await self._execute(client.update_routing_control, request, Route53ARCUpdateRoutingControlResponse)

    async def update_safety_rule(
        self,
        request: Route53ARCUpdateSafetyRuleRequest | None = None,
    ) -> Route53ARCUpdateSafetyRuleResponse:
        client = self._require_client()
        return await self._execute(client.update_safety_rule, request, Route53ARCUpdateSafetyRuleResponse)
