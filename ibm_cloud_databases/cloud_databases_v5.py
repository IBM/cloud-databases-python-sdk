# coding: utf-8

# (C) Copyright IBM Corp. 2021.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# IBM OpenAPI SDK Code Generator Version: 99-SNAPSHOT-1906c8c8-20210331-153014
 
"""
The IBM Cloud Databases API enables interaction between applications and Cloud Databases
database deployments.
Access to the API requires an IAM Bearer Token or an IAM API Key to be presented through
bearer authentication.
Deployment IDs are CRNs on the IBM Cloud Databases v5 API platform. No lookup or
translation the Compose style UUIDs is needed. The Deployment ID is a traditional UUID on
the Compose v5 API platform.
When you use CRNs, remember to URL escape the CRN value as they can include the
forward-slash (/) character.
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class CloudDatabasesV5(BaseService):
    """The Cloud Databases V5 service."""

    DEFAULT_SERVICE_URL = None
    DEFAULT_SERVICE_NAME = 'cloud_databases'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'CloudDatabasesV5':
        """
        Return a new client for the Cloud Databases service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Cloud Databases service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Deployments
    #########################


    def list_deployables(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List all deployable databases.

        Returns a list of all the types and associated major versions of database
        deployments that can be provisioned.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListDeployablesResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='list_deployables')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/deployables'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def list_regions(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List all deployable regions.

        Returns a list of all the regions that deployments can be provisioned into from
        the current region. Used to determine region availability for read-only replicas.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListRegionsResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='list_regions')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/regions'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_deployment_info(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get deployment information.

        Gets the full data that is associated with a deployment. This data includes the
        ID, name, database type, and version.

        :param str id: Deployment ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetDeploymentInfoResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='get_deployment_info')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Database Users
    #########################


    def create_database_user(self,
        id: str,
        user_type: str,
        *,
        user: 'CreateDatabaseUserRequestUser' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Creates a user based on user type.

        Creates a user in the database that can access the database through a connection.

        :param str id: Deployment ID.
        :param str user_type: User type.
        :param CreateDatabaseUserRequestUser user: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreateDatabaseUserResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if user_type is None:
            raise ValueError('user_type must be provided')
        if user is not None:
            user = convert_model(user)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='create_database_user')
        headers.update(sdk_headers)

        data = {
            'user': user
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id', 'user_type']
        path_param_values = self.encode_path_vars(id, user_type)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/users/{user_type}'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def change_user_password(self,
        id: str,
        user_type: str,
        username: str,
        *,
        user: 'APasswordSettingUser' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Set specified user's password.

        Sets the password of a specified user.

        :param str id: Deployment ID.
        :param str user_type: User type.
        :param str username: User ID.
        :param APasswordSettingUser user: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ChangeUserPasswordResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if user_type is None:
            raise ValueError('user_type must be provided')
        if username is None:
            raise ValueError('username must be provided')
        if user is not None:
            user = convert_model(user)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='change_user_password')
        headers.update(sdk_headers)

        data = {
            'user': user
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id', 'user_type', 'username']
        path_param_values = self.encode_path_vars(id, user_type, username)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/users/{user_type}/{username}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_database_user(self,
        id: str,
        user_type: str,
        username: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Deletes a user based on user type.

        Removes a user from the deployment.

        :param str id: Deployment ID.
        :param str user_type: User type.
        :param str username: Username.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteDatabaseUserResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if user_type is None:
            raise ValueError('user_type must be provided')
        if username is None:
            raise ValueError('username must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='delete_database_user')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id', 'user_type', 'username']
        path_param_values = self.encode_path_vars(id, user_type, username)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/users/{user_type}/{username}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Database Configuration
    #########################


    def update_database_configuration(self,
        id: str,
        configuration: 'SetConfigurationConfiguration',
        **kwargs
    ) -> DetailedResponse:
        """
        Change your database configuration.

        Change your database configuration. Available for PostgreSQL, EnterpriseDB, and
        Redis ONLY.

        :param str id: Deployment ID.
        :param SetConfigurationConfiguration configuration:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UpdateDatabaseConfigurationResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if configuration is None:
            raise ValueError('configuration must be provided')
        configuration = convert_model(configuration)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='update_database_configuration')
        headers.update(sdk_headers)

        data = {
            'configuration': configuration
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/configuration'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Remotes
    #########################


    def list_remotes(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        List read-only replica information.

        Get the read-only replicas associated with a deployment. Available for PostgreSQL
        and EnterpriseDB ONLY.

        :param str id: Deployment ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListRemotesResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='list_remotes')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/remotes'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def resync_replica(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Resync read-only replica.

        Reinitialize a read-only replica. Available for PostgreSQL and EnterpriseDB ONLY.

        :param str id: Deployment ID of the read-only replica.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResyncReplicaResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='resync_replica')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/remotes/resync'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def set_promotion(self,
        id: str,
        promotion: 'SetPromotionPromotion',
        **kwargs
    ) -> DetailedResponse:
        """
        Promote read-only replica to a full deployment.

        Promote a read-only replica or upgrade and promote a read-only replica. Available
        for PostgreSQL and EnterpriseDB ONLY.

        :param str id: Deployment ID of the read-only replica to promote.
        :param SetPromotionPromotion promotion:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SetPromotionResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if promotion is None:
            raise ValueError('promotion must be provided')
        promotion = convert_model(promotion)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='set_promotion')
        headers.update(sdk_headers)

        data = {
            'Promotion': promotion
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/remotes/promotion'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Tasks
    #########################


    def list_deployment_tasks(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        List currently running tasks on a deployment.

        Obtain a list of tasks currently running or recently run on a deployment. Tasks
        are ephemeral. Records of successful tasks are shown for 24-48 hours, and
        unsuccessful tasks are shown for 7-8 days.

        :param str id: Deployment ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Tasks` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='list_deployment_tasks')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/tasks'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_task(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get information about a task.

        Get information about a task and its status. Tasks themselves are persistent so
        old tasks can be consulted as well as running tasks.

        :param str id: Task ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetTaskResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='get_task')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tasks/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Backups
    #########################


    def get_backup_info(self,
        backup_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get information about a backup.

        Get information about a backup, such as creation date.

        :param str backup_id: Backup ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetBackupInfoResponse` object
        """

        if backup_id is None:
            raise ValueError('backup_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='get_backup_info')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['backup_id']
        path_param_values = self.encode_path_vars(backup_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/backups/{backup_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def list_deployment_backups(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        List currently available backups from a deployment.

        Get details of all currently available backups from a deployment.

        :param str id: Deployment ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Backups` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='list_deployment_backups')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/backups'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def start_ondemand_backup(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Initiate an on-demand backup.

        Signal the platform to create an on-demand backup for the specified deployment.
        The returned task can be polled to track progress of the backup as it takes place.

        :param str id: Deployment ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `StartOndemandBackupResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='start_ondemand_backup')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/backups'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_pit_rdata(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get earliest point-in-time-recovery timestamp.

        Returns the earliest available time for point-in-time-recovery in ISO8601 UTC
        format. PostgreSQL and EnterpriseDB only.

        :param str id: Deployment ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PointInTimeRecoveryData` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='get_pit_rdata')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/point_in_time_recovery_data'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Connections
    #########################


    def get_connection(self,
        id: str,
        user_type: str,
        user_id: str,
        endpoint_type: str,
        *,
        certificate_root: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Discover connection information for a deployment for a user with an endpoint type.

        Discover connection information for a deployment for a user with an endpoint type.

        :param str id: Deployment ID.
        :param str user_type: User type.
        :param str user_id: User ID.
        :param str endpoint_type: Endpoint Type. The endpoint must be enabled on
               the deployment before its connection information can be fetched.
        :param str certificate_root: (optional) Optional certificate root path to
               prepend certificate names. Certificates would be stored in this directory
               for use by other commands.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Connection` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if user_type is None:
            raise ValueError('user_type must be provided')
        if user_id is None:
            raise ValueError('user_id must be provided')
        if endpoint_type is None:
            raise ValueError('endpoint_type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='get_connection')
        headers.update(sdk_headers)

        params = {
            'certificate_root': certificate_root
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id', 'user_type', 'user_id', 'endpoint_type']
        path_param_values = self.encode_path_vars(id, user_type, user_id, endpoint_type)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/users/{user_type}/{user_id}/connections/{endpoint_type}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def complete_connection(self,
        id: str,
        user_type: str,
        user_id: str,
        endpoint_type: str,
        *,
        password: str = None,
        certificate_root: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Discover connection information for a deployment for a user with substitutions and an endpoint type.

        Discover connection information for a deployment for a user. Behaves the same as
        the GET method but substitutes the provided password parameter into the returned
        connection information.

        :param str id: Deployment ID.
        :param str user_type: User type of `database` is the only currently
               supported value.
        :param str user_id: User ID.
        :param str endpoint_type: Endpoint Type. The select endpoint must be
               enabled on the deployment before its connection information can be fetched.
        :param str password: (optional) Password to be substituted into the
               response.
        :param str certificate_root: (optional) Optional certificate root path to
               prepend certificate names. Certificates would be stored in this directory
               for use by other commands.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Connection` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if user_type is None:
            raise ValueError('user_type must be provided')
        if user_id is None:
            raise ValueError('user_id must be provided')
        if endpoint_type is None:
            raise ValueError('endpoint_type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='complete_connection')
        headers.update(sdk_headers)

        data = {
            'password': password,
            'certificate_root': certificate_root
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id', 'user_type', 'user_id', 'endpoint_type']
        path_param_values = self.encode_path_vars(id, user_type, user_id, endpoint_type)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/users/{user_type}/{user_id}/connections/{endpoint_type}'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Scaling
    #########################


    def list_deployment_scaling_groups(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        List currently available scaling groups from a deployment.

        Scaling groups represent the various resources that are allocated to a deployment.
        This command allows for the retrieval of all of the groups for a particular
        deployment.

        :param str id: Deployment ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Groups` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='list_deployment_scaling_groups')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/groups'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_default_scaling_groups(self,
        type: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get default scaling groups for a new deployment.

        Scaling groups represent the various resources allocated to a deployment. When a
        new deployment is created, there are a set of defaults for each database type.
        This endpoint returns them for a particular database.

        :param str type: Database type name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Groups` object
        """

        if type is None:
            raise ValueError('type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='get_default_scaling_groups')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['type']
        path_param_values = self.encode_path_vars(type)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployables/{type}/groups'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def set_deployment_scaling_group(self,
        id: str,
        group_id: str,
        set_deployment_scaling_group_request: 'SetDeploymentScalingGroupRequest',
        **kwargs
    ) -> DetailedResponse:
        """
        Set scaling values on a specified group.

        Set scaling value on a specified group. Can only be performed on
        is_adjustable=true groups. Values set are for the group as a whole and resources
        are distributed amongst the group. Values must be greater than or equal to the
        minimum size and must be a multiple of the step size.

        :param str id: Deployment ID.
        :param str group_id: Group Id.
        :param SetDeploymentScalingGroupRequest
               set_deployment_scaling_group_request: Scaling group settings.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SetDeploymentScalingGroupResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if group_id is None:
            raise ValueError('group_id must be provided')
        if set_deployment_scaling_group_request is None:
            raise ValueError('set_deployment_scaling_group_request must be provided')
        if isinstance(set_deployment_scaling_group_request, SetDeploymentScalingGroupRequest):
            set_deployment_scaling_group_request = convert_model(set_deployment_scaling_group_request)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='set_deployment_scaling_group')
        headers.update(sdk_headers)

        data = json.dumps(set_deployment_scaling_group_request)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id', 'group_id']
        path_param_values = self.encode_path_vars(id, group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/groups/{group_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Autoscaling
    #########################


    def get_autoscaling_conditions(self,
        id: str,
        group_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the autoscaling configuration from a deployment.

        The Autoscaling configuration represents the various conditions that control
        autoscaling for a deployment. This command allows for the retrieval of all
        autoscaling conditions for a particular deployment.

        :param str id: Deployment ID.
        :param str group_id: Group ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AutoscalingGroup` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if group_id is None:
            raise ValueError('group_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='get_autoscaling_conditions')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id', 'group_id']
        path_param_values = self.encode_path_vars(id, group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/groups/{group_id}/autoscaling'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def set_autoscaling_conditions(self,
        id: str,
        group_id: str,
        autoscaling: 'AutoscalingSetGroupAutoscaling',
        **kwargs
    ) -> DetailedResponse:
        """
        Set the autoscaling configuration from a deployment.

        Enable, disable, or set the conditions for autoscaling on your deployment. Memory,
        disk, and CPU (if available) can be set separately and are not all required.

        :param str id: Deployment ID.
        :param str group_id: Group ID.
        :param AutoscalingSetGroupAutoscaling autoscaling:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SetAutoscalingConditionsResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if group_id is None:
            raise ValueError('group_id must be provided')
        if autoscaling is None:
            raise ValueError('autoscaling must be provided')
        autoscaling = convert_model(autoscaling)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='set_autoscaling_conditions')
        headers.update(sdk_headers)

        data = {
            'autoscaling': autoscaling
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id', 'group_id']
        path_param_values = self.encode_path_vars(id, group_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/groups/{group_id}/autoscaling'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Management
    #########################


    def kill_connections(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Kill connections to a PostgreSQL or EnterpriseDB deployment.

        Closes all the connections on a deployment. Available for PostgreSQL and
        EnterpriseDB ONLY.

        :param str id: Deployment ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `KillConnectionsResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='kill_connections')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/management/database_connections'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Security
    #########################


    def get_allowlist(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve the allowlisted addresses and ranges for a deployment.

        Retrieve the allowlisted addresses and ranges for a deployment.

        :param str id: Deployment ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Allowlist` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='get_allowlist')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/whitelists/ip_addresses'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def set_allowlist(self,
        id: str,
        *,
        ip_addresses: List['AllowlistEntry'] = None,
        if_match: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Set the allowlist for a deployment.

        Set the allowlist for a deployment. This action overwrites all existing entries,
        so when you modify the allowlist via a GET/update/PUT, provide the GET response's
        ETag header value in this endpoint's If-Match header to ensure that changes that
        are made by other clients are not accidentally overwritten.

        :param str id: Deployment ID.
        :param List[AllowlistEntry] ip_addresses: (optional) An array of allowlist
               entries.
        :param str if_match: (optional) Verify that the current allowlist matches a
               provided ETag value. Use in conjunction with the GET operation's ETag
               header to ensure synchronicity between clients.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SetAllowlistResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if ip_addresses is not None:
            ip_addresses = [convert_model(x) for x in ip_addresses]
        headers = {
            'If-Match': if_match
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='set_allowlist')
        headers.update(sdk_headers)

        data = {
            'ip_addresses': ip_addresses
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/whitelists/ip_addresses'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def add_allowlist_entry(self,
        id: str,
        *,
        ip_address: 'AllowlistEntry' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Add an address or range to the allowlist for a deployment.

        Add an address or range to the allowlist for a deployment.

        :param str id: Deployment ID.
        :param AllowlistEntry ip_address: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AddAllowlistEntryResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if ip_address is not None:
            ip_address = convert_model(ip_address)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='add_allowlist_entry')
        headers.update(sdk_headers)

        data = {
            'ip_address': ip_address
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/whitelists/ip_addresses'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_allowlist_entry(self,
        id: str,
        ipaddress: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete an address or range from the allowlist of a deployment.

        Delete an address or range from the allowlist of a deployment.

        :param str id: Deployment ID.
        :param str ipaddress: An IPv4 address or a CIDR range (netmasked IPv4
               address).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteAllowlistEntryResponse` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if ipaddress is None:
            raise ValueError('ipaddress must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V5',
                                      operation_id='delete_allowlist_entry')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['id', 'ipaddress']
        path_param_values = self.encode_path_vars(id, ipaddress)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/deployments/{id}/whitelists/ip_addresses/{ipaddress}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


class GetConnectionEnums:
    """
    Enums for get_connection parameters.
    """

    class EndpointType(str, Enum):
        """
        Endpoint Type. The endpoint must be enabled on the deployment before its
        connection information can be fetched.
        """
        PUBLIC = 'public'
        PRIVATE = 'private'


class CompleteConnectionEnums:
    """
    Enums for complete_connection parameters.
    """

    class EndpointType(str, Enum):
        """
        Endpoint Type. The select endpoint must be enabled on the deployment before its
        connection information can be fetched.
        """
        PUBLIC = 'public'
        PRIVATE = 'private'


class GetDefaultScalingGroupsEnums:
    """
    Enums for get_default_scaling_groups parameters.
    """

    class Type(str, Enum):
        """
        Database type name.
        """
        POSTGRESQL = 'postgresql'
        ETCD = 'etcd'


##############################################################################
# Models
##############################################################################


class APasswordSettingUser():
    """
    APasswordSettingUser.

    :attr str password: (optional)
    """

    def __init__(self,
                 *,
                 password: str = None) -> None:
        """
        Initialize a APasswordSettingUser object.

        :param str password: (optional)
        """
        self.password = password

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'APasswordSettingUser':
        """Initialize a APasswordSettingUser object from a json dictionary."""
        args = {}
        if 'password' in _dict:
            args['password'] = _dict.get('password')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a APasswordSettingUser object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this APasswordSettingUser object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'APasswordSettingUser') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'APasswordSettingUser') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AddAllowlistEntryResponse():
    """
    AddAllowlistEntryResponse.

    :attr Task task: (optional)
    """

    def __init__(self,
                 *,
                 task: 'Task' = None) -> None:
        """
        Initialize a AddAllowlistEntryResponse object.

        :param Task task: (optional)
        """
        self.task = task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AddAllowlistEntryResponse':
        """Initialize a AddAllowlistEntryResponse object from a json dictionary."""
        args = {}
        if 'task' in _dict:
            args['task'] = Task.from_dict(_dict.get('task'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AddAllowlistEntryResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'task') and self.task is not None:
            _dict['task'] = self.task.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AddAllowlistEntryResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AddAllowlistEntryResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AddAllowlistEntryResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Allowlist():
    """
    Allowlist.

    :attr List[AllowlistEntry] ip_addresses: (optional) An array of allowlist
          entries.
    """

    def __init__(self,
                 *,
                 ip_addresses: List['AllowlistEntry'] = None) -> None:
        """
        Initialize a Allowlist object.

        :param List[AllowlistEntry] ip_addresses: (optional) An array of allowlist
               entries.
        """
        self.ip_addresses = ip_addresses

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Allowlist':
        """Initialize a Allowlist object from a json dictionary."""
        args = {}
        if 'ip_addresses' in _dict:
            args['ip_addresses'] = [AllowlistEntry.from_dict(x) for x in _dict.get('ip_addresses')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Allowlist object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ip_addresses') and self.ip_addresses is not None:
            _dict['ip_addresses'] = [x.to_dict() for x in self.ip_addresses]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Allowlist object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Allowlist') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Allowlist') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AllowlistEntry():
    """
    AllowlistEntry.

    :attr str address: (optional) An IPv4 address or a CIDR range (netmasked IPv4
          address).
    :attr str description: (optional) A human readable description of the address or
          range for identification purposes.
    """

    def __init__(self,
                 *,
                 address: str = None,
                 description: str = None) -> None:
        """
        Initialize a AllowlistEntry object.

        :param str address: (optional) An IPv4 address or a CIDR range (netmasked
               IPv4 address).
        :param str description: (optional) A human readable description of the
               address or range for identification purposes.
        """
        self.address = address
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AllowlistEntry':
        """Initialize a AllowlistEntry object from a json dictionary."""
        args = {}
        if 'address' in _dict:
            args['address'] = _dict.get('address')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AllowlistEntry object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'address') and self.address is not None:
            _dict['address'] = self.address
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AllowlistEntry object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AllowlistEntry') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AllowlistEntry') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingCPUGroupCPU():
    """
    AutoscalingCPUGroupCPU.

    :attr object scalers: (optional)
    :attr AutoscalingCPUGroupCPURate rate: (optional)
    """

    def __init__(self,
                 *,
                 scalers: object = None,
                 rate: 'AutoscalingCPUGroupCPURate' = None) -> None:
        """
        Initialize a AutoscalingCPUGroupCPU object.

        :param object scalers: (optional)
        :param AutoscalingCPUGroupCPURate rate: (optional)
        """
        self.scalers = scalers
        self.rate = rate

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingCPUGroupCPU':
        """Initialize a AutoscalingCPUGroupCPU object from a json dictionary."""
        args = {}
        if 'scalers' in _dict:
            args['scalers'] = _dict.get('scalers')
        if 'rate' in _dict:
            args['rate'] = AutoscalingCPUGroupCPURate.from_dict(_dict.get('rate'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingCPUGroupCPU object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'scalers') and self.scalers is not None:
            _dict['scalers'] = self.scalers
        if hasattr(self, 'rate') and self.rate is not None:
            _dict['rate'] = self.rate.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingCPUGroupCPU object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingCPUGroupCPU') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingCPUGroupCPU') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingCPUGroupCPURate():
    """
    AutoscalingCPUGroupCPURate.

    :attr float increase_percent: (optional)
    :attr int period_seconds: (optional)
    :attr int limit_count_per_member: (optional)
    :attr str units: (optional)
    """

    def __init__(self,
                 *,
                 increase_percent: float = None,
                 period_seconds: int = None,
                 limit_count_per_member: int = None,
                 units: str = None) -> None:
        """
        Initialize a AutoscalingCPUGroupCPURate object.

        :param float increase_percent: (optional)
        :param int period_seconds: (optional)
        :param int limit_count_per_member: (optional)
        :param str units: (optional)
        """
        self.increase_percent = increase_percent
        self.period_seconds = period_seconds
        self.limit_count_per_member = limit_count_per_member
        self.units = units

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingCPUGroupCPURate':
        """Initialize a AutoscalingCPUGroupCPURate object from a json dictionary."""
        args = {}
        if 'increase_percent' in _dict:
            args['increase_percent'] = _dict.get('increase_percent')
        if 'period_seconds' in _dict:
            args['period_seconds'] = _dict.get('period_seconds')
        if 'limit_count_per_member' in _dict:
            args['limit_count_per_member'] = _dict.get('limit_count_per_member')
        if 'units' in _dict:
            args['units'] = _dict.get('units')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingCPUGroupCPURate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'increase_percent') and self.increase_percent is not None:
            _dict['increase_percent'] = self.increase_percent
        if hasattr(self, 'period_seconds') and self.period_seconds is not None:
            _dict['period_seconds'] = self.period_seconds
        if hasattr(self, 'limit_count_per_member') and self.limit_count_per_member is not None:
            _dict['limit_count_per_member'] = self.limit_count_per_member
        if hasattr(self, 'units') and self.units is not None:
            _dict['units'] = self.units
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingCPUGroupCPURate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingCPUGroupCPURate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingCPUGroupCPURate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingDiskGroupDisk():
    """
    AutoscalingDiskGroupDisk.

    :attr AutoscalingDiskGroupDiskScalers scalers: (optional)
    :attr AutoscalingDiskGroupDiskRate rate: (optional)
    """

    def __init__(self,
                 *,
                 scalers: 'AutoscalingDiskGroupDiskScalers' = None,
                 rate: 'AutoscalingDiskGroupDiskRate' = None) -> None:
        """
        Initialize a AutoscalingDiskGroupDisk object.

        :param AutoscalingDiskGroupDiskScalers scalers: (optional)
        :param AutoscalingDiskGroupDiskRate rate: (optional)
        """
        self.scalers = scalers
        self.rate = rate

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingDiskGroupDisk':
        """Initialize a AutoscalingDiskGroupDisk object from a json dictionary."""
        args = {}
        if 'scalers' in _dict:
            args['scalers'] = AutoscalingDiskGroupDiskScalers.from_dict(_dict.get('scalers'))
        if 'rate' in _dict:
            args['rate'] = AutoscalingDiskGroupDiskRate.from_dict(_dict.get('rate'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingDiskGroupDisk object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'scalers') and self.scalers is not None:
            _dict['scalers'] = self.scalers.to_dict()
        if hasattr(self, 'rate') and self.rate is not None:
            _dict['rate'] = self.rate.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingDiskGroupDisk object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingDiskGroupDisk') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingDiskGroupDisk') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingDiskGroupDiskRate():
    """
    AutoscalingDiskGroupDiskRate.

    :attr float increase_percent: (optional)
    :attr int period_seconds: (optional)
    :attr float limit_mb_per_member: (optional)
    :attr str units: (optional)
    """

    def __init__(self,
                 *,
                 increase_percent: float = None,
                 period_seconds: int = None,
                 limit_mb_per_member: float = None,
                 units: str = None) -> None:
        """
        Initialize a AutoscalingDiskGroupDiskRate object.

        :param float increase_percent: (optional)
        :param int period_seconds: (optional)
        :param float limit_mb_per_member: (optional)
        :param str units: (optional)
        """
        self.increase_percent = increase_percent
        self.period_seconds = period_seconds
        self.limit_mb_per_member = limit_mb_per_member
        self.units = units

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingDiskGroupDiskRate':
        """Initialize a AutoscalingDiskGroupDiskRate object from a json dictionary."""
        args = {}
        if 'increase_percent' in _dict:
            args['increase_percent'] = _dict.get('increase_percent')
        if 'period_seconds' in _dict:
            args['period_seconds'] = _dict.get('period_seconds')
        if 'limit_mb_per_member' in _dict:
            args['limit_mb_per_member'] = _dict.get('limit_mb_per_member')
        if 'units' in _dict:
            args['units'] = _dict.get('units')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingDiskGroupDiskRate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'increase_percent') and self.increase_percent is not None:
            _dict['increase_percent'] = self.increase_percent
        if hasattr(self, 'period_seconds') and self.period_seconds is not None:
            _dict['period_seconds'] = self.period_seconds
        if hasattr(self, 'limit_mb_per_member') and self.limit_mb_per_member is not None:
            _dict['limit_mb_per_member'] = self.limit_mb_per_member
        if hasattr(self, 'units') and self.units is not None:
            _dict['units'] = self.units
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingDiskGroupDiskRate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingDiskGroupDiskRate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingDiskGroupDiskRate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingDiskGroupDiskScalers():
    """
    AutoscalingDiskGroupDiskScalers.

    :attr AutoscalingDiskGroupDiskScalersCapacity capacity: (optional)
    :attr AutoscalingDiskGroupDiskScalersIoUtilization io_utilization: (optional)
    """

    def __init__(self,
                 *,
                 capacity: 'AutoscalingDiskGroupDiskScalersCapacity' = None,
                 io_utilization: 'AutoscalingDiskGroupDiskScalersIoUtilization' = None) -> None:
        """
        Initialize a AutoscalingDiskGroupDiskScalers object.

        :param AutoscalingDiskGroupDiskScalersCapacity capacity: (optional)
        :param AutoscalingDiskGroupDiskScalersIoUtilization io_utilization:
               (optional)
        """
        self.capacity = capacity
        self.io_utilization = io_utilization

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingDiskGroupDiskScalers':
        """Initialize a AutoscalingDiskGroupDiskScalers object from a json dictionary."""
        args = {}
        if 'capacity' in _dict:
            args['capacity'] = AutoscalingDiskGroupDiskScalersCapacity.from_dict(_dict.get('capacity'))
        if 'io_utilization' in _dict:
            args['io_utilization'] = AutoscalingDiskGroupDiskScalersIoUtilization.from_dict(_dict.get('io_utilization'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingDiskGroupDiskScalers object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'capacity') and self.capacity is not None:
            _dict['capacity'] = self.capacity.to_dict()
        if hasattr(self, 'io_utilization') and self.io_utilization is not None:
            _dict['io_utilization'] = self.io_utilization.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingDiskGroupDiskScalers object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingDiskGroupDiskScalers') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingDiskGroupDiskScalers') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingDiskGroupDiskScalersCapacity():
    """
    AutoscalingDiskGroupDiskScalersCapacity.

    :attr bool enabled: (optional)
    :attr int free_space_less_than_percent: (optional)
    """

    def __init__(self,
                 *,
                 enabled: bool = None,
                 free_space_less_than_percent: int = None) -> None:
        """
        Initialize a AutoscalingDiskGroupDiskScalersCapacity object.

        :param bool enabled: (optional)
        :param int free_space_less_than_percent: (optional)
        """
        self.enabled = enabled
        self.free_space_less_than_percent = free_space_less_than_percent

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingDiskGroupDiskScalersCapacity':
        """Initialize a AutoscalingDiskGroupDiskScalersCapacity object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'free_space_less_than_percent' in _dict:
            args['free_space_less_than_percent'] = _dict.get('free_space_less_than_percent')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingDiskGroupDiskScalersCapacity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'free_space_less_than_percent') and self.free_space_less_than_percent is not None:
            _dict['free_space_less_than_percent'] = self.free_space_less_than_percent
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingDiskGroupDiskScalersCapacity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingDiskGroupDiskScalersCapacity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingDiskGroupDiskScalersCapacity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingDiskGroupDiskScalersIoUtilization():
    """
    AutoscalingDiskGroupDiskScalersIoUtilization.

    :attr bool enabled: (optional)
    :attr str over_period: (optional)
    :attr int above_percent: (optional)
    """

    def __init__(self,
                 *,
                 enabled: bool = None,
                 over_period: str = None,
                 above_percent: int = None) -> None:
        """
        Initialize a AutoscalingDiskGroupDiskScalersIoUtilization object.

        :param bool enabled: (optional)
        :param str over_period: (optional)
        :param int above_percent: (optional)
        """
        self.enabled = enabled
        self.over_period = over_period
        self.above_percent = above_percent

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingDiskGroupDiskScalersIoUtilization':
        """Initialize a AutoscalingDiskGroupDiskScalersIoUtilization object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'over_period' in _dict:
            args['over_period'] = _dict.get('over_period')
        if 'above_percent' in _dict:
            args['above_percent'] = _dict.get('above_percent')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingDiskGroupDiskScalersIoUtilization object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'over_period') and self.over_period is not None:
            _dict['over_period'] = self.over_period
        if hasattr(self, 'above_percent') and self.above_percent is not None:
            _dict['above_percent'] = self.above_percent
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingDiskGroupDiskScalersIoUtilization object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingDiskGroupDiskScalersIoUtilization') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingDiskGroupDiskScalersIoUtilization') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingGroup():
    """
    AutoscalingGroup.

    :attr AutoscalingGroupAutoscaling autoscaling:
    """

    def __init__(self,
                 autoscaling: 'AutoscalingGroupAutoscaling') -> None:
        """
        Initialize a AutoscalingGroup object.

        :param AutoscalingGroupAutoscaling autoscaling:
        """
        self.autoscaling = autoscaling

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingGroup':
        """Initialize a AutoscalingGroup object from a json dictionary."""
        args = {}
        if 'autoscaling' in _dict:
            args['autoscaling'] = AutoscalingGroupAutoscaling.from_dict(_dict.get('autoscaling'))
        else:
            raise ValueError('Required property \'autoscaling\' not present in AutoscalingGroup JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'autoscaling') and self.autoscaling is not None:
            _dict['autoscaling'] = self.autoscaling.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingGroupAutoscaling():
    """
    AutoscalingGroupAutoscaling.

    :attr AutoscalingDiskGroupDisk disk: (optional)
    :attr AutoscalingMemoryGroupMemory memory: (optional)
    :attr AutoscalingCPUGroupCPU cpu: (optional)
    """

    def __init__(self,
                 *,
                 disk: 'AutoscalingDiskGroupDisk' = None,
                 memory: 'AutoscalingMemoryGroupMemory' = None,
                 cpu: 'AutoscalingCPUGroupCPU' = None) -> None:
        """
        Initialize a AutoscalingGroupAutoscaling object.

        :param AutoscalingDiskGroupDisk disk: (optional)
        :param AutoscalingMemoryGroupMemory memory: (optional)
        :param AutoscalingCPUGroupCPU cpu: (optional)
        """
        self.disk = disk
        self.memory = memory
        self.cpu = cpu

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingGroupAutoscaling':
        """Initialize a AutoscalingGroupAutoscaling object from a json dictionary."""
        args = {}
        if 'disk' in _dict:
            args['disk'] = AutoscalingDiskGroupDisk.from_dict(_dict.get('disk'))
        if 'memory' in _dict:
            args['memory'] = AutoscalingMemoryGroupMemory.from_dict(_dict.get('memory'))
        if 'cpu' in _dict:
            args['cpu'] = AutoscalingCPUGroupCPU.from_dict(_dict.get('cpu'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingGroupAutoscaling object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'disk') and self.disk is not None:
            _dict['disk'] = self.disk.to_dict()
        if hasattr(self, 'memory') and self.memory is not None:
            _dict['memory'] = self.memory.to_dict()
        if hasattr(self, 'cpu') and self.cpu is not None:
            _dict['cpu'] = self.cpu.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingGroupAutoscaling object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingGroupAutoscaling') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingGroupAutoscaling') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingMemoryGroupMemory():
    """
    AutoscalingMemoryGroupMemory.

    :attr AutoscalingMemoryGroupMemoryScalers scalers: (optional)
    :attr AutoscalingMemoryGroupMemoryRate rate: (optional)
    """

    def __init__(self,
                 *,
                 scalers: 'AutoscalingMemoryGroupMemoryScalers' = None,
                 rate: 'AutoscalingMemoryGroupMemoryRate' = None) -> None:
        """
        Initialize a AutoscalingMemoryGroupMemory object.

        :param AutoscalingMemoryGroupMemoryScalers scalers: (optional)
        :param AutoscalingMemoryGroupMemoryRate rate: (optional)
        """
        self.scalers = scalers
        self.rate = rate

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingMemoryGroupMemory':
        """Initialize a AutoscalingMemoryGroupMemory object from a json dictionary."""
        args = {}
        if 'scalers' in _dict:
            args['scalers'] = AutoscalingMemoryGroupMemoryScalers.from_dict(_dict.get('scalers'))
        if 'rate' in _dict:
            args['rate'] = AutoscalingMemoryGroupMemoryRate.from_dict(_dict.get('rate'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingMemoryGroupMemory object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'scalers') and self.scalers is not None:
            _dict['scalers'] = self.scalers.to_dict()
        if hasattr(self, 'rate') and self.rate is not None:
            _dict['rate'] = self.rate.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingMemoryGroupMemory object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingMemoryGroupMemory') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingMemoryGroupMemory') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingMemoryGroupMemoryRate():
    """
    AutoscalingMemoryGroupMemoryRate.

    :attr float increase_percent: (optional)
    :attr int period_seconds: (optional)
    :attr float limit_mb_per_member: (optional)
    :attr str units: (optional)
    """

    def __init__(self,
                 *,
                 increase_percent: float = None,
                 period_seconds: int = None,
                 limit_mb_per_member: float = None,
                 units: str = None) -> None:
        """
        Initialize a AutoscalingMemoryGroupMemoryRate object.

        :param float increase_percent: (optional)
        :param int period_seconds: (optional)
        :param float limit_mb_per_member: (optional)
        :param str units: (optional)
        """
        self.increase_percent = increase_percent
        self.period_seconds = period_seconds
        self.limit_mb_per_member = limit_mb_per_member
        self.units = units

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingMemoryGroupMemoryRate':
        """Initialize a AutoscalingMemoryGroupMemoryRate object from a json dictionary."""
        args = {}
        if 'increase_percent' in _dict:
            args['increase_percent'] = _dict.get('increase_percent')
        if 'period_seconds' in _dict:
            args['period_seconds'] = _dict.get('period_seconds')
        if 'limit_mb_per_member' in _dict:
            args['limit_mb_per_member'] = _dict.get('limit_mb_per_member')
        if 'units' in _dict:
            args['units'] = _dict.get('units')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingMemoryGroupMemoryRate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'increase_percent') and self.increase_percent is not None:
            _dict['increase_percent'] = self.increase_percent
        if hasattr(self, 'period_seconds') and self.period_seconds is not None:
            _dict['period_seconds'] = self.period_seconds
        if hasattr(self, 'limit_mb_per_member') and self.limit_mb_per_member is not None:
            _dict['limit_mb_per_member'] = self.limit_mb_per_member
        if hasattr(self, 'units') and self.units is not None:
            _dict['units'] = self.units
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingMemoryGroupMemoryRate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingMemoryGroupMemoryRate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingMemoryGroupMemoryRate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingMemoryGroupMemoryScalers():
    """
    AutoscalingMemoryGroupMemoryScalers.

    :attr AutoscalingMemoryGroupMemoryScalersIoUtilization io_utilization:
          (optional)
    """

    def __init__(self,
                 *,
                 io_utilization: 'AutoscalingMemoryGroupMemoryScalersIoUtilization' = None) -> None:
        """
        Initialize a AutoscalingMemoryGroupMemoryScalers object.

        :param AutoscalingMemoryGroupMemoryScalersIoUtilization io_utilization:
               (optional)
        """
        self.io_utilization = io_utilization

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingMemoryGroupMemoryScalers':
        """Initialize a AutoscalingMemoryGroupMemoryScalers object from a json dictionary."""
        args = {}
        if 'io_utilization' in _dict:
            args['io_utilization'] = AutoscalingMemoryGroupMemoryScalersIoUtilization.from_dict(_dict.get('io_utilization'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingMemoryGroupMemoryScalers object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'io_utilization') and self.io_utilization is not None:
            _dict['io_utilization'] = self.io_utilization.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingMemoryGroupMemoryScalers object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingMemoryGroupMemoryScalers') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingMemoryGroupMemoryScalers') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingMemoryGroupMemoryScalersIoUtilization():
    """
    AutoscalingMemoryGroupMemoryScalersIoUtilization.

    :attr bool enabled: (optional)
    :attr str over_period: (optional)
    :attr int above_percent: (optional)
    """

    def __init__(self,
                 *,
                 enabled: bool = None,
                 over_period: str = None,
                 above_percent: int = None) -> None:
        """
        Initialize a AutoscalingMemoryGroupMemoryScalersIoUtilization object.

        :param bool enabled: (optional)
        :param str over_period: (optional)
        :param int above_percent: (optional)
        """
        self.enabled = enabled
        self.over_period = over_period
        self.above_percent = above_percent

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingMemoryGroupMemoryScalersIoUtilization':
        """Initialize a AutoscalingMemoryGroupMemoryScalersIoUtilization object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'over_period' in _dict:
            args['over_period'] = _dict.get('over_period')
        if 'above_percent' in _dict:
            args['above_percent'] = _dict.get('above_percent')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingMemoryGroupMemoryScalersIoUtilization object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'over_period') and self.over_period is not None:
            _dict['over_period'] = self.over_period
        if hasattr(self, 'above_percent') and self.above_percent is not None:
            _dict['above_percent'] = self.above_percent
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingMemoryGroupMemoryScalersIoUtilization object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingMemoryGroupMemoryScalersIoUtilization') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingMemoryGroupMemoryScalersIoUtilization') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingSetGroupAutoscaling():
    """
    AutoscalingSetGroupAutoscaling.

    """

    def __init__(self) -> None:
        """
        Initialize a AutoscalingSetGroupAutoscaling object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['AutoscalingSetGroupAutoscalingAutoscalingDiskGroup', 'AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup', 'AutoscalingSetGroupAutoscalingAutoscalingCPUGroup']))
        raise Exception(msg)

class Backup():
    """
    Backup.

    :attr str id: (optional) ID of this backup.
    :attr str deployment_id: (optional) ID of the deployment this backup relates to.
    :attr str type: (optional) The type of backup.
    :attr str status: (optional) The status of this backup.
    :attr bool is_downloadable: (optional) Is this backup available to download?.
    :attr bool is_restorable: (optional) Can this backup be used to restore an
          instance?.
    :attr datetime created_at: (optional) Date and time when this backup was
          created.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 deployment_id: str = None,
                 type: str = None,
                 status: str = None,
                 is_downloadable: bool = None,
                 is_restorable: bool = None,
                 created_at: datetime = None) -> None:
        """
        Initialize a Backup object.

        :param str id: (optional) ID of this backup.
        :param str deployment_id: (optional) ID of the deployment this backup
               relates to.
        :param str type: (optional) The type of backup.
        :param str status: (optional) The status of this backup.
        :param bool is_downloadable: (optional) Is this backup available to
               download?.
        :param bool is_restorable: (optional) Can this backup be used to restore an
               instance?.
        :param datetime created_at: (optional) Date and time when this backup was
               created.
        """
        self.id = id
        self.deployment_id = deployment_id
        self.type = type
        self.status = status
        self.is_downloadable = is_downloadable
        self.is_restorable = is_restorable
        self.created_at = created_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Backup':
        """Initialize a Backup object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'deployment_id' in _dict:
            args['deployment_id'] = _dict.get('deployment_id')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'is_downloadable' in _dict:
            args['is_downloadable'] = _dict.get('is_downloadable')
        if 'is_restorable' in _dict:
            args['is_restorable'] = _dict.get('is_restorable')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Backup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'deployment_id') and self.deployment_id is not None:
            _dict['deployment_id'] = self.deployment_id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'is_downloadable') and self.is_downloadable is not None:
            _dict['is_downloadable'] = self.is_downloadable
        if hasattr(self, 'is_restorable') and self.is_restorable is not None:
            _dict['is_restorable'] = self.is_restorable
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Backup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Backup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Backup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of backup.
        """
        SCHEDULED = 'scheduled'
        ON_DEMAND = 'on_demand'


    class StatusEnum(str, Enum):
        """
        The status of this backup.
        """
        RUNNING = 'running'
        COMPLETED = 'completed'
        FAILED = 'failed'


class Backups():
    """
    Backups.

    :attr List[Backup] backups: (optional)
    """

    def __init__(self,
                 *,
                 backups: List['Backup'] = None) -> None:
        """
        Initialize a Backups object.

        :param List[Backup] backups: (optional)
        """
        self.backups = backups

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Backups':
        """Initialize a Backups object from a json dictionary."""
        args = {}
        if 'backups' in _dict:
            args['backups'] = [Backup.from_dict(x) for x in _dict.get('backups')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Backups object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'backups') and self.backups is not None:
            _dict['backups'] = [x.to_dict() for x in self.backups]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Backups object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Backups') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Backups') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ChangeUserPasswordResponse():
    """
    ChangeUserPasswordResponse.

    :attr Task task: (optional)
    """

    def __init__(self,
                 *,
                 task: 'Task' = None) -> None:
        """
        Initialize a ChangeUserPasswordResponse object.

        :param Task task: (optional)
        """
        self.task = task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ChangeUserPasswordResponse':
        """Initialize a ChangeUserPasswordResponse object from a json dictionary."""
        args = {}
        if 'task' in _dict:
            args['task'] = Task.from_dict(_dict.get('task'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ChangeUserPasswordResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'task') and self.task is not None:
            _dict['task'] = self.task.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ChangeUserPasswordResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ChangeUserPasswordResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ChangeUserPasswordResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Connection():
    """
    Connection.

    :attr ConnectionConnection connection:
    """

    def __init__(self,
                 connection: 'ConnectionConnection') -> None:
        """
        Initialize a Connection object.

        :param ConnectionConnection connection:
        """
        self.connection = connection

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Connection':
        """Initialize a Connection object from a json dictionary."""
        args = {}
        if 'connection' in _dict:
            args['connection'] = _dict.get('connection')
        else:
            raise ValueError('Required property \'connection\' not present in Connection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Connection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'connection') and self.connection is not None:
            if isinstance(self.connection, dict):
                _dict['connection'] = self.connection
            else:
                _dict['connection'] = self.connection.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Connection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Connection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Connection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ConnectionCLI():
    """
    CLI Connection.

    :attr str type: (optional) Type of connection being described.
    :attr List[str] composed: (optional)
    :attr dict environment: (optional) A map of environment variables for a CLI
          connection.
    :attr str bin: (optional) The name of the executable the CLI should run.
    :attr List[List[str]] arguments: (optional) Sets of arguments to call the
          executable with. The outer array corresponds to a possible way to call the CLI;
          the inner array is the set of arguments to use with that call.
    :attr ConnectionCLICertificate certificate: (optional)
    """

    def __init__(self,
                 *,
                 type: str = None,
                 composed: List[str] = None,
                 environment: dict = None,
                 bin: str = None,
                 arguments: List[List[str]] = None,
                 certificate: 'ConnectionCLICertificate' = None) -> None:
        """
        Initialize a ConnectionCLI object.

        :param str type: (optional) Type of connection being described.
        :param List[str] composed: (optional)
        :param dict environment: (optional) A map of environment variables for a
               CLI connection.
        :param str bin: (optional) The name of the executable the CLI should run.
        :param List[List[str]] arguments: (optional) Sets of arguments to call the
               executable with. The outer array corresponds to a possible way to call the
               CLI; the inner array is the set of arguments to use with that call.
        :param ConnectionCLICertificate certificate: (optional)
        """
        self.type = type
        self.composed = composed
        self.environment = environment
        self.bin = bin
        self.arguments = arguments
        self.certificate = certificate

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConnectionCLI':
        """Initialize a ConnectionCLI object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'composed' in _dict:
            args['composed'] = _dict.get('composed')
        if 'environment' in _dict:
            args['environment'] = _dict.get('environment')
        if 'bin' in _dict:
            args['bin'] = _dict.get('bin')
        if 'arguments' in _dict:
            args['arguments'] = _dict.get('arguments')
        if 'certificate' in _dict:
            args['certificate'] = ConnectionCLICertificate.from_dict(_dict.get('certificate'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConnectionCLI object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'composed') and self.composed is not None:
            _dict['composed'] = self.composed
        if hasattr(self, 'environment') and self.environment is not None:
            _dict['environment'] = self.environment
        if hasattr(self, 'bin') and self.bin is not None:
            _dict['bin'] = self.bin
        if hasattr(self, 'arguments') and self.arguments is not None:
            _dict['arguments'] = self.arguments
        if hasattr(self, 'certificate') and self.certificate is not None:
            _dict['certificate'] = self.certificate.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConnectionCLI object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConnectionCLI') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConnectionCLI') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ConnectionCLICertificate():
    """
    ConnectionCLICertificate.

    :attr str name: (optional) Name associated with the certificate.
    :attr str certificate_base64: (optional) Base64 encoded version of the
          certificate.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 certificate_base64: str = None) -> None:
        """
        Initialize a ConnectionCLICertificate object.

        :param str name: (optional) Name associated with the certificate.
        :param str certificate_base64: (optional) Base64 encoded version of the
               certificate.
        """
        self.name = name
        self.certificate_base64 = certificate_base64

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConnectionCLICertificate':
        """Initialize a ConnectionCLICertificate object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'certificate_base64' in _dict:
            args['certificate_base64'] = _dict.get('certificate_base64')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConnectionCLICertificate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'certificate_base64') and self.certificate_base64 is not None:
            _dict['certificate_base64'] = self.certificate_base64
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConnectionCLICertificate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConnectionCLICertificate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConnectionCLICertificate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ConnectionConnection():
    """
    ConnectionConnection.

    """

    def __init__(self) -> None:
        """
        Initialize a ConnectionConnection object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['ConnectionConnectionPostgreSQLConnection', 'ConnectionConnectionRedisConnection', 'ConnectionConnectionElasticsearchConnection', 'ConnectionConnectionRabbitMQConnection', 'ConnectionConnectionEtcdConnection', 'ConnectionConnectionMongoDBConnection']))
        raise Exception(msg)

class CreateDatabaseUserRequestUser():
    """
    CreateDatabaseUserRequestUser.

    :attr str user_type: (optional) User type for new user.
    :attr str username: (optional) Username for new user.
    :attr str password: (optional) Password for new user.
    """

    def __init__(self,
                 *,
                 user_type: str = None,
                 username: str = None,
                 password: str = None) -> None:
        """
        Initialize a CreateDatabaseUserRequestUser object.

        :param str user_type: (optional) User type for new user.
        :param str username: (optional) Username for new user.
        :param str password: (optional) Password for new user.
        """
        self.user_type = user_type
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateDatabaseUserRequestUser':
        """Initialize a CreateDatabaseUserRequestUser object from a json dictionary."""
        args = {}
        if 'user_type' in _dict:
            args['user_type'] = _dict.get('user_type')
        if 'username' in _dict:
            args['username'] = _dict.get('username')
        if 'password' in _dict:
            args['password'] = _dict.get('password')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateDatabaseUserRequestUser object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'user_type') and self.user_type is not None:
            _dict['user_type'] = self.user_type
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateDatabaseUserRequestUser object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateDatabaseUserRequestUser') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateDatabaseUserRequestUser') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CreateDatabaseUserResponse():
    """
    CreateDatabaseUserResponse.

    :attr Task task: (optional)
    """

    def __init__(self,
                 *,
                 task: 'Task' = None) -> None:
        """
        Initialize a CreateDatabaseUserResponse object.

        :param Task task: (optional)
        """
        self.task = task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateDatabaseUserResponse':
        """Initialize a CreateDatabaseUserResponse object from a json dictionary."""
        args = {}
        if 'task' in _dict:
            args['task'] = Task.from_dict(_dict.get('task'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateDatabaseUserResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'task') and self.task is not None:
            _dict['task'] = self.task.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateDatabaseUserResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateDatabaseUserResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateDatabaseUserResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteAllowlistEntryResponse():
    """
    DeleteAllowlistEntryResponse.

    :attr Task task: (optional)
    """

    def __init__(self,
                 *,
                 task: 'Task' = None) -> None:
        """
        Initialize a DeleteAllowlistEntryResponse object.

        :param Task task: (optional)
        """
        self.task = task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteAllowlistEntryResponse':
        """Initialize a DeleteAllowlistEntryResponse object from a json dictionary."""
        args = {}
        if 'task' in _dict:
            args['task'] = Task.from_dict(_dict.get('task'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteAllowlistEntryResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'task') and self.task is not None:
            _dict['task'] = self.task.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteAllowlistEntryResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteAllowlistEntryResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteAllowlistEntryResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteDatabaseUserResponse():
    """
    DeleteDatabaseUserResponse.

    :attr Task task: (optional)
    """

    def __init__(self,
                 *,
                 task: 'Task' = None) -> None:
        """
        Initialize a DeleteDatabaseUserResponse object.

        :param Task task: (optional)
        """
        self.task = task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteDatabaseUserResponse':
        """Initialize a DeleteDatabaseUserResponse object from a json dictionary."""
        args = {}
        if 'task' in _dict:
            args['task'] = Task.from_dict(_dict.get('task'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteDatabaseUserResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'task') and self.task is not None:
            _dict['task'] = self.task.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteDatabaseUserResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteDatabaseUserResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteDatabaseUserResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Deployables():
    """
    Deployable databases with their version information.

    :attr str type: (optional) Deployment type - typically the name of the database.
    :attr List[DeployablesVersionsItem] versions: (optional) An array of versions of
          the database, their status, preferedness, and transitions.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 versions: List['DeployablesVersionsItem'] = None) -> None:
        """
        Initialize a Deployables object.

        :param str type: (optional) Deployment type - typically the name of the
               database.
        :param List[DeployablesVersionsItem] versions: (optional) An array of
               versions of the database, their status, preferedness, and transitions.
        """
        self.type = type
        self.versions = versions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Deployables':
        """Initialize a Deployables object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'versions' in _dict:
            args['versions'] = [DeployablesVersionsItem.from_dict(x) for x in _dict.get('versions')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Deployables object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'versions') and self.versions is not None:
            _dict['versions'] = [x.to_dict() for x in self.versions]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Deployables object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Deployables') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Deployables') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeployablesVersionsItem():
    """
    DeployablesVersionsItem.

    :attr str version: (optional) The version number.
    :attr str status: (optional) The status of this version: To be finalized.
    :attr bool is_preferred: (optional) Should this version be preferred over
          others?.
    :attr List[DeployablesVersionsItemTransitionsItem] transitions: (optional)
          versions that this version can be upgraded to.
    """

    def __init__(self,
                 *,
                 version: str = None,
                 status: str = None,
                 is_preferred: bool = None,
                 transitions: List['DeployablesVersionsItemTransitionsItem'] = None) -> None:
        """
        Initialize a DeployablesVersionsItem object.

        :param str version: (optional) The version number.
        :param str status: (optional) The status of this version: To be finalized.
        :param bool is_preferred: (optional) Should this version be preferred over
               others?.
        :param List[DeployablesVersionsItemTransitionsItem] transitions: (optional)
               versions that this version can be upgraded to.
        """
        self.version = version
        self.status = status
        self.is_preferred = is_preferred
        self.transitions = transitions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeployablesVersionsItem':
        """Initialize a DeployablesVersionsItem object from a json dictionary."""
        args = {}
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'is_preferred' in _dict:
            args['is_preferred'] = _dict.get('is_preferred')
        if 'transitions' in _dict:
            args['transitions'] = [DeployablesVersionsItemTransitionsItem.from_dict(x) for x in _dict.get('transitions')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeployablesVersionsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'is_preferred') and self.is_preferred is not None:
            _dict['is_preferred'] = self.is_preferred
        if hasattr(self, 'transitions') and self.transitions is not None:
            _dict['transitions'] = [x.to_dict() for x in self.transitions]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeployablesVersionsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeployablesVersionsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeployablesVersionsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The status of this version: To be finalized.
        """
        DEPRECATED = 'deprecated'
        BETA = 'beta'
        STABLE = 'stable'


class DeployablesVersionsItemTransitionsItem():
    """
    DeployablesVersionsItemTransitionsItem.

    :attr str application: (optional) The database type.
    :attr str method: (optional) method of going from from_version to to_version.
    :attr str from_version: (optional) The version the transition in from.
    :attr str to_version: (optional) The version the transition is to.
    """

    def __init__(self,
                 *,
                 application: str = None,
                 method: str = None,
                 from_version: str = None,
                 to_version: str = None) -> None:
        """
        Initialize a DeployablesVersionsItemTransitionsItem object.

        :param str application: (optional) The database type.
        :param str method: (optional) method of going from from_version to
               to_version.
        :param str from_version: (optional) The version the transition in from.
        :param str to_version: (optional) The version the transition is to.
        """
        self.application = application
        self.method = method
        self.from_version = from_version
        self.to_version = to_version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeployablesVersionsItemTransitionsItem':
        """Initialize a DeployablesVersionsItemTransitionsItem object from a json dictionary."""
        args = {}
        if 'application' in _dict:
            args['application'] = _dict.get('application')
        if 'method' in _dict:
            args['method'] = _dict.get('method')
        if 'from_version' in _dict:
            args['from_version'] = _dict.get('from_version')
        if 'to_version' in _dict:
            args['to_version'] = _dict.get('to_version')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeployablesVersionsItemTransitionsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'application') and self.application is not None:
            _dict['application'] = self.application
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'from_version') and self.from_version is not None:
            _dict['from_version'] = self.from_version
        if hasattr(self, 'to_version') and self.to_version is not None:
            _dict['to_version'] = self.to_version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeployablesVersionsItemTransitionsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeployablesVersionsItemTransitionsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeployablesVersionsItemTransitionsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Deployment():
    """
    Deployment.

    :attr str id: (optional) ID of this deployment.
    :attr str name: (optional) Readable name of this deployment.
    :attr str type: (optional) Database type within this deployment.
    :attr object platform_options: (optional) Platform-specific options for this
          deployment.
    :attr str version: (optional) Version number of the database.
    :attr dict admin_usernames: (optional) Login name of administration level user.
    :attr bool enable_public_endpoints: (optional) Whether access to this deployment
          is enabled from the public internet. This property can be modified by updating
          this service instance through the Resource Controller API.
    :attr bool enable_private_endpoints: (optional) Whether access to this
          deployment is enabled from IBM Cloud via the IBM Cloud backbone network. This
          property can be modified by updating this service instance through the Resource
          Controller API.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 type: str = None,
                 platform_options: object = None,
                 version: str = None,
                 admin_usernames: dict = None,
                 enable_public_endpoints: bool = None,
                 enable_private_endpoints: bool = None) -> None:
        """
        Initialize a Deployment object.

        :param str id: (optional) ID of this deployment.
        :param str name: (optional) Readable name of this deployment.
        :param str type: (optional) Database type within this deployment.
        :param object platform_options: (optional) Platform-specific options for
               this deployment.
        :param str version: (optional) Version number of the database.
        :param dict admin_usernames: (optional) Login name of administration level
               user.
        :param bool enable_public_endpoints: (optional) Whether access to this
               deployment is enabled from the public internet. This property can be
               modified by updating this service instance through the Resource Controller
               API.
        :param bool enable_private_endpoints: (optional) Whether access to this
               deployment is enabled from IBM Cloud via the IBM Cloud backbone network.
               This property can be modified by updating this service instance through the
               Resource Controller API.
        """
        self.id = id
        self.name = name
        self.type = type
        self.platform_options = platform_options
        self.version = version
        self.admin_usernames = admin_usernames
        self.enable_public_endpoints = enable_public_endpoints
        self.enable_private_endpoints = enable_private_endpoints

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Deployment':
        """Initialize a Deployment object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'platform_options' in _dict:
            args['platform_options'] = _dict.get('platform_options')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        if 'admin_usernames' in _dict:
            args['admin_usernames'] = _dict.get('admin_usernames')
        if 'enable_public_endpoints' in _dict:
            args['enable_public_endpoints'] = _dict.get('enable_public_endpoints')
        if 'enable_private_endpoints' in _dict:
            args['enable_private_endpoints'] = _dict.get('enable_private_endpoints')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Deployment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'platform_options') and self.platform_options is not None:
            _dict['platform_options'] = self.platform_options
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'admin_usernames') and self.admin_usernames is not None:
            _dict['admin_usernames'] = self.admin_usernames
        if hasattr(self, 'enable_public_endpoints') and self.enable_public_endpoints is not None:
            _dict['enable_public_endpoints'] = self.enable_public_endpoints
        if hasattr(self, 'enable_private_endpoints') and self.enable_private_endpoints is not None:
            _dict['enable_private_endpoints'] = self.enable_private_endpoints
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Deployment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Deployment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Deployment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ElasticsearchConnectionHTTPS():
    """
    ElasticsearchConnectionHTTPS.

    :attr str type: (optional) Type of connection being described.
    :attr List[str] composed: (optional)
    :attr str scheme: (optional) Scheme/protocol for URI connection.
    :attr List[ElasticsearchConnectionHTTPSHostsItem] hosts: (optional)
    :attr str path: (optional) Path for URI connection.
    :attr object query_options: (optional) Query options to add to the URI
          connection.
    :attr ElasticsearchConnectionHTTPSAuthentication authentication: (optional)
    :attr ElasticsearchConnectionHTTPSCertificate certificate: (optional)
    """

    def __init__(self,
                 *,
                 type: str = None,
                 composed: List[str] = None,
                 scheme: str = None,
                 hosts: List['ElasticsearchConnectionHTTPSHostsItem'] = None,
                 path: str = None,
                 query_options: object = None,
                 authentication: 'ElasticsearchConnectionHTTPSAuthentication' = None,
                 certificate: 'ElasticsearchConnectionHTTPSCertificate' = None) -> None:
        """
        Initialize a ElasticsearchConnectionHTTPS object.

        :param str type: (optional) Type of connection being described.
        :param List[str] composed: (optional)
        :param str scheme: (optional) Scheme/protocol for URI connection.
        :param List[ElasticsearchConnectionHTTPSHostsItem] hosts: (optional)
        :param str path: (optional) Path for URI connection.
        :param object query_options: (optional) Query options to add to the URI
               connection.
        :param ElasticsearchConnectionHTTPSAuthentication authentication:
               (optional)
        :param ElasticsearchConnectionHTTPSCertificate certificate: (optional)
        """
        self.type = type
        self.composed = composed
        self.scheme = scheme
        self.hosts = hosts
        self.path = path
        self.query_options = query_options
        self.authentication = authentication
        self.certificate = certificate

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ElasticsearchConnectionHTTPS':
        """Initialize a ElasticsearchConnectionHTTPS object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'composed' in _dict:
            args['composed'] = _dict.get('composed')
        if 'scheme' in _dict:
            args['scheme'] = _dict.get('scheme')
        if 'hosts' in _dict:
            args['hosts'] = [ElasticsearchConnectionHTTPSHostsItem.from_dict(x) for x in _dict.get('hosts')]
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'query_options' in _dict:
            args['query_options'] = _dict.get('query_options')
        if 'authentication' in _dict:
            args['authentication'] = ElasticsearchConnectionHTTPSAuthentication.from_dict(_dict.get('authentication'))
        if 'certificate' in _dict:
            args['certificate'] = ElasticsearchConnectionHTTPSCertificate.from_dict(_dict.get('certificate'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ElasticsearchConnectionHTTPS object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'composed') and self.composed is not None:
            _dict['composed'] = self.composed
        if hasattr(self, 'scheme') and self.scheme is not None:
            _dict['scheme'] = self.scheme
        if hasattr(self, 'hosts') and self.hosts is not None:
            _dict['hosts'] = [x.to_dict() for x in self.hosts]
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'query_options') and self.query_options is not None:
            _dict['query_options'] = self.query_options
        if hasattr(self, 'authentication') and self.authentication is not None:
            _dict['authentication'] = self.authentication.to_dict()
        if hasattr(self, 'certificate') and self.certificate is not None:
            _dict['certificate'] = self.certificate.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ElasticsearchConnectionHTTPS object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ElasticsearchConnectionHTTPS') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ElasticsearchConnectionHTTPS') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ElasticsearchConnectionHTTPSAuthentication():
    """
    ElasticsearchConnectionHTTPSAuthentication.

    :attr str method: (optional) Authentication method for this credential.
    :attr str username: (optional) Username part of credential.
    :attr str password: (optional) Password part of credential.
    """

    def __init__(self,
                 *,
                 method: str = None,
                 username: str = None,
                 password: str = None) -> None:
        """
        Initialize a ElasticsearchConnectionHTTPSAuthentication object.

        :param str method: (optional) Authentication method for this credential.
        :param str username: (optional) Username part of credential.
        :param str password: (optional) Password part of credential.
        """
        self.method = method
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ElasticsearchConnectionHTTPSAuthentication':
        """Initialize a ElasticsearchConnectionHTTPSAuthentication object from a json dictionary."""
        args = {}
        if 'method' in _dict:
            args['method'] = _dict.get('method')
        if 'username' in _dict:
            args['username'] = _dict.get('username')
        if 'password' in _dict:
            args['password'] = _dict.get('password')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ElasticsearchConnectionHTTPSAuthentication object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ElasticsearchConnectionHTTPSAuthentication object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ElasticsearchConnectionHTTPSAuthentication') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ElasticsearchConnectionHTTPSAuthentication') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ElasticsearchConnectionHTTPSCertificate():
    """
    ElasticsearchConnectionHTTPSCertificate.

    :attr str name: (optional) Name associated with the certificate.
    :attr str certificate_base64: (optional) Base64 encoded version of the
          certificate.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 certificate_base64: str = None) -> None:
        """
        Initialize a ElasticsearchConnectionHTTPSCertificate object.

        :param str name: (optional) Name associated with the certificate.
        :param str certificate_base64: (optional) Base64 encoded version of the
               certificate.
        """
        self.name = name
        self.certificate_base64 = certificate_base64

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ElasticsearchConnectionHTTPSCertificate':
        """Initialize a ElasticsearchConnectionHTTPSCertificate object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'certificate_base64' in _dict:
            args['certificate_base64'] = _dict.get('certificate_base64')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ElasticsearchConnectionHTTPSCertificate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'certificate_base64') and self.certificate_base64 is not None:
            _dict['certificate_base64'] = self.certificate_base64
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ElasticsearchConnectionHTTPSCertificate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ElasticsearchConnectionHTTPSCertificate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ElasticsearchConnectionHTTPSCertificate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ElasticsearchConnectionHTTPSHostsItem():
    """
    ElasticsearchConnectionHTTPSHostsItem.

    :attr str hostname: (optional) Hostname for connection.
    :attr int port: (optional) Port number for connection.
    """

    def __init__(self,
                 *,
                 hostname: str = None,
                 port: int = None) -> None:
        """
        Initialize a ElasticsearchConnectionHTTPSHostsItem object.

        :param str hostname: (optional) Hostname for connection.
        :param int port: (optional) Port number for connection.
        """
        self.hostname = hostname
        self.port = port

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ElasticsearchConnectionHTTPSHostsItem':
        """Initialize a ElasticsearchConnectionHTTPSHostsItem object from a json dictionary."""
        args = {}
        if 'hostname' in _dict:
            args['hostname'] = _dict.get('hostname')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ElasticsearchConnectionHTTPSHostsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ElasticsearchConnectionHTTPSHostsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ElasticsearchConnectionHTTPSHostsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ElasticsearchConnectionHTTPSHostsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GRPCConnectionURI():
    """
    GRPCConnectionURI.

    :attr str type: (optional) Type of connection being described.
    :attr List[str] composed: (optional)
    :attr str scheme: (optional) Scheme/protocol for URI connection.
    :attr List[GRPCConnectionURIHostsItem] hosts: (optional)
    :attr str path: (optional) Path for URI connection.
    :attr object query_options: (optional) Query options to add to the URI
          connection.
    :attr GRPCConnectionURIAuthentication authentication: (optional)
    :attr GRPCConnectionURICertificate certificate: (optional)
    """

    def __init__(self,
                 *,
                 type: str = None,
                 composed: List[str] = None,
                 scheme: str = None,
                 hosts: List['GRPCConnectionURIHostsItem'] = None,
                 path: str = None,
                 query_options: object = None,
                 authentication: 'GRPCConnectionURIAuthentication' = None,
                 certificate: 'GRPCConnectionURICertificate' = None) -> None:
        """
        Initialize a GRPCConnectionURI object.

        :param str type: (optional) Type of connection being described.
        :param List[str] composed: (optional)
        :param str scheme: (optional) Scheme/protocol for URI connection.
        :param List[GRPCConnectionURIHostsItem] hosts: (optional)
        :param str path: (optional) Path for URI connection.
        :param object query_options: (optional) Query options to add to the URI
               connection.
        :param GRPCConnectionURIAuthentication authentication: (optional)
        :param GRPCConnectionURICertificate certificate: (optional)
        """
        self.type = type
        self.composed = composed
        self.scheme = scheme
        self.hosts = hosts
        self.path = path
        self.query_options = query_options
        self.authentication = authentication
        self.certificate = certificate

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GRPCConnectionURI':
        """Initialize a GRPCConnectionURI object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'composed' in _dict:
            args['composed'] = _dict.get('composed')
        if 'scheme' in _dict:
            args['scheme'] = _dict.get('scheme')
        if 'hosts' in _dict:
            args['hosts'] = [GRPCConnectionURIHostsItem.from_dict(x) for x in _dict.get('hosts')]
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'query_options' in _dict:
            args['query_options'] = _dict.get('query_options')
        if 'authentication' in _dict:
            args['authentication'] = GRPCConnectionURIAuthentication.from_dict(_dict.get('authentication'))
        if 'certificate' in _dict:
            args['certificate'] = GRPCConnectionURICertificate.from_dict(_dict.get('certificate'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GRPCConnectionURI object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'composed') and self.composed is not None:
            _dict['composed'] = self.composed
        if hasattr(self, 'scheme') and self.scheme is not None:
            _dict['scheme'] = self.scheme
        if hasattr(self, 'hosts') and self.hosts is not None:
            _dict['hosts'] = [x.to_dict() for x in self.hosts]
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'query_options') and self.query_options is not None:
            _dict['query_options'] = self.query_options
        if hasattr(self, 'authentication') and self.authentication is not None:
            _dict['authentication'] = self.authentication.to_dict()
        if hasattr(self, 'certificate') and self.certificate is not None:
            _dict['certificate'] = self.certificate.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GRPCConnectionURI object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GRPCConnectionURI') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GRPCConnectionURI') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GRPCConnectionURIAuthentication():
    """
    GRPCConnectionURIAuthentication.

    :attr str method: (optional) Authentication method for this credential.
    :attr str username: (optional) Username part of credential.
    :attr str password: (optional) Password part of credential.
    """

    def __init__(self,
                 *,
                 method: str = None,
                 username: str = None,
                 password: str = None) -> None:
        """
        Initialize a GRPCConnectionURIAuthentication object.

        :param str method: (optional) Authentication method for this credential.
        :param str username: (optional) Username part of credential.
        :param str password: (optional) Password part of credential.
        """
        self.method = method
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GRPCConnectionURIAuthentication':
        """Initialize a GRPCConnectionURIAuthentication object from a json dictionary."""
        args = {}
        if 'method' in _dict:
            args['method'] = _dict.get('method')
        if 'username' in _dict:
            args['username'] = _dict.get('username')
        if 'password' in _dict:
            args['password'] = _dict.get('password')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GRPCConnectionURIAuthentication object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GRPCConnectionURIAuthentication object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GRPCConnectionURIAuthentication') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GRPCConnectionURIAuthentication') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GRPCConnectionURICertificate():
    """
    GRPCConnectionURICertificate.

    :attr str name: (optional) Name associated with the certificate.
    :attr str certificate_base64: (optional) Base64 encoded version of the
          certificate.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 certificate_base64: str = None) -> None:
        """
        Initialize a GRPCConnectionURICertificate object.

        :param str name: (optional) Name associated with the certificate.
        :param str certificate_base64: (optional) Base64 encoded version of the
               certificate.
        """
        self.name = name
        self.certificate_base64 = certificate_base64

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GRPCConnectionURICertificate':
        """Initialize a GRPCConnectionURICertificate object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'certificate_base64' in _dict:
            args['certificate_base64'] = _dict.get('certificate_base64')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GRPCConnectionURICertificate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'certificate_base64') and self.certificate_base64 is not None:
            _dict['certificate_base64'] = self.certificate_base64
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GRPCConnectionURICertificate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GRPCConnectionURICertificate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GRPCConnectionURICertificate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GRPCConnectionURIHostsItem():
    """
    GRPCConnectionURIHostsItem.

    :attr str hostname: (optional) Hostname for connection.
    :attr int port: (optional) Port number for connection.
    """

    def __init__(self,
                 *,
                 hostname: str = None,
                 port: int = None) -> None:
        """
        Initialize a GRPCConnectionURIHostsItem object.

        :param str hostname: (optional) Hostname for connection.
        :param int port: (optional) Port number for connection.
        """
        self.hostname = hostname
        self.port = port

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GRPCConnectionURIHostsItem':
        """Initialize a GRPCConnectionURIHostsItem object from a json dictionary."""
        args = {}
        if 'hostname' in _dict:
            args['hostname'] = _dict.get('hostname')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GRPCConnectionURIHostsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GRPCConnectionURIHostsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GRPCConnectionURIHostsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GRPCConnectionURIHostsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GetBackupInfoResponse():
    """
    GetBackupInfoResponse.

    :attr Backup backup: (optional)
    """

    def __init__(self,
                 *,
                 backup: 'Backup' = None) -> None:
        """
        Initialize a GetBackupInfoResponse object.

        :param Backup backup: (optional)
        """
        self.backup = backup

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetBackupInfoResponse':
        """Initialize a GetBackupInfoResponse object from a json dictionary."""
        args = {}
        if 'backup' in _dict:
            args['backup'] = Backup.from_dict(_dict.get('backup'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetBackupInfoResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'backup') and self.backup is not None:
            _dict['backup'] = self.backup.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GetBackupInfoResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetBackupInfoResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetBackupInfoResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GetDeploymentInfoResponse():
    """
    GetDeploymentInfoResponse.

    :attr Deployment deployment: (optional)
    """

    def __init__(self,
                 *,
                 deployment: 'Deployment' = None) -> None:
        """
        Initialize a GetDeploymentInfoResponse object.

        :param Deployment deployment: (optional)
        """
        self.deployment = deployment

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetDeploymentInfoResponse':
        """Initialize a GetDeploymentInfoResponse object from a json dictionary."""
        args = {}
        if 'deployment' in _dict:
            args['deployment'] = Deployment.from_dict(_dict.get('deployment'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetDeploymentInfoResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'deployment') and self.deployment is not None:
            _dict['deployment'] = self.deployment.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GetDeploymentInfoResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetDeploymentInfoResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetDeploymentInfoResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GetTaskResponse():
    """
    GetTaskResponse.

    :attr Task task: (optional)
    """

    def __init__(self,
                 *,
                 task: 'Task' = None) -> None:
        """
        Initialize a GetTaskResponse object.

        :param Task task: (optional)
        """
        self.task = task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetTaskResponse':
        """Initialize a GetTaskResponse object from a json dictionary."""
        args = {}
        if 'task' in _dict:
            args['task'] = Task.from_dict(_dict.get('task'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetTaskResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'task') and self.task is not None:
            _dict['task'] = self.task.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GetTaskResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetTaskResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetTaskResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Group():
    """
    Group.

    :attr str id: (optional) Id/name for group.
    :attr int count: (optional) Number of entities in the group.
    :attr GroupMembers members: (optional)
    :attr GroupMemory memory: (optional)
    :attr GroupCpu cpu: (optional)
    :attr GroupDisk disk: (optional)
    """

    def __init__(self,
                 *,
                 id: str = None,
                 count: int = None,
                 members: 'GroupMembers' = None,
                 memory: 'GroupMemory' = None,
                 cpu: 'GroupCpu' = None,
                 disk: 'GroupDisk' = None) -> None:
        """
        Initialize a Group object.

        :param str id: (optional) Id/name for group.
        :param int count: (optional) Number of entities in the group.
        :param GroupMembers members: (optional)
        :param GroupMemory memory: (optional)
        :param GroupCpu cpu: (optional)
        :param GroupDisk disk: (optional)
        """
        self.id = id
        self.count = count
        self.members = members
        self.memory = memory
        self.cpu = cpu
        self.disk = disk

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Group':
        """Initialize a Group object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        if 'members' in _dict:
            args['members'] = GroupMembers.from_dict(_dict.get('members'))
        if 'memory' in _dict:
            args['memory'] = GroupMemory.from_dict(_dict.get('memory'))
        if 'cpu' in _dict:
            args['cpu'] = GroupCpu.from_dict(_dict.get('cpu'))
        if 'disk' in _dict:
            args['disk'] = GroupDisk.from_dict(_dict.get('disk'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Group object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'members') and self.members is not None:
            _dict['members'] = self.members.to_dict()
        if hasattr(self, 'memory') and self.memory is not None:
            _dict['memory'] = self.memory.to_dict()
        if hasattr(self, 'cpu') and self.cpu is not None:
            _dict['cpu'] = self.cpu.to_dict()
        if hasattr(self, 'disk') and self.disk is not None:
            _dict['disk'] = self.disk.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Group object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Group') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Group') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GroupCpu():
    """
    GroupCpu.

    :attr str units: (optional) Units used for scaling cpu - count means the value
          is the number of the unit(s) available.
    :attr int allocation_count: (optional) Number of allocated CPUs.
    :attr int minimum_count: (optional) Minimum number of CPUs.
    :attr int maximum_count: (optional) Maximum number of CPUs.
    :attr int step_size_count: (optional) Step size CPUs can be adjusted.
    :attr bool is_adjustable: (optional) Is this group's CPU count adjustable.
    :attr bool is_optional: (optional) Is this group's CPU optional?.
    :attr bool can_scale_down: (optional) Can this group's CPU scale down?.
    """

    def __init__(self,
                 *,
                 units: str = None,
                 allocation_count: int = None,
                 minimum_count: int = None,
                 maximum_count: int = None,
                 step_size_count: int = None,
                 is_adjustable: bool = None,
                 is_optional: bool = None,
                 can_scale_down: bool = None) -> None:
        """
        Initialize a GroupCpu object.

        :param str units: (optional) Units used for scaling cpu - count means the
               value is the number of the unit(s) available.
        :param int allocation_count: (optional) Number of allocated CPUs.
        :param int minimum_count: (optional) Minimum number of CPUs.
        :param int maximum_count: (optional) Maximum number of CPUs.
        :param int step_size_count: (optional) Step size CPUs can be adjusted.
        :param bool is_adjustable: (optional) Is this group's CPU count adjustable.
        :param bool is_optional: (optional) Is this group's CPU optional?.
        :param bool can_scale_down: (optional) Can this group's CPU scale down?.
        """
        self.units = units
        self.allocation_count = allocation_count
        self.minimum_count = minimum_count
        self.maximum_count = maximum_count
        self.step_size_count = step_size_count
        self.is_adjustable = is_adjustable
        self.is_optional = is_optional
        self.can_scale_down = can_scale_down

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GroupCpu':
        """Initialize a GroupCpu object from a json dictionary."""
        args = {}
        if 'units' in _dict:
            args['units'] = _dict.get('units')
        if 'allocation_count' in _dict:
            args['allocation_count'] = _dict.get('allocation_count')
        if 'minimum_count' in _dict:
            args['minimum_count'] = _dict.get('minimum_count')
        if 'maximum_count' in _dict:
            args['maximum_count'] = _dict.get('maximum_count')
        if 'step_size_count' in _dict:
            args['step_size_count'] = _dict.get('step_size_count')
        if 'is_adjustable' in _dict:
            args['is_adjustable'] = _dict.get('is_adjustable')
        if 'is_optional' in _dict:
            args['is_optional'] = _dict.get('is_optional')
        if 'can_scale_down' in _dict:
            args['can_scale_down'] = _dict.get('can_scale_down')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GroupCpu object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'units') and self.units is not None:
            _dict['units'] = self.units
        if hasattr(self, 'allocation_count') and self.allocation_count is not None:
            _dict['allocation_count'] = self.allocation_count
        if hasattr(self, 'minimum_count') and self.minimum_count is not None:
            _dict['minimum_count'] = self.minimum_count
        if hasattr(self, 'maximum_count') and self.maximum_count is not None:
            _dict['maximum_count'] = self.maximum_count
        if hasattr(self, 'step_size_count') and self.step_size_count is not None:
            _dict['step_size_count'] = self.step_size_count
        if hasattr(self, 'is_adjustable') and self.is_adjustable is not None:
            _dict['is_adjustable'] = self.is_adjustable
        if hasattr(self, 'is_optional') and self.is_optional is not None:
            _dict['is_optional'] = self.is_optional
        if hasattr(self, 'can_scale_down') and self.can_scale_down is not None:
            _dict['can_scale_down'] = self.can_scale_down
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GroupCpu object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GroupCpu') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GroupCpu') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GroupDisk():
    """
    GroupDisk.

    :attr str units: (optional) Units used for scaling storage.
    :attr int allocation_mb: (optional) Allocated storage in MB.
    :attr int minimum_mb: (optional) Minimum allocated storage.
    :attr int maximum_mb: (optional) Maximum allocated storage.
    :attr int step_size_mb: (optional) Step size storage can be adjusted.
    :attr bool is_adjustable: (optional) Is this group's storage adjustable?.
    :attr bool is_optional: (optional) Is this group's storage optional?.
    :attr bool can_scale_down: (optional) Can this group's storage scale down?.
    """

    def __init__(self,
                 *,
                 units: str = None,
                 allocation_mb: int = None,
                 minimum_mb: int = None,
                 maximum_mb: int = None,
                 step_size_mb: int = None,
                 is_adjustable: bool = None,
                 is_optional: bool = None,
                 can_scale_down: bool = None) -> None:
        """
        Initialize a GroupDisk object.

        :param str units: (optional) Units used for scaling storage.
        :param int allocation_mb: (optional) Allocated storage in MB.
        :param int minimum_mb: (optional) Minimum allocated storage.
        :param int maximum_mb: (optional) Maximum allocated storage.
        :param int step_size_mb: (optional) Step size storage can be adjusted.
        :param bool is_adjustable: (optional) Is this group's storage adjustable?.
        :param bool is_optional: (optional) Is this group's storage optional?.
        :param bool can_scale_down: (optional) Can this group's storage scale
               down?.
        """
        self.units = units
        self.allocation_mb = allocation_mb
        self.minimum_mb = minimum_mb
        self.maximum_mb = maximum_mb
        self.step_size_mb = step_size_mb
        self.is_adjustable = is_adjustable
        self.is_optional = is_optional
        self.can_scale_down = can_scale_down

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GroupDisk':
        """Initialize a GroupDisk object from a json dictionary."""
        args = {}
        if 'units' in _dict:
            args['units'] = _dict.get('units')
        if 'allocation_mb' in _dict:
            args['allocation_mb'] = _dict.get('allocation_mb')
        if 'minimum_mb' in _dict:
            args['minimum_mb'] = _dict.get('minimum_mb')
        if 'maximum_mb' in _dict:
            args['maximum_mb'] = _dict.get('maximum_mb')
        if 'step_size_mb' in _dict:
            args['step_size_mb'] = _dict.get('step_size_mb')
        if 'is_adjustable' in _dict:
            args['is_adjustable'] = _dict.get('is_adjustable')
        if 'is_optional' in _dict:
            args['is_optional'] = _dict.get('is_optional')
        if 'can_scale_down' in _dict:
            args['can_scale_down'] = _dict.get('can_scale_down')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GroupDisk object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'units') and self.units is not None:
            _dict['units'] = self.units
        if hasattr(self, 'allocation_mb') and self.allocation_mb is not None:
            _dict['allocation_mb'] = self.allocation_mb
        if hasattr(self, 'minimum_mb') and self.minimum_mb is not None:
            _dict['minimum_mb'] = self.minimum_mb
        if hasattr(self, 'maximum_mb') and self.maximum_mb is not None:
            _dict['maximum_mb'] = self.maximum_mb
        if hasattr(self, 'step_size_mb') and self.step_size_mb is not None:
            _dict['step_size_mb'] = self.step_size_mb
        if hasattr(self, 'is_adjustable') and self.is_adjustable is not None:
            _dict['is_adjustable'] = self.is_adjustable
        if hasattr(self, 'is_optional') and self.is_optional is not None:
            _dict['is_optional'] = self.is_optional
        if hasattr(self, 'can_scale_down') and self.can_scale_down is not None:
            _dict['can_scale_down'] = self.can_scale_down
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GroupDisk object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GroupDisk') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GroupDisk') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GroupMembers():
    """
    GroupMembers.

    :attr str units: (optional) Units used for scaling number of members.
    :attr int allocation_count: (optional) Allocated number of members.
    :attr int minimum_count: (optional) Minimum number of members.
    :attr int maximum_count: (optional) Maximum number of members.
    :attr int step_size_count: (optional) Step size for number of members.
    :attr bool is_adjustable: (optional) Is this deployment's number of members
          adjustable?.
    :attr bool is_optional: (optional) Is this deployments's number of members
          optional?.
    :attr bool can_scale_down: (optional) Can this deployment's number of members
          scale down?.
    """

    def __init__(self,
                 *,
                 units: str = None,
                 allocation_count: int = None,
                 minimum_count: int = None,
                 maximum_count: int = None,
                 step_size_count: int = None,
                 is_adjustable: bool = None,
                 is_optional: bool = None,
                 can_scale_down: bool = None) -> None:
        """
        Initialize a GroupMembers object.

        :param str units: (optional) Units used for scaling number of members.
        :param int allocation_count: (optional) Allocated number of members.
        :param int minimum_count: (optional) Minimum number of members.
        :param int maximum_count: (optional) Maximum number of members.
        :param int step_size_count: (optional) Step size for number of members.
        :param bool is_adjustable: (optional) Is this deployment's number of
               members adjustable?.
        :param bool is_optional: (optional) Is this deployments's number of members
               optional?.
        :param bool can_scale_down: (optional) Can this deployment's number of
               members scale down?.
        """
        self.units = units
        self.allocation_count = allocation_count
        self.minimum_count = minimum_count
        self.maximum_count = maximum_count
        self.step_size_count = step_size_count
        self.is_adjustable = is_adjustable
        self.is_optional = is_optional
        self.can_scale_down = can_scale_down

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GroupMembers':
        """Initialize a GroupMembers object from a json dictionary."""
        args = {}
        if 'units' in _dict:
            args['units'] = _dict.get('units')
        if 'allocation_count' in _dict:
            args['allocation_count'] = _dict.get('allocation_count')
        if 'minimum_count' in _dict:
            args['minimum_count'] = _dict.get('minimum_count')
        if 'maximum_count' in _dict:
            args['maximum_count'] = _dict.get('maximum_count')
        if 'step_size_count' in _dict:
            args['step_size_count'] = _dict.get('step_size_count')
        if 'is_adjustable' in _dict:
            args['is_adjustable'] = _dict.get('is_adjustable')
        if 'is_optional' in _dict:
            args['is_optional'] = _dict.get('is_optional')
        if 'can_scale_down' in _dict:
            args['can_scale_down'] = _dict.get('can_scale_down')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GroupMembers object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'units') and self.units is not None:
            _dict['units'] = self.units
        if hasattr(self, 'allocation_count') and self.allocation_count is not None:
            _dict['allocation_count'] = self.allocation_count
        if hasattr(self, 'minimum_count') and self.minimum_count is not None:
            _dict['minimum_count'] = self.minimum_count
        if hasattr(self, 'maximum_count') and self.maximum_count is not None:
            _dict['maximum_count'] = self.maximum_count
        if hasattr(self, 'step_size_count') and self.step_size_count is not None:
            _dict['step_size_count'] = self.step_size_count
        if hasattr(self, 'is_adjustable') and self.is_adjustable is not None:
            _dict['is_adjustable'] = self.is_adjustable
        if hasattr(self, 'is_optional') and self.is_optional is not None:
            _dict['is_optional'] = self.is_optional
        if hasattr(self, 'can_scale_down') and self.can_scale_down is not None:
            _dict['can_scale_down'] = self.can_scale_down
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GroupMembers object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GroupMembers') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GroupMembers') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GroupMemory():
    """
    GroupMemory.

    :attr str units: (optional) Units used for scaling memory.
    :attr int allocation_mb: (optional) Allocated memory in MB.
    :attr int minimum_mb: (optional) Minimum memory in MB.
    :attr int maximum_mb: (optional) Maximum memory in MB.
    :attr int step_size_mb: (optional) Step size memory can be adjusted by in MB.
    :attr bool is_adjustable: (optional) Is this group's memory adjustable?.
    :attr bool is_optional: (optional) Is this group's memory optional?.
    :attr bool can_scale_down: (optional) Can this group's memory scale down?.
    """

    def __init__(self,
                 *,
                 units: str = None,
                 allocation_mb: int = None,
                 minimum_mb: int = None,
                 maximum_mb: int = None,
                 step_size_mb: int = None,
                 is_adjustable: bool = None,
                 is_optional: bool = None,
                 can_scale_down: bool = None) -> None:
        """
        Initialize a GroupMemory object.

        :param str units: (optional) Units used for scaling memory.
        :param int allocation_mb: (optional) Allocated memory in MB.
        :param int minimum_mb: (optional) Minimum memory in MB.
        :param int maximum_mb: (optional) Maximum memory in MB.
        :param int step_size_mb: (optional) Step size memory can be adjusted by in
               MB.
        :param bool is_adjustable: (optional) Is this group's memory adjustable?.
        :param bool is_optional: (optional) Is this group's memory optional?.
        :param bool can_scale_down: (optional) Can this group's memory scale down?.
        """
        self.units = units
        self.allocation_mb = allocation_mb
        self.minimum_mb = minimum_mb
        self.maximum_mb = maximum_mb
        self.step_size_mb = step_size_mb
        self.is_adjustable = is_adjustable
        self.is_optional = is_optional
        self.can_scale_down = can_scale_down

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GroupMemory':
        """Initialize a GroupMemory object from a json dictionary."""
        args = {}
        if 'units' in _dict:
            args['units'] = _dict.get('units')
        if 'allocation_mb' in _dict:
            args['allocation_mb'] = _dict.get('allocation_mb')
        if 'minimum_mb' in _dict:
            args['minimum_mb'] = _dict.get('minimum_mb')
        if 'maximum_mb' in _dict:
            args['maximum_mb'] = _dict.get('maximum_mb')
        if 'step_size_mb' in _dict:
            args['step_size_mb'] = _dict.get('step_size_mb')
        if 'is_adjustable' in _dict:
            args['is_adjustable'] = _dict.get('is_adjustable')
        if 'is_optional' in _dict:
            args['is_optional'] = _dict.get('is_optional')
        if 'can_scale_down' in _dict:
            args['can_scale_down'] = _dict.get('can_scale_down')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GroupMemory object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'units') and self.units is not None:
            _dict['units'] = self.units
        if hasattr(self, 'allocation_mb') and self.allocation_mb is not None:
            _dict['allocation_mb'] = self.allocation_mb
        if hasattr(self, 'minimum_mb') and self.minimum_mb is not None:
            _dict['minimum_mb'] = self.minimum_mb
        if hasattr(self, 'maximum_mb') and self.maximum_mb is not None:
            _dict['maximum_mb'] = self.maximum_mb
        if hasattr(self, 'step_size_mb') and self.step_size_mb is not None:
            _dict['step_size_mb'] = self.step_size_mb
        if hasattr(self, 'is_adjustable') and self.is_adjustable is not None:
            _dict['is_adjustable'] = self.is_adjustable
        if hasattr(self, 'is_optional') and self.is_optional is not None:
            _dict['is_optional'] = self.is_optional
        if hasattr(self, 'can_scale_down') and self.can_scale_down is not None:
            _dict['can_scale_down'] = self.can_scale_down
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GroupMemory object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GroupMemory') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GroupMemory') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Groups():
    """
    Groups.

    :attr List[Group] groups: (optional)
    """

    def __init__(self,
                 *,
                 groups: List['Group'] = None) -> None:
        """
        Initialize a Groups object.

        :param List[Group] groups: (optional)
        """
        self.groups = groups

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Groups':
        """Initialize a Groups object from a json dictionary."""
        args = {}
        if 'groups' in _dict:
            args['groups'] = [Group.from_dict(x) for x in _dict.get('groups')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Groups object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'groups') and self.groups is not None:
            _dict['groups'] = [x.to_dict() for x in self.groups]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Groups object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Groups') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Groups') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class KillConnectionsResponse():
    """
    KillConnectionsResponse.

    :attr Task task: (optional)
    """

    def __init__(self,
                 *,
                 task: 'Task' = None) -> None:
        """
        Initialize a KillConnectionsResponse object.

        :param Task task: (optional)
        """
        self.task = task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'KillConnectionsResponse':
        """Initialize a KillConnectionsResponse object from a json dictionary."""
        args = {}
        if 'task' in _dict:
            args['task'] = Task.from_dict(_dict.get('task'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KillConnectionsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'task') and self.task is not None:
            _dict['task'] = self.task.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this KillConnectionsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'KillConnectionsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'KillConnectionsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListDeployablesResponse():
    """
    ListDeployablesResponse.

    :attr List[Deployables] deployables: (optional)
    """

    def __init__(self,
                 *,
                 deployables: List['Deployables'] = None) -> None:
        """
        Initialize a ListDeployablesResponse object.

        :param List[Deployables] deployables: (optional)
        """
        self.deployables = deployables

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListDeployablesResponse':
        """Initialize a ListDeployablesResponse object from a json dictionary."""
        args = {}
        if 'deployables' in _dict:
            args['deployables'] = [Deployables.from_dict(x) for x in _dict.get('deployables')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListDeployablesResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'deployables') and self.deployables is not None:
            _dict['deployables'] = [x.to_dict() for x in self.deployables]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListDeployablesResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListDeployablesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListDeployablesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListRegionsResponse():
    """
    ListRegionsResponse.

    :attr List[str] regions: (optional) An array of region ids.
    """

    def __init__(self,
                 *,
                 regions: List[str] = None) -> None:
        """
        Initialize a ListRegionsResponse object.

        :param List[str] regions: (optional) An array of region ids.
        """
        self.regions = regions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListRegionsResponse':
        """Initialize a ListRegionsResponse object from a json dictionary."""
        args = {}
        if 'regions' in _dict:
            args['regions'] = _dict.get('regions')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListRegionsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'regions') and self.regions is not None:
            _dict['regions'] = self.regions
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListRegionsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListRegionsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListRegionsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListRemotesResponse():
    """
    ListRemotesResponse.

    :attr Remotes remotes: (optional) Remotes.
    """

    def __init__(self,
                 *,
                 remotes: 'Remotes' = None) -> None:
        """
        Initialize a ListRemotesResponse object.

        :param Remotes remotes: (optional) Remotes.
        """
        self.remotes = remotes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListRemotesResponse':
        """Initialize a ListRemotesResponse object from a json dictionary."""
        args = {}
        if 'remotes' in _dict:
            args['remotes'] = Remotes.from_dict(_dict.get('remotes'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListRemotesResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'remotes') and self.remotes is not None:
            _dict['remotes'] = self.remotes.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListRemotesResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListRemotesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListRemotesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MongoDBConnectionURI():
    """
    MongoDBConnectionURI.

    :attr str type: (optional) Type of connection being described.
    :attr List[str] composed: (optional)
    :attr str scheme: (optional) Scheme/protocol for URI connection.
    :attr List[MongoDBConnectionURIHostsItem] hosts: (optional)
    :attr str path: (optional) Path for URI connection.
    :attr object query_options: (optional) Query options to add to the URI
          connection.
    :attr MongoDBConnectionURIAuthentication authentication: (optional)
    :attr MongoDBConnectionURICertificate certificate: (optional)
    :attr str database: (optional) Name of the database to use in the URI
          connection.
    :attr str replica_set: (optional) Name of the replica set to use in the URI
          connection.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 composed: List[str] = None,
                 scheme: str = None,
                 hosts: List['MongoDBConnectionURIHostsItem'] = None,
                 path: str = None,
                 query_options: object = None,
                 authentication: 'MongoDBConnectionURIAuthentication' = None,
                 certificate: 'MongoDBConnectionURICertificate' = None,
                 database: str = None,
                 replica_set: str = None) -> None:
        """
        Initialize a MongoDBConnectionURI object.

        :param str type: (optional) Type of connection being described.
        :param List[str] composed: (optional)
        :param str scheme: (optional) Scheme/protocol for URI connection.
        :param List[MongoDBConnectionURIHostsItem] hosts: (optional)
        :param str path: (optional) Path for URI connection.
        :param object query_options: (optional) Query options to add to the URI
               connection.
        :param MongoDBConnectionURIAuthentication authentication: (optional)
        :param MongoDBConnectionURICertificate certificate: (optional)
        :param str database: (optional) Name of the database to use in the URI
               connection.
        :param str replica_set: (optional) Name of the replica set to use in the
               URI connection.
        """
        self.type = type
        self.composed = composed
        self.scheme = scheme
        self.hosts = hosts
        self.path = path
        self.query_options = query_options
        self.authentication = authentication
        self.certificate = certificate
        self.database = database
        self.replica_set = replica_set

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MongoDBConnectionURI':
        """Initialize a MongoDBConnectionURI object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'composed' in _dict:
            args['composed'] = _dict.get('composed')
        if 'scheme' in _dict:
            args['scheme'] = _dict.get('scheme')
        if 'hosts' in _dict:
            args['hosts'] = [MongoDBConnectionURIHostsItem.from_dict(x) for x in _dict.get('hosts')]
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'query_options' in _dict:
            args['query_options'] = _dict.get('query_options')
        if 'authentication' in _dict:
            args['authentication'] = MongoDBConnectionURIAuthentication.from_dict(_dict.get('authentication'))
        if 'certificate' in _dict:
            args['certificate'] = MongoDBConnectionURICertificate.from_dict(_dict.get('certificate'))
        if 'database' in _dict:
            args['database'] = _dict.get('database')
        if 'replica_set' in _dict:
            args['replica_set'] = _dict.get('replica_set')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MongoDBConnectionURI object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'composed') and self.composed is not None:
            _dict['composed'] = self.composed
        if hasattr(self, 'scheme') and self.scheme is not None:
            _dict['scheme'] = self.scheme
        if hasattr(self, 'hosts') and self.hosts is not None:
            _dict['hosts'] = [x.to_dict() for x in self.hosts]
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'query_options') and self.query_options is not None:
            _dict['query_options'] = self.query_options
        if hasattr(self, 'authentication') and self.authentication is not None:
            _dict['authentication'] = self.authentication.to_dict()
        if hasattr(self, 'certificate') and self.certificate is not None:
            _dict['certificate'] = self.certificate.to_dict()
        if hasattr(self, 'database') and self.database is not None:
            _dict['database'] = self.database
        if hasattr(self, 'replica_set') and self.replica_set is not None:
            _dict['replica_set'] = self.replica_set
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MongoDBConnectionURI object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MongoDBConnectionURI') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MongoDBConnectionURI') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MongoDBConnectionURIAuthentication():
    """
    MongoDBConnectionURIAuthentication.

    :attr str method: (optional) Authentication method for this credential.
    :attr str username: (optional) Username part of credential.
    :attr str password: (optional) Password part of credential.
    """

    def __init__(self,
                 *,
                 method: str = None,
                 username: str = None,
                 password: str = None) -> None:
        """
        Initialize a MongoDBConnectionURIAuthentication object.

        :param str method: (optional) Authentication method for this credential.
        :param str username: (optional) Username part of credential.
        :param str password: (optional) Password part of credential.
        """
        self.method = method
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MongoDBConnectionURIAuthentication':
        """Initialize a MongoDBConnectionURIAuthentication object from a json dictionary."""
        args = {}
        if 'method' in _dict:
            args['method'] = _dict.get('method')
        if 'username' in _dict:
            args['username'] = _dict.get('username')
        if 'password' in _dict:
            args['password'] = _dict.get('password')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MongoDBConnectionURIAuthentication object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MongoDBConnectionURIAuthentication object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MongoDBConnectionURIAuthentication') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MongoDBConnectionURIAuthentication') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MongoDBConnectionURICertificate():
    """
    MongoDBConnectionURICertificate.

    :attr str name: (optional) Name associated with the certificate.
    :attr str certificate_base64: (optional) Base64 encoded version of the
          certificate.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 certificate_base64: str = None) -> None:
        """
        Initialize a MongoDBConnectionURICertificate object.

        :param str name: (optional) Name associated with the certificate.
        :param str certificate_base64: (optional) Base64 encoded version of the
               certificate.
        """
        self.name = name
        self.certificate_base64 = certificate_base64

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MongoDBConnectionURICertificate':
        """Initialize a MongoDBConnectionURICertificate object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'certificate_base64' in _dict:
            args['certificate_base64'] = _dict.get('certificate_base64')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MongoDBConnectionURICertificate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'certificate_base64') and self.certificate_base64 is not None:
            _dict['certificate_base64'] = self.certificate_base64
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MongoDBConnectionURICertificate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MongoDBConnectionURICertificate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MongoDBConnectionURICertificate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MongoDBConnectionURIHostsItem():
    """
    MongoDBConnectionURIHostsItem.

    :attr str hostname: (optional) Hostname for connection.
    :attr int port: (optional) Port number for connection.
    """

    def __init__(self,
                 *,
                 hostname: str = None,
                 port: int = None) -> None:
        """
        Initialize a MongoDBConnectionURIHostsItem object.

        :param str hostname: (optional) Hostname for connection.
        :param int port: (optional) Port number for connection.
        """
        self.hostname = hostname
        self.port = port

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MongoDBConnectionURIHostsItem':
        """Initialize a MongoDBConnectionURIHostsItem object from a json dictionary."""
        args = {}
        if 'hostname' in _dict:
            args['hostname'] = _dict.get('hostname')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MongoDBConnectionURIHostsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MongoDBConnectionURIHostsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MongoDBConnectionURIHostsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MongoDBConnectionURIHostsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PointInTimeRecoveryData():
    """
    PointInTimeRecoveryData.

    :attr str earliest_point_in_time_recovery_time: (optional)
    """

    def __init__(self,
                 *,
                 earliest_point_in_time_recovery_time: str = None) -> None:
        """
        Initialize a PointInTimeRecoveryData object.

        :param str earliest_point_in_time_recovery_time: (optional)
        """
        self.earliest_point_in_time_recovery_time = earliest_point_in_time_recovery_time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PointInTimeRecoveryData':
        """Initialize a PointInTimeRecoveryData object from a json dictionary."""
        args = {}
        if 'earliest_point_in_time_recovery_time' in _dict:
            args['earliest_point_in_time_recovery_time'] = _dict.get('earliest_point_in_time_recovery_time')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PointInTimeRecoveryData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'earliest_point_in_time_recovery_time') and self.earliest_point_in_time_recovery_time is not None:
            _dict['earliest_point_in_time_recovery_time'] = self.earliest_point_in_time_recovery_time
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PointInTimeRecoveryData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PointInTimeRecoveryData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PointInTimeRecoveryData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PostgreSQLConnectionURI():
    """
    PostgreSQLConnectionURI.

    :attr str type: (optional) Type of connection being described.
    :attr List[str] composed: (optional)
    :attr str scheme: (optional) Scheme/protocol for URI connection.
    :attr List[PostgreSQLConnectionURIHostsItem] hosts: (optional)
    :attr str path: (optional) Path for URI connection.
    :attr object query_options: (optional) Query options to add to the URI
          connection.
    :attr PostgreSQLConnectionURIAuthentication authentication: (optional)
    :attr PostgreSQLConnectionURICertificate certificate: (optional)
    :attr str database: (optional) Name of the database to use in the URI
          connection.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 composed: List[str] = None,
                 scheme: str = None,
                 hosts: List['PostgreSQLConnectionURIHostsItem'] = None,
                 path: str = None,
                 query_options: object = None,
                 authentication: 'PostgreSQLConnectionURIAuthentication' = None,
                 certificate: 'PostgreSQLConnectionURICertificate' = None,
                 database: str = None) -> None:
        """
        Initialize a PostgreSQLConnectionURI object.

        :param str type: (optional) Type of connection being described.
        :param List[str] composed: (optional)
        :param str scheme: (optional) Scheme/protocol for URI connection.
        :param List[PostgreSQLConnectionURIHostsItem] hosts: (optional)
        :param str path: (optional) Path for URI connection.
        :param object query_options: (optional) Query options to add to the URI
               connection.
        :param PostgreSQLConnectionURIAuthentication authentication: (optional)
        :param PostgreSQLConnectionURICertificate certificate: (optional)
        :param str database: (optional) Name of the database to use in the URI
               connection.
        """
        self.type = type
        self.composed = composed
        self.scheme = scheme
        self.hosts = hosts
        self.path = path
        self.query_options = query_options
        self.authentication = authentication
        self.certificate = certificate
        self.database = database

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PostgreSQLConnectionURI':
        """Initialize a PostgreSQLConnectionURI object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'composed' in _dict:
            args['composed'] = _dict.get('composed')
        if 'scheme' in _dict:
            args['scheme'] = _dict.get('scheme')
        if 'hosts' in _dict:
            args['hosts'] = [PostgreSQLConnectionURIHostsItem.from_dict(x) for x in _dict.get('hosts')]
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'query_options' in _dict:
            args['query_options'] = _dict.get('query_options')
        if 'authentication' in _dict:
            args['authentication'] = PostgreSQLConnectionURIAuthentication.from_dict(_dict.get('authentication'))
        if 'certificate' in _dict:
            args['certificate'] = PostgreSQLConnectionURICertificate.from_dict(_dict.get('certificate'))
        if 'database' in _dict:
            args['database'] = _dict.get('database')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PostgreSQLConnectionURI object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'composed') and self.composed is not None:
            _dict['composed'] = self.composed
        if hasattr(self, 'scheme') and self.scheme is not None:
            _dict['scheme'] = self.scheme
        if hasattr(self, 'hosts') and self.hosts is not None:
            _dict['hosts'] = [x.to_dict() for x in self.hosts]
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'query_options') and self.query_options is not None:
            _dict['query_options'] = self.query_options
        if hasattr(self, 'authentication') and self.authentication is not None:
            _dict['authentication'] = self.authentication.to_dict()
        if hasattr(self, 'certificate') and self.certificate is not None:
            _dict['certificate'] = self.certificate.to_dict()
        if hasattr(self, 'database') and self.database is not None:
            _dict['database'] = self.database
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PostgreSQLConnectionURI object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PostgreSQLConnectionURI') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PostgreSQLConnectionURI') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PostgreSQLConnectionURIAuthentication():
    """
    PostgreSQLConnectionURIAuthentication.

    :attr str method: (optional) Authentication method for this credential.
    :attr str username: (optional) Username part of credential.
    :attr str password: (optional) Password part of credential.
    """

    def __init__(self,
                 *,
                 method: str = None,
                 username: str = None,
                 password: str = None) -> None:
        """
        Initialize a PostgreSQLConnectionURIAuthentication object.

        :param str method: (optional) Authentication method for this credential.
        :param str username: (optional) Username part of credential.
        :param str password: (optional) Password part of credential.
        """
        self.method = method
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PostgreSQLConnectionURIAuthentication':
        """Initialize a PostgreSQLConnectionURIAuthentication object from a json dictionary."""
        args = {}
        if 'method' in _dict:
            args['method'] = _dict.get('method')
        if 'username' in _dict:
            args['username'] = _dict.get('username')
        if 'password' in _dict:
            args['password'] = _dict.get('password')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PostgreSQLConnectionURIAuthentication object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PostgreSQLConnectionURIAuthentication object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PostgreSQLConnectionURIAuthentication') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PostgreSQLConnectionURIAuthentication') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PostgreSQLConnectionURICertificate():
    """
    PostgreSQLConnectionURICertificate.

    :attr str name: (optional) Name associated with the certificate.
    :attr str certificate_base64: (optional) Base64 encoded version of the
          certificate.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 certificate_base64: str = None) -> None:
        """
        Initialize a PostgreSQLConnectionURICertificate object.

        :param str name: (optional) Name associated with the certificate.
        :param str certificate_base64: (optional) Base64 encoded version of the
               certificate.
        """
        self.name = name
        self.certificate_base64 = certificate_base64

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PostgreSQLConnectionURICertificate':
        """Initialize a PostgreSQLConnectionURICertificate object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'certificate_base64' in _dict:
            args['certificate_base64'] = _dict.get('certificate_base64')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PostgreSQLConnectionURICertificate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'certificate_base64') and self.certificate_base64 is not None:
            _dict['certificate_base64'] = self.certificate_base64
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PostgreSQLConnectionURICertificate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PostgreSQLConnectionURICertificate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PostgreSQLConnectionURICertificate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PostgreSQLConnectionURIHostsItem():
    """
    PostgreSQLConnectionURIHostsItem.

    :attr str hostname: (optional) Hostname for connection.
    :attr int port: (optional) Port number for connection.
    """

    def __init__(self,
                 *,
                 hostname: str = None,
                 port: int = None) -> None:
        """
        Initialize a PostgreSQLConnectionURIHostsItem object.

        :param str hostname: (optional) Hostname for connection.
        :param int port: (optional) Port number for connection.
        """
        self.hostname = hostname
        self.port = port

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PostgreSQLConnectionURIHostsItem':
        """Initialize a PostgreSQLConnectionURIHostsItem object from a json dictionary."""
        args = {}
        if 'hostname' in _dict:
            args['hostname'] = _dict.get('hostname')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PostgreSQLConnectionURIHostsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PostgreSQLConnectionURIHostsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PostgreSQLConnectionURIHostsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PostgreSQLConnectionURIHostsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionAMQPS():
    """
    RabbitMQConnectionAMQPS.

    :attr str type: (optional) Type of connection being described.
    :attr List[str] composed: (optional)
    :attr str scheme: (optional) Scheme/protocol for URI connection.
    :attr List[RabbitMQConnectionAMQPSHostsItem] hosts: (optional)
    :attr str path: (optional) Path for URI connection.
    :attr object query_options: (optional) Query options to add to the URI
          connection.
    :attr RabbitMQConnectionAMQPSAuthentication authentication: (optional)
    :attr RabbitMQConnectionAMQPSCertificate certificate: (optional)
    """

    def __init__(self,
                 *,
                 type: str = None,
                 composed: List[str] = None,
                 scheme: str = None,
                 hosts: List['RabbitMQConnectionAMQPSHostsItem'] = None,
                 path: str = None,
                 query_options: object = None,
                 authentication: 'RabbitMQConnectionAMQPSAuthentication' = None,
                 certificate: 'RabbitMQConnectionAMQPSCertificate' = None) -> None:
        """
        Initialize a RabbitMQConnectionAMQPS object.

        :param str type: (optional) Type of connection being described.
        :param List[str] composed: (optional)
        :param str scheme: (optional) Scheme/protocol for URI connection.
        :param List[RabbitMQConnectionAMQPSHostsItem] hosts: (optional)
        :param str path: (optional) Path for URI connection.
        :param object query_options: (optional) Query options to add to the URI
               connection.
        :param RabbitMQConnectionAMQPSAuthentication authentication: (optional)
        :param RabbitMQConnectionAMQPSCertificate certificate: (optional)
        """
        self.type = type
        self.composed = composed
        self.scheme = scheme
        self.hosts = hosts
        self.path = path
        self.query_options = query_options
        self.authentication = authentication
        self.certificate = certificate

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionAMQPS':
        """Initialize a RabbitMQConnectionAMQPS object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'composed' in _dict:
            args['composed'] = _dict.get('composed')
        if 'scheme' in _dict:
            args['scheme'] = _dict.get('scheme')
        if 'hosts' in _dict:
            args['hosts'] = [RabbitMQConnectionAMQPSHostsItem.from_dict(x) for x in _dict.get('hosts')]
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'query_options' in _dict:
            args['query_options'] = _dict.get('query_options')
        if 'authentication' in _dict:
            args['authentication'] = RabbitMQConnectionAMQPSAuthentication.from_dict(_dict.get('authentication'))
        if 'certificate' in _dict:
            args['certificate'] = RabbitMQConnectionAMQPSCertificate.from_dict(_dict.get('certificate'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionAMQPS object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'composed') and self.composed is not None:
            _dict['composed'] = self.composed
        if hasattr(self, 'scheme') and self.scheme is not None:
            _dict['scheme'] = self.scheme
        if hasattr(self, 'hosts') and self.hosts is not None:
            _dict['hosts'] = [x.to_dict() for x in self.hosts]
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'query_options') and self.query_options is not None:
            _dict['query_options'] = self.query_options
        if hasattr(self, 'authentication') and self.authentication is not None:
            _dict['authentication'] = self.authentication.to_dict()
        if hasattr(self, 'certificate') and self.certificate is not None:
            _dict['certificate'] = self.certificate.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionAMQPS object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionAMQPS') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionAMQPS') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionAMQPSAuthentication():
    """
    RabbitMQConnectionAMQPSAuthentication.

    :attr str method: (optional) Authentication method for this credential.
    :attr str username: (optional) Username part of credential.
    :attr str password: (optional) Password part of credential.
    """

    def __init__(self,
                 *,
                 method: str = None,
                 username: str = None,
                 password: str = None) -> None:
        """
        Initialize a RabbitMQConnectionAMQPSAuthentication object.

        :param str method: (optional) Authentication method for this credential.
        :param str username: (optional) Username part of credential.
        :param str password: (optional) Password part of credential.
        """
        self.method = method
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionAMQPSAuthentication':
        """Initialize a RabbitMQConnectionAMQPSAuthentication object from a json dictionary."""
        args = {}
        if 'method' in _dict:
            args['method'] = _dict.get('method')
        if 'username' in _dict:
            args['username'] = _dict.get('username')
        if 'password' in _dict:
            args['password'] = _dict.get('password')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionAMQPSAuthentication object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionAMQPSAuthentication object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionAMQPSAuthentication') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionAMQPSAuthentication') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionAMQPSCertificate():
    """
    RabbitMQConnectionAMQPSCertificate.

    :attr str name: (optional) Name associated with the certificate.
    :attr str certificate_base64: (optional) Base64 encoded version of the
          certificate.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 certificate_base64: str = None) -> None:
        """
        Initialize a RabbitMQConnectionAMQPSCertificate object.

        :param str name: (optional) Name associated with the certificate.
        :param str certificate_base64: (optional) Base64 encoded version of the
               certificate.
        """
        self.name = name
        self.certificate_base64 = certificate_base64

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionAMQPSCertificate':
        """Initialize a RabbitMQConnectionAMQPSCertificate object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'certificate_base64' in _dict:
            args['certificate_base64'] = _dict.get('certificate_base64')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionAMQPSCertificate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'certificate_base64') and self.certificate_base64 is not None:
            _dict['certificate_base64'] = self.certificate_base64
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionAMQPSCertificate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionAMQPSCertificate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionAMQPSCertificate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionAMQPSHostsItem():
    """
    RabbitMQConnectionAMQPSHostsItem.

    :attr str hostname: (optional) Hostname for connection.
    :attr int port: (optional) Port number for connection.
    """

    def __init__(self,
                 *,
                 hostname: str = None,
                 port: int = None) -> None:
        """
        Initialize a RabbitMQConnectionAMQPSHostsItem object.

        :param str hostname: (optional) Hostname for connection.
        :param int port: (optional) Port number for connection.
        """
        self.hostname = hostname
        self.port = port

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionAMQPSHostsItem':
        """Initialize a RabbitMQConnectionAMQPSHostsItem object from a json dictionary."""
        args = {}
        if 'hostname' in _dict:
            args['hostname'] = _dict.get('hostname')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionAMQPSHostsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionAMQPSHostsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionAMQPSHostsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionAMQPSHostsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionHTTPS():
    """
    RabbitMQConnectionHTTPS.

    :attr str type: (optional) Type of connection being described.
    :attr List[str] composed: (optional)
    :attr str scheme: (optional) Scheme/protocol for URI connection.
    :attr List[RabbitMQConnectionHTTPSHostsItem] hosts: (optional)
    :attr str path: (optional) Path for URI connection.
    :attr object query_options: (optional) Query options to add to the URI
          connection.
    :attr RabbitMQConnectionHTTPSAuthentication authentication: (optional)
    :attr RabbitMQConnectionHTTPSCertificate certificate: (optional)
    :attr bool browser_accessible: (optional) Indicates the address is accessible by
          browser, for the RabbitMQ Management UI.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 composed: List[str] = None,
                 scheme: str = None,
                 hosts: List['RabbitMQConnectionHTTPSHostsItem'] = None,
                 path: str = None,
                 query_options: object = None,
                 authentication: 'RabbitMQConnectionHTTPSAuthentication' = None,
                 certificate: 'RabbitMQConnectionHTTPSCertificate' = None,
                 browser_accessible: bool = None) -> None:
        """
        Initialize a RabbitMQConnectionHTTPS object.

        :param str type: (optional) Type of connection being described.
        :param List[str] composed: (optional)
        :param str scheme: (optional) Scheme/protocol for URI connection.
        :param List[RabbitMQConnectionHTTPSHostsItem] hosts: (optional)
        :param str path: (optional) Path for URI connection.
        :param object query_options: (optional) Query options to add to the URI
               connection.
        :param RabbitMQConnectionHTTPSAuthentication authentication: (optional)
        :param RabbitMQConnectionHTTPSCertificate certificate: (optional)
        :param bool browser_accessible: (optional) Indicates the address is
               accessible by browser, for the RabbitMQ Management UI.
        """
        self.type = type
        self.composed = composed
        self.scheme = scheme
        self.hosts = hosts
        self.path = path
        self.query_options = query_options
        self.authentication = authentication
        self.certificate = certificate
        self.browser_accessible = browser_accessible

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionHTTPS':
        """Initialize a RabbitMQConnectionHTTPS object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'composed' in _dict:
            args['composed'] = _dict.get('composed')
        if 'scheme' in _dict:
            args['scheme'] = _dict.get('scheme')
        if 'hosts' in _dict:
            args['hosts'] = [RabbitMQConnectionHTTPSHostsItem.from_dict(x) for x in _dict.get('hosts')]
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'query_options' in _dict:
            args['query_options'] = _dict.get('query_options')
        if 'authentication' in _dict:
            args['authentication'] = RabbitMQConnectionHTTPSAuthentication.from_dict(_dict.get('authentication'))
        if 'certificate' in _dict:
            args['certificate'] = RabbitMQConnectionHTTPSCertificate.from_dict(_dict.get('certificate'))
        if 'browser_accessible' in _dict:
            args['browser_accessible'] = _dict.get('browser_accessible')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionHTTPS object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'composed') and self.composed is not None:
            _dict['composed'] = self.composed
        if hasattr(self, 'scheme') and self.scheme is not None:
            _dict['scheme'] = self.scheme
        if hasattr(self, 'hosts') and self.hosts is not None:
            _dict['hosts'] = [x.to_dict() for x in self.hosts]
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'query_options') and self.query_options is not None:
            _dict['query_options'] = self.query_options
        if hasattr(self, 'authentication') and self.authentication is not None:
            _dict['authentication'] = self.authentication.to_dict()
        if hasattr(self, 'certificate') and self.certificate is not None:
            _dict['certificate'] = self.certificate.to_dict()
        if hasattr(self, 'browser_accessible') and self.browser_accessible is not None:
            _dict['browser_accessible'] = self.browser_accessible
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionHTTPS object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionHTTPS') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionHTTPS') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionHTTPSAuthentication():
    """
    RabbitMQConnectionHTTPSAuthentication.

    :attr str method: (optional) Authentication method for this credential.
    :attr str username: (optional) Username part of credential.
    :attr str password: (optional) Password part of credential.
    """

    def __init__(self,
                 *,
                 method: str = None,
                 username: str = None,
                 password: str = None) -> None:
        """
        Initialize a RabbitMQConnectionHTTPSAuthentication object.

        :param str method: (optional) Authentication method for this credential.
        :param str username: (optional) Username part of credential.
        :param str password: (optional) Password part of credential.
        """
        self.method = method
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionHTTPSAuthentication':
        """Initialize a RabbitMQConnectionHTTPSAuthentication object from a json dictionary."""
        args = {}
        if 'method' in _dict:
            args['method'] = _dict.get('method')
        if 'username' in _dict:
            args['username'] = _dict.get('username')
        if 'password' in _dict:
            args['password'] = _dict.get('password')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionHTTPSAuthentication object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionHTTPSAuthentication object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionHTTPSAuthentication') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionHTTPSAuthentication') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionHTTPSCertificate():
    """
    RabbitMQConnectionHTTPSCertificate.

    :attr str name: (optional) Name associated with the certificate.
    :attr str certificate_base64: (optional) Base64 encoded version of the
          certificate.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 certificate_base64: str = None) -> None:
        """
        Initialize a RabbitMQConnectionHTTPSCertificate object.

        :param str name: (optional) Name associated with the certificate.
        :param str certificate_base64: (optional) Base64 encoded version of the
               certificate.
        """
        self.name = name
        self.certificate_base64 = certificate_base64

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionHTTPSCertificate':
        """Initialize a RabbitMQConnectionHTTPSCertificate object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'certificate_base64' in _dict:
            args['certificate_base64'] = _dict.get('certificate_base64')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionHTTPSCertificate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'certificate_base64') and self.certificate_base64 is not None:
            _dict['certificate_base64'] = self.certificate_base64
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionHTTPSCertificate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionHTTPSCertificate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionHTTPSCertificate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionHTTPSHostsItem():
    """
    RabbitMQConnectionHTTPSHostsItem.

    :attr str hostname: (optional) Hostname for connection.
    :attr int port: (optional) Port number for connection.
    """

    def __init__(self,
                 *,
                 hostname: str = None,
                 port: int = None) -> None:
        """
        Initialize a RabbitMQConnectionHTTPSHostsItem object.

        :param str hostname: (optional) Hostname for connection.
        :param int port: (optional) Port number for connection.
        """
        self.hostname = hostname
        self.port = port

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionHTTPSHostsItem':
        """Initialize a RabbitMQConnectionHTTPSHostsItem object from a json dictionary."""
        args = {}
        if 'hostname' in _dict:
            args['hostname'] = _dict.get('hostname')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionHTTPSHostsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionHTTPSHostsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionHTTPSHostsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionHTTPSHostsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionMQTTS():
    """
    RabbitMQConnectionMQTTS.

    :attr str type: (optional) Type of connection being described.
    :attr List[str] composed: (optional)
    :attr str scheme: (optional) Scheme/protocol for URI connection.
    :attr List[RabbitMQConnectionMQTTSHostsItem] hosts: (optional)
    :attr str path: (optional) Path for URI connection.
    :attr object query_options: (optional) Query options to add to the URI
          connection.
    :attr RabbitMQConnectionMQTTSAuthentication authentication: (optional)
    :attr RabbitMQConnectionMQTTSCertificate certificate: (optional)
    """

    def __init__(self,
                 *,
                 type: str = None,
                 composed: List[str] = None,
                 scheme: str = None,
                 hosts: List['RabbitMQConnectionMQTTSHostsItem'] = None,
                 path: str = None,
                 query_options: object = None,
                 authentication: 'RabbitMQConnectionMQTTSAuthentication' = None,
                 certificate: 'RabbitMQConnectionMQTTSCertificate' = None) -> None:
        """
        Initialize a RabbitMQConnectionMQTTS object.

        :param str type: (optional) Type of connection being described.
        :param List[str] composed: (optional)
        :param str scheme: (optional) Scheme/protocol for URI connection.
        :param List[RabbitMQConnectionMQTTSHostsItem] hosts: (optional)
        :param str path: (optional) Path for URI connection.
        :param object query_options: (optional) Query options to add to the URI
               connection.
        :param RabbitMQConnectionMQTTSAuthentication authentication: (optional)
        :param RabbitMQConnectionMQTTSCertificate certificate: (optional)
        """
        self.type = type
        self.composed = composed
        self.scheme = scheme
        self.hosts = hosts
        self.path = path
        self.query_options = query_options
        self.authentication = authentication
        self.certificate = certificate

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionMQTTS':
        """Initialize a RabbitMQConnectionMQTTS object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'composed' in _dict:
            args['composed'] = _dict.get('composed')
        if 'scheme' in _dict:
            args['scheme'] = _dict.get('scheme')
        if 'hosts' in _dict:
            args['hosts'] = [RabbitMQConnectionMQTTSHostsItem.from_dict(x) for x in _dict.get('hosts')]
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'query_options' in _dict:
            args['query_options'] = _dict.get('query_options')
        if 'authentication' in _dict:
            args['authentication'] = RabbitMQConnectionMQTTSAuthentication.from_dict(_dict.get('authentication'))
        if 'certificate' in _dict:
            args['certificate'] = RabbitMQConnectionMQTTSCertificate.from_dict(_dict.get('certificate'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionMQTTS object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'composed') and self.composed is not None:
            _dict['composed'] = self.composed
        if hasattr(self, 'scheme') and self.scheme is not None:
            _dict['scheme'] = self.scheme
        if hasattr(self, 'hosts') and self.hosts is not None:
            _dict['hosts'] = [x.to_dict() for x in self.hosts]
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'query_options') and self.query_options is not None:
            _dict['query_options'] = self.query_options
        if hasattr(self, 'authentication') and self.authentication is not None:
            _dict['authentication'] = self.authentication.to_dict()
        if hasattr(self, 'certificate') and self.certificate is not None:
            _dict['certificate'] = self.certificate.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionMQTTS object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionMQTTS') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionMQTTS') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionMQTTSAuthentication():
    """
    RabbitMQConnectionMQTTSAuthentication.

    :attr str method: (optional) Authentication method for this credential.
    :attr str username: (optional) Username part of credential.
    :attr str password: (optional) Password part of credential.
    """

    def __init__(self,
                 *,
                 method: str = None,
                 username: str = None,
                 password: str = None) -> None:
        """
        Initialize a RabbitMQConnectionMQTTSAuthentication object.

        :param str method: (optional) Authentication method for this credential.
        :param str username: (optional) Username part of credential.
        :param str password: (optional) Password part of credential.
        """
        self.method = method
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionMQTTSAuthentication':
        """Initialize a RabbitMQConnectionMQTTSAuthentication object from a json dictionary."""
        args = {}
        if 'method' in _dict:
            args['method'] = _dict.get('method')
        if 'username' in _dict:
            args['username'] = _dict.get('username')
        if 'password' in _dict:
            args['password'] = _dict.get('password')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionMQTTSAuthentication object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionMQTTSAuthentication object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionMQTTSAuthentication') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionMQTTSAuthentication') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionMQTTSCertificate():
    """
    RabbitMQConnectionMQTTSCertificate.

    :attr str name: (optional) Name associated with the certificate.
    :attr str certificate_base64: (optional) Base64 encoded version of the
          certificate.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 certificate_base64: str = None) -> None:
        """
        Initialize a RabbitMQConnectionMQTTSCertificate object.

        :param str name: (optional) Name associated with the certificate.
        :param str certificate_base64: (optional) Base64 encoded version of the
               certificate.
        """
        self.name = name
        self.certificate_base64 = certificate_base64

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionMQTTSCertificate':
        """Initialize a RabbitMQConnectionMQTTSCertificate object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'certificate_base64' in _dict:
            args['certificate_base64'] = _dict.get('certificate_base64')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionMQTTSCertificate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'certificate_base64') and self.certificate_base64 is not None:
            _dict['certificate_base64'] = self.certificate_base64
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionMQTTSCertificate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionMQTTSCertificate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionMQTTSCertificate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionMQTTSHostsItem():
    """
    RabbitMQConnectionMQTTSHostsItem.

    :attr str hostname: (optional) Hostname for connection.
    :attr int port: (optional) Port number for connection.
    """

    def __init__(self,
                 *,
                 hostname: str = None,
                 port: int = None) -> None:
        """
        Initialize a RabbitMQConnectionMQTTSHostsItem object.

        :param str hostname: (optional) Hostname for connection.
        :param int port: (optional) Port number for connection.
        """
        self.hostname = hostname
        self.port = port

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionMQTTSHostsItem':
        """Initialize a RabbitMQConnectionMQTTSHostsItem object from a json dictionary."""
        args = {}
        if 'hostname' in _dict:
            args['hostname'] = _dict.get('hostname')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionMQTTSHostsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionMQTTSHostsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionMQTTSHostsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionMQTTSHostsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionStompSSL():
    """
    RabbitMQConnectionStompSSL.

    :attr str type: (optional) Type of connection being described.
    :attr List[str] composed: (optional)
    :attr List[RabbitMQConnectionStompSSLHostsItem] hosts: (optional)
    :attr RabbitMQConnectionStompSSLAuthentication authentication: (optional)
    :attr RabbitMQConnectionStompSSLCertificate certificate: (optional)
    :attr bool ssl: (optional) Indicates ssl is required for the connection.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 composed: List[str] = None,
                 hosts: List['RabbitMQConnectionStompSSLHostsItem'] = None,
                 authentication: 'RabbitMQConnectionStompSSLAuthentication' = None,
                 certificate: 'RabbitMQConnectionStompSSLCertificate' = None,
                 ssl: bool = None) -> None:
        """
        Initialize a RabbitMQConnectionStompSSL object.

        :param str type: (optional) Type of connection being described.
        :param List[str] composed: (optional)
        :param List[RabbitMQConnectionStompSSLHostsItem] hosts: (optional)
        :param RabbitMQConnectionStompSSLAuthentication authentication: (optional)
        :param RabbitMQConnectionStompSSLCertificate certificate: (optional)
        :param bool ssl: (optional) Indicates ssl is required for the connection.
        """
        self.type = type
        self.composed = composed
        self.hosts = hosts
        self.authentication = authentication
        self.certificate = certificate
        self.ssl = ssl

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionStompSSL':
        """Initialize a RabbitMQConnectionStompSSL object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'composed' in _dict:
            args['composed'] = _dict.get('composed')
        if 'hosts' in _dict:
            args['hosts'] = [RabbitMQConnectionStompSSLHostsItem.from_dict(x) for x in _dict.get('hosts')]
        if 'authentication' in _dict:
            args['authentication'] = RabbitMQConnectionStompSSLAuthentication.from_dict(_dict.get('authentication'))
        if 'certificate' in _dict:
            args['certificate'] = RabbitMQConnectionStompSSLCertificate.from_dict(_dict.get('certificate'))
        if 'ssl' in _dict:
            args['ssl'] = _dict.get('ssl')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionStompSSL object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'composed') and self.composed is not None:
            _dict['composed'] = self.composed
        if hasattr(self, 'hosts') and self.hosts is not None:
            _dict['hosts'] = [x.to_dict() for x in self.hosts]
        if hasattr(self, 'authentication') and self.authentication is not None:
            _dict['authentication'] = self.authentication.to_dict()
        if hasattr(self, 'certificate') and self.certificate is not None:
            _dict['certificate'] = self.certificate.to_dict()
        if hasattr(self, 'ssl') and self.ssl is not None:
            _dict['ssl'] = self.ssl
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionStompSSL object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionStompSSL') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionStompSSL') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionStompSSLAuthentication():
    """
    RabbitMQConnectionStompSSLAuthentication.

    :attr str method: (optional) Authentication method for this credential.
    :attr str username: (optional) Username part of credential.
    :attr str password: (optional) Password part of credential.
    """

    def __init__(self,
                 *,
                 method: str = None,
                 username: str = None,
                 password: str = None) -> None:
        """
        Initialize a RabbitMQConnectionStompSSLAuthentication object.

        :param str method: (optional) Authentication method for this credential.
        :param str username: (optional) Username part of credential.
        :param str password: (optional) Password part of credential.
        """
        self.method = method
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionStompSSLAuthentication':
        """Initialize a RabbitMQConnectionStompSSLAuthentication object from a json dictionary."""
        args = {}
        if 'method' in _dict:
            args['method'] = _dict.get('method')
        if 'username' in _dict:
            args['username'] = _dict.get('username')
        if 'password' in _dict:
            args['password'] = _dict.get('password')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionStompSSLAuthentication object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionStompSSLAuthentication object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionStompSSLAuthentication') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionStompSSLAuthentication') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionStompSSLCertificate():
    """
    RabbitMQConnectionStompSSLCertificate.

    :attr str name: (optional) Name associated with the certificate.
    :attr str certificate_base64: (optional) Base64 encoded version of the
          certificate.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 certificate_base64: str = None) -> None:
        """
        Initialize a RabbitMQConnectionStompSSLCertificate object.

        :param str name: (optional) Name associated with the certificate.
        :param str certificate_base64: (optional) Base64 encoded version of the
               certificate.
        """
        self.name = name
        self.certificate_base64 = certificate_base64

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionStompSSLCertificate':
        """Initialize a RabbitMQConnectionStompSSLCertificate object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'certificate_base64' in _dict:
            args['certificate_base64'] = _dict.get('certificate_base64')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionStompSSLCertificate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'certificate_base64') and self.certificate_base64 is not None:
            _dict['certificate_base64'] = self.certificate_base64
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionStompSSLCertificate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionStompSSLCertificate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionStompSSLCertificate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RabbitMQConnectionStompSSLHostsItem():
    """
    RabbitMQConnectionStompSSLHostsItem.

    :attr str hostname: (optional) Hostname for connection.
    :attr int port: (optional) Port number for connection.
    """

    def __init__(self,
                 *,
                 hostname: str = None,
                 port: int = None) -> None:
        """
        Initialize a RabbitMQConnectionStompSSLHostsItem object.

        :param str hostname: (optional) Hostname for connection.
        :param int port: (optional) Port number for connection.
        """
        self.hostname = hostname
        self.port = port

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RabbitMQConnectionStompSSLHostsItem':
        """Initialize a RabbitMQConnectionStompSSLHostsItem object from a json dictionary."""
        args = {}
        if 'hostname' in _dict:
            args['hostname'] = _dict.get('hostname')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RabbitMQConnectionStompSSLHostsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RabbitMQConnectionStompSSLHostsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RabbitMQConnectionStompSSLHostsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RabbitMQConnectionStompSSLHostsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RedisConnectionURI():
    """
    RedisConnectionURI.

    :attr str type: (optional) Type of connection being described.
    :attr List[str] composed: (optional)
    :attr str scheme: (optional) Scheme/protocol for URI connection.
    :attr List[RedisConnectionURIHostsItem] hosts: (optional)
    :attr str path: (optional) Path for URI connection.
    :attr object query_options: (optional) Query options to add to the URI
          connection.
    :attr RedisConnectionURIAuthentication authentication: (optional)
    :attr RedisConnectionURICertificate certificate: (optional)
    :attr int database: (optional) Number of the database to use in the URI
          connection.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 composed: List[str] = None,
                 scheme: str = None,
                 hosts: List['RedisConnectionURIHostsItem'] = None,
                 path: str = None,
                 query_options: object = None,
                 authentication: 'RedisConnectionURIAuthentication' = None,
                 certificate: 'RedisConnectionURICertificate' = None,
                 database: int = None) -> None:
        """
        Initialize a RedisConnectionURI object.

        :param str type: (optional) Type of connection being described.
        :param List[str] composed: (optional)
        :param str scheme: (optional) Scheme/protocol for URI connection.
        :param List[RedisConnectionURIHostsItem] hosts: (optional)
        :param str path: (optional) Path for URI connection.
        :param object query_options: (optional) Query options to add to the URI
               connection.
        :param RedisConnectionURIAuthentication authentication: (optional)
        :param RedisConnectionURICertificate certificate: (optional)
        :param int database: (optional) Number of the database to use in the URI
               connection.
        """
        self.type = type
        self.composed = composed
        self.scheme = scheme
        self.hosts = hosts
        self.path = path
        self.query_options = query_options
        self.authentication = authentication
        self.certificate = certificate
        self.database = database

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RedisConnectionURI':
        """Initialize a RedisConnectionURI object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'composed' in _dict:
            args['composed'] = _dict.get('composed')
        if 'scheme' in _dict:
            args['scheme'] = _dict.get('scheme')
        if 'hosts' in _dict:
            args['hosts'] = [RedisConnectionURIHostsItem.from_dict(x) for x in _dict.get('hosts')]
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'query_options' in _dict:
            args['query_options'] = _dict.get('query_options')
        if 'authentication' in _dict:
            args['authentication'] = RedisConnectionURIAuthentication.from_dict(_dict.get('authentication'))
        if 'certificate' in _dict:
            args['certificate'] = RedisConnectionURICertificate.from_dict(_dict.get('certificate'))
        if 'database' in _dict:
            args['database'] = _dict.get('database')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RedisConnectionURI object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'composed') and self.composed is not None:
            _dict['composed'] = self.composed
        if hasattr(self, 'scheme') and self.scheme is not None:
            _dict['scheme'] = self.scheme
        if hasattr(self, 'hosts') and self.hosts is not None:
            _dict['hosts'] = [x.to_dict() for x in self.hosts]
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'query_options') and self.query_options is not None:
            _dict['query_options'] = self.query_options
        if hasattr(self, 'authentication') and self.authentication is not None:
            _dict['authentication'] = self.authentication.to_dict()
        if hasattr(self, 'certificate') and self.certificate is not None:
            _dict['certificate'] = self.certificate.to_dict()
        if hasattr(self, 'database') and self.database is not None:
            _dict['database'] = self.database
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RedisConnectionURI object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RedisConnectionURI') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RedisConnectionURI') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RedisConnectionURIAuthentication():
    """
    RedisConnectionURIAuthentication.

    :attr str method: (optional) Authentication method for this credential.
    :attr str username: (optional) Username part of credential.
    :attr str password: (optional) Password part of credential.
    """

    def __init__(self,
                 *,
                 method: str = None,
                 username: str = None,
                 password: str = None) -> None:
        """
        Initialize a RedisConnectionURIAuthentication object.

        :param str method: (optional) Authentication method for this credential.
        :param str username: (optional) Username part of credential.
        :param str password: (optional) Password part of credential.
        """
        self.method = method
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RedisConnectionURIAuthentication':
        """Initialize a RedisConnectionURIAuthentication object from a json dictionary."""
        args = {}
        if 'method' in _dict:
            args['method'] = _dict.get('method')
        if 'username' in _dict:
            args['username'] = _dict.get('username')
        if 'password' in _dict:
            args['password'] = _dict.get('password')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RedisConnectionURIAuthentication object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RedisConnectionURIAuthentication object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RedisConnectionURIAuthentication') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RedisConnectionURIAuthentication') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RedisConnectionURICertificate():
    """
    RedisConnectionURICertificate.

    :attr str name: (optional) Name associated with the certificate.
    :attr str certificate_base64: (optional) Base64 encoded version of the
          certificate.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 certificate_base64: str = None) -> None:
        """
        Initialize a RedisConnectionURICertificate object.

        :param str name: (optional) Name associated with the certificate.
        :param str certificate_base64: (optional) Base64 encoded version of the
               certificate.
        """
        self.name = name
        self.certificate_base64 = certificate_base64

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RedisConnectionURICertificate':
        """Initialize a RedisConnectionURICertificate object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'certificate_base64' in _dict:
            args['certificate_base64'] = _dict.get('certificate_base64')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RedisConnectionURICertificate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'certificate_base64') and self.certificate_base64 is not None:
            _dict['certificate_base64'] = self.certificate_base64
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RedisConnectionURICertificate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RedisConnectionURICertificate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RedisConnectionURICertificate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RedisConnectionURIHostsItem():
    """
    RedisConnectionURIHostsItem.

    :attr str hostname: (optional) Hostname for connection.
    :attr int port: (optional) Port number for connection.
    """

    def __init__(self,
                 *,
                 hostname: str = None,
                 port: int = None) -> None:
        """
        Initialize a RedisConnectionURIHostsItem object.

        :param str hostname: (optional) Hostname for connection.
        :param int port: (optional) Port number for connection.
        """
        self.hostname = hostname
        self.port = port

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RedisConnectionURIHostsItem':
        """Initialize a RedisConnectionURIHostsItem object from a json dictionary."""
        args = {}
        if 'hostname' in _dict:
            args['hostname'] = _dict.get('hostname')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RedisConnectionURIHostsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RedisConnectionURIHostsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RedisConnectionURIHostsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RedisConnectionURIHostsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Remotes():
    """
    Remotes.

    :attr str leader: (optional) Leader ID, if applicable.
    :attr List[str] replicas: (optional) Replica IDs, if applicable.
    """

    def __init__(self,
                 *,
                 leader: str = None,
                 replicas: List[str] = None) -> None:
        """
        Initialize a Remotes object.

        :param str leader: (optional) Leader ID, if applicable.
        :param List[str] replicas: (optional) Replica IDs, if applicable.
        """
        self.leader = leader
        self.replicas = replicas

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Remotes':
        """Initialize a Remotes object from a json dictionary."""
        args = {}
        if 'leader' in _dict:
            args['leader'] = _dict.get('leader')
        if 'replicas' in _dict:
            args['replicas'] = _dict.get('replicas')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Remotes object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'leader') and self.leader is not None:
            _dict['leader'] = self.leader
        if hasattr(self, 'replicas') and self.replicas is not None:
            _dict['replicas'] = self.replicas
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Remotes object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Remotes') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Remotes') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResyncReplicaResponse():
    """
    ResyncReplicaResponse.

    :attr Task task: (optional)
    """

    def __init__(self,
                 *,
                 task: 'Task' = None) -> None:
        """
        Initialize a ResyncReplicaResponse object.

        :param Task task: (optional)
        """
        self.task = task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResyncReplicaResponse':
        """Initialize a ResyncReplicaResponse object from a json dictionary."""
        args = {}
        if 'task' in _dict:
            args['task'] = Task.from_dict(_dict.get('task'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResyncReplicaResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'task') and self.task is not None:
            _dict['task'] = self.task.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResyncReplicaResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResyncReplicaResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResyncReplicaResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SetAllowlistResponse():
    """
    SetAllowlistResponse.

    :attr Task task: (optional)
    """

    def __init__(self,
                 *,
                 task: 'Task' = None) -> None:
        """
        Initialize a SetAllowlistResponse object.

        :param Task task: (optional)
        """
        self.task = task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetAllowlistResponse':
        """Initialize a SetAllowlistResponse object from a json dictionary."""
        args = {}
        if 'task' in _dict:
            args['task'] = Task.from_dict(_dict.get('task'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetAllowlistResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'task') and self.task is not None:
            _dict['task'] = self.task.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetAllowlistResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetAllowlistResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetAllowlistResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SetAutoscalingConditionsResponse():
    """
    SetAutoscalingConditionsResponse.

    :attr Task task: (optional)
    """

    def __init__(self,
                 *,
                 task: 'Task' = None) -> None:
        """
        Initialize a SetAutoscalingConditionsResponse object.

        :param Task task: (optional)
        """
        self.task = task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetAutoscalingConditionsResponse':
        """Initialize a SetAutoscalingConditionsResponse object from a json dictionary."""
        args = {}
        if 'task' in _dict:
            args['task'] = Task.from_dict(_dict.get('task'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetAutoscalingConditionsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'task') and self.task is not None:
            _dict['task'] = self.task.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetAutoscalingConditionsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetAutoscalingConditionsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetAutoscalingConditionsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SetCPUGroupCPU():
    """
    SetCPUGroupCPU.

    :attr int allocation_count: (optional) Number of allocated CPUs.
    """

    def __init__(self,
                 *,
                 allocation_count: int = None) -> None:
        """
        Initialize a SetCPUGroupCPU object.

        :param int allocation_count: (optional) Number of allocated CPUs.
        """
        self.allocation_count = allocation_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetCPUGroupCPU':
        """Initialize a SetCPUGroupCPU object from a json dictionary."""
        args = {}
        if 'allocation_count' in _dict:
            args['allocation_count'] = _dict.get('allocation_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetCPUGroupCPU object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'allocation_count') and self.allocation_count is not None:
            _dict['allocation_count'] = self.allocation_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetCPUGroupCPU object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetCPUGroupCPU') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetCPUGroupCPU') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SetConfigurationConfiguration():
    """
    SetConfigurationConfiguration.

    """

    def __init__(self) -> None:
        """
        Initialize a SetConfigurationConfiguration object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['SetConfigurationConfigurationPGConfiguration', 'SetConfigurationConfigurationRedisConfiguration']))
        raise Exception(msg)

class SetDeploymentScalingGroupRequest():
    """
    SetDeploymentScalingGroupRequest.

    """

    def __init__(self) -> None:
        """
        Initialize a SetDeploymentScalingGroupRequest object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['SetDeploymentScalingGroupRequestSetMembersGroup', 'SetDeploymentScalingGroupRequestSetMemoryGroup', 'SetDeploymentScalingGroupRequestSetCPUGroup', 'SetDeploymentScalingGroupRequestSetDiskGroup']))
        raise Exception(msg)

class SetDeploymentScalingGroupResponse():
    """
    SetDeploymentScalingGroupResponse.

    :attr Task task: (optional)
    """

    def __init__(self,
                 *,
                 task: 'Task' = None) -> None:
        """
        Initialize a SetDeploymentScalingGroupResponse object.

        :param Task task: (optional)
        """
        self.task = task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetDeploymentScalingGroupResponse':
        """Initialize a SetDeploymentScalingGroupResponse object from a json dictionary."""
        args = {}
        if 'task' in _dict:
            args['task'] = Task.from_dict(_dict.get('task'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetDeploymentScalingGroupResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'task') and self.task is not None:
            _dict['task'] = self.task.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetDeploymentScalingGroupResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetDeploymentScalingGroupResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetDeploymentScalingGroupResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SetDiskGroupDisk():
    """
    SetDiskGroupDisk.

    :attr int allocation_mb: (optional) Allocated storage in MB.
    """

    def __init__(self,
                 *,
                 allocation_mb: int = None) -> None:
        """
        Initialize a SetDiskGroupDisk object.

        :param int allocation_mb: (optional) Allocated storage in MB.
        """
        self.allocation_mb = allocation_mb

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetDiskGroupDisk':
        """Initialize a SetDiskGroupDisk object from a json dictionary."""
        args = {}
        if 'allocation_mb' in _dict:
            args['allocation_mb'] = _dict.get('allocation_mb')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetDiskGroupDisk object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'allocation_mb') and self.allocation_mb is not None:
            _dict['allocation_mb'] = self.allocation_mb
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetDiskGroupDisk object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetDiskGroupDisk') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetDiskGroupDisk') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SetMembersGroupMembers():
    """
    SetMembersGroupMembers.

    :attr int allocation_count: (optional) Allocated number of members.
    """

    def __init__(self,
                 *,
                 allocation_count: int = None) -> None:
        """
        Initialize a SetMembersGroupMembers object.

        :param int allocation_count: (optional) Allocated number of members.
        """
        self.allocation_count = allocation_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetMembersGroupMembers':
        """Initialize a SetMembersGroupMembers object from a json dictionary."""
        args = {}
        if 'allocation_count' in _dict:
            args['allocation_count'] = _dict.get('allocation_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetMembersGroupMembers object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'allocation_count') and self.allocation_count is not None:
            _dict['allocation_count'] = self.allocation_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetMembersGroupMembers object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetMembersGroupMembers') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetMembersGroupMembers') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SetMemoryGroupMemory():
    """
    SetMemoryGroupMemory.

    :attr int allocation_mb: (optional) Allocated memory in MB.
    """

    def __init__(self,
                 *,
                 allocation_mb: int = None) -> None:
        """
        Initialize a SetMemoryGroupMemory object.

        :param int allocation_mb: (optional) Allocated memory in MB.
        """
        self.allocation_mb = allocation_mb

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetMemoryGroupMemory':
        """Initialize a SetMemoryGroupMemory object from a json dictionary."""
        args = {}
        if 'allocation_mb' in _dict:
            args['allocation_mb'] = _dict.get('allocation_mb')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetMemoryGroupMemory object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'allocation_mb') and self.allocation_mb is not None:
            _dict['allocation_mb'] = self.allocation_mb
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetMemoryGroupMemory object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetMemoryGroupMemory') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetMemoryGroupMemory') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SetPromotionPromotion():
    """
    SetPromotionPromotion.

    """

    def __init__(self) -> None:
        """
        Initialize a SetPromotionPromotion object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['SetPromotionPromotionPromote', 'SetPromotionPromotionUpgradePromote']))
        raise Exception(msg)

class SetPromotionResponse():
    """
    SetPromotionResponse.

    :attr Task task: (optional)
    """

    def __init__(self,
                 *,
                 task: 'Task' = None) -> None:
        """
        Initialize a SetPromotionResponse object.

        :param Task task: (optional)
        """
        self.task = task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetPromotionResponse':
        """Initialize a SetPromotionResponse object from a json dictionary."""
        args = {}
        if 'task' in _dict:
            args['task'] = Task.from_dict(_dict.get('task'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetPromotionResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'task') and self.task is not None:
            _dict['task'] = self.task.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetPromotionResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetPromotionResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetPromotionResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class StartOndemandBackupResponse():
    """
    StartOndemandBackupResponse.

    :attr Task task: (optional)
    """

    def __init__(self,
                 *,
                 task: 'Task' = None) -> None:
        """
        Initialize a StartOndemandBackupResponse object.

        :param Task task: (optional)
        """
        self.task = task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StartOndemandBackupResponse':
        """Initialize a StartOndemandBackupResponse object from a json dictionary."""
        args = {}
        if 'task' in _dict:
            args['task'] = Task.from_dict(_dict.get('task'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StartOndemandBackupResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'task') and self.task is not None:
            _dict['task'] = self.task.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StartOndemandBackupResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StartOndemandBackupResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StartOndemandBackupResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Task():
    """
    Task.

    :attr str id: (optional) ID of the task.
    :attr str description: (optional) Human-readable description of the task.
    :attr str status: (optional) The status of the task.
    :attr str deployment_id: (optional) ID of the deployment the task is being
          performed on.
    :attr int progress_percent: (optional) Indicator as percentage of progress of
          the task.
    :attr datetime created_at: (optional) Date and time when the task was created.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 description: str = None,
                 status: str = None,
                 deployment_id: str = None,
                 progress_percent: int = None,
                 created_at: datetime = None) -> None:
        """
        Initialize a Task object.

        :param str id: (optional) ID of the task.
        :param str description: (optional) Human-readable description of the task.
        :param str status: (optional) The status of the task.
        :param str deployment_id: (optional) ID of the deployment the task is being
               performed on.
        :param int progress_percent: (optional) Indicator as percentage of progress
               of the task.
        :param datetime created_at: (optional) Date and time when the task was
               created.
        """
        self.id = id
        self.description = description
        self.status = status
        self.deployment_id = deployment_id
        self.progress_percent = progress_percent
        self.created_at = created_at

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Task':
        """Initialize a Task object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'deployment_id' in _dict:
            args['deployment_id'] = _dict.get('deployment_id')
        if 'progress_percent' in _dict:
            args['progress_percent'] = _dict.get('progress_percent')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Task object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'deployment_id') and self.deployment_id is not None:
            _dict['deployment_id'] = self.deployment_id
        if hasattr(self, 'progress_percent') and self.progress_percent is not None:
            _dict['progress_percent'] = self.progress_percent
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Task object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Task') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Task') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The status of the task.
        """
        RUNNING = 'running'
        COMPLETED = 'completed'
        FAILED = 'failed'


class Tasks():
    """
    Tasks.

    :attr List[Task] tasks: (optional)
    """

    def __init__(self,
                 *,
                 tasks: List['Task'] = None) -> None:
        """
        Initialize a Tasks object.

        :param List[Task] tasks: (optional)
        """
        self.tasks = tasks

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Tasks':
        """Initialize a Tasks object from a json dictionary."""
        args = {}
        if 'tasks' in _dict:
            args['tasks'] = [Task.from_dict(x) for x in _dict.get('tasks')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Tasks object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'tasks') and self.tasks is not None:
            _dict['tasks'] = [x.to_dict() for x in self.tasks]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Tasks object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Tasks') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Tasks') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class UpdateDatabaseConfigurationResponse():
    """
    UpdateDatabaseConfigurationResponse.

    :attr Task task: (optional)
    """

    def __init__(self,
                 *,
                 task: 'Task' = None) -> None:
        """
        Initialize a UpdateDatabaseConfigurationResponse object.

        :param Task task: (optional)
        """
        self.task = task

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdateDatabaseConfigurationResponse':
        """Initialize a UpdateDatabaseConfigurationResponse object from a json dictionary."""
        args = {}
        if 'task' in _dict:
            args['task'] = Task.from_dict(_dict.get('task'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdateDatabaseConfigurationResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'task') and self.task is not None:
            _dict['task'] = self.task.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UpdateDatabaseConfigurationResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UpdateDatabaseConfigurationResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdateDatabaseConfigurationResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingSetGroupAutoscalingAutoscalingCPUGroup(AutoscalingSetGroupAutoscaling):
    """
    AutoscalingSetGroupAutoscalingAutoscalingCPUGroup.

    :attr AutoscalingCPUGroupCPU cpu: (optional)
    """

    def __init__(self,
                 *,
                 cpu: 'AutoscalingCPUGroupCPU' = None) -> None:
        """
        Initialize a AutoscalingSetGroupAutoscalingAutoscalingCPUGroup object.

        :param AutoscalingCPUGroupCPU cpu: (optional)
        """
        # pylint: disable=super-init-not-called
        self.cpu = cpu

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingSetGroupAutoscalingAutoscalingCPUGroup':
        """Initialize a AutoscalingSetGroupAutoscalingAutoscalingCPUGroup object from a json dictionary."""
        args = {}
        if 'cpu' in _dict:
            args['cpu'] = AutoscalingCPUGroupCPU.from_dict(_dict.get('cpu'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingSetGroupAutoscalingAutoscalingCPUGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cpu') and self.cpu is not None:
            _dict['cpu'] = self.cpu.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingSetGroupAutoscalingAutoscalingCPUGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingSetGroupAutoscalingAutoscalingCPUGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingSetGroupAutoscalingAutoscalingCPUGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingSetGroupAutoscalingAutoscalingDiskGroup(AutoscalingSetGroupAutoscaling):
    """
    AutoscalingSetGroupAutoscalingAutoscalingDiskGroup.

    :attr AutoscalingDiskGroupDisk disk: (optional)
    """

    def __init__(self,
                 *,
                 disk: 'AutoscalingDiskGroupDisk' = None) -> None:
        """
        Initialize a AutoscalingSetGroupAutoscalingAutoscalingDiskGroup object.

        :param AutoscalingDiskGroupDisk disk: (optional)
        """
        # pylint: disable=super-init-not-called
        self.disk = disk

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingSetGroupAutoscalingAutoscalingDiskGroup':
        """Initialize a AutoscalingSetGroupAutoscalingAutoscalingDiskGroup object from a json dictionary."""
        args = {}
        if 'disk' in _dict:
            args['disk'] = AutoscalingDiskGroupDisk.from_dict(_dict.get('disk'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingSetGroupAutoscalingAutoscalingDiskGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'disk') and self.disk is not None:
            _dict['disk'] = self.disk.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingSetGroupAutoscalingAutoscalingDiskGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingSetGroupAutoscalingAutoscalingDiskGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingSetGroupAutoscalingAutoscalingDiskGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup(AutoscalingSetGroupAutoscaling):
    """
    AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup.

    :attr AutoscalingMemoryGroupMemory memory: (optional)
    """

    def __init__(self,
                 *,
                 memory: 'AutoscalingMemoryGroupMemory' = None) -> None:
        """
        Initialize a AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup object.

        :param AutoscalingMemoryGroupMemory memory: (optional)
        """
        # pylint: disable=super-init-not-called
        self.memory = memory

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup':
        """Initialize a AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup object from a json dictionary."""
        args = {}
        if 'memory' in _dict:
            args['memory'] = AutoscalingMemoryGroupMemory.from_dict(_dict.get('memory'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'memory') and self.memory is not None:
            _dict['memory'] = self.memory.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ConnectionConnectionElasticsearchConnection(ConnectionConnection):
    """
    Elasticsearch Connection Strings.

    :attr ElasticsearchConnectionHTTPS https: Elasticsearch Connection information
          for drivers and libraries.
    :attr ConnectionCLI cli: Connection information for cURL.
    """

    def __init__(self,
                 https: 'ElasticsearchConnectionHTTPS',
                 cli: 'ConnectionCLI') -> None:
        """
        Initialize a ConnectionConnectionElasticsearchConnection object.

        :param ElasticsearchConnectionHTTPS https: Elasticsearch Connection
               information for drivers and libraries.
        :param ConnectionCLI cli: Connection information for cURL.
        """
        # pylint: disable=super-init-not-called
        self.https = https
        self.cli = cli

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConnectionConnectionElasticsearchConnection':
        """Initialize a ConnectionConnectionElasticsearchConnection object from a json dictionary."""
        args = {}
        if 'https' in _dict:
            args['https'] = ElasticsearchConnectionHTTPS.from_dict(_dict.get('https'))
        else:
            raise ValueError('Required property \'https\' not present in ConnectionConnectionElasticsearchConnection JSON')
        if 'cli' in _dict:
            args['cli'] = ConnectionCLI.from_dict(_dict.get('cli'))
        else:
            raise ValueError('Required property \'cli\' not present in ConnectionConnectionElasticsearchConnection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConnectionConnectionElasticsearchConnection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'https') and self.https is not None:
            _dict['https'] = self.https.to_dict()
        if hasattr(self, 'cli') and self.cli is not None:
            _dict['cli'] = self.cli.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConnectionConnectionElasticsearchConnection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConnectionConnectionElasticsearchConnection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConnectionConnectionElasticsearchConnection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ConnectionConnectionEtcdConnection(ConnectionConnection):
    """
    etcd3 Connection Strings.

    :attr GRPCConnectionURI grpc: GRPC(etcd3) Connection information for drivers and
          libraries.
    :attr ConnectionCLI cli: Connection information for etcdctl.
    """

    def __init__(self,
                 grpc: 'GRPCConnectionURI',
                 cli: 'ConnectionCLI') -> None:
        """
        Initialize a ConnectionConnectionEtcdConnection object.

        :param GRPCConnectionURI grpc: GRPC(etcd3) Connection information for
               drivers and libraries.
        :param ConnectionCLI cli: Connection information for etcdctl.
        """
        # pylint: disable=super-init-not-called
        self.grpc = grpc
        self.cli = cli

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConnectionConnectionEtcdConnection':
        """Initialize a ConnectionConnectionEtcdConnection object from a json dictionary."""
        args = {}
        if 'grpc' in _dict:
            args['grpc'] = GRPCConnectionURI.from_dict(_dict.get('grpc'))
        else:
            raise ValueError('Required property \'grpc\' not present in ConnectionConnectionEtcdConnection JSON')
        if 'cli' in _dict:
            args['cli'] = ConnectionCLI.from_dict(_dict.get('cli'))
        else:
            raise ValueError('Required property \'cli\' not present in ConnectionConnectionEtcdConnection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConnectionConnectionEtcdConnection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'grpc') and self.grpc is not None:
            _dict['grpc'] = self.grpc.to_dict()
        if hasattr(self, 'cli') and self.cli is not None:
            _dict['cli'] = self.cli.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConnectionConnectionEtcdConnection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConnectionConnectionEtcdConnection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConnectionConnectionEtcdConnection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ConnectionConnectionMongoDBConnection(ConnectionConnection):
    """
    MongoDB Connection Strings.

    :attr MongoDBConnectionURI mongodb: MongoDB Connection information for drivers
          and libraries.
    :attr ConnectionCLI cli: Connection information for mongo shell.
    """

    def __init__(self,
                 mongodb: 'MongoDBConnectionURI',
                 cli: 'ConnectionCLI') -> None:
        """
        Initialize a ConnectionConnectionMongoDBConnection object.

        :param MongoDBConnectionURI mongodb: MongoDB Connection information for
               drivers and libraries.
        :param ConnectionCLI cli: Connection information for mongo shell.
        """
        # pylint: disable=super-init-not-called
        self.mongodb = mongodb
        self.cli = cli

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConnectionConnectionMongoDBConnection':
        """Initialize a ConnectionConnectionMongoDBConnection object from a json dictionary."""
        args = {}
        if 'mongodb' in _dict:
            args['mongodb'] = MongoDBConnectionURI.from_dict(_dict.get('mongodb'))
        else:
            raise ValueError('Required property \'mongodb\' not present in ConnectionConnectionMongoDBConnection JSON')
        if 'cli' in _dict:
            args['cli'] = ConnectionCLI.from_dict(_dict.get('cli'))
        else:
            raise ValueError('Required property \'cli\' not present in ConnectionConnectionMongoDBConnection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConnectionConnectionMongoDBConnection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'mongodb') and self.mongodb is not None:
            _dict['mongodb'] = self.mongodb.to_dict()
        if hasattr(self, 'cli') and self.cli is not None:
            _dict['cli'] = self.cli.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConnectionConnectionMongoDBConnection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConnectionConnectionMongoDBConnection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConnectionConnectionMongoDBConnection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ConnectionConnectionPostgreSQLConnection(ConnectionConnection):
    """
    PostgreSQL and EnterpriseDB Connection Strings.

    :attr PostgreSQLConnectionURI postgres: Connection information for drivers and
          libraries.
    :attr ConnectionCLI cli: Connection information for psql.
    """

    def __init__(self,
                 postgres: 'PostgreSQLConnectionURI',
                 cli: 'ConnectionCLI') -> None:
        """
        Initialize a ConnectionConnectionPostgreSQLConnection object.

        :param PostgreSQLConnectionURI postgres: Connection information for drivers
               and libraries.
        :param ConnectionCLI cli: Connection information for psql.
        """
        # pylint: disable=super-init-not-called
        self.postgres = postgres
        self.cli = cli

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConnectionConnectionPostgreSQLConnection':
        """Initialize a ConnectionConnectionPostgreSQLConnection object from a json dictionary."""
        args = {}
        if 'postgres' in _dict:
            args['postgres'] = PostgreSQLConnectionURI.from_dict(_dict.get('postgres'))
        else:
            raise ValueError('Required property \'postgres\' not present in ConnectionConnectionPostgreSQLConnection JSON')
        if 'cli' in _dict:
            args['cli'] = ConnectionCLI.from_dict(_dict.get('cli'))
        else:
            raise ValueError('Required property \'cli\' not present in ConnectionConnectionPostgreSQLConnection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConnectionConnectionPostgreSQLConnection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'postgres') and self.postgres is not None:
            _dict['postgres'] = self.postgres.to_dict()
        if hasattr(self, 'cli') and self.cli is not None:
            _dict['cli'] = self.cli.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConnectionConnectionPostgreSQLConnection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConnectionConnectionPostgreSQLConnection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConnectionConnectionPostgreSQLConnection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ConnectionConnectionRabbitMQConnection(ConnectionConnection):
    """
    RabbitMQ Connection Strings.

    :attr RabbitMQConnectionAMQPS amqps: RabbitMQ Connection information for AMQPS
          drivers and libraries.
    :attr RabbitMQConnectionMQTTS mqtts: RabbitMQ Connection information for MQTTS
          drivers and libraries.
    :attr RabbitMQConnectionStompSSL stomp_ssl: RabbitMQ Connection information for
          STOMP drivers and libraries.
    :attr RabbitMQConnectionHTTPS https: RabbitMQ Connection information for HTTPS.
    :attr ConnectionCLI cli: Connection information for rabbitmqadmin.
    """

    def __init__(self,
                 amqps: 'RabbitMQConnectionAMQPS',
                 mqtts: 'RabbitMQConnectionMQTTS',
                 stomp_ssl: 'RabbitMQConnectionStompSSL',
                 https: 'RabbitMQConnectionHTTPS',
                 cli: 'ConnectionCLI') -> None:
        """
        Initialize a ConnectionConnectionRabbitMQConnection object.

        :param RabbitMQConnectionAMQPS amqps: RabbitMQ Connection information for
               AMQPS drivers and libraries.
        :param RabbitMQConnectionMQTTS mqtts: RabbitMQ Connection information for
               MQTTS drivers and libraries.
        :param RabbitMQConnectionStompSSL stomp_ssl: RabbitMQ Connection
               information for STOMP drivers and libraries.
        :param RabbitMQConnectionHTTPS https: RabbitMQ Connection information for
               HTTPS.
        :param ConnectionCLI cli: Connection information for rabbitmqadmin.
        """
        # pylint: disable=super-init-not-called
        self.amqps = amqps
        self.mqtts = mqtts
        self.stomp_ssl = stomp_ssl
        self.https = https
        self.cli = cli

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConnectionConnectionRabbitMQConnection':
        """Initialize a ConnectionConnectionRabbitMQConnection object from a json dictionary."""
        args = {}
        if 'amqps' in _dict:
            args['amqps'] = RabbitMQConnectionAMQPS.from_dict(_dict.get('amqps'))
        else:
            raise ValueError('Required property \'amqps\' not present in ConnectionConnectionRabbitMQConnection JSON')
        if 'mqtts' in _dict:
            args['mqtts'] = RabbitMQConnectionMQTTS.from_dict(_dict.get('mqtts'))
        else:
            raise ValueError('Required property \'mqtts\' not present in ConnectionConnectionRabbitMQConnection JSON')
        if 'stomp_ssl' in _dict:
            args['stomp_ssl'] = RabbitMQConnectionStompSSL.from_dict(_dict.get('stomp_ssl'))
        else:
            raise ValueError('Required property \'stomp_ssl\' not present in ConnectionConnectionRabbitMQConnection JSON')
        if 'https' in _dict:
            args['https'] = RabbitMQConnectionHTTPS.from_dict(_dict.get('https'))
        else:
            raise ValueError('Required property \'https\' not present in ConnectionConnectionRabbitMQConnection JSON')
        if 'cli' in _dict:
            args['cli'] = ConnectionCLI.from_dict(_dict.get('cli'))
        else:
            raise ValueError('Required property \'cli\' not present in ConnectionConnectionRabbitMQConnection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConnectionConnectionRabbitMQConnection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'amqps') and self.amqps is not None:
            _dict['amqps'] = self.amqps.to_dict()
        if hasattr(self, 'mqtts') and self.mqtts is not None:
            _dict['mqtts'] = self.mqtts.to_dict()
        if hasattr(self, 'stomp_ssl') and self.stomp_ssl is not None:
            _dict['stomp_ssl'] = self.stomp_ssl.to_dict()
        if hasattr(self, 'https') and self.https is not None:
            _dict['https'] = self.https.to_dict()
        if hasattr(self, 'cli') and self.cli is not None:
            _dict['cli'] = self.cli.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConnectionConnectionRabbitMQConnection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConnectionConnectionRabbitMQConnection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConnectionConnectionRabbitMQConnection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ConnectionConnectionRedisConnection(ConnectionConnection):
    """
    Redis Connection Strings.

    :attr RedisConnectionURI rediss: Connection information for drivers and
          libraries.
    :attr ConnectionCLI cli: Connection information for a Redis CLI client.
    """

    def __init__(self,
                 rediss: 'RedisConnectionURI',
                 cli: 'ConnectionCLI') -> None:
        """
        Initialize a ConnectionConnectionRedisConnection object.

        :param RedisConnectionURI rediss: Connection information for drivers and
               libraries.
        :param ConnectionCLI cli: Connection information for a Redis CLI client.
        """
        # pylint: disable=super-init-not-called
        self.rediss = rediss
        self.cli = cli

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConnectionConnectionRedisConnection':
        """Initialize a ConnectionConnectionRedisConnection object from a json dictionary."""
        args = {}
        if 'rediss' in _dict:
            args['rediss'] = RedisConnectionURI.from_dict(_dict.get('rediss'))
        else:
            raise ValueError('Required property \'rediss\' not present in ConnectionConnectionRedisConnection JSON')
        if 'cli' in _dict:
            args['cli'] = ConnectionCLI.from_dict(_dict.get('cli'))
        else:
            raise ValueError('Required property \'cli\' not present in ConnectionConnectionRedisConnection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConnectionConnectionRedisConnection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'rediss') and self.rediss is not None:
            _dict['rediss'] = self.rediss.to_dict()
        if hasattr(self, 'cli') and self.cli is not None:
            _dict['cli'] = self.cli.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConnectionConnectionRedisConnection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConnectionConnectionRedisConnection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConnectionConnectionRedisConnection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SetConfigurationConfigurationPGConfiguration(SetConfigurationConfiguration):
    """
    PostgreSQL and EnterpriseDB Configuration.

    :attr int max_connections: (optional) Maximum connections allowed.
    :attr int max_prepared_transactions: (optional) Max number of transactions that
          can be in the "prepared" state simultaneously.
    :attr int deadlock_timeout: (optional) Deadlock timeout in ms. The time to wait
          on a lock before checking for deadlock.  Also the duration where lock waits will
          be logged.
    :attr int effective_io_concurrency: (optional) Number of simultaneous requests
          that can be handled efficiently by the disk subsystem.
    :attr int max_replication_slots: (optional) Maximum number of simultaneously
          defined replication slots.
    :attr int max_wal_senders: (optional) Maximum number of simultaneously running
          WAL sender processes.
    :attr int shared_buffers: (optional) The number of 8kB shared memory buffers
          used by the server.  Set to 1/4 of memory.  Setting too high will cause crashes
          or prevent the database from starting.
    :attr str synchronous_commit: (optional) Sets the current transaction's
          synchronization level.  Off can result in data loss.  remote_write with enable
          synchronous replication which will impact performance and availabilty.
    :attr str wal_level: (optional) WAL level.  Set to logical to use logical
          decoding or logical replication.
    :attr int archive_timeout: (optional) The number of seconds to wait before
          forces a switch to the next WAL file if a new file has not been started.
    :attr int log_min_duration_statement: (optional) The minimum number of
          milliseconds for execution time above which statements will be logged.
    """

    def __init__(self,
                 *,
                 max_connections: int = None,
                 max_prepared_transactions: int = None,
                 deadlock_timeout: int = None,
                 effective_io_concurrency: int = None,
                 max_replication_slots: int = None,
                 max_wal_senders: int = None,
                 shared_buffers: int = None,
                 synchronous_commit: str = None,
                 wal_level: str = None,
                 archive_timeout: int = None,
                 log_min_duration_statement: int = None) -> None:
        """
        Initialize a SetConfigurationConfigurationPGConfiguration object.

        :param int max_connections: (optional) Maximum connections allowed.
        :param int max_prepared_transactions: (optional) Max number of transactions
               that can be in the "prepared" state simultaneously.
        :param int deadlock_timeout: (optional) Deadlock timeout in ms. The time to
               wait on a lock before checking for deadlock.  Also the duration where lock
               waits will be logged.
        :param int effective_io_concurrency: (optional) Number of simultaneous
               requests that can be handled efficiently by the disk subsystem.
        :param int max_replication_slots: (optional) Maximum number of
               simultaneously defined replication slots.
        :param int max_wal_senders: (optional) Maximum number of simultaneously
               running WAL sender processes.
        :param int shared_buffers: (optional) The number of 8kB shared memory
               buffers used by the server.  Set to 1/4 of memory.  Setting too high will
               cause crashes or prevent the database from starting.
        :param str synchronous_commit: (optional) Sets the current transaction's
               synchronization level.  Off can result in data loss.  remote_write with
               enable synchronous replication which will impact performance and
               availabilty.
        :param str wal_level: (optional) WAL level.  Set to logical to use logical
               decoding or logical replication.
        :param int archive_timeout: (optional) The number of seconds to wait before
               forces a switch to the next WAL file if a new file has not been started.
        :param int log_min_duration_statement: (optional) The minimum number of
               milliseconds for execution time above which statements will be logged.
        """
        # pylint: disable=super-init-not-called
        self.max_connections = max_connections
        self.max_prepared_transactions = max_prepared_transactions
        self.deadlock_timeout = deadlock_timeout
        self.effective_io_concurrency = effective_io_concurrency
        self.max_replication_slots = max_replication_slots
        self.max_wal_senders = max_wal_senders
        self.shared_buffers = shared_buffers
        self.synchronous_commit = synchronous_commit
        self.wal_level = wal_level
        self.archive_timeout = archive_timeout
        self.log_min_duration_statement = log_min_duration_statement

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetConfigurationConfigurationPGConfiguration':
        """Initialize a SetConfigurationConfigurationPGConfiguration object from a json dictionary."""
        args = {}
        if 'max_connections' in _dict:
            args['max_connections'] = _dict.get('max_connections')
        if 'max_prepared_transactions' in _dict:
            args['max_prepared_transactions'] = _dict.get('max_prepared_transactions')
        if 'deadlock_timeout' in _dict:
            args['deadlock_timeout'] = _dict.get('deadlock_timeout')
        if 'effective_io_concurrency' in _dict:
            args['effective_io_concurrency'] = _dict.get('effective_io_concurrency')
        if 'max_replication_slots' in _dict:
            args['max_replication_slots'] = _dict.get('max_replication_slots')
        if 'max_wal_senders' in _dict:
            args['max_wal_senders'] = _dict.get('max_wal_senders')
        if 'shared_buffers' in _dict:
            args['shared_buffers'] = _dict.get('shared_buffers')
        if 'synchronous_commit' in _dict:
            args['synchronous_commit'] = _dict.get('synchronous_commit')
        if 'wal_level' in _dict:
            args['wal_level'] = _dict.get('wal_level')
        if 'archive_timeout' in _dict:
            args['archive_timeout'] = _dict.get('archive_timeout')
        if 'log_min_duration_statement' in _dict:
            args['log_min_duration_statement'] = _dict.get('log_min_duration_statement')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetConfigurationConfigurationPGConfiguration object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'max_connections') and self.max_connections is not None:
            _dict['max_connections'] = self.max_connections
        if hasattr(self, 'max_prepared_transactions') and self.max_prepared_transactions is not None:
            _dict['max_prepared_transactions'] = self.max_prepared_transactions
        if hasattr(self, 'deadlock_timeout') and self.deadlock_timeout is not None:
            _dict['deadlock_timeout'] = self.deadlock_timeout
        if hasattr(self, 'effective_io_concurrency') and self.effective_io_concurrency is not None:
            _dict['effective_io_concurrency'] = self.effective_io_concurrency
        if hasattr(self, 'max_replication_slots') and self.max_replication_slots is not None:
            _dict['max_replication_slots'] = self.max_replication_slots
        if hasattr(self, 'max_wal_senders') and self.max_wal_senders is not None:
            _dict['max_wal_senders'] = self.max_wal_senders
        if hasattr(self, 'shared_buffers') and self.shared_buffers is not None:
            _dict['shared_buffers'] = self.shared_buffers
        if hasattr(self, 'synchronous_commit') and self.synchronous_commit is not None:
            _dict['synchronous_commit'] = self.synchronous_commit
        if hasattr(self, 'wal_level') and self.wal_level is not None:
            _dict['wal_level'] = self.wal_level
        if hasattr(self, 'archive_timeout') and self.archive_timeout is not None:
            _dict['archive_timeout'] = self.archive_timeout
        if hasattr(self, 'log_min_duration_statement') and self.log_min_duration_statement is not None:
            _dict['log_min_duration_statement'] = self.log_min_duration_statement
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetConfigurationConfigurationPGConfiguration object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetConfigurationConfigurationPGConfiguration') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetConfigurationConfigurationPGConfiguration') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SynchronousCommitEnum(str, Enum):
        """
        Sets the current transaction's synchronization level.  Off can result in data
        loss.  remote_write with enable synchronous replication which will impact
        performance and availabilty.
        """
        LOCAL = 'local'
        OFF = 'off'


    class WalLevelEnum(str, Enum):
        """
        WAL level.  Set to logical to use logical decoding or logical replication.
        """
        HOT_STANDBY = 'hot_standby'
        LOGICAL = 'logical'


class SetConfigurationConfigurationRedisConfiguration(SetConfigurationConfiguration):
    """
    Redis Configuration.

    :attr int maxmemory_redis: (optional) The maximum memory Redis should use, as
          bytes.
    :attr str maxmemory_policy: (optional) The policy with which Redis evicts keys
          when maximum memory is reached.
    :attr str appendonly: (optional) If set to yes this will enable AOF persistence.
    :attr int maxmemory_samples: (optional) The maximum memory Redis should use, as
          bytes.
    :attr str stop_writes_on_bgsave_error: (optional) Whether or not to stop
          accepting writes when background persistence actions fail.
    """

    def __init__(self,
                 *,
                 maxmemory_redis: int = None,
                 maxmemory_policy: str = None,
                 appendonly: str = None,
                 maxmemory_samples: int = None,
                 stop_writes_on_bgsave_error: str = None) -> None:
        """
        Initialize a SetConfigurationConfigurationRedisConfiguration object.

        :param int maxmemory_redis: (optional) The maximum memory Redis should use,
               as bytes.
        :param str maxmemory_policy: (optional) The policy with which Redis evicts
               keys when maximum memory is reached.
        :param str appendonly: (optional) If set to yes this will enable AOF
               persistence.
        :param int maxmemory_samples: (optional) The maximum memory Redis should
               use, as bytes.
        :param str stop_writes_on_bgsave_error: (optional) Whether or not to stop
               accepting writes when background persistence actions fail.
        """
        # pylint: disable=super-init-not-called
        self.maxmemory_redis = maxmemory_redis
        self.maxmemory_policy = maxmemory_policy
        self.appendonly = appendonly
        self.maxmemory_samples = maxmemory_samples
        self.stop_writes_on_bgsave_error = stop_writes_on_bgsave_error

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetConfigurationConfigurationRedisConfiguration':
        """Initialize a SetConfigurationConfigurationRedisConfiguration object from a json dictionary."""
        args = {}
        if 'maxmemory-redis' in _dict:
            args['maxmemory_redis'] = _dict.get('maxmemory-redis')
        if 'maxmemory-policy' in _dict:
            args['maxmemory_policy'] = _dict.get('maxmemory-policy')
        if 'appendonly' in _dict:
            args['appendonly'] = _dict.get('appendonly')
        if 'maxmemory-samples' in _dict:
            args['maxmemory_samples'] = _dict.get('maxmemory-samples')
        if 'stop-writes-on-bgsave-error' in _dict:
            args['stop_writes_on_bgsave_error'] = _dict.get('stop-writes-on-bgsave-error')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetConfigurationConfigurationRedisConfiguration object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'maxmemory_redis') and self.maxmemory_redis is not None:
            _dict['maxmemory-redis'] = self.maxmemory_redis
        if hasattr(self, 'maxmemory_policy') and self.maxmemory_policy is not None:
            _dict['maxmemory-policy'] = self.maxmemory_policy
        if hasattr(self, 'appendonly') and self.appendonly is not None:
            _dict['appendonly'] = self.appendonly
        if hasattr(self, 'maxmemory_samples') and self.maxmemory_samples is not None:
            _dict['maxmemory-samples'] = self.maxmemory_samples
        if hasattr(self, 'stop_writes_on_bgsave_error') and self.stop_writes_on_bgsave_error is not None:
            _dict['stop-writes-on-bgsave-error'] = self.stop_writes_on_bgsave_error
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetConfigurationConfigurationRedisConfiguration object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetConfigurationConfigurationRedisConfiguration') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetConfigurationConfigurationRedisConfiguration') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class MaxmemoryPolicyEnum(str, Enum):
        """
        The policy with which Redis evicts keys when maximum memory is reached.
        """
        VOLATILE_LRU = 'volatile-lru'
        ALLKEYS_LRU = 'allkeys-lru'
        VOLATILE_RANDOM = 'volatile-random'
        ALLKEYS_RANDOM = 'allkeys-random'
        VOLATILE_TTL = 'volatile-ttl'
        NOEVICTION = 'noeviction'


    class AppendonlyEnum(str, Enum):
        """
        If set to yes this will enable AOF persistence.
        """
        YES = 'yes'
        NO = 'no'


    class StopWritesOnBgsaveErrorEnum(str, Enum):
        """
        Whether or not to stop accepting writes when background persistence actions fail.
        """
        YES = 'yes'
        NO = 'no'


class SetDeploymentScalingGroupRequestSetCPUGroup(SetDeploymentScalingGroupRequest):
    """
    SetDeploymentScalingGroupRequestSetCPUGroup.

    :attr SetCPUGroupCPU cpu: (optional)
    """

    def __init__(self,
                 *,
                 cpu: 'SetCPUGroupCPU' = None) -> None:
        """
        Initialize a SetDeploymentScalingGroupRequestSetCPUGroup object.

        :param SetCPUGroupCPU cpu: (optional)
        """
        # pylint: disable=super-init-not-called
        self.cpu = cpu

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetDeploymentScalingGroupRequestSetCPUGroup':
        """Initialize a SetDeploymentScalingGroupRequestSetCPUGroup object from a json dictionary."""
        args = {}
        if 'cpu' in _dict:
            args['cpu'] = SetCPUGroupCPU.from_dict(_dict.get('cpu'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetDeploymentScalingGroupRequestSetCPUGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cpu') and self.cpu is not None:
            _dict['cpu'] = self.cpu.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetDeploymentScalingGroupRequestSetCPUGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetDeploymentScalingGroupRequestSetCPUGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetDeploymentScalingGroupRequestSetCPUGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SetDeploymentScalingGroupRequestSetDiskGroup(SetDeploymentScalingGroupRequest):
    """
    SetDeploymentScalingGroupRequestSetDiskGroup.

    :attr SetDiskGroupDisk disk: (optional)
    """

    def __init__(self,
                 *,
                 disk: 'SetDiskGroupDisk' = None) -> None:
        """
        Initialize a SetDeploymentScalingGroupRequestSetDiskGroup object.

        :param SetDiskGroupDisk disk: (optional)
        """
        # pylint: disable=super-init-not-called
        self.disk = disk

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetDeploymentScalingGroupRequestSetDiskGroup':
        """Initialize a SetDeploymentScalingGroupRequestSetDiskGroup object from a json dictionary."""
        args = {}
        if 'disk' in _dict:
            args['disk'] = SetDiskGroupDisk.from_dict(_dict.get('disk'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetDeploymentScalingGroupRequestSetDiskGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'disk') and self.disk is not None:
            _dict['disk'] = self.disk.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetDeploymentScalingGroupRequestSetDiskGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetDeploymentScalingGroupRequestSetDiskGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetDeploymentScalingGroupRequestSetDiskGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SetDeploymentScalingGroupRequestSetMembersGroup(SetDeploymentScalingGroupRequest):
    """
    SetDeploymentScalingGroupRequestSetMembersGroup.

    :attr SetMembersGroupMembers members: (optional)
    """

    def __init__(self,
                 *,
                 members: 'SetMembersGroupMembers' = None) -> None:
        """
        Initialize a SetDeploymentScalingGroupRequestSetMembersGroup object.

        :param SetMembersGroupMembers members: (optional)
        """
        # pylint: disable=super-init-not-called
        self.members = members

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetDeploymentScalingGroupRequestSetMembersGroup':
        """Initialize a SetDeploymentScalingGroupRequestSetMembersGroup object from a json dictionary."""
        args = {}
        if 'members' in _dict:
            args['members'] = SetMembersGroupMembers.from_dict(_dict.get('members'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetDeploymentScalingGroupRequestSetMembersGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'members') and self.members is not None:
            _dict['members'] = self.members.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetDeploymentScalingGroupRequestSetMembersGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetDeploymentScalingGroupRequestSetMembersGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetDeploymentScalingGroupRequestSetMembersGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SetDeploymentScalingGroupRequestSetMemoryGroup(SetDeploymentScalingGroupRequest):
    """
    SetDeploymentScalingGroupRequestSetMemoryGroup.

    :attr SetMemoryGroupMemory memory: (optional)
    """

    def __init__(self,
                 *,
                 memory: 'SetMemoryGroupMemory' = None) -> None:
        """
        Initialize a SetDeploymentScalingGroupRequestSetMemoryGroup object.

        :param SetMemoryGroupMemory memory: (optional)
        """
        # pylint: disable=super-init-not-called
        self.memory = memory

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetDeploymentScalingGroupRequestSetMemoryGroup':
        """Initialize a SetDeploymentScalingGroupRequestSetMemoryGroup object from a json dictionary."""
        args = {}
        if 'memory' in _dict:
            args['memory'] = SetMemoryGroupMemory.from_dict(_dict.get('memory'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetDeploymentScalingGroupRequestSetMemoryGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'memory') and self.memory is not None:
            _dict['memory'] = self.memory.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetDeploymentScalingGroupRequestSetMemoryGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetDeploymentScalingGroupRequestSetMemoryGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetDeploymentScalingGroupRequestSetMemoryGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SetPromotionPromotionPromote(SetPromotionPromotion):
    """
    Promotes a read-only replica to a full deployment.

    :attr dict promotion: (optional) Promotion options.
    """

    def __init__(self,
                 *,
                 promotion: dict = None) -> None:
        """
        Initialize a SetPromotionPromotionPromote object.

        :param dict promotion: (optional) Promotion options.
        """
        # pylint: disable=super-init-not-called
        self.promotion = promotion

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetPromotionPromotionPromote':
        """Initialize a SetPromotionPromotionPromote object from a json dictionary."""
        args = {}
        if 'promotion' in _dict:
            args['promotion'] = _dict.get('promotion')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetPromotionPromotionPromote object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'promotion') and self.promotion is not None:
            _dict['promotion'] = self.promotion
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetPromotionPromotionPromote object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetPromotionPromotionPromote') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetPromotionPromotionPromote') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SetPromotionPromotionUpgradePromote(SetPromotionPromotion):
    """
    Promotes a read-only replica to a full deployment running a new database version.

    :attr dict promotion: (optional) Promotion and Upgrade options.
    """

    def __init__(self,
                 *,
                 promotion: dict = None) -> None:
        """
        Initialize a SetPromotionPromotionUpgradePromote object.

        :param dict promotion: (optional) Promotion and Upgrade options.
        """
        # pylint: disable=super-init-not-called
        self.promotion = promotion

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SetPromotionPromotionUpgradePromote':
        """Initialize a SetPromotionPromotionUpgradePromote object from a json dictionary."""
        args = {}
        if 'promotion' in _dict:
            args['promotion'] = _dict.get('promotion')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SetPromotionPromotionUpgradePromote object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'promotion') and self.promotion is not None:
            _dict['promotion'] = self.promotion
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SetPromotionPromotionUpgradePromote object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SetPromotionPromotionUpgradePromote') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SetPromotionPromotionUpgradePromote') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
