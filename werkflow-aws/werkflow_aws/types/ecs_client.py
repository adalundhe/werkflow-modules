from abc import ABC, abstractmethod
import datetime
from typing import Any
from botocore.paginate import Paginator


class ECSClient(ABC):

    @abstractmethod
    def associate_gateway_with_cluster(
        self,
        *,
        gateway: str,
        cluster: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def continue_service_deployment(
        self,
        *,
        serviceDeploymentArn: str,
        hookId: str,
        action: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_capacity_provider(
        self,
        *,
        name: str,
        cluster: str | None = None,
        autoScalingGroupProvider: dict[str, Any] | None = None,
        managedInstancesProvider: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_cluster(
        self,
        *,
        clusterName: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        settings: list[dict[str, Any]] | None = None,
        configuration: dict[str, Any] | None = None,
        capacityProviders: list[str] | None = None,
        defaultCapacityProviderStrategy: list[dict[str, Any]] | None = None,
        serviceConnectDefaults: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_daemon(
        self,
        *,
        daemonName: str,
        daemonTaskDefinitionArn: str,
        capacityProviderArns: list[str],
        clusterArn: str | None = None,
        deploymentConfiguration: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
        propagateTags: str | None = None,
        enableECSManagedTags: bool | None = None,
        enableExecuteCommand: bool | None = None,
        clientToken: str | None = None,
        critical: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_express_gateway_service(
        self,
        *,
        infrastructureRoleArn: str,
        executionRoleArn: str | None = None,
        serviceName: str | None = None,
        cluster: str | None = None,
        healthCheckPath: str | None = None,
        primaryContainer: dict[str, Any] | None = None,
        taskRoleArn: str | None = None,
        networkConfiguration: dict[str, Any] | None = None,
        cpu: str | None = None,
        memory: str | None = None,
        cpuArchitecture: str | None = None,
        scalingTarget: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
        taskDefinitionArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_gateway(
        self,
        *,
        name: str,
        infrastructureRoleArn: str,
        configuration: dict[str, Any],
        clientToken: str | None = None,
        deletionProtection: bool | None = None,
        tags: list[dict[str, Any]] | None = None,
        propagateTags: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_service(
        self,
        *,
        serviceName: str,
        cluster: str | None = None,
        taskDefinition: str | None = None,
        availabilityZoneRebalancing: str | None = None,
        loadBalancers: list[dict[str, Any]] | None = None,
        serviceRegistries: list[dict[str, Any]] | None = None,
        desiredCount: int | None = None,
        clientToken: str | None = None,
        launchType: str | None = None,
        capacityProviderStrategy: list[dict[str, Any]] | None = None,
        platformVersion: str | None = None,
        role: str | None = None,
        deploymentConfiguration: dict[str, Any] | None = None,
        placementConstraints: list[dict[str, Any]] | None = None,
        placementStrategy: list[dict[str, Any]] | None = None,
        networkConfiguration: dict[str, Any] | None = None,
        healthCheckGracePeriodSeconds: int | None = None,
        schedulingStrategy: str | None = None,
        deploymentController: dict[str, Any] | None = None,
        tags: list[dict[str, Any]] | None = None,
        enableECSManagedTags: bool | None = None,
        propagateTags: str | None = None,
        enableExecuteCommand: bool | None = None,
        serviceConnectConfiguration: dict[str, Any] | None = None,
        volumeConfigurations: list[dict[str, Any]] | None = None,
        vpcLatticeConfigurations: list[dict[str, Any]] | None = None,
        gatewayConnectors: list[dict[str, Any]] | None = None,
        monitoring: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def create_task_set(
        self,
        *,
        service: str,
        cluster: str,
        taskDefinition: str,
        externalId: str | None = None,
        networkConfiguration: dict[str, Any] | None = None,
        loadBalancers: list[dict[str, Any]] | None = None,
        serviceRegistries: list[dict[str, Any]] | None = None,
        launchType: str | None = None,
        capacityProviderStrategy: list[dict[str, Any]] | None = None,
        platformVersion: str | None = None,
        scale: dict[str, Any] | None = None,
        clientToken: str | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_account_setting(
        self,
        *,
        name: str,
        principalArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_attributes(
        self,
        *,
        attributes: list[dict[str, Any]],
        cluster: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_capacity_provider(
        self,
        *,
        capacityProvider: str,
        cluster: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_cluster(
        self,
        *,
        cluster: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_daemon(
        self,
        *,
        daemonArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_daemon_task_definition(
        self,
        *,
        daemonTaskDefinition: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_express_gateway_service(
        self,
        *,
        serviceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_gateway(
        self,
        *,
        gateway: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_service(
        self,
        *,
        service: str,
        cluster: str | None = None,
        force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_task_definitions(
        self,
        *,
        taskDefinitions: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def delete_task_set(
        self,
        *,
        cluster: str,
        service: str,
        taskSet: str,
        force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_container_instance(
        self,
        *,
        containerInstance: str,
        cluster: str | None = None,
        force: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def deregister_task_definition(
        self,
        *,
        taskDefinition: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_capacity_providers(
        self,
        *,
        capacityProviders: list[str] | None = None,
        cluster: str | None = None,
        include: list[str] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_clusters(
        self,
        *,
        clusters: list[str] | None = None,
        include: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_container_instances(
        self,
        *,
        containerInstances: list[str],
        cluster: str | None = None,
        include: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_daemon(
        self,
        *,
        daemonArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_daemon_deployments(
        self,
        *,
        daemonDeploymentArns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_daemon_revisions(
        self,
        *,
        daemonRevisionArns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_daemon_task_definition(
        self,
        *,
        daemonTaskDefinition: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_express_gateway_service(
        self,
        *,
        serviceArn: str,
        include: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_gateway(
        self,
        *,
        gateway: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_gateway_resources(
        self,
        *,
        gateway: str,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_gateway_route(
        self,
        *,
        gatewayRouteArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_service_deployments(
        self,
        *,
        serviceDeploymentArns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_service_revisions(
        self,
        *,
        serviceRevisionArns: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_services(
        self,
        *,
        services: list[str],
        cluster: str | None = None,
        include: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_task_definition(
        self,
        *,
        taskDefinition: str,
        include: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_task_sets(
        self,
        *,
        cluster: str,
        service: str,
        taskSets: list[str] | None = None,
        include: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def describe_tasks(
        self,
        *,
        tasks: list[str],
        cluster: str | None = None,
        include: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def disassociate_gateway_from_cluster(
        self,
        *,
        gateway: str,
        cluster: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def discover_poll_endpoint(
        self,
        *,
        containerInstance: str | None = None,
        cluster: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def execute_command(
        self,
        *,
        command: str,
        interactive: bool,
        task: str,
        cluster: str | None = None,
        container: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_task_protection(
        self,
        *,
        cluster: str,
        tasks: list[str] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_account_settings(
        self,
        *,
        name: str | None = None,
        value: str | None = None,
        principalArn: str | None = None,
        effectiveSettings: bool | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_attributes(
        self,
        *,
        targetType: str,
        cluster: str | None = None,
        attributeName: str | None = None,
        attributeValue: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_clusters(
        self,
        *,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_container_instances(
        self,
        *,
        cluster: str | None = None,
        filter: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        status: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_daemon_deployments(
        self,
        *,
        daemonArn: str,
        status: list[str] | None = None,
        createdAt: dict[str, Any] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_daemon_task_definitions(
        self,
        *,
        familyPrefix: str | None = None,
        family: str | None = None,
        revision: str | None = None,
        status: str | None = None,
        sort: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_daemons(
        self,
        *,
        clusterArn: str | None = None,
        capacityProviderArns: list[str] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_gateway_cluster_associations(
        self,
        *,
        gateway: str | None = None,
        cluster: str | None = None,
        status: list[str] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_gateway_routes(
        self,
        *,
        gateway: str | None = None,
        cluster: str | None = None,
        service: str | None = None,
        serviceContainerPortName: str | None = None,
        status: list[str] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_gateways(
        self,
        *,
        names: list[str] | None = None,
        status: list[str] | None = None,
        maxResults: int | None = None,
        nextToken: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_service_deployments(
        self,
        *,
        service: str,
        cluster: str | None = None,
        status: list[str] | None = None,
        createdAt: dict[str, Any] | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_services(
        self,
        *,
        cluster: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        launchType: str | None = None,
        schedulingStrategy: str | None = None,
        resourceManagementType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_services_by_namespace(
        self,
        *,
        namespace: str,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tags_for_resource(
        self,
        *,
        resourceArn: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_task_definition_families(
        self,
        *,
        familyPrefix: str | None = None,
        status: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_task_definitions(
        self,
        *,
        familyPrefix: str | None = None,
        status: str | None = None,
        sort: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def list_tasks(
        self,
        *,
        cluster: str | None = None,
        containerInstance: str | None = None,
        family: str | None = None,
        nextToken: str | None = None,
        maxResults: int | None = None,
        startedBy: str | None = None,
        serviceName: str | None = None,
        desiredStatus: str | None = None,
        launchType: str | None = None,
        daemonName: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_setting(
        self,
        *,
        name: str,
        value: str,
        principalArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_account_setting_default(
        self,
        *,
        name: str,
        value: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_attributes(
        self,
        *,
        attributes: list[dict[str, Any]],
        cluster: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def put_cluster_capacity_providers(
        self,
        *,
        cluster: str,
        capacityProviders: list[str],
        defaultCapacityProviderStrategy: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_container_instance(
        self,
        *,
        cluster: str | None = None,
        instanceIdentityDocument: str | None = None,
        instanceIdentityDocumentSignature: str | None = None,
        totalResources: list[dict[str, Any]] | None = None,
        versionInfo: dict[str, Any] | None = None,
        containerInstanceArn: str | None = None,
        attributes: list[dict[str, Any]] | None = None,
        platformDevices: list[dict[str, Any]] | None = None,
        tags: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_daemon_task_definition(
        self,
        *,
        family: str,
        containerDefinitions: list[dict[str, Any]],
        taskRoleArn: str | None = None,
        executionRoleArn: str | None = None,
        cpu: str | None = None,
        memory: str | None = None,
        volumes: list[dict[str, Any]] | None = None,
        tags: list[dict[str, Any]] | None = None,
        pidMode: str | None = None,
        ipcMode: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def register_task_definition(
        self,
        *,
        family: str,
        containerDefinitions: list[dict[str, Any]],
        taskRoleArn: str | None = None,
        executionRoleArn: str | None = None,
        networkMode: str | None = None,
        volumes: list[dict[str, Any]] | None = None,
        placementConstraints: list[dict[str, Any]] | None = None,
        requiresCompatibilities: list[str] | None = None,
        cpu: str | None = None,
        memory: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        pidMode: str | None = None,
        ipcMode: str | None = None,
        proxyConfiguration: dict[str, Any] | None = None,
        inferenceAccelerators: list[dict[str, Any]] | None = None,
        ephemeralStorage: dict[str, Any] | None = None,
        runtimePlatform: dict[str, Any] | None = None,
        enableFaultInjection: bool | None = None,
        trustedExecutionConfiguration: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def run_task(
        self,
        *,
        taskDefinition: str,
        capacityProviderStrategy: list[dict[str, Any]] | None = None,
        cluster: str | None = None,
        count: int | None = None,
        enableECSManagedTags: bool | None = None,
        enableExecuteCommand: bool | None = None,
        group: str | None = None,
        launchType: str | None = None,
        networkConfiguration: dict[str, Any] | None = None,
        overrides: dict[str, Any] | None = None,
        placementConstraints: list[dict[str, Any]] | None = None,
        placementStrategy: list[dict[str, Any]] | None = None,
        platformVersion: str | None = None,
        propagateTags: str | None = None,
        referenceId: str | None = None,
        startedBy: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        clientToken: str | None = None,
        volumeConfigurations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def start_task(
        self,
        *,
        containerInstances: list[str],
        taskDefinition: str,
        cluster: str | None = None,
        enableECSManagedTags: bool | None = None,
        enableExecuteCommand: bool | None = None,
        group: str | None = None,
        networkConfiguration: dict[str, Any] | None = None,
        overrides: dict[str, Any] | None = None,
        propagateTags: str | None = None,
        referenceId: str | None = None,
        startedBy: str | None = None,
        tags: list[dict[str, Any]] | None = None,
        volumeConfigurations: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_service_deployment(
        self,
        *,
        serviceDeploymentArn: str,
        stopType: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def stop_task(
        self,
        *,
        task: str,
        cluster: str | None = None,
        reason: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def submit_attachment_state_changes(
        self,
        *,
        attachments: list[dict[str, Any]],
        cluster: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def submit_container_state_change(
        self,
        *,
        cluster: str | None = None,
        task: str | None = None,
        containerName: str | None = None,
        runtimeId: str | None = None,
        status: str | None = None,
        exitCode: int | None = None,
        reason: str | None = None,
        networkBindings: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def submit_task_state_change(
        self,
        *,
        cluster: str | None = None,
        task: str | None = None,
        status: str | None = None,
        reason: str | None = None,
        containers: list[dict[str, Any]] | None = None,
        attachments: list[dict[str, Any]] | None = None,
        managedAgents: list[dict[str, Any]] | None = None,
        pullStartedAt: datetime.datetime | str | None = None,
        pullStoppedAt: datetime.datetime | str | None = None,
        executionStoppedAt: datetime.datetime | str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def tag_resource(
        self,
        *,
        resourceArn: str,
        tags: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def untag_resource(
        self,
        *,
        resourceArn: str,
        tagKeys: list[str],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_capacity_provider(
        self,
        *,
        name: str,
        cluster: str | None = None,
        autoScalingGroupProvider: dict[str, Any] | None = None,
        managedInstancesProvider: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cluster(
        self,
        *,
        cluster: str,
        settings: list[dict[str, Any]] | None = None,
        configuration: dict[str, Any] | None = None,
        serviceConnectDefaults: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_cluster_settings(
        self,
        *,
        cluster: str,
        settings: list[dict[str, Any]],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_container_agent(
        self,
        *,
        containerInstance: str,
        cluster: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_container_instances_state(
        self,
        *,
        containerInstances: list[str],
        status: str,
        cluster: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_daemon(
        self,
        *,
        daemonArn: str,
        daemonTaskDefinitionArn: str,
        capacityProviderArns: list[str],
        deploymentConfiguration: dict[str, Any] | None = None,
        propagateTags: str | None = None,
        enableECSManagedTags: bool | None = None,
        enableExecuteCommand: bool | None = None,
        critical: bool | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_express_gateway_service(
        self,
        *,
        serviceArn: str,
        executionRoleArn: str | None = None,
        healthCheckPath: str | None = None,
        primaryContainer: dict[str, Any] | None = None,
        taskRoleArn: str | None = None,
        networkConfiguration: dict[str, Any] | None = None,
        cpu: str | None = None,
        memory: str | None = None,
        cpuArchitecture: str | None = None,
        scalingTarget: dict[str, Any] | None = None,
        taskDefinitionArn: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_gateway(
        self,
        *,
        gateway: str,
        infrastructureRoleArn: str | None = None,
        deletionProtection: bool | None = None,
        configuration: dict[str, Any] | None = None,
        propagateTags: str | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_service(
        self,
        *,
        service: str,
        cluster: str | None = None,
        desiredCount: int | None = None,
        taskDefinition: str | None = None,
        capacityProviderStrategy: list[dict[str, Any]] | None = None,
        deploymentConfiguration: dict[str, Any] | None = None,
        availabilityZoneRebalancing: str | None = None,
        networkConfiguration: dict[str, Any] | None = None,
        placementConstraints: list[dict[str, Any]] | None = None,
        placementStrategy: list[dict[str, Any]] | None = None,
        platformVersion: str | None = None,
        forceNewDeployment: bool | None = None,
        healthCheckGracePeriodSeconds: int | None = None,
        deploymentController: dict[str, Any] | None = None,
        enableExecuteCommand: bool | None = None,
        enableECSManagedTags: bool | None = None,
        loadBalancers: list[dict[str, Any]] | None = None,
        propagateTags: str | None = None,
        serviceRegistries: list[dict[str, Any]] | None = None,
        serviceConnectConfiguration: dict[str, Any] | None = None,
        volumeConfigurations: list[dict[str, Any]] | None = None,
        vpcLatticeConfigurations: list[dict[str, Any]] | None = None,
        gatewayConnectors: list[dict[str, Any]] | None = None,
        monitoring: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_service_primary_task_set(
        self,
        *,
        cluster: str,
        service: str,
        primaryTaskSet: str,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_task_protection(
        self,
        *,
        cluster: str,
        tasks: list[str],
        protectionEnabled: bool,
        expiresInMinutes: int | None = None,
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def update_task_set(
        self,
        *,
        cluster: str,
        service: str,
        taskSet: str,
        scale: dict[str, Any],
    ) -> dict[str, Any]:
        pass

    @abstractmethod
    def get_paginator(self, operation_name: str) -> Paginator:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
