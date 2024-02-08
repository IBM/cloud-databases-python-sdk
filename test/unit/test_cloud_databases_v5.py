# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2024.
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

"""
Unit Tests for CloudDatabasesV5
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_cloud_databases.cloud_databases_v5 import *


_service = CloudDatabasesV5(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://api.us-south.databases.cloud.ibm.com/v5/ibm'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
        return re.compile(request_url.rstrip('/') + '/+')


def test_parameterized_url():
    """
    Test formatting the parameterized service URL with the default variable values.
    """
    default_formatted_url = 'https://api.us-south.databases.cloud.ibm.com/v5/ibm'
    assert CloudDatabasesV5.construct_service_url() == default_formatted_url


##############################################################################
# Start of Service: Deployments
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CloudDatabasesV5.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CloudDatabasesV5)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CloudDatabasesV5.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListDeployables():
    """
    Test Class for list_deployables
    """

    @responses.activate
    def test_list_deployables_all_params(self):
        """
        list_deployables()
        """
        # Set up mock
        url = preprocess_url('/deployables')
        mock_response = '{"deployables": [{"type": "elasticsearch", "versions": [{"version": "5.6", "status": "stable", "is_preferred": true, "transitions": [{"application": "elasticsearch", "method": "restore", "from_version": "5.6", "to_version": "6.7"}]}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_deployables()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_deployables_all_params_with_retries(self):
        # Enable retries and run test_list_deployables_all_params.
        _service.enable_retries()
        self.test_list_deployables_all_params()

        # Disable retries and run test_list_deployables_all_params.
        _service.disable_retries()
        self.test_list_deployables_all_params()

class TestListRegions():
    """
    Test Class for list_regions
    """

    @responses.activate
    def test_list_regions_all_params(self):
        """
        list_regions()
        """
        # Set up mock
        url = preprocess_url('/regions')
        mock_response = '{"regions": ["regions"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_regions()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_regions_all_params_with_retries(self):
        # Enable retries and run test_list_regions_all_params.
        _service.enable_retries()
        self.test_list_regions_all_params()

        # Disable retries and run test_list_regions_all_params.
        _service.disable_retries()
        self.test_list_regions_all_params()

class TestGetDeploymentInfo():
    """
    Test Class for get_deployment_info
    """

    @responses.activate
    def test_get_deployment_info_all_params(self):
        """
        get_deployment_info()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString')
        mock_response = '{"deployment": {"id": "crn:v1:bluemix:public:databases-for-redis:us-south:a/274074dce64e9c423ffc238516c755e1:29caf0e7-120f-4da8-9551-3abf57ebcfc7::", "name": "crn:v1:bluemix:public:databases-for-redis:us-south:a/274074dce64e9c423ffc238516c755e1:29caf0e7-120f-4da8-9551-3abf57ebcfc7::", "type": "redis", "platform": "satellite, classic", "platform_options": {"anyKey": "anyValue"}, "version": "4", "admin_usernames": {"mapKey": "inner"}, "enable_public_endpoints": true, "enable_private_endpoints": false}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_deployment_info(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_deployment_info_all_params_with_retries(self):
        # Enable retries and run test_get_deployment_info_all_params.
        _service.enable_retries()
        self.test_get_deployment_info_all_params()

        # Disable retries and run test_get_deployment_info_all_params.
        _service.disable_retries()
        self.test_get_deployment_info_all_params()

    @responses.activate
    def test_get_deployment_info_value_error(self):
        """
        test_get_deployment_info_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString')
        mock_response = '{"deployment": {"id": "crn:v1:bluemix:public:databases-for-redis:us-south:a/274074dce64e9c423ffc238516c755e1:29caf0e7-120f-4da8-9551-3abf57ebcfc7::", "name": "crn:v1:bluemix:public:databases-for-redis:us-south:a/274074dce64e9c423ffc238516c755e1:29caf0e7-120f-4da8-9551-3abf57ebcfc7::", "type": "redis", "platform": "satellite, classic", "platform_options": {"anyKey": "anyValue"}, "version": "4", "admin_usernames": {"mapKey": "inner"}, "enable_public_endpoints": true, "enable_private_endpoints": false}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_deployment_info(**req_copy)

    def test_get_deployment_info_value_error_with_retries(self):
        # Enable retries and run test_get_deployment_info_value_error.
        _service.enable_retries()
        self.test_get_deployment_info_value_error()

        # Disable retries and run test_get_deployment_info_value_error.
        _service.disable_retries()
        self.test_get_deployment_info_value_error()

# endregion
##############################################################################
# End of Service: Deployments
##############################################################################

##############################################################################
# Start of Service: DatabaseUsers
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CloudDatabasesV5.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CloudDatabasesV5)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CloudDatabasesV5.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestCreateDatabaseUser():
    """
    Test Class for create_database_user
    """

    @responses.activate
    def test_create_database_user_all_params(self):
        """
        create_database_user()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/users/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a UserDatabaseUser model
        user_model = {}
        user_model['username'] = 'user'
        user_model['password'] = 'v3ry-1-secUre-pAssword-2'

        # Set up parameter values
        id = 'testString'
        user_type = 'testString'
        user = user_model

        # Invoke method
        response = _service.create_database_user(
            id,
            user_type,
            user=user,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['user'] == user_model

    def test_create_database_user_all_params_with_retries(self):
        # Enable retries and run test_create_database_user_all_params.
        _service.enable_retries()
        self.test_create_database_user_all_params()

        # Disable retries and run test_create_database_user_all_params.
        _service.disable_retries()
        self.test_create_database_user_all_params()

    @responses.activate
    def test_create_database_user_value_error(self):
        """
        test_create_database_user_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/users/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a UserDatabaseUser model
        user_model = {}
        user_model['username'] = 'user'
        user_model['password'] = 'v3ry-1-secUre-pAssword-2'

        # Set up parameter values
        id = 'testString'
        user_type = 'testString'
        user = user_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "user_type": user_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_database_user(**req_copy)

    def test_create_database_user_value_error_with_retries(self):
        # Enable retries and run test_create_database_user_value_error.
        _service.enable_retries()
        self.test_create_database_user_value_error()

        # Disable retries and run test_create_database_user_value_error.
        _service.disable_retries()
        self.test_create_database_user_value_error()

class TestUpdateUser():
    """
    Test Class for update_user
    """

    @responses.activate
    def test_update_user_all_params(self):
        """
        update_user()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/users/database/user')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a UserUpdatePasswordSetting model
        user_update_model = {}
        user_update_model['password'] = 'v3ry-1-secUre-pAssword-2'

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        username = 'user'
        user = user_update_model

        # Invoke method
        response = _service.update_user(
            id,
            user_type,
            username,
            user=user,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['user'] == user_update_model

    def test_update_user_all_params_with_retries(self):
        # Enable retries and run test_update_user_all_params.
        _service.enable_retries()
        self.test_update_user_all_params()

        # Disable retries and run test_update_user_all_params.
        _service.disable_retries()
        self.test_update_user_all_params()

    @responses.activate
    def test_update_user_value_error(self):
        """
        test_update_user_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/users/database/user')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a UserUpdatePasswordSetting model
        user_update_model = {}
        user_update_model['password'] = 'v3ry-1-secUre-pAssword-2'

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        username = 'user'
        user = user_update_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "user_type": user_type,
            "username": username,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_user(**req_copy)

    def test_update_user_value_error_with_retries(self):
        # Enable retries and run test_update_user_value_error.
        _service.enable_retries()
        self.test_update_user_value_error()

        # Disable retries and run test_update_user_value_error.
        _service.disable_retries()
        self.test_update_user_value_error()

class TestDeleteDatabaseUser():
    """
    Test Class for delete_database_user
    """

    @responses.activate
    def test_delete_database_user_all_params(self):
        """
        delete_database_user()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/users/database/user')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        username = 'user'

        # Invoke method
        response = _service.delete_database_user(
            id,
            user_type,
            username,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_database_user_all_params_with_retries(self):
        # Enable retries and run test_delete_database_user_all_params.
        _service.enable_retries()
        self.test_delete_database_user_all_params()

        # Disable retries and run test_delete_database_user_all_params.
        _service.disable_retries()
        self.test_delete_database_user_all_params()

    @responses.activate
    def test_delete_database_user_value_error(self):
        """
        test_delete_database_user_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/users/database/user')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        username = 'user'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "user_type": user_type,
            "username": username,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_database_user(**req_copy)

    def test_delete_database_user_value_error_with_retries(self):
        # Enable retries and run test_delete_database_user_value_error.
        _service.enable_retries()
        self.test_delete_database_user_value_error()

        # Disable retries and run test_delete_database_user_value_error.
        _service.disable_retries()
        self.test_delete_database_user_value_error()

# endregion
##############################################################################
# End of Service: DatabaseUsers
##############################################################################

##############################################################################
# Start of Service: DatabaseConfiguration
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CloudDatabasesV5.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CloudDatabasesV5)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CloudDatabasesV5.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestUpdateDatabaseConfiguration():
    """
    Test Class for update_database_configuration
    """

    @responses.activate
    def test_update_database_configuration_all_params(self):
        """
        update_database_configuration()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/configuration')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ConfigurationPGConfiguration model
        configuration_model = {}
        configuration_model['archive_timeout'] = 300
        configuration_model['deadlock_timeout'] = 100
        configuration_model['effective_io_concurrency'] = 1
        configuration_model['log_connections'] = 'off'
        configuration_model['log_disconnections'] = 'off'
        configuration_model['log_min_duration_statement'] = 100
        configuration_model['max_connections'] = 200
        configuration_model['max_prepared_transactions'] = 0
        configuration_model['max_replication_slots'] = 10
        configuration_model['max_wal_senders'] = 12
        configuration_model['shared_buffers'] = 16
        configuration_model['synchronous_commit'] = 'local'
        configuration_model['tcp_keepalives_count'] = 0
        configuration_model['tcp_keepalives_idle'] = 0
        configuration_model['tcp_keepalives_interval'] = 0
        configuration_model['wal_level'] = 'hot_standby'

        # Set up parameter values
        id = 'testString'
        configuration = configuration_model

        # Invoke method
        response = _service.update_database_configuration(
            id,
            configuration=configuration,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['configuration'] == configuration_model

    def test_update_database_configuration_all_params_with_retries(self):
        # Enable retries and run test_update_database_configuration_all_params.
        _service.enable_retries()
        self.test_update_database_configuration_all_params()

        # Disable retries and run test_update_database_configuration_all_params.
        _service.disable_retries()
        self.test_update_database_configuration_all_params()

    @responses.activate
    def test_update_database_configuration_value_error(self):
        """
        test_update_database_configuration_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/configuration')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ConfigurationPGConfiguration model
        configuration_model = {}
        configuration_model['archive_timeout'] = 300
        configuration_model['deadlock_timeout'] = 100
        configuration_model['effective_io_concurrency'] = 1
        configuration_model['log_connections'] = 'off'
        configuration_model['log_disconnections'] = 'off'
        configuration_model['log_min_duration_statement'] = 100
        configuration_model['max_connections'] = 200
        configuration_model['max_prepared_transactions'] = 0
        configuration_model['max_replication_slots'] = 10
        configuration_model['max_wal_senders'] = 12
        configuration_model['shared_buffers'] = 16
        configuration_model['synchronous_commit'] = 'local'
        configuration_model['tcp_keepalives_count'] = 0
        configuration_model['tcp_keepalives_idle'] = 0
        configuration_model['tcp_keepalives_interval'] = 0
        configuration_model['wal_level'] = 'hot_standby'

        # Set up parameter values
        id = 'testString'
        configuration = configuration_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_database_configuration(**req_copy)

    def test_update_database_configuration_value_error_with_retries(self):
        # Enable retries and run test_update_database_configuration_value_error.
        _service.enable_retries()
        self.test_update_database_configuration_value_error()

        # Disable retries and run test_update_database_configuration_value_error.
        _service.disable_retries()
        self.test_update_database_configuration_value_error()

# endregion
##############################################################################
# End of Service: DatabaseConfiguration
##############################################################################

##############################################################################
# Start of Service: Remotes
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CloudDatabasesV5.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CloudDatabasesV5)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CloudDatabasesV5.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListRemotes():
    """
    Test Class for list_remotes
    """

    @responses.activate
    def test_list_remotes_all_params(self):
        """
        list_remotes()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/remotes')
        mock_response = '{"remotes": {"leader": "01f30581-54f8-41a4-8193-4a04cc022e9b-h", "replicas": ["replicas"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.list_remotes(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_remotes_all_params_with_retries(self):
        # Enable retries and run test_list_remotes_all_params.
        _service.enable_retries()
        self.test_list_remotes_all_params()

        # Disable retries and run test_list_remotes_all_params.
        _service.disable_retries()
        self.test_list_remotes_all_params()

    @responses.activate
    def test_list_remotes_value_error(self):
        """
        test_list_remotes_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/remotes')
        mock_response = '{"remotes": {"leader": "01f30581-54f8-41a4-8193-4a04cc022e9b-h", "replicas": ["replicas"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_remotes(**req_copy)

    def test_list_remotes_value_error_with_retries(self):
        # Enable retries and run test_list_remotes_value_error.
        _service.enable_retries()
        self.test_list_remotes_value_error()

        # Disable retries and run test_list_remotes_value_error.
        _service.disable_retries()
        self.test_list_remotes_value_error()

class TestResyncReplica():
    """
    Test Class for resync_replica
    """

    @responses.activate
    def test_resync_replica_all_params(self):
        """
        resync_replica()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/remotes/resync')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.resync_replica(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_resync_replica_all_params_with_retries(self):
        # Enable retries and run test_resync_replica_all_params.
        _service.enable_retries()
        self.test_resync_replica_all_params()

        # Disable retries and run test_resync_replica_all_params.
        _service.disable_retries()
        self.test_resync_replica_all_params()

    @responses.activate
    def test_resync_replica_value_error(self):
        """
        test_resync_replica_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/remotes/resync')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.resync_replica(**req_copy)

    def test_resync_replica_value_error_with_retries(self):
        # Enable retries and run test_resync_replica_value_error.
        _service.enable_retries()
        self.test_resync_replica_value_error()

        # Disable retries and run test_resync_replica_value_error.
        _service.disable_retries()
        self.test_resync_replica_value_error()

class TestPromoteReadOnlyReplica():
    """
    Test Class for promote_read_only_replica
    """

    @responses.activate
    def test_promote_read_only_replica_all_params(self):
        """
        promote_read_only_replica()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/remotes/promotion')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        promotion = {'foo': 'bar'}

        # Invoke method
        response = _service.promote_read_only_replica(
            id,
            promotion=promotion,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['promotion'] == {'foo': 'bar'}

    def test_promote_read_only_replica_all_params_with_retries(self):
        # Enable retries and run test_promote_read_only_replica_all_params.
        _service.enable_retries()
        self.test_promote_read_only_replica_all_params()

        # Disable retries and run test_promote_read_only_replica_all_params.
        _service.disable_retries()
        self.test_promote_read_only_replica_all_params()

    @responses.activate
    def test_promote_read_only_replica_value_error(self):
        """
        test_promote_read_only_replica_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/remotes/promotion')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        promotion = {'foo': 'bar'}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.promote_read_only_replica(**req_copy)

    def test_promote_read_only_replica_value_error_with_retries(self):
        # Enable retries and run test_promote_read_only_replica_value_error.
        _service.enable_retries()
        self.test_promote_read_only_replica_value_error()

        # Disable retries and run test_promote_read_only_replica_value_error.
        _service.disable_retries()
        self.test_promote_read_only_replica_value_error()

# endregion
##############################################################################
# End of Service: Remotes
##############################################################################

##############################################################################
# Start of Service: Tasks
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CloudDatabasesV5.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CloudDatabasesV5)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CloudDatabasesV5.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListDeploymentTasks():
    """
    Test Class for list_deployment_tasks
    """

    @responses.activate
    def test_list_deployment_tasks_all_params(self):
        """
        list_deployment_tasks()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/tasks')
        mock_response = '{"tasks": [{"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.list_deployment_tasks(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_deployment_tasks_all_params_with_retries(self):
        # Enable retries and run test_list_deployment_tasks_all_params.
        _service.enable_retries()
        self.test_list_deployment_tasks_all_params()

        # Disable retries and run test_list_deployment_tasks_all_params.
        _service.disable_retries()
        self.test_list_deployment_tasks_all_params()

    @responses.activate
    def test_list_deployment_tasks_value_error(self):
        """
        test_list_deployment_tasks_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/tasks')
        mock_response = '{"tasks": [{"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_deployment_tasks(**req_copy)

    def test_list_deployment_tasks_value_error_with_retries(self):
        # Enable retries and run test_list_deployment_tasks_value_error.
        _service.enable_retries()
        self.test_list_deployment_tasks_value_error()

        # Disable retries and run test_list_deployment_tasks_value_error.
        _service.disable_retries()
        self.test_list_deployment_tasks_value_error()

class TestGetTask():
    """
    Test Class for get_task
    """

    @responses.activate
    def test_get_task_all_params(self):
        """
        get_task()
        """
        # Set up mock
        url = preprocess_url('/tasks/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_task(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_task_all_params_with_retries(self):
        # Enable retries and run test_get_task_all_params.
        _service.enable_retries()
        self.test_get_task_all_params()

        # Disable retries and run test_get_task_all_params.
        _service.disable_retries()
        self.test_get_task_all_params()

    @responses.activate
    def test_get_task_value_error(self):
        """
        test_get_task_value_error()
        """
        # Set up mock
        url = preprocess_url('/tasks/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_task(**req_copy)

    def test_get_task_value_error_with_retries(self):
        # Enable retries and run test_get_task_value_error.
        _service.enable_retries()
        self.test_get_task_value_error()

        # Disable retries and run test_get_task_value_error.
        _service.disable_retries()
        self.test_get_task_value_error()

# endregion
##############################################################################
# End of Service: Tasks
##############################################################################

##############################################################################
# Start of Service: Backups
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CloudDatabasesV5.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CloudDatabasesV5)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CloudDatabasesV5.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestGetBackupInfo():
    """
    Test Class for get_backup_info
    """

    @responses.activate
    def test_get_backup_info_all_params(self):
        """
        get_backup_info()
        """
        # Set up mock
        url = preprocess_url('/backups/testString')
        mock_response = '{"backup": {"id": "5a970218cb7544000671c094", "deployment_id": "595eada310b7ac00116dd48b", "type": "scheduled", "status": "running", "is_downloadable": true, "is_restorable": true, "download_link": "https://securedownloadservice.com/backup-2018-02-28T19:25:12Z.tgz", "created_at": "2018-02-28T19:25:12.000Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        backup_id = 'testString'

        # Invoke method
        response = _service.get_backup_info(
            backup_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_backup_info_all_params_with_retries(self):
        # Enable retries and run test_get_backup_info_all_params.
        _service.enable_retries()
        self.test_get_backup_info_all_params()

        # Disable retries and run test_get_backup_info_all_params.
        _service.disable_retries()
        self.test_get_backup_info_all_params()

    @responses.activate
    def test_get_backup_info_value_error(self):
        """
        test_get_backup_info_value_error()
        """
        # Set up mock
        url = preprocess_url('/backups/testString')
        mock_response = '{"backup": {"id": "5a970218cb7544000671c094", "deployment_id": "595eada310b7ac00116dd48b", "type": "scheduled", "status": "running", "is_downloadable": true, "is_restorable": true, "download_link": "https://securedownloadservice.com/backup-2018-02-28T19:25:12Z.tgz", "created_at": "2018-02-28T19:25:12.000Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        backup_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "backup_id": backup_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_backup_info(**req_copy)

    def test_get_backup_info_value_error_with_retries(self):
        # Enable retries and run test_get_backup_info_value_error.
        _service.enable_retries()
        self.test_get_backup_info_value_error()

        # Disable retries and run test_get_backup_info_value_error.
        _service.disable_retries()
        self.test_get_backup_info_value_error()

class TestListDeploymentBackups():
    """
    Test Class for list_deployment_backups
    """

    @responses.activate
    def test_list_deployment_backups_all_params(self):
        """
        list_deployment_backups()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/backups')
        mock_response = '{"backups": [{"id": "5a970218cb7544000671c094", "deployment_id": "595eada310b7ac00116dd48b", "type": "scheduled", "status": "running", "is_downloadable": true, "is_restorable": true, "download_link": "https://securedownloadservice.com/backup-2018-02-28T19:25:12Z.tgz", "created_at": "2018-02-28T19:25:12.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.list_deployment_backups(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_deployment_backups_all_params_with_retries(self):
        # Enable retries and run test_list_deployment_backups_all_params.
        _service.enable_retries()
        self.test_list_deployment_backups_all_params()

        # Disable retries and run test_list_deployment_backups_all_params.
        _service.disable_retries()
        self.test_list_deployment_backups_all_params()

    @responses.activate
    def test_list_deployment_backups_value_error(self):
        """
        test_list_deployment_backups_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/backups')
        mock_response = '{"backups": [{"id": "5a970218cb7544000671c094", "deployment_id": "595eada310b7ac00116dd48b", "type": "scheduled", "status": "running", "is_downloadable": true, "is_restorable": true, "download_link": "https://securedownloadservice.com/backup-2018-02-28T19:25:12Z.tgz", "created_at": "2018-02-28T19:25:12.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_deployment_backups(**req_copy)

    def test_list_deployment_backups_value_error_with_retries(self):
        # Enable retries and run test_list_deployment_backups_value_error.
        _service.enable_retries()
        self.test_list_deployment_backups_value_error()

        # Disable retries and run test_list_deployment_backups_value_error.
        _service.disable_retries()
        self.test_list_deployment_backups_value_error()

class TestStartOndemandBackup():
    """
    Test Class for start_ondemand_backup
    """

    @responses.activate
    def test_start_ondemand_backup_all_params(self):
        """
        start_ondemand_backup()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/backups')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.start_ondemand_backup(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_start_ondemand_backup_all_params_with_retries(self):
        # Enable retries and run test_start_ondemand_backup_all_params.
        _service.enable_retries()
        self.test_start_ondemand_backup_all_params()

        # Disable retries and run test_start_ondemand_backup_all_params.
        _service.disable_retries()
        self.test_start_ondemand_backup_all_params()

    @responses.activate
    def test_start_ondemand_backup_value_error(self):
        """
        test_start_ondemand_backup_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/backups')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.start_ondemand_backup(**req_copy)

    def test_start_ondemand_backup_value_error_with_retries(self):
        # Enable retries and run test_start_ondemand_backup_value_error.
        _service.enable_retries()
        self.test_start_ondemand_backup_value_error()

        # Disable retries and run test_start_ondemand_backup_value_error.
        _service.disable_retries()
        self.test_start_ondemand_backup_value_error()

class TestGetPitrData():
    """
    Test Class for get_pitr_data
    """

    @responses.activate
    def test_get_pitr_data_all_params(self):
        """
        get_pitr_data()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/point_in_time_recovery_data')
        mock_response = '{"point_in_time_recovery_data": {"earliest_point_in_time_recovery_time": "earliest_point_in_time_recovery_time"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_pitr_data(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_pitr_data_all_params_with_retries(self):
        # Enable retries and run test_get_pitr_data_all_params.
        _service.enable_retries()
        self.test_get_pitr_data_all_params()

        # Disable retries and run test_get_pitr_data_all_params.
        _service.disable_retries()
        self.test_get_pitr_data_all_params()

    @responses.activate
    def test_get_pitr_data_value_error(self):
        """
        test_get_pitr_data_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/point_in_time_recovery_data')
        mock_response = '{"point_in_time_recovery_data": {"earliest_point_in_time_recovery_time": "earliest_point_in_time_recovery_time"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_pitr_data(**req_copy)

    def test_get_pitr_data_value_error_with_retries(self):
        # Enable retries and run test_get_pitr_data_value_error.
        _service.enable_retries()
        self.test_get_pitr_data_value_error()

        # Disable retries and run test_get_pitr_data_value_error.
        _service.disable_retries()
        self.test_get_pitr_data_value_error()

# endregion
##############################################################################
# End of Service: Backups
##############################################################################

##############################################################################
# Start of Service: Connections
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CloudDatabasesV5.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CloudDatabasesV5)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CloudDatabasesV5.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestGetConnection():
    """
    Test Class for get_connection
    """

    @responses.activate
    def test_get_connection_all_params(self):
        """
        get_connection()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/users/database/testString/connections/public')
        mock_response = '{"connection": {"postgres": {"type": "uri", "composed": ["composed"], "scheme": "scheme", "hosts": [{"hostname": "hostname", "port": 4}], "path": "path", "query_options": {"anyKey": "anyValue"}, "authentication": {"method": "method", "username": "username", "password": "password"}, "certificate": {"name": "name", "certificate_base64": "certificate_base64"}, "ssl": false, "browser_accessible": true, "database": "database"}, "cli": {"type": "cli", "composed": ["composed"], "environment": {"anyKey": "anyValue"}, "bin": "bin", "arguments": [["arguments"]], "certificate": {"name": "name", "certificate_base64": "certificate_base64"}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        user_id = 'testString'
        endpoint_type = 'public'
        certificate_root = 'testString'

        # Invoke method
        response = _service.get_connection(
            id,
            user_type,
            user_id,
            endpoint_type,
            certificate_root=certificate_root,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'certificate_root={}'.format(certificate_root) in query_string

    def test_get_connection_all_params_with_retries(self):
        # Enable retries and run test_get_connection_all_params.
        _service.enable_retries()
        self.test_get_connection_all_params()

        # Disable retries and run test_get_connection_all_params.
        _service.disable_retries()
        self.test_get_connection_all_params()

    @responses.activate
    def test_get_connection_required_params(self):
        """
        test_get_connection_required_params()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/users/database/testString/connections/public')
        mock_response = '{"connection": {"postgres": {"type": "uri", "composed": ["composed"], "scheme": "scheme", "hosts": [{"hostname": "hostname", "port": 4}], "path": "path", "query_options": {"anyKey": "anyValue"}, "authentication": {"method": "method", "username": "username", "password": "password"}, "certificate": {"name": "name", "certificate_base64": "certificate_base64"}, "ssl": false, "browser_accessible": true, "database": "database"}, "cli": {"type": "cli", "composed": ["composed"], "environment": {"anyKey": "anyValue"}, "bin": "bin", "arguments": [["arguments"]], "certificate": {"name": "name", "certificate_base64": "certificate_base64"}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        user_id = 'testString'
        endpoint_type = 'public'

        # Invoke method
        response = _service.get_connection(
            id,
            user_type,
            user_id,
            endpoint_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_connection_required_params_with_retries(self):
        # Enable retries and run test_get_connection_required_params.
        _service.enable_retries()
        self.test_get_connection_required_params()

        # Disable retries and run test_get_connection_required_params.
        _service.disable_retries()
        self.test_get_connection_required_params()

    @responses.activate
    def test_get_connection_value_error(self):
        """
        test_get_connection_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/users/database/testString/connections/public')
        mock_response = '{"connection": {"postgres": {"type": "uri", "composed": ["composed"], "scheme": "scheme", "hosts": [{"hostname": "hostname", "port": 4}], "path": "path", "query_options": {"anyKey": "anyValue"}, "authentication": {"method": "method", "username": "username", "password": "password"}, "certificate": {"name": "name", "certificate_base64": "certificate_base64"}, "ssl": false, "browser_accessible": true, "database": "database"}, "cli": {"type": "cli", "composed": ["composed"], "environment": {"anyKey": "anyValue"}, "bin": "bin", "arguments": [["arguments"]], "certificate": {"name": "name", "certificate_base64": "certificate_base64"}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        user_id = 'testString'
        endpoint_type = 'public'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "user_type": user_type,
            "user_id": user_id,
            "endpoint_type": endpoint_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_connection(**req_copy)

    def test_get_connection_value_error_with_retries(self):
        # Enable retries and run test_get_connection_value_error.
        _service.enable_retries()
        self.test_get_connection_value_error()

        # Disable retries and run test_get_connection_value_error.
        _service.disable_retries()
        self.test_get_connection_value_error()

class TestCompleteConnection():
    """
    Test Class for complete_connection
    """

    @responses.activate
    def test_complete_connection_all_params(self):
        """
        complete_connection()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/users/database/testString/connections/public')
        mock_response = '{"connection": {"postgres": {"type": "uri", "composed": ["composed"], "scheme": "scheme", "hosts": [{"hostname": "hostname", "port": 4}], "path": "path", "query_options": {"anyKey": "anyValue"}, "authentication": {"method": "method", "username": "username", "password": "password"}, "certificate": {"name": "name", "certificate_base64": "certificate_base64"}, "ssl": false, "browser_accessible": true, "database": "database"}, "cli": {"type": "cli", "composed": ["composed"], "environment": {"anyKey": "anyValue"}, "bin": "bin", "arguments": [["arguments"]], "certificate": {"name": "name", "certificate_base64": "certificate_base64"}}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        user_id = 'testString'
        endpoint_type = 'public'
        password = 'providedpassword'
        certificate_root = 'testString'

        # Invoke method
        response = _service.complete_connection(
            id,
            user_type,
            user_id,
            endpoint_type,
            password=password,
            certificate_root=certificate_root,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['password'] == 'providedpassword'
        assert req_body['certificate_root'] == 'testString'

    def test_complete_connection_all_params_with_retries(self):
        # Enable retries and run test_complete_connection_all_params.
        _service.enable_retries()
        self.test_complete_connection_all_params()

        # Disable retries and run test_complete_connection_all_params.
        _service.disable_retries()
        self.test_complete_connection_all_params()

    @responses.activate
    def test_complete_connection_required_params(self):
        """
        test_complete_connection_required_params()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/users/database/testString/connections/public')
        mock_response = '{"connection": {"postgres": {"type": "uri", "composed": ["composed"], "scheme": "scheme", "hosts": [{"hostname": "hostname", "port": 4}], "path": "path", "query_options": {"anyKey": "anyValue"}, "authentication": {"method": "method", "username": "username", "password": "password"}, "certificate": {"name": "name", "certificate_base64": "certificate_base64"}, "ssl": false, "browser_accessible": true, "database": "database"}, "cli": {"type": "cli", "composed": ["composed"], "environment": {"anyKey": "anyValue"}, "bin": "bin", "arguments": [["arguments"]], "certificate": {"name": "name", "certificate_base64": "certificate_base64"}}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        user_id = 'testString'
        endpoint_type = 'public'

        # Invoke method
        response = _service.complete_connection(
            id,
            user_type,
            user_id,
            endpoint_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_complete_connection_required_params_with_retries(self):
        # Enable retries and run test_complete_connection_required_params.
        _service.enable_retries()
        self.test_complete_connection_required_params()

        # Disable retries and run test_complete_connection_required_params.
        _service.disable_retries()
        self.test_complete_connection_required_params()

    @responses.activate
    def test_complete_connection_value_error(self):
        """
        test_complete_connection_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/users/database/testString/connections/public')
        mock_response = '{"connection": {"postgres": {"type": "uri", "composed": ["composed"], "scheme": "scheme", "hosts": [{"hostname": "hostname", "port": 4}], "path": "path", "query_options": {"anyKey": "anyValue"}, "authentication": {"method": "method", "username": "username", "password": "password"}, "certificate": {"name": "name", "certificate_base64": "certificate_base64"}, "ssl": false, "browser_accessible": true, "database": "database"}, "cli": {"type": "cli", "composed": ["composed"], "environment": {"anyKey": "anyValue"}, "bin": "bin", "arguments": [["arguments"]], "certificate": {"name": "name", "certificate_base64": "certificate_base64"}}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        user_type = 'database'
        user_id = 'testString'
        endpoint_type = 'public'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "user_type": user_type,
            "user_id": user_id,
            "endpoint_type": endpoint_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.complete_connection(**req_copy)

    def test_complete_connection_value_error_with_retries(self):
        # Enable retries and run test_complete_connection_value_error.
        _service.enable_retries()
        self.test_complete_connection_value_error()

        # Disable retries and run test_complete_connection_value_error.
        _service.disable_retries()
        self.test_complete_connection_value_error()

# endregion
##############################################################################
# End of Service: Connections
##############################################################################

##############################################################################
# Start of Service: Scaling
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CloudDatabasesV5.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CloudDatabasesV5)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CloudDatabasesV5.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListDeploymentScalingGroups():
    """
    Test Class for list_deployment_scaling_groups
    """

    @responses.activate
    def test_list_deployment_scaling_groups_all_params(self):
        """
        list_deployment_scaling_groups()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/groups')
        mock_response = '{"groups": [{"id": "member", "count": 2, "members": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 20, "step_size_count": 1, "is_adjustable": true, "is_optional": false, "can_scale_down": false}, "memory": {"units": "mb", "allocation_mb": 12288, "minimum_mb": 1024, "maximum_mb": 114688, "step_size_mb": 1024, "is_adjustable": true, "is_optional": false, "can_scale_down": true}, "cpu": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 32, "step_size_count": 2, "is_adjustable": false, "is_optional": false, "can_scale_down": true}, "disk": {"units": "mb", "allocation_mb": 10240, "minimum_mb": 2048, "maximum_mb": 4194304, "step_size_mb": 2048, "is_adjustable": true, "is_optional": false, "can_scale_down": false}, "host_flavor": {"id": "b3c.4x16.encrypted", "name": "4x16", "hosting_size": "xs"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.list_deployment_scaling_groups(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_deployment_scaling_groups_all_params_with_retries(self):
        # Enable retries and run test_list_deployment_scaling_groups_all_params.
        _service.enable_retries()
        self.test_list_deployment_scaling_groups_all_params()

        # Disable retries and run test_list_deployment_scaling_groups_all_params.
        _service.disable_retries()
        self.test_list_deployment_scaling_groups_all_params()

    @responses.activate
    def test_list_deployment_scaling_groups_value_error(self):
        """
        test_list_deployment_scaling_groups_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/groups')
        mock_response = '{"groups": [{"id": "member", "count": 2, "members": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 20, "step_size_count": 1, "is_adjustable": true, "is_optional": false, "can_scale_down": false}, "memory": {"units": "mb", "allocation_mb": 12288, "minimum_mb": 1024, "maximum_mb": 114688, "step_size_mb": 1024, "is_adjustable": true, "is_optional": false, "can_scale_down": true}, "cpu": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 32, "step_size_count": 2, "is_adjustable": false, "is_optional": false, "can_scale_down": true}, "disk": {"units": "mb", "allocation_mb": 10240, "minimum_mb": 2048, "maximum_mb": 4194304, "step_size_mb": 2048, "is_adjustable": true, "is_optional": false, "can_scale_down": false}, "host_flavor": {"id": "b3c.4x16.encrypted", "name": "4x16", "hosting_size": "xs"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_deployment_scaling_groups(**req_copy)

    def test_list_deployment_scaling_groups_value_error_with_retries(self):
        # Enable retries and run test_list_deployment_scaling_groups_value_error.
        _service.enable_retries()
        self.test_list_deployment_scaling_groups_value_error()

        # Disable retries and run test_list_deployment_scaling_groups_value_error.
        _service.disable_retries()
        self.test_list_deployment_scaling_groups_value_error()

class TestGetDefaultScalingGroups():
    """
    Test Class for get_default_scaling_groups
    """

    @responses.activate
    def test_get_default_scaling_groups_all_params(self):
        """
        get_default_scaling_groups()
        """
        # Set up mock
        url = preprocess_url('/deployables/postgresql/groups')
        mock_response = '{"groups": [{"id": "member", "count": 2, "members": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 20, "step_size_count": 1, "is_adjustable": true, "is_optional": false, "can_scale_down": false}, "memory": {"units": "mb", "allocation_mb": 12288, "minimum_mb": 1024, "maximum_mb": 114688, "step_size_mb": 1024, "is_adjustable": true, "is_optional": false, "can_scale_down": true}, "cpu": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 32, "step_size_count": 2, "is_adjustable": false, "is_optional": false, "can_scale_down": true}, "disk": {"units": "mb", "allocation_mb": 10240, "minimum_mb": 2048, "maximum_mb": 4194304, "step_size_mb": 2048, "is_adjustable": true, "is_optional": false, "can_scale_down": false}, "host_flavor": {"id": "b3c.4x16.encrypted", "name": "4x16", "hosting_size": "xs"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        type = 'postgresql'

        # Invoke method
        response = _service.get_default_scaling_groups(
            type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_default_scaling_groups_all_params_with_retries(self):
        # Enable retries and run test_get_default_scaling_groups_all_params.
        _service.enable_retries()
        self.test_get_default_scaling_groups_all_params()

        # Disable retries and run test_get_default_scaling_groups_all_params.
        _service.disable_retries()
        self.test_get_default_scaling_groups_all_params()

    @responses.activate
    def test_get_default_scaling_groups_value_error(self):
        """
        test_get_default_scaling_groups_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployables/postgresql/groups')
        mock_response = '{"groups": [{"id": "member", "count": 2, "members": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 20, "step_size_count": 1, "is_adjustable": true, "is_optional": false, "can_scale_down": false}, "memory": {"units": "mb", "allocation_mb": 12288, "minimum_mb": 1024, "maximum_mb": 114688, "step_size_mb": 1024, "is_adjustable": true, "is_optional": false, "can_scale_down": true}, "cpu": {"units": "count", "allocation_count": 2, "minimum_count": 2, "maximum_count": 32, "step_size_count": 2, "is_adjustable": false, "is_optional": false, "can_scale_down": true}, "disk": {"units": "mb", "allocation_mb": 10240, "minimum_mb": 2048, "maximum_mb": 4194304, "step_size_mb": 2048, "is_adjustable": true, "is_optional": false, "can_scale_down": false}, "host_flavor": {"id": "b3c.4x16.encrypted", "name": "4x16", "hosting_size": "xs"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        type = 'postgresql'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_default_scaling_groups(**req_copy)

    def test_get_default_scaling_groups_value_error_with_retries(self):
        # Enable retries and run test_get_default_scaling_groups_value_error.
        _service.enable_retries()
        self.test_get_default_scaling_groups_value_error()

        # Disable retries and run test_get_default_scaling_groups_value_error.
        _service.disable_retries()
        self.test_get_default_scaling_groups_value_error()

class TestSetDeploymentScalingGroup():
    """
    Test Class for set_deployment_scaling_group
    """

    @responses.activate
    def test_set_deployment_scaling_group_all_params(self):
        """
        set_deployment_scaling_group()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/groups/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a GroupScalingMembers model
        group_scaling_members_model = {}
        group_scaling_members_model['allocation_count'] = 4

        # Construct a dict representation of a GroupScalingMemory model
        group_scaling_memory_model = {}
        group_scaling_memory_model['allocation_mb'] = 12288

        # Construct a dict representation of a GroupScalingCpu model
        group_scaling_cpu_model = {}
        group_scaling_cpu_model['allocation_count'] = 2

        # Construct a dict representation of a GroupScalingDisk model
        group_scaling_disk_model = {}
        group_scaling_disk_model['allocation_mb'] = 20480

        # Construct a dict representation of a GroupScalingHostFlavor model
        group_scaling_host_flavor_model = {}
        group_scaling_host_flavor_model['id'] = 'b3c.16x64.encrypted'

        # Construct a dict representation of a GroupScaling model
        group_scaling_model = {}
        group_scaling_model['members'] = group_scaling_members_model
        group_scaling_model['memory'] = group_scaling_memory_model
        group_scaling_model['cpu'] = group_scaling_cpu_model
        group_scaling_model['disk'] = group_scaling_disk_model
        group_scaling_model['host_flavor'] = group_scaling_host_flavor_model

        # Set up parameter values
        id = 'testString'
        group_id = 'testString'
        group = group_scaling_model

        # Invoke method
        response = _service.set_deployment_scaling_group(
            id,
            group_id,
            group=group,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['group'] == group_scaling_model

    def test_set_deployment_scaling_group_all_params_with_retries(self):
        # Enable retries and run test_set_deployment_scaling_group_all_params.
        _service.enable_retries()
        self.test_set_deployment_scaling_group_all_params()

        # Disable retries and run test_set_deployment_scaling_group_all_params.
        _service.disable_retries()
        self.test_set_deployment_scaling_group_all_params()

    @responses.activate
    def test_set_deployment_scaling_group_value_error(self):
        """
        test_set_deployment_scaling_group_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/groups/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a GroupScalingMembers model
        group_scaling_members_model = {}
        group_scaling_members_model['allocation_count'] = 4

        # Construct a dict representation of a GroupScalingMemory model
        group_scaling_memory_model = {}
        group_scaling_memory_model['allocation_mb'] = 12288

        # Construct a dict representation of a GroupScalingCpu model
        group_scaling_cpu_model = {}
        group_scaling_cpu_model['allocation_count'] = 2

        # Construct a dict representation of a GroupScalingDisk model
        group_scaling_disk_model = {}
        group_scaling_disk_model['allocation_mb'] = 20480

        # Construct a dict representation of a GroupScalingHostFlavor model
        group_scaling_host_flavor_model = {}
        group_scaling_host_flavor_model['id'] = 'b3c.16x64.encrypted'

        # Construct a dict representation of a GroupScaling model
        group_scaling_model = {}
        group_scaling_model['members'] = group_scaling_members_model
        group_scaling_model['memory'] = group_scaling_memory_model
        group_scaling_model['cpu'] = group_scaling_cpu_model
        group_scaling_model['disk'] = group_scaling_disk_model
        group_scaling_model['host_flavor'] = group_scaling_host_flavor_model

        # Set up parameter values
        id = 'testString'
        group_id = 'testString'
        group = group_scaling_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "group_id": group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.set_deployment_scaling_group(**req_copy)

    def test_set_deployment_scaling_group_value_error_with_retries(self):
        # Enable retries and run test_set_deployment_scaling_group_value_error.
        _service.enable_retries()
        self.test_set_deployment_scaling_group_value_error()

        # Disable retries and run test_set_deployment_scaling_group_value_error.
        _service.disable_retries()
        self.test_set_deployment_scaling_group_value_error()

# endregion
##############################################################################
# End of Service: Scaling
##############################################################################

##############################################################################
# Start of Service: Autoscaling
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CloudDatabasesV5.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CloudDatabasesV5)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CloudDatabasesV5.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestGetAutoscalingConditions():
    """
    Test Class for get_autoscaling_conditions
    """

    @responses.activate
    def test_get_autoscaling_conditions_all_params(self):
        """
        get_autoscaling_conditions()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/groups/testString/autoscaling')
        mock_response = '{"autoscaling": {"disk": {"scalers": {"capacity": {"enabled": true, "free_space_less_than_percent": 10}, "io_utilization": {"enabled": true, "over_period": "30m", "above_percent": 45}}, "rate": {"increase_percent": 20, "period_seconds": 900, "limit_mb_per_member": 3670016, "units": "mb"}}, "memory": {"scalers": {"io_utilization": {"enabled": true, "over_period": "30m", "above_percent": 45}}, "rate": {"increase_percent": 10, "period_seconds": 900, "limit_mb_per_member": 3670016, "units": "mb"}}, "cpu": {"scalers": {"anyKey": "anyValue"}, "rate": {"increase_percent": 10, "period_seconds": 900, "limit_count_per_member": 10, "units": "count"}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        group_id = 'testString'

        # Invoke method
        response = _service.get_autoscaling_conditions(
            id,
            group_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_autoscaling_conditions_all_params_with_retries(self):
        # Enable retries and run test_get_autoscaling_conditions_all_params.
        _service.enable_retries()
        self.test_get_autoscaling_conditions_all_params()

        # Disable retries and run test_get_autoscaling_conditions_all_params.
        _service.disable_retries()
        self.test_get_autoscaling_conditions_all_params()

    @responses.activate
    def test_get_autoscaling_conditions_value_error(self):
        """
        test_get_autoscaling_conditions_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/groups/testString/autoscaling')
        mock_response = '{"autoscaling": {"disk": {"scalers": {"capacity": {"enabled": true, "free_space_less_than_percent": 10}, "io_utilization": {"enabled": true, "over_period": "30m", "above_percent": 45}}, "rate": {"increase_percent": 20, "period_seconds": 900, "limit_mb_per_member": 3670016, "units": "mb"}}, "memory": {"scalers": {"io_utilization": {"enabled": true, "over_period": "30m", "above_percent": 45}}, "rate": {"increase_percent": 10, "period_seconds": 900, "limit_mb_per_member": 3670016, "units": "mb"}}, "cpu": {"scalers": {"anyKey": "anyValue"}, "rate": {"increase_percent": 10, "period_seconds": 900, "limit_count_per_member": 10, "units": "count"}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "group_id": group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_autoscaling_conditions(**req_copy)

    def test_get_autoscaling_conditions_value_error_with_retries(self):
        # Enable retries and run test_get_autoscaling_conditions_value_error.
        _service.enable_retries()
        self.test_get_autoscaling_conditions_value_error()

        # Disable retries and run test_get_autoscaling_conditions_value_error.
        _service.disable_retries()
        self.test_get_autoscaling_conditions_value_error()

class TestSetAutoscalingConditions():
    """
    Test Class for set_autoscaling_conditions
    """

    @responses.activate
    def test_set_autoscaling_conditions_all_params(self):
        """
        set_autoscaling_conditions()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/groups/testString/autoscaling')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a AutoscalingMemoryGroupMemoryScalersIoUtilization model
        autoscaling_memory_group_memory_scalers_io_utilization_model = {}
        autoscaling_memory_group_memory_scalers_io_utilization_model['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model['over_period'] = '5m'
        autoscaling_memory_group_memory_scalers_io_utilization_model['above_percent'] = 90

        # Construct a dict representation of a AutoscalingMemoryGroupMemoryScalers model
        autoscaling_memory_group_memory_scalers_model = {}
        autoscaling_memory_group_memory_scalers_model['io_utilization'] = autoscaling_memory_group_memory_scalers_io_utilization_model

        # Construct a dict representation of a AutoscalingMemoryGroupMemoryRate model
        autoscaling_memory_group_memory_rate_model = {}
        autoscaling_memory_group_memory_rate_model['increase_percent'] = 10
        autoscaling_memory_group_memory_rate_model['period_seconds'] = 300
        autoscaling_memory_group_memory_rate_model['limit_mb_per_member'] = 125952
        autoscaling_memory_group_memory_rate_model['units'] = 'mb'

        # Construct a dict representation of a AutoscalingMemoryGroupMemory model
        autoscaling_memory_group_memory_model = {}
        autoscaling_memory_group_memory_model['scalers'] = autoscaling_memory_group_memory_scalers_model
        autoscaling_memory_group_memory_model['rate'] = autoscaling_memory_group_memory_rate_model

        # Construct a dict representation of a AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup model
        autoscaling_set_group_autoscaling_model = {}
        autoscaling_set_group_autoscaling_model['memory'] = autoscaling_memory_group_memory_model

        # Set up parameter values
        id = 'testString'
        group_id = 'testString'
        autoscaling = autoscaling_set_group_autoscaling_model

        # Invoke method
        response = _service.set_autoscaling_conditions(
            id,
            group_id,
            autoscaling,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['autoscaling'] == autoscaling_set_group_autoscaling_model

    def test_set_autoscaling_conditions_all_params_with_retries(self):
        # Enable retries and run test_set_autoscaling_conditions_all_params.
        _service.enable_retries()
        self.test_set_autoscaling_conditions_all_params()

        # Disable retries and run test_set_autoscaling_conditions_all_params.
        _service.disable_retries()
        self.test_set_autoscaling_conditions_all_params()

    @responses.activate
    def test_set_autoscaling_conditions_value_error(self):
        """
        test_set_autoscaling_conditions_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/groups/testString/autoscaling')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a AutoscalingMemoryGroupMemoryScalersIoUtilization model
        autoscaling_memory_group_memory_scalers_io_utilization_model = {}
        autoscaling_memory_group_memory_scalers_io_utilization_model['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model['over_period'] = '5m'
        autoscaling_memory_group_memory_scalers_io_utilization_model['above_percent'] = 90

        # Construct a dict representation of a AutoscalingMemoryGroupMemoryScalers model
        autoscaling_memory_group_memory_scalers_model = {}
        autoscaling_memory_group_memory_scalers_model['io_utilization'] = autoscaling_memory_group_memory_scalers_io_utilization_model

        # Construct a dict representation of a AutoscalingMemoryGroupMemoryRate model
        autoscaling_memory_group_memory_rate_model = {}
        autoscaling_memory_group_memory_rate_model['increase_percent'] = 10
        autoscaling_memory_group_memory_rate_model['period_seconds'] = 300
        autoscaling_memory_group_memory_rate_model['limit_mb_per_member'] = 125952
        autoscaling_memory_group_memory_rate_model['units'] = 'mb'

        # Construct a dict representation of a AutoscalingMemoryGroupMemory model
        autoscaling_memory_group_memory_model = {}
        autoscaling_memory_group_memory_model['scalers'] = autoscaling_memory_group_memory_scalers_model
        autoscaling_memory_group_memory_model['rate'] = autoscaling_memory_group_memory_rate_model

        # Construct a dict representation of a AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup model
        autoscaling_set_group_autoscaling_model = {}
        autoscaling_set_group_autoscaling_model['memory'] = autoscaling_memory_group_memory_model

        # Set up parameter values
        id = 'testString'
        group_id = 'testString'
        autoscaling = autoscaling_set_group_autoscaling_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "group_id": group_id,
            "autoscaling": autoscaling,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.set_autoscaling_conditions(**req_copy)

    def test_set_autoscaling_conditions_value_error_with_retries(self):
        # Enable retries and run test_set_autoscaling_conditions_value_error.
        _service.enable_retries()
        self.test_set_autoscaling_conditions_value_error()

        # Disable retries and run test_set_autoscaling_conditions_value_error.
        _service.disable_retries()
        self.test_set_autoscaling_conditions_value_error()

# endregion
##############################################################################
# End of Service: Autoscaling
##############################################################################

##############################################################################
# Start of Service: Management
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CloudDatabasesV5.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CloudDatabasesV5)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CloudDatabasesV5.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestKillConnections():
    """
    Test Class for kill_connections
    """

    @responses.activate
    def test_kill_connections_all_params(self):
        """
        kill_connections()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/management/database_connections')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.kill_connections(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_kill_connections_all_params_with_retries(self):
        # Enable retries and run test_kill_connections_all_params.
        _service.enable_retries()
        self.test_kill_connections_all_params()

        # Disable retries and run test_kill_connections_all_params.
        _service.disable_retries()
        self.test_kill_connections_all_params()

    @responses.activate
    def test_kill_connections_value_error(self):
        """
        test_kill_connections_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/management/database_connections')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.kill_connections(**req_copy)

    def test_kill_connections_value_error_with_retries(self):
        # Enable retries and run test_kill_connections_value_error.
        _service.enable_retries()
        self.test_kill_connections_value_error()

        # Disable retries and run test_kill_connections_value_error.
        _service.disable_retries()
        self.test_kill_connections_value_error()

class TestCreateLogicalReplicationSlot():
    """
    Test Class for create_logical_replication_slot
    """

    @responses.activate
    def test_create_logical_replication_slot_all_params(self):
        """
        create_logical_replication_slot()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/postgresql/logical_replication_slots')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a LogicalReplicationSlot model
        logical_replication_slot_model = {}
        logical_replication_slot_model['name'] = 'customer_replication'
        logical_replication_slot_model['database_name'] = 'customers'
        logical_replication_slot_model['plugin_type'] = 'wal2json'

        # Set up parameter values
        id = 'testString'
        logical_replication_slot = logical_replication_slot_model

        # Invoke method
        response = _service.create_logical_replication_slot(
            id,
            logical_replication_slot=logical_replication_slot,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['logical_replication_slot'] == logical_replication_slot_model

    def test_create_logical_replication_slot_all_params_with_retries(self):
        # Enable retries and run test_create_logical_replication_slot_all_params.
        _service.enable_retries()
        self.test_create_logical_replication_slot_all_params()

        # Disable retries and run test_create_logical_replication_slot_all_params.
        _service.disable_retries()
        self.test_create_logical_replication_slot_all_params()

    @responses.activate
    def test_create_logical_replication_slot_value_error(self):
        """
        test_create_logical_replication_slot_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/postgresql/logical_replication_slots')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a LogicalReplicationSlot model
        logical_replication_slot_model = {}
        logical_replication_slot_model['name'] = 'customer_replication'
        logical_replication_slot_model['database_name'] = 'customers'
        logical_replication_slot_model['plugin_type'] = 'wal2json'

        # Set up parameter values
        id = 'testString'
        logical_replication_slot = logical_replication_slot_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_logical_replication_slot(**req_copy)

    def test_create_logical_replication_slot_value_error_with_retries(self):
        # Enable retries and run test_create_logical_replication_slot_value_error.
        _service.enable_retries()
        self.test_create_logical_replication_slot_value_error()

        # Disable retries and run test_create_logical_replication_slot_value_error.
        _service.disable_retries()
        self.test_create_logical_replication_slot_value_error()

class TestDeleteLogicalReplicationSlot():
    """
    Test Class for delete_logical_replication_slot
    """

    @responses.activate
    def test_delete_logical_replication_slot_all_params(self):
        """
        delete_logical_replication_slot()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/postgresql/logical_replication_slots/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'
        name = 'testString'

        # Invoke method
        response = _service.delete_logical_replication_slot(
            id,
            name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_logical_replication_slot_all_params_with_retries(self):
        # Enable retries and run test_delete_logical_replication_slot_all_params.
        _service.enable_retries()
        self.test_delete_logical_replication_slot_all_params()

        # Disable retries and run test_delete_logical_replication_slot_all_params.
        _service.disable_retries()
        self.test_delete_logical_replication_slot_all_params()

    @responses.activate
    def test_delete_logical_replication_slot_value_error(self):
        """
        test_delete_logical_replication_slot_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/postgresql/logical_replication_slots/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'
        name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_logical_replication_slot(**req_copy)

    def test_delete_logical_replication_slot_value_error_with_retries(self):
        # Enable retries and run test_delete_logical_replication_slot_value_error.
        _service.enable_retries()
        self.test_delete_logical_replication_slot_value_error()

        # Disable retries and run test_delete_logical_replication_slot_value_error.
        _service.disable_retries()
        self.test_delete_logical_replication_slot_value_error()

# endregion
##############################################################################
# End of Service: Management
##############################################################################

##############################################################################
# Start of Service: Security
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = CloudDatabasesV5.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CloudDatabasesV5)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CloudDatabasesV5.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestGetAllowlist():
    """
    Test Class for get_allowlist
    """

    @responses.activate
    def test_get_allowlist_all_params(self):
        """
        get_allowlist()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/allowlists/ip_addresses')
        mock_response = '{"ip_addresses": [{"address": "address", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_allowlist(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_allowlist_all_params_with_retries(self):
        # Enable retries and run test_get_allowlist_all_params.
        _service.enable_retries()
        self.test_get_allowlist_all_params()

        # Disable retries and run test_get_allowlist_all_params.
        _service.disable_retries()
        self.test_get_allowlist_all_params()

    @responses.activate
    def test_get_allowlist_value_error(self):
        """
        test_get_allowlist_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/allowlists/ip_addresses')
        mock_response = '{"ip_addresses": [{"address": "address", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_allowlist(**req_copy)

    def test_get_allowlist_value_error_with_retries(self):
        # Enable retries and run test_get_allowlist_value_error.
        _service.enable_retries()
        self.test_get_allowlist_value_error()

        # Disable retries and run test_get_allowlist_value_error.
        _service.disable_retries()
        self.test_get_allowlist_value_error()

class TestSetAllowlist():
    """
    Test Class for set_allowlist
    """

    @responses.activate
    def test_set_allowlist_all_params(self):
        """
        set_allowlist()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/allowlists/ip_addresses')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a AllowlistEntry model
        allowlist_entry_model = {}
        allowlist_entry_model['address'] = '195.212.0.0/16'
        allowlist_entry_model['description'] = 'Dev IP space 1'

        # Set up parameter values
        id = 'testString'
        ip_addresses = [allowlist_entry_model]
        if_match = 'testString'

        # Invoke method
        response = _service.set_allowlist(
            id,
            ip_addresses=ip_addresses,
            if_match=if_match,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['ip_addresses'] == [allowlist_entry_model]

    def test_set_allowlist_all_params_with_retries(self):
        # Enable retries and run test_set_allowlist_all_params.
        _service.enable_retries()
        self.test_set_allowlist_all_params()

        # Disable retries and run test_set_allowlist_all_params.
        _service.disable_retries()
        self.test_set_allowlist_all_params()

    @responses.activate
    def test_set_allowlist_required_params(self):
        """
        test_set_allowlist_required_params()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/allowlists/ip_addresses')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a AllowlistEntry model
        allowlist_entry_model = {}
        allowlist_entry_model['address'] = '195.212.0.0/16'
        allowlist_entry_model['description'] = 'Dev IP space 1'

        # Set up parameter values
        id = 'testString'
        ip_addresses = [allowlist_entry_model]

        # Invoke method
        response = _service.set_allowlist(
            id,
            ip_addresses=ip_addresses,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['ip_addresses'] == [allowlist_entry_model]

    def test_set_allowlist_required_params_with_retries(self):
        # Enable retries and run test_set_allowlist_required_params.
        _service.enable_retries()
        self.test_set_allowlist_required_params()

        # Disable retries and run test_set_allowlist_required_params.
        _service.disable_retries()
        self.test_set_allowlist_required_params()

    @responses.activate
    def test_set_allowlist_value_error(self):
        """
        test_set_allowlist_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/allowlists/ip_addresses')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a AllowlistEntry model
        allowlist_entry_model = {}
        allowlist_entry_model['address'] = '195.212.0.0/16'
        allowlist_entry_model['description'] = 'Dev IP space 1'

        # Set up parameter values
        id = 'testString'
        ip_addresses = [allowlist_entry_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.set_allowlist(**req_copy)

    def test_set_allowlist_value_error_with_retries(self):
        # Enable retries and run test_set_allowlist_value_error.
        _service.enable_retries()
        self.test_set_allowlist_value_error()

        # Disable retries and run test_set_allowlist_value_error.
        _service.disable_retries()
        self.test_set_allowlist_value_error()

class TestAddAllowlistEntry():
    """
    Test Class for add_allowlist_entry
    """

    @responses.activate
    def test_add_allowlist_entry_all_params(self):
        """
        add_allowlist_entry()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/allowlists/ip_addresses')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a AllowlistEntry model
        allowlist_entry_model = {}
        allowlist_entry_model['address'] = '172.16.0.0/16'
        allowlist_entry_model['description'] = 'Dev IP space 3'

        # Set up parameter values
        id = 'testString'
        ip_address = allowlist_entry_model

        # Invoke method
        response = _service.add_allowlist_entry(
            id,
            ip_address=ip_address,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['ip_address'] == allowlist_entry_model

    def test_add_allowlist_entry_all_params_with_retries(self):
        # Enable retries and run test_add_allowlist_entry_all_params.
        _service.enable_retries()
        self.test_add_allowlist_entry_all_params()

        # Disable retries and run test_add_allowlist_entry_all_params.
        _service.disable_retries()
        self.test_add_allowlist_entry_all_params()

    @responses.activate
    def test_add_allowlist_entry_value_error(self):
        """
        test_add_allowlist_entry_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/allowlists/ip_addresses')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a AllowlistEntry model
        allowlist_entry_model = {}
        allowlist_entry_model['address'] = '172.16.0.0/16'
        allowlist_entry_model['description'] = 'Dev IP space 3'

        # Set up parameter values
        id = 'testString'
        ip_address = allowlist_entry_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_allowlist_entry(**req_copy)

    def test_add_allowlist_entry_value_error_with_retries(self):
        # Enable retries and run test_add_allowlist_entry_value_error.
        _service.enable_retries()
        self.test_add_allowlist_entry_value_error()

        # Disable retries and run test_add_allowlist_entry_value_error.
        _service.disable_retries()
        self.test_add_allowlist_entry_value_error()

class TestDeleteAllowlistEntry():
    """
    Test Class for delete_allowlist_entry
    """

    @responses.activate
    def test_delete_allowlist_entry_all_params(self):
        """
        delete_allowlist_entry()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/allowlists/ip_addresses/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'
        ipaddress = 'testString'

        # Invoke method
        response = _service.delete_allowlist_entry(
            id,
            ipaddress,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_allowlist_entry_all_params_with_retries(self):
        # Enable retries and run test_delete_allowlist_entry_all_params.
        _service.enable_retries()
        self.test_delete_allowlist_entry_all_params()

        # Disable retries and run test_delete_allowlist_entry_all_params.
        _service.disable_retries()
        self.test_delete_allowlist_entry_all_params()

    @responses.activate
    def test_delete_allowlist_entry_value_error(self):
        """
        test_delete_allowlist_entry_value_error()
        """
        # Set up mock
        url = preprocess_url('/deployments/testString/allowlists/ip_addresses/testString')
        mock_response = '{"task": {"id": "id", "description": "description", "status": "running", "deployment_id": "deployment_id", "progress_percent": 16, "created_at": "2019-01-01T12:00:00.000Z"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'
        ipaddress = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "ipaddress": ipaddress,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_allowlist_entry(**req_copy)

    def test_delete_allowlist_entry_value_error_with_retries(self):
        # Enable retries and run test_delete_allowlist_entry_value_error.
        _service.enable_retries()
        self.test_delete_allowlist_entry_value_error()

        # Disable retries and run test_delete_allowlist_entry_value_error.
        _service.disable_retries()
        self.test_delete_allowlist_entry_value_error()

# endregion
##############################################################################
# End of Service: Security
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_AddAllowlistEntryResponse():
    """
    Test Class for AddAllowlistEntryResponse
    """

    def test_add_allowlist_entry_response_serialization(self):
        """
        Test serialization/deserialization for AddAllowlistEntryResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f3-d9c96544393b'
        task_model['description'] = 'Adding allowlist entry for database'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 10
        task_model['created_at'] = '2018-03-28T10:21:30Z'

        # Construct a json representation of a AddAllowlistEntryResponse model
        add_allowlist_entry_response_model_json = {}
        add_allowlist_entry_response_model_json['task'] = task_model

        # Construct a model instance of AddAllowlistEntryResponse by calling from_dict on the json representation
        add_allowlist_entry_response_model = AddAllowlistEntryResponse.from_dict(add_allowlist_entry_response_model_json)
        assert add_allowlist_entry_response_model != False

        # Construct a model instance of AddAllowlistEntryResponse by calling from_dict on the json representation
        add_allowlist_entry_response_model_dict = AddAllowlistEntryResponse.from_dict(add_allowlist_entry_response_model_json).__dict__
        add_allowlist_entry_response_model2 = AddAllowlistEntryResponse(**add_allowlist_entry_response_model_dict)

        # Verify the model instances are equivalent
        assert add_allowlist_entry_response_model == add_allowlist_entry_response_model2

        # Convert model instance back to dict and verify no loss of data
        add_allowlist_entry_response_model_json2 = add_allowlist_entry_response_model.to_dict()
        assert add_allowlist_entry_response_model_json2 == add_allowlist_entry_response_model_json

class TestModel_AllowlistEntry():
    """
    Test Class for AllowlistEntry
    """

    def test_allowlist_entry_serialization(self):
        """
        Test serialization/deserialization for AllowlistEntry
        """

        # Construct a json representation of a AllowlistEntry model
        allowlist_entry_model_json = {}
        allowlist_entry_model_json['address'] = 'testString'
        allowlist_entry_model_json['description'] = 'testString'

        # Construct a model instance of AllowlistEntry by calling from_dict on the json representation
        allowlist_entry_model = AllowlistEntry.from_dict(allowlist_entry_model_json)
        assert allowlist_entry_model != False

        # Construct a model instance of AllowlistEntry by calling from_dict on the json representation
        allowlist_entry_model_dict = AllowlistEntry.from_dict(allowlist_entry_model_json).__dict__
        allowlist_entry_model2 = AllowlistEntry(**allowlist_entry_model_dict)

        # Verify the model instances are equivalent
        assert allowlist_entry_model == allowlist_entry_model2

        # Convert model instance back to dict and verify no loss of data
        allowlist_entry_model_json2 = allowlist_entry_model.to_dict()
        assert allowlist_entry_model_json2 == allowlist_entry_model_json

class TestModel_AutoscalingCPUGroupCPU():
    """
    Test Class for AutoscalingCPUGroupCPU
    """

    def test_autoscaling_cpu_group_cpu_serialization(self):
        """
        Test serialization/deserialization for AutoscalingCPUGroupCPU
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_cpu_group_cpu_rate_model = {} # AutoscalingCPUGroupCPURate
        autoscaling_cpu_group_cpu_rate_model['increase_percent'] = 10
        autoscaling_cpu_group_cpu_rate_model['period_seconds'] = 900
        autoscaling_cpu_group_cpu_rate_model['limit_count_per_member'] = 10
        autoscaling_cpu_group_cpu_rate_model['units'] = 'count'

        # Construct a json representation of a AutoscalingCPUGroupCPU model
        autoscaling_cpu_group_cpu_model_json = {}
        autoscaling_cpu_group_cpu_model_json['scalers'] = {'foo': 'bar'}
        autoscaling_cpu_group_cpu_model_json['rate'] = autoscaling_cpu_group_cpu_rate_model

        # Construct a model instance of AutoscalingCPUGroupCPU by calling from_dict on the json representation
        autoscaling_cpu_group_cpu_model = AutoscalingCPUGroupCPU.from_dict(autoscaling_cpu_group_cpu_model_json)
        assert autoscaling_cpu_group_cpu_model != False

        # Construct a model instance of AutoscalingCPUGroupCPU by calling from_dict on the json representation
        autoscaling_cpu_group_cpu_model_dict = AutoscalingCPUGroupCPU.from_dict(autoscaling_cpu_group_cpu_model_json).__dict__
        autoscaling_cpu_group_cpu_model2 = AutoscalingCPUGroupCPU(**autoscaling_cpu_group_cpu_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_cpu_group_cpu_model == autoscaling_cpu_group_cpu_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_cpu_group_cpu_model_json2 = autoscaling_cpu_group_cpu_model.to_dict()
        assert autoscaling_cpu_group_cpu_model_json2 == autoscaling_cpu_group_cpu_model_json

class TestModel_AutoscalingCPUGroupCPURate():
    """
    Test Class for AutoscalingCPUGroupCPURate
    """

    def test_autoscaling_cpu_group_cpu_rate_serialization(self):
        """
        Test serialization/deserialization for AutoscalingCPUGroupCPURate
        """

        # Construct a json representation of a AutoscalingCPUGroupCPURate model
        autoscaling_cpu_group_cpu_rate_model_json = {}
        autoscaling_cpu_group_cpu_rate_model_json['increase_percent'] = 10
        autoscaling_cpu_group_cpu_rate_model_json['period_seconds'] = 900
        autoscaling_cpu_group_cpu_rate_model_json['limit_count_per_member'] = 10
        autoscaling_cpu_group_cpu_rate_model_json['units'] = 'count'

        # Construct a model instance of AutoscalingCPUGroupCPURate by calling from_dict on the json representation
        autoscaling_cpu_group_cpu_rate_model = AutoscalingCPUGroupCPURate.from_dict(autoscaling_cpu_group_cpu_rate_model_json)
        assert autoscaling_cpu_group_cpu_rate_model != False

        # Construct a model instance of AutoscalingCPUGroupCPURate by calling from_dict on the json representation
        autoscaling_cpu_group_cpu_rate_model_dict = AutoscalingCPUGroupCPURate.from_dict(autoscaling_cpu_group_cpu_rate_model_json).__dict__
        autoscaling_cpu_group_cpu_rate_model2 = AutoscalingCPUGroupCPURate(**autoscaling_cpu_group_cpu_rate_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_cpu_group_cpu_rate_model == autoscaling_cpu_group_cpu_rate_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_cpu_group_cpu_rate_model_json2 = autoscaling_cpu_group_cpu_rate_model.to_dict()
        assert autoscaling_cpu_group_cpu_rate_model_json2 == autoscaling_cpu_group_cpu_rate_model_json

class TestModel_AutoscalingDiskGroupDisk():
    """
    Test Class for AutoscalingDiskGroupDisk
    """

    def test_autoscaling_disk_group_disk_serialization(self):
        """
        Test serialization/deserialization for AutoscalingDiskGroupDisk
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_disk_group_disk_scalers_capacity_model = {} # AutoscalingDiskGroupDiskScalersCapacity
        autoscaling_disk_group_disk_scalers_capacity_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_capacity_model['free_space_less_than_percent'] = 10

        autoscaling_disk_group_disk_scalers_io_utilization_model = {} # AutoscalingDiskGroupDiskScalersIoUtilization
        autoscaling_disk_group_disk_scalers_io_utilization_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_disk_group_disk_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_disk_group_disk_scalers_model = {} # AutoscalingDiskGroupDiskScalers
        autoscaling_disk_group_disk_scalers_model['capacity'] = autoscaling_disk_group_disk_scalers_capacity_model
        autoscaling_disk_group_disk_scalers_model['io_utilization'] = autoscaling_disk_group_disk_scalers_io_utilization_model

        autoscaling_disk_group_disk_rate_model = {} # AutoscalingDiskGroupDiskRate
        autoscaling_disk_group_disk_rate_model['increase_percent'] = 20
        autoscaling_disk_group_disk_rate_model['period_seconds'] = 900
        autoscaling_disk_group_disk_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_disk_group_disk_rate_model['units'] = 'mb'

        # Construct a json representation of a AutoscalingDiskGroupDisk model
        autoscaling_disk_group_disk_model_json = {}
        autoscaling_disk_group_disk_model_json['scalers'] = autoscaling_disk_group_disk_scalers_model
        autoscaling_disk_group_disk_model_json['rate'] = autoscaling_disk_group_disk_rate_model

        # Construct a model instance of AutoscalingDiskGroupDisk by calling from_dict on the json representation
        autoscaling_disk_group_disk_model = AutoscalingDiskGroupDisk.from_dict(autoscaling_disk_group_disk_model_json)
        assert autoscaling_disk_group_disk_model != False

        # Construct a model instance of AutoscalingDiskGroupDisk by calling from_dict on the json representation
        autoscaling_disk_group_disk_model_dict = AutoscalingDiskGroupDisk.from_dict(autoscaling_disk_group_disk_model_json).__dict__
        autoscaling_disk_group_disk_model2 = AutoscalingDiskGroupDisk(**autoscaling_disk_group_disk_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_disk_group_disk_model == autoscaling_disk_group_disk_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_disk_group_disk_model_json2 = autoscaling_disk_group_disk_model.to_dict()
        assert autoscaling_disk_group_disk_model_json2 == autoscaling_disk_group_disk_model_json

class TestModel_AutoscalingDiskGroupDiskRate():
    """
    Test Class for AutoscalingDiskGroupDiskRate
    """

    def test_autoscaling_disk_group_disk_rate_serialization(self):
        """
        Test serialization/deserialization for AutoscalingDiskGroupDiskRate
        """

        # Construct a json representation of a AutoscalingDiskGroupDiskRate model
        autoscaling_disk_group_disk_rate_model_json = {}
        autoscaling_disk_group_disk_rate_model_json['increase_percent'] = 20
        autoscaling_disk_group_disk_rate_model_json['period_seconds'] = 900
        autoscaling_disk_group_disk_rate_model_json['limit_mb_per_member'] = 3670016
        autoscaling_disk_group_disk_rate_model_json['units'] = 'mb'

        # Construct a model instance of AutoscalingDiskGroupDiskRate by calling from_dict on the json representation
        autoscaling_disk_group_disk_rate_model = AutoscalingDiskGroupDiskRate.from_dict(autoscaling_disk_group_disk_rate_model_json)
        assert autoscaling_disk_group_disk_rate_model != False

        # Construct a model instance of AutoscalingDiskGroupDiskRate by calling from_dict on the json representation
        autoscaling_disk_group_disk_rate_model_dict = AutoscalingDiskGroupDiskRate.from_dict(autoscaling_disk_group_disk_rate_model_json).__dict__
        autoscaling_disk_group_disk_rate_model2 = AutoscalingDiskGroupDiskRate(**autoscaling_disk_group_disk_rate_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_disk_group_disk_rate_model == autoscaling_disk_group_disk_rate_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_disk_group_disk_rate_model_json2 = autoscaling_disk_group_disk_rate_model.to_dict()
        assert autoscaling_disk_group_disk_rate_model_json2 == autoscaling_disk_group_disk_rate_model_json

class TestModel_AutoscalingDiskGroupDiskScalers():
    """
    Test Class for AutoscalingDiskGroupDiskScalers
    """

    def test_autoscaling_disk_group_disk_scalers_serialization(self):
        """
        Test serialization/deserialization for AutoscalingDiskGroupDiskScalers
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_disk_group_disk_scalers_capacity_model = {} # AutoscalingDiskGroupDiskScalersCapacity
        autoscaling_disk_group_disk_scalers_capacity_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_capacity_model['free_space_less_than_percent'] = 10

        autoscaling_disk_group_disk_scalers_io_utilization_model = {} # AutoscalingDiskGroupDiskScalersIoUtilization
        autoscaling_disk_group_disk_scalers_io_utilization_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_disk_group_disk_scalers_io_utilization_model['above_percent'] = 45

        # Construct a json representation of a AutoscalingDiskGroupDiskScalers model
        autoscaling_disk_group_disk_scalers_model_json = {}
        autoscaling_disk_group_disk_scalers_model_json['capacity'] = autoscaling_disk_group_disk_scalers_capacity_model
        autoscaling_disk_group_disk_scalers_model_json['io_utilization'] = autoscaling_disk_group_disk_scalers_io_utilization_model

        # Construct a model instance of AutoscalingDiskGroupDiskScalers by calling from_dict on the json representation
        autoscaling_disk_group_disk_scalers_model = AutoscalingDiskGroupDiskScalers.from_dict(autoscaling_disk_group_disk_scalers_model_json)
        assert autoscaling_disk_group_disk_scalers_model != False

        # Construct a model instance of AutoscalingDiskGroupDiskScalers by calling from_dict on the json representation
        autoscaling_disk_group_disk_scalers_model_dict = AutoscalingDiskGroupDiskScalers.from_dict(autoscaling_disk_group_disk_scalers_model_json).__dict__
        autoscaling_disk_group_disk_scalers_model2 = AutoscalingDiskGroupDiskScalers(**autoscaling_disk_group_disk_scalers_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_disk_group_disk_scalers_model == autoscaling_disk_group_disk_scalers_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_disk_group_disk_scalers_model_json2 = autoscaling_disk_group_disk_scalers_model.to_dict()
        assert autoscaling_disk_group_disk_scalers_model_json2 == autoscaling_disk_group_disk_scalers_model_json

class TestModel_AutoscalingDiskGroupDiskScalersCapacity():
    """
    Test Class for AutoscalingDiskGroupDiskScalersCapacity
    """

    def test_autoscaling_disk_group_disk_scalers_capacity_serialization(self):
        """
        Test serialization/deserialization for AutoscalingDiskGroupDiskScalersCapacity
        """

        # Construct a json representation of a AutoscalingDiskGroupDiskScalersCapacity model
        autoscaling_disk_group_disk_scalers_capacity_model_json = {}
        autoscaling_disk_group_disk_scalers_capacity_model_json['enabled'] = True
        autoscaling_disk_group_disk_scalers_capacity_model_json['free_space_less_than_percent'] = 10

        # Construct a model instance of AutoscalingDiskGroupDiskScalersCapacity by calling from_dict on the json representation
        autoscaling_disk_group_disk_scalers_capacity_model = AutoscalingDiskGroupDiskScalersCapacity.from_dict(autoscaling_disk_group_disk_scalers_capacity_model_json)
        assert autoscaling_disk_group_disk_scalers_capacity_model != False

        # Construct a model instance of AutoscalingDiskGroupDiskScalersCapacity by calling from_dict on the json representation
        autoscaling_disk_group_disk_scalers_capacity_model_dict = AutoscalingDiskGroupDiskScalersCapacity.from_dict(autoscaling_disk_group_disk_scalers_capacity_model_json).__dict__
        autoscaling_disk_group_disk_scalers_capacity_model2 = AutoscalingDiskGroupDiskScalersCapacity(**autoscaling_disk_group_disk_scalers_capacity_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_disk_group_disk_scalers_capacity_model == autoscaling_disk_group_disk_scalers_capacity_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_disk_group_disk_scalers_capacity_model_json2 = autoscaling_disk_group_disk_scalers_capacity_model.to_dict()
        assert autoscaling_disk_group_disk_scalers_capacity_model_json2 == autoscaling_disk_group_disk_scalers_capacity_model_json

class TestModel_AutoscalingDiskGroupDiskScalersIoUtilization():
    """
    Test Class for AutoscalingDiskGroupDiskScalersIoUtilization
    """

    def test_autoscaling_disk_group_disk_scalers_io_utilization_serialization(self):
        """
        Test serialization/deserialization for AutoscalingDiskGroupDiskScalersIoUtilization
        """

        # Construct a json representation of a AutoscalingDiskGroupDiskScalersIoUtilization model
        autoscaling_disk_group_disk_scalers_io_utilization_model_json = {}
        autoscaling_disk_group_disk_scalers_io_utilization_model_json['enabled'] = True
        autoscaling_disk_group_disk_scalers_io_utilization_model_json['over_period'] = '30m'
        autoscaling_disk_group_disk_scalers_io_utilization_model_json['above_percent'] = 45

        # Construct a model instance of AutoscalingDiskGroupDiskScalersIoUtilization by calling from_dict on the json representation
        autoscaling_disk_group_disk_scalers_io_utilization_model = AutoscalingDiskGroupDiskScalersIoUtilization.from_dict(autoscaling_disk_group_disk_scalers_io_utilization_model_json)
        assert autoscaling_disk_group_disk_scalers_io_utilization_model != False

        # Construct a model instance of AutoscalingDiskGroupDiskScalersIoUtilization by calling from_dict on the json representation
        autoscaling_disk_group_disk_scalers_io_utilization_model_dict = AutoscalingDiskGroupDiskScalersIoUtilization.from_dict(autoscaling_disk_group_disk_scalers_io_utilization_model_json).__dict__
        autoscaling_disk_group_disk_scalers_io_utilization_model2 = AutoscalingDiskGroupDiskScalersIoUtilization(**autoscaling_disk_group_disk_scalers_io_utilization_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_disk_group_disk_scalers_io_utilization_model == autoscaling_disk_group_disk_scalers_io_utilization_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_disk_group_disk_scalers_io_utilization_model_json2 = autoscaling_disk_group_disk_scalers_io_utilization_model.to_dict()
        assert autoscaling_disk_group_disk_scalers_io_utilization_model_json2 == autoscaling_disk_group_disk_scalers_io_utilization_model_json

class TestModel_AutoscalingGroup():
    """
    Test Class for AutoscalingGroup
    """

    def test_autoscaling_group_serialization(self):
        """
        Test serialization/deserialization for AutoscalingGroup
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_disk_group_disk_scalers_capacity_model = {} # AutoscalingDiskGroupDiskScalersCapacity
        autoscaling_disk_group_disk_scalers_capacity_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_capacity_model['free_space_less_than_percent'] = 10

        autoscaling_disk_group_disk_scalers_io_utilization_model = {} # AutoscalingDiskGroupDiskScalersIoUtilization
        autoscaling_disk_group_disk_scalers_io_utilization_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_disk_group_disk_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_disk_group_disk_scalers_model = {} # AutoscalingDiskGroupDiskScalers
        autoscaling_disk_group_disk_scalers_model['capacity'] = autoscaling_disk_group_disk_scalers_capacity_model
        autoscaling_disk_group_disk_scalers_model['io_utilization'] = autoscaling_disk_group_disk_scalers_io_utilization_model

        autoscaling_disk_group_disk_rate_model = {} # AutoscalingDiskGroupDiskRate
        autoscaling_disk_group_disk_rate_model['increase_percent'] = 20
        autoscaling_disk_group_disk_rate_model['period_seconds'] = 900
        autoscaling_disk_group_disk_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_disk_group_disk_rate_model['units'] = 'mb'

        autoscaling_disk_group_disk_model = {} # AutoscalingDiskGroupDisk
        autoscaling_disk_group_disk_model['scalers'] = autoscaling_disk_group_disk_scalers_model
        autoscaling_disk_group_disk_model['rate'] = autoscaling_disk_group_disk_rate_model

        autoscaling_memory_group_memory_scalers_io_utilization_model = {} # AutoscalingMemoryGroupMemoryScalersIoUtilization
        autoscaling_memory_group_memory_scalers_io_utilization_model['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_memory_group_memory_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_memory_group_memory_scalers_model = {} # AutoscalingMemoryGroupMemoryScalers
        autoscaling_memory_group_memory_scalers_model['io_utilization'] = autoscaling_memory_group_memory_scalers_io_utilization_model

        autoscaling_memory_group_memory_rate_model = {} # AutoscalingMemoryGroupMemoryRate
        autoscaling_memory_group_memory_rate_model['increase_percent'] = 10
        autoscaling_memory_group_memory_rate_model['period_seconds'] = 900
        autoscaling_memory_group_memory_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_memory_group_memory_rate_model['units'] = 'mb'

        autoscaling_memory_group_memory_model = {} # AutoscalingMemoryGroupMemory
        autoscaling_memory_group_memory_model['scalers'] = autoscaling_memory_group_memory_scalers_model
        autoscaling_memory_group_memory_model['rate'] = autoscaling_memory_group_memory_rate_model

        autoscaling_cpu_group_cpu_rate_model = {} # AutoscalingCPUGroupCPURate
        autoscaling_cpu_group_cpu_rate_model['increase_percent'] = 10
        autoscaling_cpu_group_cpu_rate_model['period_seconds'] = 900
        autoscaling_cpu_group_cpu_rate_model['limit_count_per_member'] = 10
        autoscaling_cpu_group_cpu_rate_model['units'] = 'count'

        autoscaling_cpu_group_cpu_model = {} # AutoscalingCPUGroupCPU
        autoscaling_cpu_group_cpu_model['scalers'] = {'foo': 'bar'}
        autoscaling_cpu_group_cpu_model['rate'] = autoscaling_cpu_group_cpu_rate_model

        autoscaling_group_autoscaling_model = {} # AutoscalingGroupAutoscaling
        autoscaling_group_autoscaling_model['disk'] = autoscaling_disk_group_disk_model
        autoscaling_group_autoscaling_model['memory'] = autoscaling_memory_group_memory_model
        autoscaling_group_autoscaling_model['cpu'] = autoscaling_cpu_group_cpu_model

        # Construct a json representation of a AutoscalingGroup model
        autoscaling_group_model_json = {}
        autoscaling_group_model_json['autoscaling'] = autoscaling_group_autoscaling_model

        # Construct a model instance of AutoscalingGroup by calling from_dict on the json representation
        autoscaling_group_model = AutoscalingGroup.from_dict(autoscaling_group_model_json)
        assert autoscaling_group_model != False

        # Construct a model instance of AutoscalingGroup by calling from_dict on the json representation
        autoscaling_group_model_dict = AutoscalingGroup.from_dict(autoscaling_group_model_json).__dict__
        autoscaling_group_model2 = AutoscalingGroup(**autoscaling_group_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_group_model == autoscaling_group_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_group_model_json2 = autoscaling_group_model.to_dict()
        assert autoscaling_group_model_json2 == autoscaling_group_model_json

class TestModel_AutoscalingGroupAutoscaling():
    """
    Test Class for AutoscalingGroupAutoscaling
    """

    def test_autoscaling_group_autoscaling_serialization(self):
        """
        Test serialization/deserialization for AutoscalingGroupAutoscaling
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_disk_group_disk_scalers_capacity_model = {} # AutoscalingDiskGroupDiskScalersCapacity
        autoscaling_disk_group_disk_scalers_capacity_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_capacity_model['free_space_less_than_percent'] = 10

        autoscaling_disk_group_disk_scalers_io_utilization_model = {} # AutoscalingDiskGroupDiskScalersIoUtilization
        autoscaling_disk_group_disk_scalers_io_utilization_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_disk_group_disk_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_disk_group_disk_scalers_model = {} # AutoscalingDiskGroupDiskScalers
        autoscaling_disk_group_disk_scalers_model['capacity'] = autoscaling_disk_group_disk_scalers_capacity_model
        autoscaling_disk_group_disk_scalers_model['io_utilization'] = autoscaling_disk_group_disk_scalers_io_utilization_model

        autoscaling_disk_group_disk_rate_model = {} # AutoscalingDiskGroupDiskRate
        autoscaling_disk_group_disk_rate_model['increase_percent'] = 20
        autoscaling_disk_group_disk_rate_model['period_seconds'] = 900
        autoscaling_disk_group_disk_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_disk_group_disk_rate_model['units'] = 'mb'

        autoscaling_disk_group_disk_model = {} # AutoscalingDiskGroupDisk
        autoscaling_disk_group_disk_model['scalers'] = autoscaling_disk_group_disk_scalers_model
        autoscaling_disk_group_disk_model['rate'] = autoscaling_disk_group_disk_rate_model

        autoscaling_memory_group_memory_scalers_io_utilization_model = {} # AutoscalingMemoryGroupMemoryScalersIoUtilization
        autoscaling_memory_group_memory_scalers_io_utilization_model['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_memory_group_memory_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_memory_group_memory_scalers_model = {} # AutoscalingMemoryGroupMemoryScalers
        autoscaling_memory_group_memory_scalers_model['io_utilization'] = autoscaling_memory_group_memory_scalers_io_utilization_model

        autoscaling_memory_group_memory_rate_model = {} # AutoscalingMemoryGroupMemoryRate
        autoscaling_memory_group_memory_rate_model['increase_percent'] = 10
        autoscaling_memory_group_memory_rate_model['period_seconds'] = 900
        autoscaling_memory_group_memory_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_memory_group_memory_rate_model['units'] = 'mb'

        autoscaling_memory_group_memory_model = {} # AutoscalingMemoryGroupMemory
        autoscaling_memory_group_memory_model['scalers'] = autoscaling_memory_group_memory_scalers_model
        autoscaling_memory_group_memory_model['rate'] = autoscaling_memory_group_memory_rate_model

        autoscaling_cpu_group_cpu_rate_model = {} # AutoscalingCPUGroupCPURate
        autoscaling_cpu_group_cpu_rate_model['increase_percent'] = 10
        autoscaling_cpu_group_cpu_rate_model['period_seconds'] = 900
        autoscaling_cpu_group_cpu_rate_model['limit_count_per_member'] = 10
        autoscaling_cpu_group_cpu_rate_model['units'] = 'count'

        autoscaling_cpu_group_cpu_model = {} # AutoscalingCPUGroupCPU
        autoscaling_cpu_group_cpu_model['scalers'] = {'foo': 'bar'}
        autoscaling_cpu_group_cpu_model['rate'] = autoscaling_cpu_group_cpu_rate_model

        # Construct a json representation of a AutoscalingGroupAutoscaling model
        autoscaling_group_autoscaling_model_json = {}
        autoscaling_group_autoscaling_model_json['disk'] = autoscaling_disk_group_disk_model
        autoscaling_group_autoscaling_model_json['memory'] = autoscaling_memory_group_memory_model
        autoscaling_group_autoscaling_model_json['cpu'] = autoscaling_cpu_group_cpu_model

        # Construct a model instance of AutoscalingGroupAutoscaling by calling from_dict on the json representation
        autoscaling_group_autoscaling_model = AutoscalingGroupAutoscaling.from_dict(autoscaling_group_autoscaling_model_json)
        assert autoscaling_group_autoscaling_model != False

        # Construct a model instance of AutoscalingGroupAutoscaling by calling from_dict on the json representation
        autoscaling_group_autoscaling_model_dict = AutoscalingGroupAutoscaling.from_dict(autoscaling_group_autoscaling_model_json).__dict__
        autoscaling_group_autoscaling_model2 = AutoscalingGroupAutoscaling(**autoscaling_group_autoscaling_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_group_autoscaling_model == autoscaling_group_autoscaling_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_group_autoscaling_model_json2 = autoscaling_group_autoscaling_model.to_dict()
        assert autoscaling_group_autoscaling_model_json2 == autoscaling_group_autoscaling_model_json

class TestModel_AutoscalingMemoryGroupMemory():
    """
    Test Class for AutoscalingMemoryGroupMemory
    """

    def test_autoscaling_memory_group_memory_serialization(self):
        """
        Test serialization/deserialization for AutoscalingMemoryGroupMemory
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_memory_group_memory_scalers_io_utilization_model = {} # AutoscalingMemoryGroupMemoryScalersIoUtilization
        autoscaling_memory_group_memory_scalers_io_utilization_model['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_memory_group_memory_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_memory_group_memory_scalers_model = {} # AutoscalingMemoryGroupMemoryScalers
        autoscaling_memory_group_memory_scalers_model['io_utilization'] = autoscaling_memory_group_memory_scalers_io_utilization_model

        autoscaling_memory_group_memory_rate_model = {} # AutoscalingMemoryGroupMemoryRate
        autoscaling_memory_group_memory_rate_model['increase_percent'] = 10
        autoscaling_memory_group_memory_rate_model['period_seconds'] = 900
        autoscaling_memory_group_memory_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_memory_group_memory_rate_model['units'] = 'mb'

        # Construct a json representation of a AutoscalingMemoryGroupMemory model
        autoscaling_memory_group_memory_model_json = {}
        autoscaling_memory_group_memory_model_json['scalers'] = autoscaling_memory_group_memory_scalers_model
        autoscaling_memory_group_memory_model_json['rate'] = autoscaling_memory_group_memory_rate_model

        # Construct a model instance of AutoscalingMemoryGroupMemory by calling from_dict on the json representation
        autoscaling_memory_group_memory_model = AutoscalingMemoryGroupMemory.from_dict(autoscaling_memory_group_memory_model_json)
        assert autoscaling_memory_group_memory_model != False

        # Construct a model instance of AutoscalingMemoryGroupMemory by calling from_dict on the json representation
        autoscaling_memory_group_memory_model_dict = AutoscalingMemoryGroupMemory.from_dict(autoscaling_memory_group_memory_model_json).__dict__
        autoscaling_memory_group_memory_model2 = AutoscalingMemoryGroupMemory(**autoscaling_memory_group_memory_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_memory_group_memory_model == autoscaling_memory_group_memory_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_memory_group_memory_model_json2 = autoscaling_memory_group_memory_model.to_dict()
        assert autoscaling_memory_group_memory_model_json2 == autoscaling_memory_group_memory_model_json

class TestModel_AutoscalingMemoryGroupMemoryRate():
    """
    Test Class for AutoscalingMemoryGroupMemoryRate
    """

    def test_autoscaling_memory_group_memory_rate_serialization(self):
        """
        Test serialization/deserialization for AutoscalingMemoryGroupMemoryRate
        """

        # Construct a json representation of a AutoscalingMemoryGroupMemoryRate model
        autoscaling_memory_group_memory_rate_model_json = {}
        autoscaling_memory_group_memory_rate_model_json['increase_percent'] = 10
        autoscaling_memory_group_memory_rate_model_json['period_seconds'] = 900
        autoscaling_memory_group_memory_rate_model_json['limit_mb_per_member'] = 3670016
        autoscaling_memory_group_memory_rate_model_json['units'] = 'mb'

        # Construct a model instance of AutoscalingMemoryGroupMemoryRate by calling from_dict on the json representation
        autoscaling_memory_group_memory_rate_model = AutoscalingMemoryGroupMemoryRate.from_dict(autoscaling_memory_group_memory_rate_model_json)
        assert autoscaling_memory_group_memory_rate_model != False

        # Construct a model instance of AutoscalingMemoryGroupMemoryRate by calling from_dict on the json representation
        autoscaling_memory_group_memory_rate_model_dict = AutoscalingMemoryGroupMemoryRate.from_dict(autoscaling_memory_group_memory_rate_model_json).__dict__
        autoscaling_memory_group_memory_rate_model2 = AutoscalingMemoryGroupMemoryRate(**autoscaling_memory_group_memory_rate_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_memory_group_memory_rate_model == autoscaling_memory_group_memory_rate_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_memory_group_memory_rate_model_json2 = autoscaling_memory_group_memory_rate_model.to_dict()
        assert autoscaling_memory_group_memory_rate_model_json2 == autoscaling_memory_group_memory_rate_model_json

class TestModel_AutoscalingMemoryGroupMemoryScalers():
    """
    Test Class for AutoscalingMemoryGroupMemoryScalers
    """

    def test_autoscaling_memory_group_memory_scalers_serialization(self):
        """
        Test serialization/deserialization for AutoscalingMemoryGroupMemoryScalers
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_memory_group_memory_scalers_io_utilization_model = {} # AutoscalingMemoryGroupMemoryScalersIoUtilization
        autoscaling_memory_group_memory_scalers_io_utilization_model['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_memory_group_memory_scalers_io_utilization_model['above_percent'] = 45

        # Construct a json representation of a AutoscalingMemoryGroupMemoryScalers model
        autoscaling_memory_group_memory_scalers_model_json = {}
        autoscaling_memory_group_memory_scalers_model_json['io_utilization'] = autoscaling_memory_group_memory_scalers_io_utilization_model

        # Construct a model instance of AutoscalingMemoryGroupMemoryScalers by calling from_dict on the json representation
        autoscaling_memory_group_memory_scalers_model = AutoscalingMemoryGroupMemoryScalers.from_dict(autoscaling_memory_group_memory_scalers_model_json)
        assert autoscaling_memory_group_memory_scalers_model != False

        # Construct a model instance of AutoscalingMemoryGroupMemoryScalers by calling from_dict on the json representation
        autoscaling_memory_group_memory_scalers_model_dict = AutoscalingMemoryGroupMemoryScalers.from_dict(autoscaling_memory_group_memory_scalers_model_json).__dict__
        autoscaling_memory_group_memory_scalers_model2 = AutoscalingMemoryGroupMemoryScalers(**autoscaling_memory_group_memory_scalers_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_memory_group_memory_scalers_model == autoscaling_memory_group_memory_scalers_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_memory_group_memory_scalers_model_json2 = autoscaling_memory_group_memory_scalers_model.to_dict()
        assert autoscaling_memory_group_memory_scalers_model_json2 == autoscaling_memory_group_memory_scalers_model_json

class TestModel_AutoscalingMemoryGroupMemoryScalersIoUtilization():
    """
    Test Class for AutoscalingMemoryGroupMemoryScalersIoUtilization
    """

    def test_autoscaling_memory_group_memory_scalers_io_utilization_serialization(self):
        """
        Test serialization/deserialization for AutoscalingMemoryGroupMemoryScalersIoUtilization
        """

        # Construct a json representation of a AutoscalingMemoryGroupMemoryScalersIoUtilization model
        autoscaling_memory_group_memory_scalers_io_utilization_model_json = {}
        autoscaling_memory_group_memory_scalers_io_utilization_model_json['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model_json['over_period'] = '30m'
        autoscaling_memory_group_memory_scalers_io_utilization_model_json['above_percent'] = 45

        # Construct a model instance of AutoscalingMemoryGroupMemoryScalersIoUtilization by calling from_dict on the json representation
        autoscaling_memory_group_memory_scalers_io_utilization_model = AutoscalingMemoryGroupMemoryScalersIoUtilization.from_dict(autoscaling_memory_group_memory_scalers_io_utilization_model_json)
        assert autoscaling_memory_group_memory_scalers_io_utilization_model != False

        # Construct a model instance of AutoscalingMemoryGroupMemoryScalersIoUtilization by calling from_dict on the json representation
        autoscaling_memory_group_memory_scalers_io_utilization_model_dict = AutoscalingMemoryGroupMemoryScalersIoUtilization.from_dict(autoscaling_memory_group_memory_scalers_io_utilization_model_json).__dict__
        autoscaling_memory_group_memory_scalers_io_utilization_model2 = AutoscalingMemoryGroupMemoryScalersIoUtilization(**autoscaling_memory_group_memory_scalers_io_utilization_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_memory_group_memory_scalers_io_utilization_model == autoscaling_memory_group_memory_scalers_io_utilization_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_memory_group_memory_scalers_io_utilization_model_json2 = autoscaling_memory_group_memory_scalers_io_utilization_model.to_dict()
        assert autoscaling_memory_group_memory_scalers_io_utilization_model_json2 == autoscaling_memory_group_memory_scalers_io_utilization_model_json

class TestModel_Backup():
    """
    Test Class for Backup
    """

    def test_backup_serialization(self):
        """
        Test serialization/deserialization for Backup
        """

        # Construct a json representation of a Backup model
        backup_model_json = {}
        backup_model_json['id'] = '5a970218cb7544000671c094'
        backup_model_json['deployment_id'] = '595eada310b7ac00116dd48b'
        backup_model_json['type'] = 'scheduled'
        backup_model_json['status'] = 'running'
        backup_model_json['is_downloadable'] = True
        backup_model_json['is_restorable'] = True
        backup_model_json['download_link'] = 'https://securedownloadservice.com/backup-2018-02-28T19:25:12Z.tgz'
        backup_model_json['created_at'] = '2018-02-28T19:25:12Z'

        # Construct a model instance of Backup by calling from_dict on the json representation
        backup_model = Backup.from_dict(backup_model_json)
        assert backup_model != False

        # Construct a model instance of Backup by calling from_dict on the json representation
        backup_model_dict = Backup.from_dict(backup_model_json).__dict__
        backup_model2 = Backup(**backup_model_dict)

        # Verify the model instances are equivalent
        assert backup_model == backup_model2

        # Convert model instance back to dict and verify no loss of data
        backup_model_json2 = backup_model.to_dict()
        assert backup_model_json2 == backup_model_json

class TestModel_Backups():
    """
    Test Class for Backups
    """

    def test_backups_serialization(self):
        """
        Test serialization/deserialization for Backups
        """

        # Construct dict forms of any model objects needed in order to build this model.

        backup_model = {} # Backup
        backup_model['id'] = 'crn:v1:bluemix:public:databases-for-elasticsearch:us-south:a/2740839ce64e9c423ffc238516c755e1:afa742a3-6f83-4f6e-a06e-b5c501e9e87a:backup:e47213d6-4a13-47f4-a511-9ef459670192'
        backup_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-elasticsearch:us-south:a/2740839ce64e9c423ffc238516c755e1:afa742a3-6f83-4f6e-a06e-b5c501e9e87a::'
        backup_model['type'] = 'scheduled'
        backup_model['status'] = 'completed'
        backup_model['is_downloadable'] = False
        backup_model['is_restorable'] = True
        backup_model['download_link'] = 'https://securedownloadservice.com/backup-2018-02-28T19:25:12Z.tgz'
        backup_model['created_at'] = '2019-05-29T14:30:46Z'

        # Construct a json representation of a Backups model
        backups_model_json = {}
        backups_model_json['backups'] = [backup_model]

        # Construct a model instance of Backups by calling from_dict on the json representation
        backups_model = Backups.from_dict(backups_model_json)
        assert backups_model != False

        # Construct a model instance of Backups by calling from_dict on the json representation
        backups_model_dict = Backups.from_dict(backups_model_json).__dict__
        backups_model2 = Backups(**backups_model_dict)

        # Verify the model instances are equivalent
        assert backups_model == backups_model2

        # Convert model instance back to dict and verify no loss of data
        backups_model_json2 = backups_model.to_dict()
        assert backups_model_json2 == backups_model_json

class TestModel_CompleteConnectionResponse():
    """
    Test Class for CompleteConnectionResponse
    """

    def test_complete_connection_response_serialization(self):
        """
        Test serialization/deserialization for CompleteConnectionResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        postgre_sql_connection_uri_model = {} # PostgreSQLConnectionURI
        postgre_sql_connection_uri_model['type'] = 'uri'
        postgre_sql_connection_uri_model['composed'] = ['testString']
        postgre_sql_connection_uri_model['scheme'] = 'testString'
        postgre_sql_connection_uri_model['hosts'] = [connection_host_model]
        postgre_sql_connection_uri_model['path'] = 'testString'
        postgre_sql_connection_uri_model['query_options'] = {'foo': 'bar'}
        postgre_sql_connection_uri_model['authentication'] = connection_authentication_model
        postgre_sql_connection_uri_model['certificate'] = connection_certificate_model
        postgre_sql_connection_uri_model['ssl'] = True
        postgre_sql_connection_uri_model['browser_accessible'] = True
        postgre_sql_connection_uri_model['database'] = 'testString'

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {'foo': 'bar'}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_certificate_model

        connection_model = {} # ConnectionPostgreSQLConnection
        connection_model['postgres'] = postgre_sql_connection_uri_model
        connection_model['cli'] = connection_cli_model

        # Construct a json representation of a CompleteConnectionResponse model
        complete_connection_response_model_json = {}
        complete_connection_response_model_json['connection'] = connection_model

        # Construct a model instance of CompleteConnectionResponse by calling from_dict on the json representation
        complete_connection_response_model = CompleteConnectionResponse.from_dict(complete_connection_response_model_json)
        assert complete_connection_response_model != False

        # Construct a model instance of CompleteConnectionResponse by calling from_dict on the json representation
        complete_connection_response_model_dict = CompleteConnectionResponse.from_dict(complete_connection_response_model_json).__dict__
        complete_connection_response_model2 = CompleteConnectionResponse(**complete_connection_response_model_dict)

        # Verify the model instances are equivalent
        assert complete_connection_response_model == complete_connection_response_model2

        # Convert model instance back to dict and verify no loss of data
        complete_connection_response_model_json2 = complete_connection_response_model.to_dict()
        assert complete_connection_response_model_json2 == complete_connection_response_model_json

class TestModel_ConnectionAuthentication():
    """
    Test Class for ConnectionAuthentication
    """

    def test_connection_authentication_serialization(self):
        """
        Test serialization/deserialization for ConnectionAuthentication
        """

        # Construct a json representation of a ConnectionAuthentication model
        connection_authentication_model_json = {}
        connection_authentication_model_json['method'] = 'testString'
        connection_authentication_model_json['username'] = 'testString'
        connection_authentication_model_json['password'] = 'testString'

        # Construct a model instance of ConnectionAuthentication by calling from_dict on the json representation
        connection_authentication_model = ConnectionAuthentication.from_dict(connection_authentication_model_json)
        assert connection_authentication_model != False

        # Construct a model instance of ConnectionAuthentication by calling from_dict on the json representation
        connection_authentication_model_dict = ConnectionAuthentication.from_dict(connection_authentication_model_json).__dict__
        connection_authentication_model2 = ConnectionAuthentication(**connection_authentication_model_dict)

        # Verify the model instances are equivalent
        assert connection_authentication_model == connection_authentication_model2

        # Convert model instance back to dict and verify no loss of data
        connection_authentication_model_json2 = connection_authentication_model.to_dict()
        assert connection_authentication_model_json2 == connection_authentication_model_json

class TestModel_ConnectionBundle():
    """
    Test Class for ConnectionBundle
    """

    def test_connection_bundle_serialization(self):
        """
        Test serialization/deserialization for ConnectionBundle
        """

        # Construct a json representation of a ConnectionBundle model
        connection_bundle_model_json = {}
        connection_bundle_model_json['name'] = 'testString'
        connection_bundle_model_json['bundle_base64'] = 'testString'

        # Construct a model instance of ConnectionBundle by calling from_dict on the json representation
        connection_bundle_model = ConnectionBundle.from_dict(connection_bundle_model_json)
        assert connection_bundle_model != False

        # Construct a model instance of ConnectionBundle by calling from_dict on the json representation
        connection_bundle_model_dict = ConnectionBundle.from_dict(connection_bundle_model_json).__dict__
        connection_bundle_model2 = ConnectionBundle(**connection_bundle_model_dict)

        # Verify the model instances are equivalent
        assert connection_bundle_model == connection_bundle_model2

        # Convert model instance back to dict and verify no loss of data
        connection_bundle_model_json2 = connection_bundle_model.to_dict()
        assert connection_bundle_model_json2 == connection_bundle_model_json

class TestModel_ConnectionCLI():
    """
    Test Class for ConnectionCLI
    """

    def test_connection_cli_serialization(self):
        """
        Test serialization/deserialization for ConnectionCLI
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a ConnectionCLI model
        connection_cli_model_json = {}
        connection_cli_model_json['type'] = 'cli'
        connection_cli_model_json['composed'] = ['testString']
        connection_cli_model_json['environment'] = {'foo': 'bar'}
        connection_cli_model_json['bin'] = 'testString'
        connection_cli_model_json['arguments'] = [['testString']]
        connection_cli_model_json['certificate'] = connection_certificate_model

        # Construct a model instance of ConnectionCLI by calling from_dict on the json representation
        connection_cli_model = ConnectionCLI.from_dict(connection_cli_model_json)
        assert connection_cli_model != False

        # Construct a model instance of ConnectionCLI by calling from_dict on the json representation
        connection_cli_model_dict = ConnectionCLI.from_dict(connection_cli_model_json).__dict__
        connection_cli_model2 = ConnectionCLI(**connection_cli_model_dict)

        # Verify the model instances are equivalent
        assert connection_cli_model == connection_cli_model2

        # Convert model instance back to dict and verify no loss of data
        connection_cli_model_json2 = connection_cli_model.to_dict()
        assert connection_cli_model_json2 == connection_cli_model_json

class TestModel_ConnectionCertificate():
    """
    Test Class for ConnectionCertificate
    """

    def test_connection_certificate_serialization(self):
        """
        Test serialization/deserialization for ConnectionCertificate
        """

        # Construct a json representation of a ConnectionCertificate model
        connection_certificate_model_json = {}
        connection_certificate_model_json['name'] = 'testString'
        connection_certificate_model_json['certificate_base64'] = 'testString'

        # Construct a model instance of ConnectionCertificate by calling from_dict on the json representation
        connection_certificate_model = ConnectionCertificate.from_dict(connection_certificate_model_json)
        assert connection_certificate_model != False

        # Construct a model instance of ConnectionCertificate by calling from_dict on the json representation
        connection_certificate_model_dict = ConnectionCertificate.from_dict(connection_certificate_model_json).__dict__
        connection_certificate_model2 = ConnectionCertificate(**connection_certificate_model_dict)

        # Verify the model instances are equivalent
        assert connection_certificate_model == connection_certificate_model2

        # Convert model instance back to dict and verify no loss of data
        connection_certificate_model_json2 = connection_certificate_model.to_dict()
        assert connection_certificate_model_json2 == connection_certificate_model_json

class TestModel_ConnectionHost():
    """
    Test Class for ConnectionHost
    """

    def test_connection_host_serialization(self):
        """
        Test serialization/deserialization for ConnectionHost
        """

        # Construct a json representation of a ConnectionHost model
        connection_host_model_json = {}
        connection_host_model_json['hostname'] = 'testString'
        connection_host_model_json['port'] = 38

        # Construct a model instance of ConnectionHost by calling from_dict on the json representation
        connection_host_model = ConnectionHost.from_dict(connection_host_model_json)
        assert connection_host_model != False

        # Construct a model instance of ConnectionHost by calling from_dict on the json representation
        connection_host_model_dict = ConnectionHost.from_dict(connection_host_model_json).__dict__
        connection_host_model2 = ConnectionHost(**connection_host_model_dict)

        # Verify the model instances are equivalent
        assert connection_host_model == connection_host_model2

        # Convert model instance back to dict and verify no loss of data
        connection_host_model_json2 = connection_host_model.to_dict()
        assert connection_host_model_json2 == connection_host_model_json

class TestModel_ConnectionURI():
    """
    Test Class for ConnectionURI
    """

    def test_connection_uri_serialization(self):
        """
        Test serialization/deserialization for ConnectionURI
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a ConnectionURI model
        connection_uri_model_json = {}
        connection_uri_model_json['type'] = 'uri'
        connection_uri_model_json['composed'] = ['testString']
        connection_uri_model_json['scheme'] = 'testString'
        connection_uri_model_json['hosts'] = [connection_host_model]
        connection_uri_model_json['path'] = 'testString'
        connection_uri_model_json['query_options'] = {'foo': 'bar'}
        connection_uri_model_json['authentication'] = connection_authentication_model
        connection_uri_model_json['certificate'] = connection_certificate_model
        connection_uri_model_json['ssl'] = True
        connection_uri_model_json['browser_accessible'] = True

        # Construct a model instance of ConnectionURI by calling from_dict on the json representation
        connection_uri_model = ConnectionURI.from_dict(connection_uri_model_json)
        assert connection_uri_model != False

        # Construct a model instance of ConnectionURI by calling from_dict on the json representation
        connection_uri_model_dict = ConnectionURI.from_dict(connection_uri_model_json).__dict__
        connection_uri_model2 = ConnectionURI(**connection_uri_model_dict)

        # Verify the model instances are equivalent
        assert connection_uri_model == connection_uri_model2

        # Convert model instance back to dict and verify no loss of data
        connection_uri_model_json2 = connection_uri_model.to_dict()
        assert connection_uri_model_json2 == connection_uri_model_json

class TestModel_CreateDatabaseUserResponse():
    """
    Test Class for CreateDatabaseUserResponse
    """

    def test_create_database_user_response_serialization(self):
        """
        Test serialization/deserialization for CreateDatabaseUserResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f3-b5c96544393b'
        task_model['description'] = 'Creating user for database'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = '2018-03-28T10:21:30Z'

        # Construct a json representation of a CreateDatabaseUserResponse model
        create_database_user_response_model_json = {}
        create_database_user_response_model_json['task'] = task_model

        # Construct a model instance of CreateDatabaseUserResponse by calling from_dict on the json representation
        create_database_user_response_model = CreateDatabaseUserResponse.from_dict(create_database_user_response_model_json)
        assert create_database_user_response_model != False

        # Construct a model instance of CreateDatabaseUserResponse by calling from_dict on the json representation
        create_database_user_response_model_dict = CreateDatabaseUserResponse.from_dict(create_database_user_response_model_json).__dict__
        create_database_user_response_model2 = CreateDatabaseUserResponse(**create_database_user_response_model_dict)

        # Verify the model instances are equivalent
        assert create_database_user_response_model == create_database_user_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_database_user_response_model_json2 = create_database_user_response_model.to_dict()
        assert create_database_user_response_model_json2 == create_database_user_response_model_json

class TestModel_CreateLogicalReplicationSlotResponse():
    """
    Test Class for CreateLogicalReplicationSlotResponse
    """

    def test_create_logical_replication_slot_response_serialization(self):
        """
        Test serialization/deserialization for CreateLogicalReplicationSlotResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:eu-de:a/057f598ff0b94d9663c28b68843eaab3:b544602f-ad0a-405b-ba39-2e69d04ff3a2:task:d29ea458-5c11-486f-9182-1984ec5d5314'
        task_model['description'] = 'Creating logical replication slot'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:eu-de:a/057f598ff0b94d9663c28b68843eaab3:b544602f-ad0a-405b-ba39-2e69d04ff3a2::'
        task_model['progress_percent'] = 0
        task_model['created_at'] = '2019-05-31T10:20:30Z'

        # Construct a json representation of a CreateLogicalReplicationSlotResponse model
        create_logical_replication_slot_response_model_json = {}
        create_logical_replication_slot_response_model_json['task'] = task_model

        # Construct a model instance of CreateLogicalReplicationSlotResponse by calling from_dict on the json representation
        create_logical_replication_slot_response_model = CreateLogicalReplicationSlotResponse.from_dict(create_logical_replication_slot_response_model_json)
        assert create_logical_replication_slot_response_model != False

        # Construct a model instance of CreateLogicalReplicationSlotResponse by calling from_dict on the json representation
        create_logical_replication_slot_response_model_dict = CreateLogicalReplicationSlotResponse.from_dict(create_logical_replication_slot_response_model_json).__dict__
        create_logical_replication_slot_response_model2 = CreateLogicalReplicationSlotResponse(**create_logical_replication_slot_response_model_dict)

        # Verify the model instances are equivalent
        assert create_logical_replication_slot_response_model == create_logical_replication_slot_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_logical_replication_slot_response_model_json2 = create_logical_replication_slot_response_model.to_dict()
        assert create_logical_replication_slot_response_model_json2 == create_logical_replication_slot_response_model_json

class TestModel_DataStaxConnectionURI():
    """
    Test Class for DataStaxConnectionURI
    """

    def test_data_stax_connection_uri_serialization(self):
        """
        Test serialization/deserialization for DataStaxConnectionURI
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_bundle_model = {} # ConnectionBundle
        connection_bundle_model['name'] = 'testString'
        connection_bundle_model['bundle_base64'] = 'testString'

        # Construct a json representation of a DataStaxConnectionURI model
        data_stax_connection_uri_model_json = {}
        data_stax_connection_uri_model_json['hosts'] = [connection_host_model]
        data_stax_connection_uri_model_json['authentication'] = connection_authentication_model
        data_stax_connection_uri_model_json['bundle'] = connection_bundle_model

        # Construct a model instance of DataStaxConnectionURI by calling from_dict on the json representation
        data_stax_connection_uri_model = DataStaxConnectionURI.from_dict(data_stax_connection_uri_model_json)
        assert data_stax_connection_uri_model != False

        # Construct a model instance of DataStaxConnectionURI by calling from_dict on the json representation
        data_stax_connection_uri_model_dict = DataStaxConnectionURI.from_dict(data_stax_connection_uri_model_json).__dict__
        data_stax_connection_uri_model2 = DataStaxConnectionURI(**data_stax_connection_uri_model_dict)

        # Verify the model instances are equivalent
        assert data_stax_connection_uri_model == data_stax_connection_uri_model2

        # Convert model instance back to dict and verify no loss of data
        data_stax_connection_uri_model_json2 = data_stax_connection_uri_model.to_dict()
        assert data_stax_connection_uri_model_json2 == data_stax_connection_uri_model_json

class TestModel_DeleteAllowlistEntryResponse():
    """
    Test Class for DeleteAllowlistEntryResponse
    """

    def test_delete_allowlist_entry_response_serialization(self):
        """
        Test serialization/deserialization for DeleteAllowlistEntryResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4d36-92f3-b5c96544393b'
        task_model['description'] = 'Deleting allowlist entry for database'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 15
        task_model['created_at'] = '2018-03-28T10:25:30Z'

        # Construct a json representation of a DeleteAllowlistEntryResponse model
        delete_allowlist_entry_response_model_json = {}
        delete_allowlist_entry_response_model_json['task'] = task_model

        # Construct a model instance of DeleteAllowlistEntryResponse by calling from_dict on the json representation
        delete_allowlist_entry_response_model = DeleteAllowlistEntryResponse.from_dict(delete_allowlist_entry_response_model_json)
        assert delete_allowlist_entry_response_model != False

        # Construct a model instance of DeleteAllowlistEntryResponse by calling from_dict on the json representation
        delete_allowlist_entry_response_model_dict = DeleteAllowlistEntryResponse.from_dict(delete_allowlist_entry_response_model_json).__dict__
        delete_allowlist_entry_response_model2 = DeleteAllowlistEntryResponse(**delete_allowlist_entry_response_model_dict)

        # Verify the model instances are equivalent
        assert delete_allowlist_entry_response_model == delete_allowlist_entry_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_allowlist_entry_response_model_json2 = delete_allowlist_entry_response_model.to_dict()
        assert delete_allowlist_entry_response_model_json2 == delete_allowlist_entry_response_model_json

class TestModel_DeleteDatabaseUserResponse():
    """
    Test Class for DeleteDatabaseUserResponse
    """

    def test_delete_database_user_response_serialization(self):
        """
        Test serialization/deserialization for DeleteDatabaseUserResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f3-b5c96555393b'
        task_model['description'] = 'Deleting user from database'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-99bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 10
        task_model['created_at'] = '2018-03-28T10:23:30Z'

        # Construct a json representation of a DeleteDatabaseUserResponse model
        delete_database_user_response_model_json = {}
        delete_database_user_response_model_json['task'] = task_model

        # Construct a model instance of DeleteDatabaseUserResponse by calling from_dict on the json representation
        delete_database_user_response_model = DeleteDatabaseUserResponse.from_dict(delete_database_user_response_model_json)
        assert delete_database_user_response_model != False

        # Construct a model instance of DeleteDatabaseUserResponse by calling from_dict on the json representation
        delete_database_user_response_model_dict = DeleteDatabaseUserResponse.from_dict(delete_database_user_response_model_json).__dict__
        delete_database_user_response_model2 = DeleteDatabaseUserResponse(**delete_database_user_response_model_dict)

        # Verify the model instances are equivalent
        assert delete_database_user_response_model == delete_database_user_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_database_user_response_model_json2 = delete_database_user_response_model.to_dict()
        assert delete_database_user_response_model_json2 == delete_database_user_response_model_json

class TestModel_DeleteLogicalReplicationSlotResponse():
    """
    Test Class for DeleteLogicalReplicationSlotResponse
    """

    def test_delete_logical_replication_slot_response_serialization(self):
        """
        Test serialization/deserialization for DeleteLogicalReplicationSlotResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:eu-de:a/057f598ff0b94d9663c28b68843eaab3:b544602f-ad0a-405b-ba39-2e69d04ff3a2:task:d29ea458-5c11-486f-9182-1894ec5d5314'
        task_model['description'] = 'Deleting logical replication slot'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:eu-de:a/057f598ff0b94d9663c28b68843eaab3:b544602f-ad0a-405b-ba39-2e69d04ff3a2::'
        task_model['progress_percent'] = 0
        task_model['created_at'] = '2019-05-31T10:20:30Z'

        # Construct a json representation of a DeleteLogicalReplicationSlotResponse model
        delete_logical_replication_slot_response_model_json = {}
        delete_logical_replication_slot_response_model_json['task'] = task_model

        # Construct a model instance of DeleteLogicalReplicationSlotResponse by calling from_dict on the json representation
        delete_logical_replication_slot_response_model = DeleteLogicalReplicationSlotResponse.from_dict(delete_logical_replication_slot_response_model_json)
        assert delete_logical_replication_slot_response_model != False

        # Construct a model instance of DeleteLogicalReplicationSlotResponse by calling from_dict on the json representation
        delete_logical_replication_slot_response_model_dict = DeleteLogicalReplicationSlotResponse.from_dict(delete_logical_replication_slot_response_model_json).__dict__
        delete_logical_replication_slot_response_model2 = DeleteLogicalReplicationSlotResponse(**delete_logical_replication_slot_response_model_dict)

        # Verify the model instances are equivalent
        assert delete_logical_replication_slot_response_model == delete_logical_replication_slot_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_logical_replication_slot_response_model_json2 = delete_logical_replication_slot_response_model.to_dict()
        assert delete_logical_replication_slot_response_model_json2 == delete_logical_replication_slot_response_model_json

class TestModel_Deployables():
    """
    Test Class for Deployables
    """

    def test_deployables_serialization(self):
        """
        Test serialization/deserialization for Deployables
        """

        # Construct dict forms of any model objects needed in order to build this model.

        deployables_versions_item_transitions_item_model = {} # DeployablesVersionsItemTransitionsItem
        deployables_versions_item_transitions_item_model['application'] = 'elasticsearch'
        deployables_versions_item_transitions_item_model['method'] = 'restore'
        deployables_versions_item_transitions_item_model['from_version'] = '5.6'
        deployables_versions_item_transitions_item_model['to_version'] = '6.7'

        deployables_versions_item_model = {} # DeployablesVersionsItem
        deployables_versions_item_model['version'] = '5.6'
        deployables_versions_item_model['status'] = 'stable'
        deployables_versions_item_model['is_preferred'] = True
        deployables_versions_item_model['transitions'] = [deployables_versions_item_transitions_item_model]

        # Construct a json representation of a Deployables model
        deployables_model_json = {}
        deployables_model_json['type'] = 'elasticsearch'
        deployables_model_json['versions'] = [deployables_versions_item_model]

        # Construct a model instance of Deployables by calling from_dict on the json representation
        deployables_model = Deployables.from_dict(deployables_model_json)
        assert deployables_model != False

        # Construct a model instance of Deployables by calling from_dict on the json representation
        deployables_model_dict = Deployables.from_dict(deployables_model_json).__dict__
        deployables_model2 = Deployables(**deployables_model_dict)

        # Verify the model instances are equivalent
        assert deployables_model == deployables_model2

        # Convert model instance back to dict and verify no loss of data
        deployables_model_json2 = deployables_model.to_dict()
        assert deployables_model_json2 == deployables_model_json

class TestModel_DeployablesVersionsItem():
    """
    Test Class for DeployablesVersionsItem
    """

    def test_deployables_versions_item_serialization(self):
        """
        Test serialization/deserialization for DeployablesVersionsItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        deployables_versions_item_transitions_item_model = {} # DeployablesVersionsItemTransitionsItem
        deployables_versions_item_transitions_item_model['application'] = 'elasticsearch'
        deployables_versions_item_transitions_item_model['method'] = 'restore'
        deployables_versions_item_transitions_item_model['from_version'] = '5.6'
        deployables_versions_item_transitions_item_model['to_version'] = '6.7'

        # Construct a json representation of a DeployablesVersionsItem model
        deployables_versions_item_model_json = {}
        deployables_versions_item_model_json['version'] = '5.6'
        deployables_versions_item_model_json['status'] = 'stable'
        deployables_versions_item_model_json['is_preferred'] = True
        deployables_versions_item_model_json['transitions'] = [deployables_versions_item_transitions_item_model]

        # Construct a model instance of DeployablesVersionsItem by calling from_dict on the json representation
        deployables_versions_item_model = DeployablesVersionsItem.from_dict(deployables_versions_item_model_json)
        assert deployables_versions_item_model != False

        # Construct a model instance of DeployablesVersionsItem by calling from_dict on the json representation
        deployables_versions_item_model_dict = DeployablesVersionsItem.from_dict(deployables_versions_item_model_json).__dict__
        deployables_versions_item_model2 = DeployablesVersionsItem(**deployables_versions_item_model_dict)

        # Verify the model instances are equivalent
        assert deployables_versions_item_model == deployables_versions_item_model2

        # Convert model instance back to dict and verify no loss of data
        deployables_versions_item_model_json2 = deployables_versions_item_model.to_dict()
        assert deployables_versions_item_model_json2 == deployables_versions_item_model_json

class TestModel_DeployablesVersionsItemTransitionsItem():
    """
    Test Class for DeployablesVersionsItemTransitionsItem
    """

    def test_deployables_versions_item_transitions_item_serialization(self):
        """
        Test serialization/deserialization for DeployablesVersionsItemTransitionsItem
        """

        # Construct a json representation of a DeployablesVersionsItemTransitionsItem model
        deployables_versions_item_transitions_item_model_json = {}
        deployables_versions_item_transitions_item_model_json['application'] = 'elasticsearch'
        deployables_versions_item_transitions_item_model_json['method'] = 'restore'
        deployables_versions_item_transitions_item_model_json['from_version'] = '5.6'
        deployables_versions_item_transitions_item_model_json['to_version'] = '6.7'

        # Construct a model instance of DeployablesVersionsItemTransitionsItem by calling from_dict on the json representation
        deployables_versions_item_transitions_item_model = DeployablesVersionsItemTransitionsItem.from_dict(deployables_versions_item_transitions_item_model_json)
        assert deployables_versions_item_transitions_item_model != False

        # Construct a model instance of DeployablesVersionsItemTransitionsItem by calling from_dict on the json representation
        deployables_versions_item_transitions_item_model_dict = DeployablesVersionsItemTransitionsItem.from_dict(deployables_versions_item_transitions_item_model_json).__dict__
        deployables_versions_item_transitions_item_model2 = DeployablesVersionsItemTransitionsItem(**deployables_versions_item_transitions_item_model_dict)

        # Verify the model instances are equivalent
        assert deployables_versions_item_transitions_item_model == deployables_versions_item_transitions_item_model2

        # Convert model instance back to dict and verify no loss of data
        deployables_versions_item_transitions_item_model_json2 = deployables_versions_item_transitions_item_model.to_dict()
        assert deployables_versions_item_transitions_item_model_json2 == deployables_versions_item_transitions_item_model_json

class TestModel_Deployment():
    """
    Test Class for Deployment
    """

    def test_deployment_serialization(self):
        """
        Test serialization/deserialization for Deployment
        """

        # Construct a json representation of a Deployment model
        deployment_model_json = {}
        deployment_model_json['id'] = 'crn:v1:bluemix:public:databases-for-redis:us-south:a/274074dce64e9c423ffc238516c755e1:29caf0e7-120f-4da8-9551-3abf57ebcfc7::'
        deployment_model_json['name'] = 'crn:v1:bluemix:public:databases-for-redis:us-south:a/274074dce64e9c423ffc238516c755e1:29caf0e7-120f-4da8-9551-3abf57ebcfc7::'
        deployment_model_json['type'] = 'redis'
        deployment_model_json['platform'] = 'satellite, classic'
        deployment_model_json['platform_options'] = {'foo': 'bar'}
        deployment_model_json['version'] = '4'
        deployment_model_json['admin_usernames'] = {'key1': 'testString'}
        deployment_model_json['enable_public_endpoints'] = True
        deployment_model_json['enable_private_endpoints'] = False

        # Construct a model instance of Deployment by calling from_dict on the json representation
        deployment_model = Deployment.from_dict(deployment_model_json)
        assert deployment_model != False

        # Construct a model instance of Deployment by calling from_dict on the json representation
        deployment_model_dict = Deployment.from_dict(deployment_model_json).__dict__
        deployment_model2 = Deployment(**deployment_model_dict)

        # Verify the model instances are equivalent
        assert deployment_model == deployment_model2

        # Convert model instance back to dict and verify no loss of data
        deployment_model_json2 = deployment_model.to_dict()
        assert deployment_model_json2 == deployment_model_json

class TestModel_GetAllowlistResponse():
    """
    Test Class for GetAllowlistResponse
    """

    def test_get_allowlist_response_serialization(self):
        """
        Test serialization/deserialization for GetAllowlistResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        allowlist_entry_model = {} # AllowlistEntry
        allowlist_entry_model['address'] = 'testString'
        allowlist_entry_model['description'] = 'testString'

        # Construct a json representation of a GetAllowlistResponse model
        get_allowlist_response_model_json = {}
        get_allowlist_response_model_json['ip_addresses'] = [allowlist_entry_model]

        # Construct a model instance of GetAllowlistResponse by calling from_dict on the json representation
        get_allowlist_response_model = GetAllowlistResponse.from_dict(get_allowlist_response_model_json)
        assert get_allowlist_response_model != False

        # Construct a model instance of GetAllowlistResponse by calling from_dict on the json representation
        get_allowlist_response_model_dict = GetAllowlistResponse.from_dict(get_allowlist_response_model_json).__dict__
        get_allowlist_response_model2 = GetAllowlistResponse(**get_allowlist_response_model_dict)

        # Verify the model instances are equivalent
        assert get_allowlist_response_model == get_allowlist_response_model2

        # Convert model instance back to dict and verify no loss of data
        get_allowlist_response_model_json2 = get_allowlist_response_model.to_dict()
        assert get_allowlist_response_model_json2 == get_allowlist_response_model_json

class TestModel_GetBackupInfoResponse():
    """
    Test Class for GetBackupInfoResponse
    """

    def test_get_backup_info_response_serialization(self):
        """
        Test serialization/deserialization for GetBackupInfoResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        backup_model = {} # Backup
        backup_model['id'] = 'crn:v1:bluemix:public:databases-for-elasticsearch:us-south:a/274074dce64e9c423ffc238516c755e1:afa742a3-6f83-4f6e-a06e-b5c501e9e87a:backup:87635880-b11c-4359-9d06-41fd9f90feaf'
        backup_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-elasticsearch:us-south:a/274074dce64e9c423ffc238516c755e1:afa742a3-6f83-4f6e-a06e-b5c501e9e87a::'
        backup_model['type'] = 'scheduled'
        backup_model['status'] = 'completed'
        backup_model['is_downloadable'] = False
        backup_model['is_restorable'] = True
        backup_model['download_link'] = 'https://securedownloadservice.com/backup-2018-02-28T19:25:12Z.tgz'
        backup_model['created_at'] = '2019-06-10T14:31:40Z'

        # Construct a json representation of a GetBackupInfoResponse model
        get_backup_info_response_model_json = {}
        get_backup_info_response_model_json['backup'] = backup_model

        # Construct a model instance of GetBackupInfoResponse by calling from_dict on the json representation
        get_backup_info_response_model = GetBackupInfoResponse.from_dict(get_backup_info_response_model_json)
        assert get_backup_info_response_model != False

        # Construct a model instance of GetBackupInfoResponse by calling from_dict on the json representation
        get_backup_info_response_model_dict = GetBackupInfoResponse.from_dict(get_backup_info_response_model_json).__dict__
        get_backup_info_response_model2 = GetBackupInfoResponse(**get_backup_info_response_model_dict)

        # Verify the model instances are equivalent
        assert get_backup_info_response_model == get_backup_info_response_model2

        # Convert model instance back to dict and verify no loss of data
        get_backup_info_response_model_json2 = get_backup_info_response_model.to_dict()
        assert get_backup_info_response_model_json2 == get_backup_info_response_model_json

class TestModel_GetConnectionResponse():
    """
    Test Class for GetConnectionResponse
    """

    def test_get_connection_response_serialization(self):
        """
        Test serialization/deserialization for GetConnectionResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        postgre_sql_connection_uri_model = {} # PostgreSQLConnectionURI
        postgre_sql_connection_uri_model['type'] = 'uri'
        postgre_sql_connection_uri_model['composed'] = ['testString']
        postgre_sql_connection_uri_model['scheme'] = 'testString'
        postgre_sql_connection_uri_model['hosts'] = [connection_host_model]
        postgre_sql_connection_uri_model['path'] = 'testString'
        postgre_sql_connection_uri_model['query_options'] = {'foo': 'bar'}
        postgre_sql_connection_uri_model['authentication'] = connection_authentication_model
        postgre_sql_connection_uri_model['certificate'] = connection_certificate_model
        postgre_sql_connection_uri_model['ssl'] = True
        postgre_sql_connection_uri_model['browser_accessible'] = True
        postgre_sql_connection_uri_model['database'] = 'testString'

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {'foo': 'bar'}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_certificate_model

        connection_model = {} # ConnectionPostgreSQLConnection
        connection_model['postgres'] = postgre_sql_connection_uri_model
        connection_model['cli'] = connection_cli_model

        # Construct a json representation of a GetConnectionResponse model
        get_connection_response_model_json = {}
        get_connection_response_model_json['connection'] = connection_model

        # Construct a model instance of GetConnectionResponse by calling from_dict on the json representation
        get_connection_response_model = GetConnectionResponse.from_dict(get_connection_response_model_json)
        assert get_connection_response_model != False

        # Construct a model instance of GetConnectionResponse by calling from_dict on the json representation
        get_connection_response_model_dict = GetConnectionResponse.from_dict(get_connection_response_model_json).__dict__
        get_connection_response_model2 = GetConnectionResponse(**get_connection_response_model_dict)

        # Verify the model instances are equivalent
        assert get_connection_response_model == get_connection_response_model2

        # Convert model instance back to dict and verify no loss of data
        get_connection_response_model_json2 = get_connection_response_model.to_dict()
        assert get_connection_response_model_json2 == get_connection_response_model_json

class TestModel_GetDefaultScalingGroupsResponse():
    """
    Test Class for GetDefaultScalingGroupsResponse
    """

    def test_get_default_scaling_groups_response_serialization(self):
        """
        Test serialization/deserialization for GetDefaultScalingGroupsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        group_members_model = {} # GroupMembers
        group_members_model['units'] = 'count'
        group_members_model['allocation_count'] = 2
        group_members_model['minimum_count'] = 2
        group_members_model['maximum_count'] = 20
        group_members_model['step_size_count'] = 1
        group_members_model['is_adjustable'] = True
        group_members_model['is_optional'] = False
        group_members_model['can_scale_down'] = False

        group_memory_model = {} # GroupMemory
        group_memory_model['units'] = 'mb'
        group_memory_model['allocation_mb'] = 12288
        group_memory_model['minimum_mb'] = 1024
        group_memory_model['maximum_mb'] = 114688
        group_memory_model['step_size_mb'] = 1024
        group_memory_model['is_adjustable'] = True
        group_memory_model['is_optional'] = False
        group_memory_model['can_scale_down'] = True

        group_cpu_model = {} # GroupCpu
        group_cpu_model['units'] = 'count'
        group_cpu_model['allocation_count'] = 2
        group_cpu_model['minimum_count'] = 2
        group_cpu_model['maximum_count'] = 32
        group_cpu_model['step_size_count'] = 2
        group_cpu_model['is_adjustable'] = False
        group_cpu_model['is_optional'] = False
        group_cpu_model['can_scale_down'] = True

        group_disk_model = {} # GroupDisk
        group_disk_model['units'] = 'mb'
        group_disk_model['allocation_mb'] = 10240
        group_disk_model['minimum_mb'] = 2048
        group_disk_model['maximum_mb'] = 4194304
        group_disk_model['step_size_mb'] = 2048
        group_disk_model['is_adjustable'] = True
        group_disk_model['is_optional'] = False
        group_disk_model['can_scale_down'] = False

        group_host_flavor_model = {} # GroupHostFlavor
        group_host_flavor_model['id'] = 'b3c.4x16.encrypted'
        group_host_flavor_model['name'] = '4x16'
        group_host_flavor_model['hosting_size'] = 'xs'

        group_model = {} # Group
        group_model['id'] = 'member'
        group_model['count'] = 2
        group_model['members'] = group_members_model
        group_model['memory'] = group_memory_model
        group_model['cpu'] = group_cpu_model
        group_model['disk'] = group_disk_model
        group_model['host_flavor'] = group_host_flavor_model

        # Construct a json representation of a GetDefaultScalingGroupsResponse model
        get_default_scaling_groups_response_model_json = {}
        get_default_scaling_groups_response_model_json['groups'] = [group_model]

        # Construct a model instance of GetDefaultScalingGroupsResponse by calling from_dict on the json representation
        get_default_scaling_groups_response_model = GetDefaultScalingGroupsResponse.from_dict(get_default_scaling_groups_response_model_json)
        assert get_default_scaling_groups_response_model != False

        # Construct a model instance of GetDefaultScalingGroupsResponse by calling from_dict on the json representation
        get_default_scaling_groups_response_model_dict = GetDefaultScalingGroupsResponse.from_dict(get_default_scaling_groups_response_model_json).__dict__
        get_default_scaling_groups_response_model2 = GetDefaultScalingGroupsResponse(**get_default_scaling_groups_response_model_dict)

        # Verify the model instances are equivalent
        assert get_default_scaling_groups_response_model == get_default_scaling_groups_response_model2

        # Convert model instance back to dict and verify no loss of data
        get_default_scaling_groups_response_model_json2 = get_default_scaling_groups_response_model.to_dict()
        assert get_default_scaling_groups_response_model_json2 == get_default_scaling_groups_response_model_json

class TestModel_GetDeploymentInfoResponse():
    """
    Test Class for GetDeploymentInfoResponse
    """

    def test_get_deployment_info_response_serialization(self):
        """
        Test serialization/deserialization for GetDeploymentInfoResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        deployment_model = {} # Deployment
        deployment_model['id'] = 'crn:v1:staging:public:databases-for-enterprisedb:us-south:a/b9552134280015ebfde430a819fa4bb3:5589ecbf-de5f-4eac-9917-df0dd7e706c8::'
        deployment_model['name'] = 'crn:v1:staging:public:databases-for-enterprisedb:us-south:a/b9552134280015ebfde430a819fa4bb3:5589ecbf-de5f-4eac-9917-df0dd7e706c8::'
        deployment_model['type'] = 'enterprisedb'
        deployment_model['platform'] = 'classic'
        deployment_model['platform_options'] = {'foo': 'bar'}
        deployment_model['version'] = '12'
        deployment_model['admin_usernames'] = {'key1': 'testString'}
        deployment_model['enable_public_endpoints'] = True
        deployment_model['enable_private_endpoints'] = False

        # Construct a json representation of a GetDeploymentInfoResponse model
        get_deployment_info_response_model_json = {}
        get_deployment_info_response_model_json['deployment'] = deployment_model

        # Construct a model instance of GetDeploymentInfoResponse by calling from_dict on the json representation
        get_deployment_info_response_model = GetDeploymentInfoResponse.from_dict(get_deployment_info_response_model_json)
        assert get_deployment_info_response_model != False

        # Construct a model instance of GetDeploymentInfoResponse by calling from_dict on the json representation
        get_deployment_info_response_model_dict = GetDeploymentInfoResponse.from_dict(get_deployment_info_response_model_json).__dict__
        get_deployment_info_response_model2 = GetDeploymentInfoResponse(**get_deployment_info_response_model_dict)

        # Verify the model instances are equivalent
        assert get_deployment_info_response_model == get_deployment_info_response_model2

        # Convert model instance back to dict and verify no loss of data
        get_deployment_info_response_model_json2 = get_deployment_info_response_model.to_dict()
        assert get_deployment_info_response_model_json2 == get_deployment_info_response_model_json

class TestModel_GetPITRDataResponse():
    """
    Test Class for GetPITRDataResponse
    """

    def test_get_pitr_data_response_serialization(self):
        """
        Test serialization/deserialization for GetPITRDataResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        point_in_time_recovery_data_model = {} # PointInTimeRecoveryData
        point_in_time_recovery_data_model['earliest_point_in_time_recovery_time'] = 'testString'

        # Construct a json representation of a GetPITRDataResponse model
        get_pitr_data_response_model_json = {}
        get_pitr_data_response_model_json['point_in_time_recovery_data'] = point_in_time_recovery_data_model

        # Construct a model instance of GetPITRDataResponse by calling from_dict on the json representation
        get_pitr_data_response_model = GetPITRDataResponse.from_dict(get_pitr_data_response_model_json)
        assert get_pitr_data_response_model != False

        # Construct a model instance of GetPITRDataResponse by calling from_dict on the json representation
        get_pitr_data_response_model_dict = GetPITRDataResponse.from_dict(get_pitr_data_response_model_json).__dict__
        get_pitr_data_response_model2 = GetPITRDataResponse(**get_pitr_data_response_model_dict)

        # Verify the model instances are equivalent
        assert get_pitr_data_response_model == get_pitr_data_response_model2

        # Convert model instance back to dict and verify no loss of data
        get_pitr_data_response_model_json2 = get_pitr_data_response_model.to_dict()
        assert get_pitr_data_response_model_json2 == get_pitr_data_response_model_json

class TestModel_GetTaskResponse():
    """
    Test Class for GetTaskResponse
    """

    def test_get_task_response_serialization(self):
        """
        Test serialization/deserialization for GetTaskResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f4-b5c96544393b'
        task_model['description'] = 'Backing up database on-demand'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = '2018-03-28T10:31:30Z'

        # Construct a json representation of a GetTaskResponse model
        get_task_response_model_json = {}
        get_task_response_model_json['task'] = task_model

        # Construct a model instance of GetTaskResponse by calling from_dict on the json representation
        get_task_response_model = GetTaskResponse.from_dict(get_task_response_model_json)
        assert get_task_response_model != False

        # Construct a model instance of GetTaskResponse by calling from_dict on the json representation
        get_task_response_model_dict = GetTaskResponse.from_dict(get_task_response_model_json).__dict__
        get_task_response_model2 = GetTaskResponse(**get_task_response_model_dict)

        # Verify the model instances are equivalent
        assert get_task_response_model == get_task_response_model2

        # Convert model instance back to dict and verify no loss of data
        get_task_response_model_json2 = get_task_response_model.to_dict()
        assert get_task_response_model_json2 == get_task_response_model_json

class TestModel_Group():
    """
    Test Class for Group
    """

    def test_group_serialization(self):
        """
        Test serialization/deserialization for Group
        """

        # Construct dict forms of any model objects needed in order to build this model.

        group_members_model = {} # GroupMembers
        group_members_model['units'] = 'count'
        group_members_model['allocation_count'] = 2
        group_members_model['minimum_count'] = 2
        group_members_model['maximum_count'] = 20
        group_members_model['step_size_count'] = 1
        group_members_model['is_adjustable'] = True
        group_members_model['is_optional'] = False
        group_members_model['can_scale_down'] = False

        group_memory_model = {} # GroupMemory
        group_memory_model['units'] = 'mb'
        group_memory_model['allocation_mb'] = 12288
        group_memory_model['minimum_mb'] = 1024
        group_memory_model['maximum_mb'] = 114688
        group_memory_model['step_size_mb'] = 1024
        group_memory_model['is_adjustable'] = True
        group_memory_model['is_optional'] = False
        group_memory_model['can_scale_down'] = True

        group_cpu_model = {} # GroupCpu
        group_cpu_model['units'] = 'count'
        group_cpu_model['allocation_count'] = 2
        group_cpu_model['minimum_count'] = 2
        group_cpu_model['maximum_count'] = 32
        group_cpu_model['step_size_count'] = 2
        group_cpu_model['is_adjustable'] = False
        group_cpu_model['is_optional'] = False
        group_cpu_model['can_scale_down'] = True

        group_disk_model = {} # GroupDisk
        group_disk_model['units'] = 'mb'
        group_disk_model['allocation_mb'] = 10240
        group_disk_model['minimum_mb'] = 2048
        group_disk_model['maximum_mb'] = 4194304
        group_disk_model['step_size_mb'] = 2048
        group_disk_model['is_adjustable'] = True
        group_disk_model['is_optional'] = False
        group_disk_model['can_scale_down'] = False

        group_host_flavor_model = {} # GroupHostFlavor
        group_host_flavor_model['id'] = 'b3c.4x16.encrypted'
        group_host_flavor_model['name'] = '4x16'
        group_host_flavor_model['hosting_size'] = 'xs'

        # Construct a json representation of a Group model
        group_model_json = {}
        group_model_json['id'] = 'member'
        group_model_json['count'] = 2
        group_model_json['members'] = group_members_model
        group_model_json['memory'] = group_memory_model
        group_model_json['cpu'] = group_cpu_model
        group_model_json['disk'] = group_disk_model
        group_model_json['host_flavor'] = group_host_flavor_model

        # Construct a model instance of Group by calling from_dict on the json representation
        group_model = Group.from_dict(group_model_json)
        assert group_model != False

        # Construct a model instance of Group by calling from_dict on the json representation
        group_model_dict = Group.from_dict(group_model_json).__dict__
        group_model2 = Group(**group_model_dict)

        # Verify the model instances are equivalent
        assert group_model == group_model2

        # Convert model instance back to dict and verify no loss of data
        group_model_json2 = group_model.to_dict()
        assert group_model_json2 == group_model_json

class TestModel_GroupCpu():
    """
    Test Class for GroupCpu
    """

    def test_group_cpu_serialization(self):
        """
        Test serialization/deserialization for GroupCpu
        """

        # Construct a json representation of a GroupCpu model
        group_cpu_model_json = {}
        group_cpu_model_json['units'] = 'count'
        group_cpu_model_json['allocation_count'] = 2
        group_cpu_model_json['minimum_count'] = 2
        group_cpu_model_json['maximum_count'] = 32
        group_cpu_model_json['step_size_count'] = 2
        group_cpu_model_json['is_adjustable'] = False
        group_cpu_model_json['is_optional'] = False
        group_cpu_model_json['can_scale_down'] = True

        # Construct a model instance of GroupCpu by calling from_dict on the json representation
        group_cpu_model = GroupCpu.from_dict(group_cpu_model_json)
        assert group_cpu_model != False

        # Construct a model instance of GroupCpu by calling from_dict on the json representation
        group_cpu_model_dict = GroupCpu.from_dict(group_cpu_model_json).__dict__
        group_cpu_model2 = GroupCpu(**group_cpu_model_dict)

        # Verify the model instances are equivalent
        assert group_cpu_model == group_cpu_model2

        # Convert model instance back to dict and verify no loss of data
        group_cpu_model_json2 = group_cpu_model.to_dict()
        assert group_cpu_model_json2 == group_cpu_model_json

class TestModel_GroupDisk():
    """
    Test Class for GroupDisk
    """

    def test_group_disk_serialization(self):
        """
        Test serialization/deserialization for GroupDisk
        """

        # Construct a json representation of a GroupDisk model
        group_disk_model_json = {}
        group_disk_model_json['units'] = 'mb'
        group_disk_model_json['allocation_mb'] = 10240
        group_disk_model_json['minimum_mb'] = 2048
        group_disk_model_json['maximum_mb'] = 4194304
        group_disk_model_json['step_size_mb'] = 2048
        group_disk_model_json['is_adjustable'] = True
        group_disk_model_json['is_optional'] = False
        group_disk_model_json['can_scale_down'] = False

        # Construct a model instance of GroupDisk by calling from_dict on the json representation
        group_disk_model = GroupDisk.from_dict(group_disk_model_json)
        assert group_disk_model != False

        # Construct a model instance of GroupDisk by calling from_dict on the json representation
        group_disk_model_dict = GroupDisk.from_dict(group_disk_model_json).__dict__
        group_disk_model2 = GroupDisk(**group_disk_model_dict)

        # Verify the model instances are equivalent
        assert group_disk_model == group_disk_model2

        # Convert model instance back to dict and verify no loss of data
        group_disk_model_json2 = group_disk_model.to_dict()
        assert group_disk_model_json2 == group_disk_model_json

class TestModel_GroupHostFlavor():
    """
    Test Class for GroupHostFlavor
    """

    def test_group_host_flavor_serialization(self):
        """
        Test serialization/deserialization for GroupHostFlavor
        """

        # Construct a json representation of a GroupHostFlavor model
        group_host_flavor_model_json = {}
        group_host_flavor_model_json['id'] = 'b3c.4x16.encrypted'
        group_host_flavor_model_json['name'] = '4x16'
        group_host_flavor_model_json['hosting_size'] = 'xs'

        # Construct a model instance of GroupHostFlavor by calling from_dict on the json representation
        group_host_flavor_model = GroupHostFlavor.from_dict(group_host_flavor_model_json)
        assert group_host_flavor_model != False

        # Construct a model instance of GroupHostFlavor by calling from_dict on the json representation
        group_host_flavor_model_dict = GroupHostFlavor.from_dict(group_host_flavor_model_json).__dict__
        group_host_flavor_model2 = GroupHostFlavor(**group_host_flavor_model_dict)

        # Verify the model instances are equivalent
        assert group_host_flavor_model == group_host_flavor_model2

        # Convert model instance back to dict and verify no loss of data
        group_host_flavor_model_json2 = group_host_flavor_model.to_dict()
        assert group_host_flavor_model_json2 == group_host_flavor_model_json

class TestModel_GroupMembers():
    """
    Test Class for GroupMembers
    """

    def test_group_members_serialization(self):
        """
        Test serialization/deserialization for GroupMembers
        """

        # Construct a json representation of a GroupMembers model
        group_members_model_json = {}
        group_members_model_json['units'] = 'count'
        group_members_model_json['allocation_count'] = 2
        group_members_model_json['minimum_count'] = 2
        group_members_model_json['maximum_count'] = 20
        group_members_model_json['step_size_count'] = 1
        group_members_model_json['is_adjustable'] = True
        group_members_model_json['is_optional'] = False
        group_members_model_json['can_scale_down'] = False

        # Construct a model instance of GroupMembers by calling from_dict on the json representation
        group_members_model = GroupMembers.from_dict(group_members_model_json)
        assert group_members_model != False

        # Construct a model instance of GroupMembers by calling from_dict on the json representation
        group_members_model_dict = GroupMembers.from_dict(group_members_model_json).__dict__
        group_members_model2 = GroupMembers(**group_members_model_dict)

        # Verify the model instances are equivalent
        assert group_members_model == group_members_model2

        # Convert model instance back to dict and verify no loss of data
        group_members_model_json2 = group_members_model.to_dict()
        assert group_members_model_json2 == group_members_model_json

class TestModel_GroupMemory():
    """
    Test Class for GroupMemory
    """

    def test_group_memory_serialization(self):
        """
        Test serialization/deserialization for GroupMemory
        """

        # Construct a json representation of a GroupMemory model
        group_memory_model_json = {}
        group_memory_model_json['units'] = 'mb'
        group_memory_model_json['allocation_mb'] = 12288
        group_memory_model_json['minimum_mb'] = 1024
        group_memory_model_json['maximum_mb'] = 114688
        group_memory_model_json['step_size_mb'] = 1024
        group_memory_model_json['is_adjustable'] = True
        group_memory_model_json['is_optional'] = False
        group_memory_model_json['can_scale_down'] = True

        # Construct a model instance of GroupMemory by calling from_dict on the json representation
        group_memory_model = GroupMemory.from_dict(group_memory_model_json)
        assert group_memory_model != False

        # Construct a model instance of GroupMemory by calling from_dict on the json representation
        group_memory_model_dict = GroupMemory.from_dict(group_memory_model_json).__dict__
        group_memory_model2 = GroupMemory(**group_memory_model_dict)

        # Verify the model instances are equivalent
        assert group_memory_model == group_memory_model2

        # Convert model instance back to dict and verify no loss of data
        group_memory_model_json2 = group_memory_model.to_dict()
        assert group_memory_model_json2 == group_memory_model_json

class TestModel_GroupScaling():
    """
    Test Class for GroupScaling
    """

    def test_group_scaling_serialization(self):
        """
        Test serialization/deserialization for GroupScaling
        """

        # Construct dict forms of any model objects needed in order to build this model.

        group_scaling_members_model = {} # GroupScalingMembers
        group_scaling_members_model['allocation_count'] = 4

        group_scaling_memory_model = {} # GroupScalingMemory
        group_scaling_memory_model['allocation_mb'] = 12288

        group_scaling_cpu_model = {} # GroupScalingCpu
        group_scaling_cpu_model['allocation_count'] = 2

        group_scaling_disk_model = {} # GroupScalingDisk
        group_scaling_disk_model['allocation_mb'] = 20480

        group_scaling_host_flavor_model = {} # GroupScalingHostFlavor
        group_scaling_host_flavor_model['id'] = 'b3c.16x64.encrypted'

        # Construct a json representation of a GroupScaling model
        group_scaling_model_json = {}
        group_scaling_model_json['members'] = group_scaling_members_model
        group_scaling_model_json['memory'] = group_scaling_memory_model
        group_scaling_model_json['cpu'] = group_scaling_cpu_model
        group_scaling_model_json['disk'] = group_scaling_disk_model
        group_scaling_model_json['host_flavor'] = group_scaling_host_flavor_model

        # Construct a model instance of GroupScaling by calling from_dict on the json representation
        group_scaling_model = GroupScaling.from_dict(group_scaling_model_json)
        assert group_scaling_model != False

        # Construct a model instance of GroupScaling by calling from_dict on the json representation
        group_scaling_model_dict = GroupScaling.from_dict(group_scaling_model_json).__dict__
        group_scaling_model2 = GroupScaling(**group_scaling_model_dict)

        # Verify the model instances are equivalent
        assert group_scaling_model == group_scaling_model2

        # Convert model instance back to dict and verify no loss of data
        group_scaling_model_json2 = group_scaling_model.to_dict()
        assert group_scaling_model_json2 == group_scaling_model_json

class TestModel_GroupScalingCpu():
    """
    Test Class for GroupScalingCpu
    """

    def test_group_scaling_cpu_serialization(self):
        """
        Test serialization/deserialization for GroupScalingCpu
        """

        # Construct a json representation of a GroupScalingCpu model
        group_scaling_cpu_model_json = {}
        group_scaling_cpu_model_json['allocation_count'] = 2

        # Construct a model instance of GroupScalingCpu by calling from_dict on the json representation
        group_scaling_cpu_model = GroupScalingCpu.from_dict(group_scaling_cpu_model_json)
        assert group_scaling_cpu_model != False

        # Construct a model instance of GroupScalingCpu by calling from_dict on the json representation
        group_scaling_cpu_model_dict = GroupScalingCpu.from_dict(group_scaling_cpu_model_json).__dict__
        group_scaling_cpu_model2 = GroupScalingCpu(**group_scaling_cpu_model_dict)

        # Verify the model instances are equivalent
        assert group_scaling_cpu_model == group_scaling_cpu_model2

        # Convert model instance back to dict and verify no loss of data
        group_scaling_cpu_model_json2 = group_scaling_cpu_model.to_dict()
        assert group_scaling_cpu_model_json2 == group_scaling_cpu_model_json

class TestModel_GroupScalingDisk():
    """
    Test Class for GroupScalingDisk
    """

    def test_group_scaling_disk_serialization(self):
        """
        Test serialization/deserialization for GroupScalingDisk
        """

        # Construct a json representation of a GroupScalingDisk model
        group_scaling_disk_model_json = {}
        group_scaling_disk_model_json['allocation_mb'] = 20480

        # Construct a model instance of GroupScalingDisk by calling from_dict on the json representation
        group_scaling_disk_model = GroupScalingDisk.from_dict(group_scaling_disk_model_json)
        assert group_scaling_disk_model != False

        # Construct a model instance of GroupScalingDisk by calling from_dict on the json representation
        group_scaling_disk_model_dict = GroupScalingDisk.from_dict(group_scaling_disk_model_json).__dict__
        group_scaling_disk_model2 = GroupScalingDisk(**group_scaling_disk_model_dict)

        # Verify the model instances are equivalent
        assert group_scaling_disk_model == group_scaling_disk_model2

        # Convert model instance back to dict and verify no loss of data
        group_scaling_disk_model_json2 = group_scaling_disk_model.to_dict()
        assert group_scaling_disk_model_json2 == group_scaling_disk_model_json

class TestModel_GroupScalingHostFlavor():
    """
    Test Class for GroupScalingHostFlavor
    """

    def test_group_scaling_host_flavor_serialization(self):
        """
        Test serialization/deserialization for GroupScalingHostFlavor
        """

        # Construct a json representation of a GroupScalingHostFlavor model
        group_scaling_host_flavor_model_json = {}
        group_scaling_host_flavor_model_json['id'] = 'b3c.16x64.encrypted'

        # Construct a model instance of GroupScalingHostFlavor by calling from_dict on the json representation
        group_scaling_host_flavor_model = GroupScalingHostFlavor.from_dict(group_scaling_host_flavor_model_json)
        assert group_scaling_host_flavor_model != False

        # Construct a model instance of GroupScalingHostFlavor by calling from_dict on the json representation
        group_scaling_host_flavor_model_dict = GroupScalingHostFlavor.from_dict(group_scaling_host_flavor_model_json).__dict__
        group_scaling_host_flavor_model2 = GroupScalingHostFlavor(**group_scaling_host_flavor_model_dict)

        # Verify the model instances are equivalent
        assert group_scaling_host_flavor_model == group_scaling_host_flavor_model2

        # Convert model instance back to dict and verify no loss of data
        group_scaling_host_flavor_model_json2 = group_scaling_host_flavor_model.to_dict()
        assert group_scaling_host_flavor_model_json2 == group_scaling_host_flavor_model_json

class TestModel_GroupScalingMembers():
    """
    Test Class for GroupScalingMembers
    """

    def test_group_scaling_members_serialization(self):
        """
        Test serialization/deserialization for GroupScalingMembers
        """

        # Construct a json representation of a GroupScalingMembers model
        group_scaling_members_model_json = {}
        group_scaling_members_model_json['allocation_count'] = 4

        # Construct a model instance of GroupScalingMembers by calling from_dict on the json representation
        group_scaling_members_model = GroupScalingMembers.from_dict(group_scaling_members_model_json)
        assert group_scaling_members_model != False

        # Construct a model instance of GroupScalingMembers by calling from_dict on the json representation
        group_scaling_members_model_dict = GroupScalingMembers.from_dict(group_scaling_members_model_json).__dict__
        group_scaling_members_model2 = GroupScalingMembers(**group_scaling_members_model_dict)

        # Verify the model instances are equivalent
        assert group_scaling_members_model == group_scaling_members_model2

        # Convert model instance back to dict and verify no loss of data
        group_scaling_members_model_json2 = group_scaling_members_model.to_dict()
        assert group_scaling_members_model_json2 == group_scaling_members_model_json

class TestModel_GroupScalingMemory():
    """
    Test Class for GroupScalingMemory
    """

    def test_group_scaling_memory_serialization(self):
        """
        Test serialization/deserialization for GroupScalingMemory
        """

        # Construct a json representation of a GroupScalingMemory model
        group_scaling_memory_model_json = {}
        group_scaling_memory_model_json['allocation_mb'] = 12288

        # Construct a model instance of GroupScalingMemory by calling from_dict on the json representation
        group_scaling_memory_model = GroupScalingMemory.from_dict(group_scaling_memory_model_json)
        assert group_scaling_memory_model != False

        # Construct a model instance of GroupScalingMemory by calling from_dict on the json representation
        group_scaling_memory_model_dict = GroupScalingMemory.from_dict(group_scaling_memory_model_json).__dict__
        group_scaling_memory_model2 = GroupScalingMemory(**group_scaling_memory_model_dict)

        # Verify the model instances are equivalent
        assert group_scaling_memory_model == group_scaling_memory_model2

        # Convert model instance back to dict and verify no loss of data
        group_scaling_memory_model_json2 = group_scaling_memory_model.to_dict()
        assert group_scaling_memory_model_json2 == group_scaling_memory_model_json

class TestModel_KillConnectionsResponse():
    """
    Test Class for KillConnectionsResponse
    """

    def test_kill_connections_response_serialization(self):
        """
        Test serialization/deserialization for KillConnectionsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0c59-4db6-92f3-b5c96544393b'
        task_model['description'] = 'Killing all database connections.'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = '2018-03-28T10:31:30Z'

        # Construct a json representation of a KillConnectionsResponse model
        kill_connections_response_model_json = {}
        kill_connections_response_model_json['task'] = task_model

        # Construct a model instance of KillConnectionsResponse by calling from_dict on the json representation
        kill_connections_response_model = KillConnectionsResponse.from_dict(kill_connections_response_model_json)
        assert kill_connections_response_model != False

        # Construct a model instance of KillConnectionsResponse by calling from_dict on the json representation
        kill_connections_response_model_dict = KillConnectionsResponse.from_dict(kill_connections_response_model_json).__dict__
        kill_connections_response_model2 = KillConnectionsResponse(**kill_connections_response_model_dict)

        # Verify the model instances are equivalent
        assert kill_connections_response_model == kill_connections_response_model2

        # Convert model instance back to dict and verify no loss of data
        kill_connections_response_model_json2 = kill_connections_response_model.to_dict()
        assert kill_connections_response_model_json2 == kill_connections_response_model_json

class TestModel_ListDeployablesResponse():
    """
    Test Class for ListDeployablesResponse
    """

    def test_list_deployables_response_serialization(self):
        """
        Test serialization/deserialization for ListDeployablesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        deployables_versions_item_transitions_item_model = {} # DeployablesVersionsItemTransitionsItem
        deployables_versions_item_transitions_item_model['application'] = 'elasticsearch'
        deployables_versions_item_transitions_item_model['method'] = 'restore'
        deployables_versions_item_transitions_item_model['from_version'] = '5.6'
        deployables_versions_item_transitions_item_model['to_version'] = '6.7'

        deployables_versions_item_model = {} # DeployablesVersionsItem
        deployables_versions_item_model['version'] = '6.7'
        deployables_versions_item_model['status'] = 'stable'
        deployables_versions_item_model['is_preferred'] = True
        deployables_versions_item_model['transitions'] = [deployables_versions_item_transitions_item_model]

        deployables_model = {} # Deployables
        deployables_model['type'] = 'elasticsearch'
        deployables_model['versions'] = [deployables_versions_item_model]

        # Construct a json representation of a ListDeployablesResponse model
        list_deployables_response_model_json = {}
        list_deployables_response_model_json['deployables'] = [deployables_model]

        # Construct a model instance of ListDeployablesResponse by calling from_dict on the json representation
        list_deployables_response_model = ListDeployablesResponse.from_dict(list_deployables_response_model_json)
        assert list_deployables_response_model != False

        # Construct a model instance of ListDeployablesResponse by calling from_dict on the json representation
        list_deployables_response_model_dict = ListDeployablesResponse.from_dict(list_deployables_response_model_json).__dict__
        list_deployables_response_model2 = ListDeployablesResponse(**list_deployables_response_model_dict)

        # Verify the model instances are equivalent
        assert list_deployables_response_model == list_deployables_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_deployables_response_model_json2 = list_deployables_response_model.to_dict()
        assert list_deployables_response_model_json2 == list_deployables_response_model_json

class TestModel_ListDeploymentScalingGroupsResponse():
    """
    Test Class for ListDeploymentScalingGroupsResponse
    """

    def test_list_deployment_scaling_groups_response_serialization(self):
        """
        Test serialization/deserialization for ListDeploymentScalingGroupsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        group_members_model = {} # GroupMembers
        group_members_model['units'] = 'count'
        group_members_model['allocation_count'] = 2
        group_members_model['minimum_count'] = 2
        group_members_model['maximum_count'] = 20
        group_members_model['step_size_count'] = 1
        group_members_model['is_adjustable'] = True
        group_members_model['is_optional'] = False
        group_members_model['can_scale_down'] = False

        group_memory_model = {} # GroupMemory
        group_memory_model['units'] = 'mb'
        group_memory_model['allocation_mb'] = 12288
        group_memory_model['minimum_mb'] = 1024
        group_memory_model['maximum_mb'] = 114688
        group_memory_model['step_size_mb'] = 1024
        group_memory_model['is_adjustable'] = True
        group_memory_model['is_optional'] = False
        group_memory_model['can_scale_down'] = True

        group_cpu_model = {} # GroupCpu
        group_cpu_model['units'] = 'count'
        group_cpu_model['allocation_count'] = 2
        group_cpu_model['minimum_count'] = 2
        group_cpu_model['maximum_count'] = 32
        group_cpu_model['step_size_count'] = 2
        group_cpu_model['is_adjustable'] = False
        group_cpu_model['is_optional'] = False
        group_cpu_model['can_scale_down'] = True

        group_disk_model = {} # GroupDisk
        group_disk_model['units'] = 'mb'
        group_disk_model['allocation_mb'] = 10240
        group_disk_model['minimum_mb'] = 2048
        group_disk_model['maximum_mb'] = 4194304
        group_disk_model['step_size_mb'] = 2048
        group_disk_model['is_adjustable'] = True
        group_disk_model['is_optional'] = False
        group_disk_model['can_scale_down'] = False

        group_host_flavor_model = {} # GroupHostFlavor
        group_host_flavor_model['id'] = 'b3c.4x16.encrypted'
        group_host_flavor_model['name'] = '4x16'
        group_host_flavor_model['hosting_size'] = 'xs'

        group_model = {} # Group
        group_model['id'] = 'member'
        group_model['count'] = 2
        group_model['members'] = group_members_model
        group_model['memory'] = group_memory_model
        group_model['cpu'] = group_cpu_model
        group_model['disk'] = group_disk_model
        group_model['host_flavor'] = group_host_flavor_model

        # Construct a json representation of a ListDeploymentScalingGroupsResponse model
        list_deployment_scaling_groups_response_model_json = {}
        list_deployment_scaling_groups_response_model_json['groups'] = [group_model]

        # Construct a model instance of ListDeploymentScalingGroupsResponse by calling from_dict on the json representation
        list_deployment_scaling_groups_response_model = ListDeploymentScalingGroupsResponse.from_dict(list_deployment_scaling_groups_response_model_json)
        assert list_deployment_scaling_groups_response_model != False

        # Construct a model instance of ListDeploymentScalingGroupsResponse by calling from_dict on the json representation
        list_deployment_scaling_groups_response_model_dict = ListDeploymentScalingGroupsResponse.from_dict(list_deployment_scaling_groups_response_model_json).__dict__
        list_deployment_scaling_groups_response_model2 = ListDeploymentScalingGroupsResponse(**list_deployment_scaling_groups_response_model_dict)

        # Verify the model instances are equivalent
        assert list_deployment_scaling_groups_response_model == list_deployment_scaling_groups_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_deployment_scaling_groups_response_model_json2 = list_deployment_scaling_groups_response_model.to_dict()
        assert list_deployment_scaling_groups_response_model_json2 == list_deployment_scaling_groups_response_model_json

class TestModel_ListRegionsResponse():
    """
    Test Class for ListRegionsResponse
    """

    def test_list_regions_response_serialization(self):
        """
        Test serialization/deserialization for ListRegionsResponse
        """

        # Construct a json representation of a ListRegionsResponse model
        list_regions_response_model_json = {}
        list_regions_response_model_json['regions'] = ['testString']

        # Construct a model instance of ListRegionsResponse by calling from_dict on the json representation
        list_regions_response_model = ListRegionsResponse.from_dict(list_regions_response_model_json)
        assert list_regions_response_model != False

        # Construct a model instance of ListRegionsResponse by calling from_dict on the json representation
        list_regions_response_model_dict = ListRegionsResponse.from_dict(list_regions_response_model_json).__dict__
        list_regions_response_model2 = ListRegionsResponse(**list_regions_response_model_dict)

        # Verify the model instances are equivalent
        assert list_regions_response_model == list_regions_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_regions_response_model_json2 = list_regions_response_model.to_dict()
        assert list_regions_response_model_json2 == list_regions_response_model_json

class TestModel_ListRemotesResponse():
    """
    Test Class for ListRemotesResponse
    """

    def test_list_remotes_response_serialization(self):
        """
        Test serialization/deserialization for ListRemotesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        remotes_model = {} # Remotes
        remotes_model['leader'] = 'testString'
        remotes_model['replicas'] = ['crn:v1:bluemix:public:databases-for-postgresql:us-south:a/389574dce64e9c423ffc238516c755e1:0e399ae3-4a1a-476d-b85b-755c7af54788::']

        # Construct a json representation of a ListRemotesResponse model
        list_remotes_response_model_json = {}
        list_remotes_response_model_json['remotes'] = remotes_model

        # Construct a model instance of ListRemotesResponse by calling from_dict on the json representation
        list_remotes_response_model = ListRemotesResponse.from_dict(list_remotes_response_model_json)
        assert list_remotes_response_model != False

        # Construct a model instance of ListRemotesResponse by calling from_dict on the json representation
        list_remotes_response_model_dict = ListRemotesResponse.from_dict(list_remotes_response_model_json).__dict__
        list_remotes_response_model2 = ListRemotesResponse(**list_remotes_response_model_dict)

        # Verify the model instances are equivalent
        assert list_remotes_response_model == list_remotes_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_remotes_response_model_json2 = list_remotes_response_model.to_dict()
        assert list_remotes_response_model_json2 == list_remotes_response_model_json

class TestModel_LogicalReplicationSlot():
    """
    Test Class for LogicalReplicationSlot
    """

    def test_logical_replication_slot_serialization(self):
        """
        Test serialization/deserialization for LogicalReplicationSlot
        """

        # Construct a json representation of a LogicalReplicationSlot model
        logical_replication_slot_model_json = {}
        logical_replication_slot_model_json['name'] = 'customer_replication'
        logical_replication_slot_model_json['database_name'] = 'customers'
        logical_replication_slot_model_json['plugin_type'] = 'wal2json'

        # Construct a model instance of LogicalReplicationSlot by calling from_dict on the json representation
        logical_replication_slot_model = LogicalReplicationSlot.from_dict(logical_replication_slot_model_json)
        assert logical_replication_slot_model != False

        # Construct a model instance of LogicalReplicationSlot by calling from_dict on the json representation
        logical_replication_slot_model_dict = LogicalReplicationSlot.from_dict(logical_replication_slot_model_json).__dict__
        logical_replication_slot_model2 = LogicalReplicationSlot(**logical_replication_slot_model_dict)

        # Verify the model instances are equivalent
        assert logical_replication_slot_model == logical_replication_slot_model2

        # Convert model instance back to dict and verify no loss of data
        logical_replication_slot_model_json2 = logical_replication_slot_model.to_dict()
        assert logical_replication_slot_model_json2 == logical_replication_slot_model_json

class TestModel_MongoDBConnectionURI():
    """
    Test Class for MongoDBConnectionURI
    """

    def test_mongo_db_connection_uri_serialization(self):
        """
        Test serialization/deserialization for MongoDBConnectionURI
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a MongoDBConnectionURI model
        mongo_db_connection_uri_model_json = {}
        mongo_db_connection_uri_model_json['type'] = 'uri'
        mongo_db_connection_uri_model_json['composed'] = ['testString']
        mongo_db_connection_uri_model_json['scheme'] = 'testString'
        mongo_db_connection_uri_model_json['hosts'] = [connection_host_model]
        mongo_db_connection_uri_model_json['path'] = 'testString'
        mongo_db_connection_uri_model_json['query_options'] = {'foo': 'bar'}
        mongo_db_connection_uri_model_json['authentication'] = connection_authentication_model
        mongo_db_connection_uri_model_json['certificate'] = connection_certificate_model
        mongo_db_connection_uri_model_json['ssl'] = True
        mongo_db_connection_uri_model_json['browser_accessible'] = True
        mongo_db_connection_uri_model_json['database'] = 'testString'
        mongo_db_connection_uri_model_json['replica_set'] = 'testString'

        # Construct a model instance of MongoDBConnectionURI by calling from_dict on the json representation
        mongo_db_connection_uri_model = MongoDBConnectionURI.from_dict(mongo_db_connection_uri_model_json)
        assert mongo_db_connection_uri_model != False

        # Construct a model instance of MongoDBConnectionURI by calling from_dict on the json representation
        mongo_db_connection_uri_model_dict = MongoDBConnectionURI.from_dict(mongo_db_connection_uri_model_json).__dict__
        mongo_db_connection_uri_model2 = MongoDBConnectionURI(**mongo_db_connection_uri_model_dict)

        # Verify the model instances are equivalent
        assert mongo_db_connection_uri_model == mongo_db_connection_uri_model2

        # Convert model instance back to dict and verify no loss of data
        mongo_db_connection_uri_model_json2 = mongo_db_connection_uri_model.to_dict()
        assert mongo_db_connection_uri_model_json2 == mongo_db_connection_uri_model_json

class TestModel_MySQLConnectionURI():
    """
    Test Class for MySQLConnectionURI
    """

    def test_my_sql_connection_uri_serialization(self):
        """
        Test serialization/deserialization for MySQLConnectionURI
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a MySQLConnectionURI model
        my_sql_connection_uri_model_json = {}
        my_sql_connection_uri_model_json['type'] = 'uri'
        my_sql_connection_uri_model_json['composed'] = ['testString']
        my_sql_connection_uri_model_json['scheme'] = 'testString'
        my_sql_connection_uri_model_json['hosts'] = [connection_host_model]
        my_sql_connection_uri_model_json['path'] = 'testString'
        my_sql_connection_uri_model_json['query_options'] = {'foo': 'bar'}
        my_sql_connection_uri_model_json['authentication'] = connection_authentication_model
        my_sql_connection_uri_model_json['certificate'] = connection_certificate_model
        my_sql_connection_uri_model_json['ssl'] = True
        my_sql_connection_uri_model_json['browser_accessible'] = True
        my_sql_connection_uri_model_json['database'] = 'testString'

        # Construct a model instance of MySQLConnectionURI by calling from_dict on the json representation
        my_sql_connection_uri_model = MySQLConnectionURI.from_dict(my_sql_connection_uri_model_json)
        assert my_sql_connection_uri_model != False

        # Construct a model instance of MySQLConnectionURI by calling from_dict on the json representation
        my_sql_connection_uri_model_dict = MySQLConnectionURI.from_dict(my_sql_connection_uri_model_json).__dict__
        my_sql_connection_uri_model2 = MySQLConnectionURI(**my_sql_connection_uri_model_dict)

        # Verify the model instances are equivalent
        assert my_sql_connection_uri_model == my_sql_connection_uri_model2

        # Convert model instance back to dict and verify no loss of data
        my_sql_connection_uri_model_json2 = my_sql_connection_uri_model.to_dict()
        assert my_sql_connection_uri_model_json2 == my_sql_connection_uri_model_json

class TestModel_PointInTimeRecoveryData():
    """
    Test Class for PointInTimeRecoveryData
    """

    def test_point_in_time_recovery_data_serialization(self):
        """
        Test serialization/deserialization for PointInTimeRecoveryData
        """

        # Construct a json representation of a PointInTimeRecoveryData model
        point_in_time_recovery_data_model_json = {}
        point_in_time_recovery_data_model_json['earliest_point_in_time_recovery_time'] = 'testString'

        # Construct a model instance of PointInTimeRecoveryData by calling from_dict on the json representation
        point_in_time_recovery_data_model = PointInTimeRecoveryData.from_dict(point_in_time_recovery_data_model_json)
        assert point_in_time_recovery_data_model != False

        # Construct a model instance of PointInTimeRecoveryData by calling from_dict on the json representation
        point_in_time_recovery_data_model_dict = PointInTimeRecoveryData.from_dict(point_in_time_recovery_data_model_json).__dict__
        point_in_time_recovery_data_model2 = PointInTimeRecoveryData(**point_in_time_recovery_data_model_dict)

        # Verify the model instances are equivalent
        assert point_in_time_recovery_data_model == point_in_time_recovery_data_model2

        # Convert model instance back to dict and verify no loss of data
        point_in_time_recovery_data_model_json2 = point_in_time_recovery_data_model.to_dict()
        assert point_in_time_recovery_data_model_json2 == point_in_time_recovery_data_model_json

class TestModel_PostgreSQLConnectionURI():
    """
    Test Class for PostgreSQLConnectionURI
    """

    def test_postgre_sql_connection_uri_serialization(self):
        """
        Test serialization/deserialization for PostgreSQLConnectionURI
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a PostgreSQLConnectionURI model
        postgre_sql_connection_uri_model_json = {}
        postgre_sql_connection_uri_model_json['type'] = 'uri'
        postgre_sql_connection_uri_model_json['composed'] = ['testString']
        postgre_sql_connection_uri_model_json['scheme'] = 'testString'
        postgre_sql_connection_uri_model_json['hosts'] = [connection_host_model]
        postgre_sql_connection_uri_model_json['path'] = 'testString'
        postgre_sql_connection_uri_model_json['query_options'] = {'foo': 'bar'}
        postgre_sql_connection_uri_model_json['authentication'] = connection_authentication_model
        postgre_sql_connection_uri_model_json['certificate'] = connection_certificate_model
        postgre_sql_connection_uri_model_json['ssl'] = True
        postgre_sql_connection_uri_model_json['browser_accessible'] = True
        postgre_sql_connection_uri_model_json['database'] = 'testString'

        # Construct a model instance of PostgreSQLConnectionURI by calling from_dict on the json representation
        postgre_sql_connection_uri_model = PostgreSQLConnectionURI.from_dict(postgre_sql_connection_uri_model_json)
        assert postgre_sql_connection_uri_model != False

        # Construct a model instance of PostgreSQLConnectionURI by calling from_dict on the json representation
        postgre_sql_connection_uri_model_dict = PostgreSQLConnectionURI.from_dict(postgre_sql_connection_uri_model_json).__dict__
        postgre_sql_connection_uri_model2 = PostgreSQLConnectionURI(**postgre_sql_connection_uri_model_dict)

        # Verify the model instances are equivalent
        assert postgre_sql_connection_uri_model == postgre_sql_connection_uri_model2

        # Convert model instance back to dict and verify no loss of data
        postgre_sql_connection_uri_model_json2 = postgre_sql_connection_uri_model.to_dict()
        assert postgre_sql_connection_uri_model_json2 == postgre_sql_connection_uri_model_json

class TestModel_PromoteReadOnlyReplicaResponse():
    """
    Test Class for PromoteReadOnlyReplicaResponse
    """

    def test_promote_read_only_replica_response_serialization(self):
        """
        Test serialization/deserialization for PromoteReadOnlyReplicaResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc257516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:5abb6a7d11a1a5001479a0b0'
        task_model['description'] = 'Promoting read-only replica to standalone instance.'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc257516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = '2018-03-28T10:31:30Z'

        # Construct a json representation of a PromoteReadOnlyReplicaResponse model
        promote_read_only_replica_response_model_json = {}
        promote_read_only_replica_response_model_json['task'] = task_model

        # Construct a model instance of PromoteReadOnlyReplicaResponse by calling from_dict on the json representation
        promote_read_only_replica_response_model = PromoteReadOnlyReplicaResponse.from_dict(promote_read_only_replica_response_model_json)
        assert promote_read_only_replica_response_model != False

        # Construct a model instance of PromoteReadOnlyReplicaResponse by calling from_dict on the json representation
        promote_read_only_replica_response_model_dict = PromoteReadOnlyReplicaResponse.from_dict(promote_read_only_replica_response_model_json).__dict__
        promote_read_only_replica_response_model2 = PromoteReadOnlyReplicaResponse(**promote_read_only_replica_response_model_dict)

        # Verify the model instances are equivalent
        assert promote_read_only_replica_response_model == promote_read_only_replica_response_model2

        # Convert model instance back to dict and verify no loss of data
        promote_read_only_replica_response_model_json2 = promote_read_only_replica_response_model.to_dict()
        assert promote_read_only_replica_response_model_json2 == promote_read_only_replica_response_model_json

class TestModel_RedisConnectionURI():
    """
    Test Class for RedisConnectionURI
    """

    def test_redis_connection_uri_serialization(self):
        """
        Test serialization/deserialization for RedisConnectionURI
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        # Construct a json representation of a RedisConnectionURI model
        redis_connection_uri_model_json = {}
        redis_connection_uri_model_json['type'] = 'uri'
        redis_connection_uri_model_json['composed'] = ['testString']
        redis_connection_uri_model_json['scheme'] = 'testString'
        redis_connection_uri_model_json['hosts'] = [connection_host_model]
        redis_connection_uri_model_json['path'] = 'testString'
        redis_connection_uri_model_json['query_options'] = {'foo': 'bar'}
        redis_connection_uri_model_json['authentication'] = connection_authentication_model
        redis_connection_uri_model_json['certificate'] = connection_certificate_model
        redis_connection_uri_model_json['ssl'] = True
        redis_connection_uri_model_json['browser_accessible'] = True
        redis_connection_uri_model_json['database'] = 38

        # Construct a model instance of RedisConnectionURI by calling from_dict on the json representation
        redis_connection_uri_model = RedisConnectionURI.from_dict(redis_connection_uri_model_json)
        assert redis_connection_uri_model != False

        # Construct a model instance of RedisConnectionURI by calling from_dict on the json representation
        redis_connection_uri_model_dict = RedisConnectionURI.from_dict(redis_connection_uri_model_json).__dict__
        redis_connection_uri_model2 = RedisConnectionURI(**redis_connection_uri_model_dict)

        # Verify the model instances are equivalent
        assert redis_connection_uri_model == redis_connection_uri_model2

        # Convert model instance back to dict and verify no loss of data
        redis_connection_uri_model_json2 = redis_connection_uri_model.to_dict()
        assert redis_connection_uri_model_json2 == redis_connection_uri_model_json

class TestModel_Remotes():
    """
    Test Class for Remotes
    """

    def test_remotes_serialization(self):
        """
        Test serialization/deserialization for Remotes
        """

        # Construct a json representation of a Remotes model
        remotes_model_json = {}
        remotes_model_json['leader'] = '01f30581-54f8-41a4-8193-4a04cc022e9b-h'
        remotes_model_json['replicas'] = ['23h40521-57g6-31b5-9256-6b15df456f7j-g', 'g1d8g764-hngm-595j-7349450f3058-y']

        # Construct a model instance of Remotes by calling from_dict on the json representation
        remotes_model = Remotes.from_dict(remotes_model_json)
        assert remotes_model != False

        # Construct a model instance of Remotes by calling from_dict on the json representation
        remotes_model_dict = Remotes.from_dict(remotes_model_json).__dict__
        remotes_model2 = Remotes(**remotes_model_dict)

        # Verify the model instances are equivalent
        assert remotes_model == remotes_model2

        # Convert model instance back to dict and verify no loss of data
        remotes_model_json2 = remotes_model.to_dict()
        assert remotes_model_json2 == remotes_model_json

class TestModel_ResyncReplicaResponse():
    """
    Test Class for ResyncReplicaResponse
    """

    def test_resync_replica_response_serialization(self):
        """
        Test serialization/deserialization for ResyncReplicaResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc257516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:5abb6a7d11a1a5001479a0b0'
        task_model['description'] = 'Reinitializing read-only replica.'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc257516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = '2018-03-28T10:31:30Z'

        # Construct a json representation of a ResyncReplicaResponse model
        resync_replica_response_model_json = {}
        resync_replica_response_model_json['task'] = task_model

        # Construct a model instance of ResyncReplicaResponse by calling from_dict on the json representation
        resync_replica_response_model = ResyncReplicaResponse.from_dict(resync_replica_response_model_json)
        assert resync_replica_response_model != False

        # Construct a model instance of ResyncReplicaResponse by calling from_dict on the json representation
        resync_replica_response_model_dict = ResyncReplicaResponse.from_dict(resync_replica_response_model_json).__dict__
        resync_replica_response_model2 = ResyncReplicaResponse(**resync_replica_response_model_dict)

        # Verify the model instances are equivalent
        assert resync_replica_response_model == resync_replica_response_model2

        # Convert model instance back to dict and verify no loss of data
        resync_replica_response_model_json2 = resync_replica_response_model.to_dict()
        assert resync_replica_response_model_json2 == resync_replica_response_model_json

class TestModel_SetAllowlistResponse():
    """
    Test Class for SetAllowlistResponse
    """

    def test_set_allowlist_response_serialization(self):
        """
        Test serialization/deserialization for SetAllowlistResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f3-b5c96544573b'
        task_model['description'] = 'Updating allowlist for database'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 10
        task_model['created_at'] = '2018-03-28T10:21:30Z'

        # Construct a json representation of a SetAllowlistResponse model
        set_allowlist_response_model_json = {}
        set_allowlist_response_model_json['task'] = task_model

        # Construct a model instance of SetAllowlistResponse by calling from_dict on the json representation
        set_allowlist_response_model = SetAllowlistResponse.from_dict(set_allowlist_response_model_json)
        assert set_allowlist_response_model != False

        # Construct a model instance of SetAllowlistResponse by calling from_dict on the json representation
        set_allowlist_response_model_dict = SetAllowlistResponse.from_dict(set_allowlist_response_model_json).__dict__
        set_allowlist_response_model2 = SetAllowlistResponse(**set_allowlist_response_model_dict)

        # Verify the model instances are equivalent
        assert set_allowlist_response_model == set_allowlist_response_model2

        # Convert model instance back to dict and verify no loss of data
        set_allowlist_response_model_json2 = set_allowlist_response_model.to_dict()
        assert set_allowlist_response_model_json2 == set_allowlist_response_model_json

class TestModel_SetAutoscalingConditionsResponse():
    """
    Test Class for SetAutoscalingConditionsResponse
    """

    def test_set_autoscaling_conditions_response_serialization(self):
        """
        Test serialization/deserialization for SetAutoscalingConditionsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423a4ef238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4d36-92f3-b5c96544393b'
        task_model['description'] = 'Synthesized autoscaling'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 38
        task_model['created_at'] = '2019-10-17T14:15:52.393000Z'

        # Construct a json representation of a SetAutoscalingConditionsResponse model
        set_autoscaling_conditions_response_model_json = {}
        set_autoscaling_conditions_response_model_json['task'] = task_model

        # Construct a model instance of SetAutoscalingConditionsResponse by calling from_dict on the json representation
        set_autoscaling_conditions_response_model = SetAutoscalingConditionsResponse.from_dict(set_autoscaling_conditions_response_model_json)
        assert set_autoscaling_conditions_response_model != False

        # Construct a model instance of SetAutoscalingConditionsResponse by calling from_dict on the json representation
        set_autoscaling_conditions_response_model_dict = SetAutoscalingConditionsResponse.from_dict(set_autoscaling_conditions_response_model_json).__dict__
        set_autoscaling_conditions_response_model2 = SetAutoscalingConditionsResponse(**set_autoscaling_conditions_response_model_dict)

        # Verify the model instances are equivalent
        assert set_autoscaling_conditions_response_model == set_autoscaling_conditions_response_model2

        # Convert model instance back to dict and verify no loss of data
        set_autoscaling_conditions_response_model_json2 = set_autoscaling_conditions_response_model.to_dict()
        assert set_autoscaling_conditions_response_model_json2 == set_autoscaling_conditions_response_model_json

class TestModel_SetDeploymentScalingGroupResponse():
    """
    Test Class for SetDeploymentScalingGroupResponse
    """

    def test_set_deployment_scaling_group_response_serialization(self):
        """
        Test serialization/deserialization for SetDeploymentScalingGroupResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f4-b5c96544393b'
        task_model['description'] = 'Scaling database deployment'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = '2018-03-28T10:20:30Z'

        # Construct a json representation of a SetDeploymentScalingGroupResponse model
        set_deployment_scaling_group_response_model_json = {}
        set_deployment_scaling_group_response_model_json['task'] = task_model

        # Construct a model instance of SetDeploymentScalingGroupResponse by calling from_dict on the json representation
        set_deployment_scaling_group_response_model = SetDeploymentScalingGroupResponse.from_dict(set_deployment_scaling_group_response_model_json)
        assert set_deployment_scaling_group_response_model != False

        # Construct a model instance of SetDeploymentScalingGroupResponse by calling from_dict on the json representation
        set_deployment_scaling_group_response_model_dict = SetDeploymentScalingGroupResponse.from_dict(set_deployment_scaling_group_response_model_json).__dict__
        set_deployment_scaling_group_response_model2 = SetDeploymentScalingGroupResponse(**set_deployment_scaling_group_response_model_dict)

        # Verify the model instances are equivalent
        assert set_deployment_scaling_group_response_model == set_deployment_scaling_group_response_model2

        # Convert model instance back to dict and verify no loss of data
        set_deployment_scaling_group_response_model_json2 = set_deployment_scaling_group_response_model.to_dict()
        assert set_deployment_scaling_group_response_model_json2 == set_deployment_scaling_group_response_model_json

class TestModel_StartOndemandBackupResponse():
    """
    Test Class for StartOndemandBackupResponse
    """

    def test_start_ondemand_backup_response_serialization(self):
        """
        Test serialization/deserialization for StartOndemandBackupResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f4-b5c96544393b'
        task_model['description'] = 'Backing up database on-demand'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = '2018-03-28T10:30:30Z'

        # Construct a json representation of a StartOndemandBackupResponse model
        start_ondemand_backup_response_model_json = {}
        start_ondemand_backup_response_model_json['task'] = task_model

        # Construct a model instance of StartOndemandBackupResponse by calling from_dict on the json representation
        start_ondemand_backup_response_model = StartOndemandBackupResponse.from_dict(start_ondemand_backup_response_model_json)
        assert start_ondemand_backup_response_model != False

        # Construct a model instance of StartOndemandBackupResponse by calling from_dict on the json representation
        start_ondemand_backup_response_model_dict = StartOndemandBackupResponse.from_dict(start_ondemand_backup_response_model_json).__dict__
        start_ondemand_backup_response_model2 = StartOndemandBackupResponse(**start_ondemand_backup_response_model_dict)

        # Verify the model instances are equivalent
        assert start_ondemand_backup_response_model == start_ondemand_backup_response_model2

        # Convert model instance back to dict and verify no loss of data
        start_ondemand_backup_response_model_json2 = start_ondemand_backup_response_model.to_dict()
        assert start_ondemand_backup_response_model_json2 == start_ondemand_backup_response_model_json

class TestModel_Task():
    """
    Test Class for Task
    """

    def test_task_serialization(self):
        """
        Test serialization/deserialization for Task
        """

        # Construct a json representation of a Task model
        task_model_json = {}
        task_model_json['id'] = 'testString'
        task_model_json['description'] = 'testString'
        task_model_json['status'] = 'running'
        task_model_json['deployment_id'] = 'testString'
        task_model_json['progress_percent'] = 38
        task_model_json['created_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of Task by calling from_dict on the json representation
        task_model = Task.from_dict(task_model_json)
        assert task_model != False

        # Construct a model instance of Task by calling from_dict on the json representation
        task_model_dict = Task.from_dict(task_model_json).__dict__
        task_model2 = Task(**task_model_dict)

        # Verify the model instances are equivalent
        assert task_model == task_model2

        # Convert model instance back to dict and verify no loss of data
        task_model_json2 = task_model.to_dict()
        assert task_model_json2 == task_model_json

class TestModel_Tasks():
    """
    Test Class for Tasks
    """

    def test_tasks_serialization(self):
        """
        Test serialization/deserialization for Tasks
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f4-b5c96544393b'
        task_model['description'] = 'Backing up database on-demand'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = '2018-03-28T10:31:30Z'

        # Construct a json representation of a Tasks model
        tasks_model_json = {}
        tasks_model_json['tasks'] = [task_model]

        # Construct a model instance of Tasks by calling from_dict on the json representation
        tasks_model = Tasks.from_dict(tasks_model_json)
        assert tasks_model != False

        # Construct a model instance of Tasks by calling from_dict on the json representation
        tasks_model_dict = Tasks.from_dict(tasks_model_json).__dict__
        tasks_model2 = Tasks(**tasks_model_dict)

        # Verify the model instances are equivalent
        assert tasks_model == tasks_model2

        # Convert model instance back to dict and verify no loss of data
        tasks_model_json2 = tasks_model.to_dict()
        assert tasks_model_json2 == tasks_model_json

class TestModel_UpdateDatabaseConfigurationResponse():
    """
    Test Class for UpdateDatabaseConfigurationResponse
    """

    def test_update_database_configuration_response_serialization(self):
        """
        Test serialization/deserialization for UpdateDatabaseConfigurationResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f3-b5c96544393a'
        task_model['description'] = 'Applying new configuration'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = '2018-03-28T10:31:30Z'

        # Construct a json representation of a UpdateDatabaseConfigurationResponse model
        update_database_configuration_response_model_json = {}
        update_database_configuration_response_model_json['task'] = task_model

        # Construct a model instance of UpdateDatabaseConfigurationResponse by calling from_dict on the json representation
        update_database_configuration_response_model = UpdateDatabaseConfigurationResponse.from_dict(update_database_configuration_response_model_json)
        assert update_database_configuration_response_model != False

        # Construct a model instance of UpdateDatabaseConfigurationResponse by calling from_dict on the json representation
        update_database_configuration_response_model_dict = UpdateDatabaseConfigurationResponse.from_dict(update_database_configuration_response_model_json).__dict__
        update_database_configuration_response_model2 = UpdateDatabaseConfigurationResponse(**update_database_configuration_response_model_dict)

        # Verify the model instances are equivalent
        assert update_database_configuration_response_model == update_database_configuration_response_model2

        # Convert model instance back to dict and verify no loss of data
        update_database_configuration_response_model_json2 = update_database_configuration_response_model.to_dict()
        assert update_database_configuration_response_model_json2 == update_database_configuration_response_model_json

class TestModel_UpdateUserResponse():
    """
    Test Class for UpdateUserResponse
    """

    def test_update_user_response_serialization(self):
        """
        Test serialization/deserialization for UpdateUserResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        task_model = {} # Task
        task_model['id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd:task:3dc480bd-0cd9-4db6-92f3-b5c96544393b'
        task_model['description'] = 'Setting user password for database'
        task_model['status'] = 'running'
        task_model['deployment_id'] = 'crn:v1:bluemix:public:databases-for-postgresql:us-south:a/274074dce64e9c423ffc238516c755e1:a127f76a-98bf-4f8b-b263-01d9e16b15bd::'
        task_model['progress_percent'] = 5
        task_model['created_at'] = '2018-03-28T10:22:30Z'

        # Construct a json representation of a UpdateUserResponse model
        update_user_response_model_json = {}
        update_user_response_model_json['task'] = task_model

        # Construct a model instance of UpdateUserResponse by calling from_dict on the json representation
        update_user_response_model = UpdateUserResponse.from_dict(update_user_response_model_json)
        assert update_user_response_model != False

        # Construct a model instance of UpdateUserResponse by calling from_dict on the json representation
        update_user_response_model_dict = UpdateUserResponse.from_dict(update_user_response_model_json).__dict__
        update_user_response_model2 = UpdateUserResponse(**update_user_response_model_dict)

        # Verify the model instances are equivalent
        assert update_user_response_model == update_user_response_model2

        # Convert model instance back to dict and verify no loss of data
        update_user_response_model_json2 = update_user_response_model.to_dict()
        assert update_user_response_model_json2 == update_user_response_model_json

class TestModel_AutoscalingSetGroupAutoscalingAutoscalingCPUGroup():
    """
    Test Class for AutoscalingSetGroupAutoscalingAutoscalingCPUGroup
    """

    def test_autoscaling_set_group_autoscaling_autoscaling_cpu_group_serialization(self):
        """
        Test serialization/deserialization for AutoscalingSetGroupAutoscalingAutoscalingCPUGroup
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_cpu_group_cpu_rate_model = {} # AutoscalingCPUGroupCPURate
        autoscaling_cpu_group_cpu_rate_model['increase_percent'] = 10
        autoscaling_cpu_group_cpu_rate_model['period_seconds'] = 900
        autoscaling_cpu_group_cpu_rate_model['limit_count_per_member'] = 10
        autoscaling_cpu_group_cpu_rate_model['units'] = 'count'

        autoscaling_cpu_group_cpu_model = {} # AutoscalingCPUGroupCPU
        autoscaling_cpu_group_cpu_model['scalers'] = {'foo': 'bar'}
        autoscaling_cpu_group_cpu_model['rate'] = autoscaling_cpu_group_cpu_rate_model

        # Construct a json representation of a AutoscalingSetGroupAutoscalingAutoscalingCPUGroup model
        autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_json = {}
        autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_json['cpu'] = autoscaling_cpu_group_cpu_model

        # Construct a model instance of AutoscalingSetGroupAutoscalingAutoscalingCPUGroup by calling from_dict on the json representation
        autoscaling_set_group_autoscaling_autoscaling_cpu_group_model = AutoscalingSetGroupAutoscalingAutoscalingCPUGroup.from_dict(autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_json)
        assert autoscaling_set_group_autoscaling_autoscaling_cpu_group_model != False

        # Construct a model instance of AutoscalingSetGroupAutoscalingAutoscalingCPUGroup by calling from_dict on the json representation
        autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_dict = AutoscalingSetGroupAutoscalingAutoscalingCPUGroup.from_dict(autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_json).__dict__
        autoscaling_set_group_autoscaling_autoscaling_cpu_group_model2 = AutoscalingSetGroupAutoscalingAutoscalingCPUGroup(**autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_set_group_autoscaling_autoscaling_cpu_group_model == autoscaling_set_group_autoscaling_autoscaling_cpu_group_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_json2 = autoscaling_set_group_autoscaling_autoscaling_cpu_group_model.to_dict()
        assert autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_json2 == autoscaling_set_group_autoscaling_autoscaling_cpu_group_model_json

class TestModel_AutoscalingSetGroupAutoscalingAutoscalingDiskGroup():
    """
    Test Class for AutoscalingSetGroupAutoscalingAutoscalingDiskGroup
    """

    def test_autoscaling_set_group_autoscaling_autoscaling_disk_group_serialization(self):
        """
        Test serialization/deserialization for AutoscalingSetGroupAutoscalingAutoscalingDiskGroup
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_disk_group_disk_scalers_capacity_model = {} # AutoscalingDiskGroupDiskScalersCapacity
        autoscaling_disk_group_disk_scalers_capacity_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_capacity_model['free_space_less_than_percent'] = 10

        autoscaling_disk_group_disk_scalers_io_utilization_model = {} # AutoscalingDiskGroupDiskScalersIoUtilization
        autoscaling_disk_group_disk_scalers_io_utilization_model['enabled'] = True
        autoscaling_disk_group_disk_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_disk_group_disk_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_disk_group_disk_scalers_model = {} # AutoscalingDiskGroupDiskScalers
        autoscaling_disk_group_disk_scalers_model['capacity'] = autoscaling_disk_group_disk_scalers_capacity_model
        autoscaling_disk_group_disk_scalers_model['io_utilization'] = autoscaling_disk_group_disk_scalers_io_utilization_model

        autoscaling_disk_group_disk_rate_model = {} # AutoscalingDiskGroupDiskRate
        autoscaling_disk_group_disk_rate_model['increase_percent'] = 20
        autoscaling_disk_group_disk_rate_model['period_seconds'] = 900
        autoscaling_disk_group_disk_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_disk_group_disk_rate_model['units'] = 'mb'

        autoscaling_disk_group_disk_model = {} # AutoscalingDiskGroupDisk
        autoscaling_disk_group_disk_model['scalers'] = autoscaling_disk_group_disk_scalers_model
        autoscaling_disk_group_disk_model['rate'] = autoscaling_disk_group_disk_rate_model

        # Construct a json representation of a AutoscalingSetGroupAutoscalingAutoscalingDiskGroup model
        autoscaling_set_group_autoscaling_autoscaling_disk_group_model_json = {}
        autoscaling_set_group_autoscaling_autoscaling_disk_group_model_json['disk'] = autoscaling_disk_group_disk_model

        # Construct a model instance of AutoscalingSetGroupAutoscalingAutoscalingDiskGroup by calling from_dict on the json representation
        autoscaling_set_group_autoscaling_autoscaling_disk_group_model = AutoscalingSetGroupAutoscalingAutoscalingDiskGroup.from_dict(autoscaling_set_group_autoscaling_autoscaling_disk_group_model_json)
        assert autoscaling_set_group_autoscaling_autoscaling_disk_group_model != False

        # Construct a model instance of AutoscalingSetGroupAutoscalingAutoscalingDiskGroup by calling from_dict on the json representation
        autoscaling_set_group_autoscaling_autoscaling_disk_group_model_dict = AutoscalingSetGroupAutoscalingAutoscalingDiskGroup.from_dict(autoscaling_set_group_autoscaling_autoscaling_disk_group_model_json).__dict__
        autoscaling_set_group_autoscaling_autoscaling_disk_group_model2 = AutoscalingSetGroupAutoscalingAutoscalingDiskGroup(**autoscaling_set_group_autoscaling_autoscaling_disk_group_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_set_group_autoscaling_autoscaling_disk_group_model == autoscaling_set_group_autoscaling_autoscaling_disk_group_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_set_group_autoscaling_autoscaling_disk_group_model_json2 = autoscaling_set_group_autoscaling_autoscaling_disk_group_model.to_dict()
        assert autoscaling_set_group_autoscaling_autoscaling_disk_group_model_json2 == autoscaling_set_group_autoscaling_autoscaling_disk_group_model_json

class TestModel_AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup():
    """
    Test Class for AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup
    """

    def test_autoscaling_set_group_autoscaling_autoscaling_memory_group_serialization(self):
        """
        Test serialization/deserialization for AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup
        """

        # Construct dict forms of any model objects needed in order to build this model.

        autoscaling_memory_group_memory_scalers_io_utilization_model = {} # AutoscalingMemoryGroupMemoryScalersIoUtilization
        autoscaling_memory_group_memory_scalers_io_utilization_model['enabled'] = True
        autoscaling_memory_group_memory_scalers_io_utilization_model['over_period'] = '30m'
        autoscaling_memory_group_memory_scalers_io_utilization_model['above_percent'] = 45

        autoscaling_memory_group_memory_scalers_model = {} # AutoscalingMemoryGroupMemoryScalers
        autoscaling_memory_group_memory_scalers_model['io_utilization'] = autoscaling_memory_group_memory_scalers_io_utilization_model

        autoscaling_memory_group_memory_rate_model = {} # AutoscalingMemoryGroupMemoryRate
        autoscaling_memory_group_memory_rate_model['increase_percent'] = 10
        autoscaling_memory_group_memory_rate_model['period_seconds'] = 900
        autoscaling_memory_group_memory_rate_model['limit_mb_per_member'] = 3670016
        autoscaling_memory_group_memory_rate_model['units'] = 'mb'

        autoscaling_memory_group_memory_model = {} # AutoscalingMemoryGroupMemory
        autoscaling_memory_group_memory_model['scalers'] = autoscaling_memory_group_memory_scalers_model
        autoscaling_memory_group_memory_model['rate'] = autoscaling_memory_group_memory_rate_model

        # Construct a json representation of a AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup model
        autoscaling_set_group_autoscaling_autoscaling_memory_group_model_json = {}
        autoscaling_set_group_autoscaling_autoscaling_memory_group_model_json['memory'] = autoscaling_memory_group_memory_model

        # Construct a model instance of AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup by calling from_dict on the json representation
        autoscaling_set_group_autoscaling_autoscaling_memory_group_model = AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup.from_dict(autoscaling_set_group_autoscaling_autoscaling_memory_group_model_json)
        assert autoscaling_set_group_autoscaling_autoscaling_memory_group_model != False

        # Construct a model instance of AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup by calling from_dict on the json representation
        autoscaling_set_group_autoscaling_autoscaling_memory_group_model_dict = AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup.from_dict(autoscaling_set_group_autoscaling_autoscaling_memory_group_model_json).__dict__
        autoscaling_set_group_autoscaling_autoscaling_memory_group_model2 = AutoscalingSetGroupAutoscalingAutoscalingMemoryGroup(**autoscaling_set_group_autoscaling_autoscaling_memory_group_model_dict)

        # Verify the model instances are equivalent
        assert autoscaling_set_group_autoscaling_autoscaling_memory_group_model == autoscaling_set_group_autoscaling_autoscaling_memory_group_model2

        # Convert model instance back to dict and verify no loss of data
        autoscaling_set_group_autoscaling_autoscaling_memory_group_model_json2 = autoscaling_set_group_autoscaling_autoscaling_memory_group_model.to_dict()
        assert autoscaling_set_group_autoscaling_autoscaling_memory_group_model_json2 == autoscaling_set_group_autoscaling_autoscaling_memory_group_model_json

class TestModel_ConfigurationMySQLConfiguration():
    """
    Test Class for ConfigurationMySQLConfiguration
    """

    def test_configuration_my_sql_configuration_serialization(self):
        """
        Test serialization/deserialization for ConfigurationMySQLConfiguration
        """

        # Construct a json representation of a ConfigurationMySQLConfiguration model
        configuration_my_sql_configuration_model_json = {}
        configuration_my_sql_configuration_model_json['default_authentication_plugin'] = 'sha256_password'
        configuration_my_sql_configuration_model_json['innodb_buffer_pool_size_percentage'] = 10
        configuration_my_sql_configuration_model_json['innodb_flush_log_at_trx_commit'] = 0
        configuration_my_sql_configuration_model_json['innodb_log_buffer_size'] = 1048576
        configuration_my_sql_configuration_model_json['innodb_log_file_size'] = 4194304
        configuration_my_sql_configuration_model_json['innodb_lru_scan_depth'] = 128
        configuration_my_sql_configuration_model_json['innodb_read_io_threads'] = 1
        configuration_my_sql_configuration_model_json['innodb_write_io_threads'] = 1
        configuration_my_sql_configuration_model_json['max_allowed_packet'] = 1024
        configuration_my_sql_configuration_model_json['max_connections'] = 100
        configuration_my_sql_configuration_model_json['mysql_max_binlog_age_sec'] = 300
        configuration_my_sql_configuration_model_json['net_read_timeout'] = 1
        configuration_my_sql_configuration_model_json['net_write_timeout'] = 1
        configuration_my_sql_configuration_model_json['sql_mode'] = 'testString'
        configuration_my_sql_configuration_model_json['wait_timeout'] = 1
        configuration_my_sql_configuration_model_json['max_prepared_stmt_count'] = 0

        # Construct a model instance of ConfigurationMySQLConfiguration by calling from_dict on the json representation
        configuration_my_sql_configuration_model = ConfigurationMySQLConfiguration.from_dict(configuration_my_sql_configuration_model_json)
        assert configuration_my_sql_configuration_model != False

        # Construct a model instance of ConfigurationMySQLConfiguration by calling from_dict on the json representation
        configuration_my_sql_configuration_model_dict = ConfigurationMySQLConfiguration.from_dict(configuration_my_sql_configuration_model_json).__dict__
        configuration_my_sql_configuration_model2 = ConfigurationMySQLConfiguration(**configuration_my_sql_configuration_model_dict)

        # Verify the model instances are equivalent
        assert configuration_my_sql_configuration_model == configuration_my_sql_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        configuration_my_sql_configuration_model_json2 = configuration_my_sql_configuration_model.to_dict()
        assert configuration_my_sql_configuration_model_json2 == configuration_my_sql_configuration_model_json

class TestModel_ConfigurationPGConfiguration():
    """
    Test Class for ConfigurationPGConfiguration
    """

    def test_configuration_pg_configuration_serialization(self):
        """
        Test serialization/deserialization for ConfigurationPGConfiguration
        """

        # Construct a json representation of a ConfigurationPGConfiguration model
        configuration_pg_configuration_model_json = {}
        configuration_pg_configuration_model_json['archive_timeout'] = 300
        configuration_pg_configuration_model_json['deadlock_timeout'] = 100
        configuration_pg_configuration_model_json['effective_io_concurrency'] = 1
        configuration_pg_configuration_model_json['log_connections'] = 'off'
        configuration_pg_configuration_model_json['log_disconnections'] = 'off'
        configuration_pg_configuration_model_json['log_min_duration_statement'] = 100
        configuration_pg_configuration_model_json['max_connections'] = 115
        configuration_pg_configuration_model_json['max_prepared_transactions'] = 0
        configuration_pg_configuration_model_json['max_replication_slots'] = 10
        configuration_pg_configuration_model_json['max_wal_senders'] = 12
        configuration_pg_configuration_model_json['shared_buffers'] = 16
        configuration_pg_configuration_model_json['synchronous_commit'] = 'local'
        configuration_pg_configuration_model_json['tcp_keepalives_count'] = 0
        configuration_pg_configuration_model_json['tcp_keepalives_idle'] = 0
        configuration_pg_configuration_model_json['tcp_keepalives_interval'] = 0
        configuration_pg_configuration_model_json['wal_level'] = 'hot_standby'

        # Construct a model instance of ConfigurationPGConfiguration by calling from_dict on the json representation
        configuration_pg_configuration_model = ConfigurationPGConfiguration.from_dict(configuration_pg_configuration_model_json)
        assert configuration_pg_configuration_model != False

        # Construct a model instance of ConfigurationPGConfiguration by calling from_dict on the json representation
        configuration_pg_configuration_model_dict = ConfigurationPGConfiguration.from_dict(configuration_pg_configuration_model_json).__dict__
        configuration_pg_configuration_model2 = ConfigurationPGConfiguration(**configuration_pg_configuration_model_dict)

        # Verify the model instances are equivalent
        assert configuration_pg_configuration_model == configuration_pg_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        configuration_pg_configuration_model_json2 = configuration_pg_configuration_model.to_dict()
        assert configuration_pg_configuration_model_json2 == configuration_pg_configuration_model_json

class TestModel_ConfigurationRabbitMQConfiguration():
    """
    Test Class for ConfigurationRabbitMQConfiguration
    """

    def test_configuration_rabbit_mq_configuration_serialization(self):
        """
        Test serialization/deserialization for ConfigurationRabbitMQConfiguration
        """

        # Construct a json representation of a ConfigurationRabbitMQConfiguration model
        configuration_rabbit_mq_configuration_model_json = {}
        configuration_rabbit_mq_configuration_model_json['delete_undefined_queues'] = True

        # Construct a model instance of ConfigurationRabbitMQConfiguration by calling from_dict on the json representation
        configuration_rabbit_mq_configuration_model = ConfigurationRabbitMQConfiguration.from_dict(configuration_rabbit_mq_configuration_model_json)
        assert configuration_rabbit_mq_configuration_model != False

        # Construct a model instance of ConfigurationRabbitMQConfiguration by calling from_dict on the json representation
        configuration_rabbit_mq_configuration_model_dict = ConfigurationRabbitMQConfiguration.from_dict(configuration_rabbit_mq_configuration_model_json).__dict__
        configuration_rabbit_mq_configuration_model2 = ConfigurationRabbitMQConfiguration(**configuration_rabbit_mq_configuration_model_dict)

        # Verify the model instances are equivalent
        assert configuration_rabbit_mq_configuration_model == configuration_rabbit_mq_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        configuration_rabbit_mq_configuration_model_json2 = configuration_rabbit_mq_configuration_model.to_dict()
        assert configuration_rabbit_mq_configuration_model_json2 == configuration_rabbit_mq_configuration_model_json

class TestModel_ConfigurationRedisConfiguration():
    """
    Test Class for ConfigurationRedisConfiguration
    """

    def test_configuration_redis_configuration_serialization(self):
        """
        Test serialization/deserialization for ConfigurationRedisConfiguration
        """

        # Construct a json representation of a ConfigurationRedisConfiguration model
        configuration_redis_configuration_model_json = {}
        configuration_redis_configuration_model_json['maxmemory'] = 0
        configuration_redis_configuration_model_json['maxmemory-policy'] = 'volatile-lru'
        configuration_redis_configuration_model_json['appendonly'] = 'yes'
        configuration_redis_configuration_model_json['maxmemory-samples'] = 0
        configuration_redis_configuration_model_json['stop-writes-on-bgsave-error'] = 'yes'

        # Construct a model instance of ConfigurationRedisConfiguration by calling from_dict on the json representation
        configuration_redis_configuration_model = ConfigurationRedisConfiguration.from_dict(configuration_redis_configuration_model_json)
        assert configuration_redis_configuration_model != False

        # Construct a model instance of ConfigurationRedisConfiguration by calling from_dict on the json representation
        configuration_redis_configuration_model_dict = ConfigurationRedisConfiguration.from_dict(configuration_redis_configuration_model_json).__dict__
        configuration_redis_configuration_model2 = ConfigurationRedisConfiguration(**configuration_redis_configuration_model_dict)

        # Verify the model instances are equivalent
        assert configuration_redis_configuration_model == configuration_redis_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        configuration_redis_configuration_model_json2 = configuration_redis_configuration_model.to_dict()
        assert configuration_redis_configuration_model_json2 == configuration_redis_configuration_model_json

class TestModel_ConnectionDataStaxConnection():
    """
    Test Class for ConnectionDataStaxConnection
    """

    def test_connection_data_stax_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionDataStaxConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_bundle_model = {} # ConnectionBundle
        connection_bundle_model['name'] = 'testString'
        connection_bundle_model['bundle_base64'] = 'testString'

        data_stax_connection_uri_model = {} # DataStaxConnectionURI
        data_stax_connection_uri_model['hosts'] = [connection_host_model]
        data_stax_connection_uri_model['authentication'] = connection_authentication_model
        data_stax_connection_uri_model['bundle'] = connection_bundle_model

        # Construct a json representation of a ConnectionDataStaxConnection model
        connection_data_stax_connection_model_json = {}
        connection_data_stax_connection_model_json['secure'] = data_stax_connection_uri_model

        # Construct a model instance of ConnectionDataStaxConnection by calling from_dict on the json representation
        connection_data_stax_connection_model = ConnectionDataStaxConnection.from_dict(connection_data_stax_connection_model_json)
        assert connection_data_stax_connection_model != False

        # Construct a model instance of ConnectionDataStaxConnection by calling from_dict on the json representation
        connection_data_stax_connection_model_dict = ConnectionDataStaxConnection.from_dict(connection_data_stax_connection_model_json).__dict__
        connection_data_stax_connection_model2 = ConnectionDataStaxConnection(**connection_data_stax_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_data_stax_connection_model == connection_data_stax_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_data_stax_connection_model_json2 = connection_data_stax_connection_model.to_dict()
        assert connection_data_stax_connection_model_json2 == connection_data_stax_connection_model_json

class TestModel_ConnectionElasticsearchConnection():
    """
    Test Class for ConnectionElasticsearchConnection
    """

    def test_connection_elasticsearch_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionElasticsearchConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        connection_uri_model = {} # ConnectionURI
        connection_uri_model['type'] = 'uri'
        connection_uri_model['composed'] = ['testString']
        connection_uri_model['scheme'] = 'testString'
        connection_uri_model['hosts'] = [connection_host_model]
        connection_uri_model['path'] = 'testString'
        connection_uri_model['query_options'] = {'foo': 'bar'}
        connection_uri_model['authentication'] = connection_authentication_model
        connection_uri_model['certificate'] = connection_certificate_model
        connection_uri_model['ssl'] = True
        connection_uri_model['browser_accessible'] = True

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {'foo': 'bar'}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_certificate_model

        # Construct a json representation of a ConnectionElasticsearchConnection model
        connection_elasticsearch_connection_model_json = {}
        connection_elasticsearch_connection_model_json['https'] = connection_uri_model
        connection_elasticsearch_connection_model_json['cli'] = connection_cli_model

        # Construct a model instance of ConnectionElasticsearchConnection by calling from_dict on the json representation
        connection_elasticsearch_connection_model = ConnectionElasticsearchConnection.from_dict(connection_elasticsearch_connection_model_json)
        assert connection_elasticsearch_connection_model != False

        # Construct a model instance of ConnectionElasticsearchConnection by calling from_dict on the json representation
        connection_elasticsearch_connection_model_dict = ConnectionElasticsearchConnection.from_dict(connection_elasticsearch_connection_model_json).__dict__
        connection_elasticsearch_connection_model2 = ConnectionElasticsearchConnection(**connection_elasticsearch_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_elasticsearch_connection_model == connection_elasticsearch_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_elasticsearch_connection_model_json2 = connection_elasticsearch_connection_model.to_dict()
        assert connection_elasticsearch_connection_model_json2 == connection_elasticsearch_connection_model_json

class TestModel_ConnectionEnterpriseDBConnection():
    """
    Test Class for ConnectionEnterpriseDBConnection
    """

    def test_connection_enterprise_db_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionEnterpriseDBConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        postgre_sql_connection_uri_model = {} # PostgreSQLConnectionURI
        postgre_sql_connection_uri_model['type'] = 'uri'
        postgre_sql_connection_uri_model['composed'] = ['testString']
        postgre_sql_connection_uri_model['scheme'] = 'testString'
        postgre_sql_connection_uri_model['hosts'] = [connection_host_model]
        postgre_sql_connection_uri_model['path'] = 'testString'
        postgre_sql_connection_uri_model['query_options'] = {'foo': 'bar'}
        postgre_sql_connection_uri_model['authentication'] = connection_authentication_model
        postgre_sql_connection_uri_model['certificate'] = connection_certificate_model
        postgre_sql_connection_uri_model['ssl'] = True
        postgre_sql_connection_uri_model['browser_accessible'] = True
        postgre_sql_connection_uri_model['database'] = 'testString'

        connection_uri_model = {} # ConnectionURI
        connection_uri_model['type'] = 'uri'
        connection_uri_model['composed'] = ['testString']
        connection_uri_model['scheme'] = 'testString'
        connection_uri_model['hosts'] = [connection_host_model]
        connection_uri_model['path'] = 'testString'
        connection_uri_model['query_options'] = {'foo': 'bar'}
        connection_uri_model['authentication'] = connection_authentication_model
        connection_uri_model['certificate'] = connection_certificate_model
        connection_uri_model['ssl'] = True
        connection_uri_model['browser_accessible'] = True

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {'foo': 'bar'}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_certificate_model

        # Construct a json representation of a ConnectionEnterpriseDBConnection model
        connection_enterprise_db_connection_model_json = {}
        connection_enterprise_db_connection_model_json['postgres'] = postgre_sql_connection_uri_model
        connection_enterprise_db_connection_model_json['emp'] = connection_uri_model
        connection_enterprise_db_connection_model_json['cli'] = connection_cli_model

        # Construct a model instance of ConnectionEnterpriseDBConnection by calling from_dict on the json representation
        connection_enterprise_db_connection_model = ConnectionEnterpriseDBConnection.from_dict(connection_enterprise_db_connection_model_json)
        assert connection_enterprise_db_connection_model != False

        # Construct a model instance of ConnectionEnterpriseDBConnection by calling from_dict on the json representation
        connection_enterprise_db_connection_model_dict = ConnectionEnterpriseDBConnection.from_dict(connection_enterprise_db_connection_model_json).__dict__
        connection_enterprise_db_connection_model2 = ConnectionEnterpriseDBConnection(**connection_enterprise_db_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_enterprise_db_connection_model == connection_enterprise_db_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_enterprise_db_connection_model_json2 = connection_enterprise_db_connection_model.to_dict()
        assert connection_enterprise_db_connection_model_json2 == connection_enterprise_db_connection_model_json

class TestModel_ConnectionEtcdConnection():
    """
    Test Class for ConnectionEtcdConnection
    """

    def test_connection_etcd_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionEtcdConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        connection_uri_model = {} # ConnectionURI
        connection_uri_model['type'] = 'uri'
        connection_uri_model['composed'] = ['testString']
        connection_uri_model['scheme'] = 'testString'
        connection_uri_model['hosts'] = [connection_host_model]
        connection_uri_model['path'] = 'testString'
        connection_uri_model['query_options'] = {'foo': 'bar'}
        connection_uri_model['authentication'] = connection_authentication_model
        connection_uri_model['certificate'] = connection_certificate_model
        connection_uri_model['ssl'] = True
        connection_uri_model['browser_accessible'] = True

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {'foo': 'bar'}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_certificate_model

        # Construct a json representation of a ConnectionEtcdConnection model
        connection_etcd_connection_model_json = {}
        connection_etcd_connection_model_json['grpc'] = connection_uri_model
        connection_etcd_connection_model_json['cli'] = connection_cli_model

        # Construct a model instance of ConnectionEtcdConnection by calling from_dict on the json representation
        connection_etcd_connection_model = ConnectionEtcdConnection.from_dict(connection_etcd_connection_model_json)
        assert connection_etcd_connection_model != False

        # Construct a model instance of ConnectionEtcdConnection by calling from_dict on the json representation
        connection_etcd_connection_model_dict = ConnectionEtcdConnection.from_dict(connection_etcd_connection_model_json).__dict__
        connection_etcd_connection_model2 = ConnectionEtcdConnection(**connection_etcd_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_etcd_connection_model == connection_etcd_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_etcd_connection_model_json2 = connection_etcd_connection_model.to_dict()
        assert connection_etcd_connection_model_json2 == connection_etcd_connection_model_json

class TestModel_ConnectionMongoDBConnection():
    """
    Test Class for ConnectionMongoDBConnection
    """

    def test_connection_mongo_db_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionMongoDBConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        mongo_db_connection_uri_model = {} # MongoDBConnectionURI
        mongo_db_connection_uri_model['type'] = 'uri'
        mongo_db_connection_uri_model['composed'] = ['testString']
        mongo_db_connection_uri_model['scheme'] = 'testString'
        mongo_db_connection_uri_model['hosts'] = [connection_host_model]
        mongo_db_connection_uri_model['path'] = 'testString'
        mongo_db_connection_uri_model['query_options'] = {'foo': 'bar'}
        mongo_db_connection_uri_model['authentication'] = connection_authentication_model
        mongo_db_connection_uri_model['certificate'] = connection_certificate_model
        mongo_db_connection_uri_model['ssl'] = True
        mongo_db_connection_uri_model['browser_accessible'] = True
        mongo_db_connection_uri_model['database'] = 'testString'
        mongo_db_connection_uri_model['replica_set'] = 'testString'

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {'foo': 'bar'}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_certificate_model

        # Construct a json representation of a ConnectionMongoDBConnection model
        connection_mongo_db_connection_model_json = {}
        connection_mongo_db_connection_model_json['mongodb'] = mongo_db_connection_uri_model
        connection_mongo_db_connection_model_json['cli'] = connection_cli_model

        # Construct a model instance of ConnectionMongoDBConnection by calling from_dict on the json representation
        connection_mongo_db_connection_model = ConnectionMongoDBConnection.from_dict(connection_mongo_db_connection_model_json)
        assert connection_mongo_db_connection_model != False

        # Construct a model instance of ConnectionMongoDBConnection by calling from_dict on the json representation
        connection_mongo_db_connection_model_dict = ConnectionMongoDBConnection.from_dict(connection_mongo_db_connection_model_json).__dict__
        connection_mongo_db_connection_model2 = ConnectionMongoDBConnection(**connection_mongo_db_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_mongo_db_connection_model == connection_mongo_db_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_mongo_db_connection_model_json2 = connection_mongo_db_connection_model.to_dict()
        assert connection_mongo_db_connection_model_json2 == connection_mongo_db_connection_model_json

class TestModel_ConnectionMongoDBEEConnection():
    """
    Test Class for ConnectionMongoDBEEConnection
    """

    def test_connection_mongo_dbee_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionMongoDBEEConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        mongo_db_connection_uri_model = {} # MongoDBConnectionURI
        mongo_db_connection_uri_model['type'] = 'uri'
        mongo_db_connection_uri_model['composed'] = ['testString']
        mongo_db_connection_uri_model['scheme'] = 'testString'
        mongo_db_connection_uri_model['hosts'] = [connection_host_model]
        mongo_db_connection_uri_model['path'] = 'testString'
        mongo_db_connection_uri_model['query_options'] = {'foo': 'bar'}
        mongo_db_connection_uri_model['authentication'] = connection_authentication_model
        mongo_db_connection_uri_model['certificate'] = connection_certificate_model
        mongo_db_connection_uri_model['ssl'] = True
        mongo_db_connection_uri_model['browser_accessible'] = True
        mongo_db_connection_uri_model['database'] = 'testString'
        mongo_db_connection_uri_model['replica_set'] = 'testString'

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {'foo': 'bar'}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_certificate_model

        connection_uri_model = {} # ConnectionURI
        connection_uri_model['type'] = 'uri'
        connection_uri_model['composed'] = ['testString']
        connection_uri_model['scheme'] = 'testString'
        connection_uri_model['hosts'] = [connection_host_model]
        connection_uri_model['path'] = 'testString'
        connection_uri_model['query_options'] = {'foo': 'bar'}
        connection_uri_model['authentication'] = connection_authentication_model
        connection_uri_model['certificate'] = connection_certificate_model
        connection_uri_model['ssl'] = True
        connection_uri_model['browser_accessible'] = True

        # Construct a json representation of a ConnectionMongoDBEEConnection model
        connection_mongo_dbee_connection_model_json = {}
        connection_mongo_dbee_connection_model_json['mongodb'] = mongo_db_connection_uri_model
        connection_mongo_dbee_connection_model_json['cli'] = connection_cli_model
        connection_mongo_dbee_connection_model_json['bi_connector'] = connection_uri_model
        connection_mongo_dbee_connection_model_json['analytics'] = connection_uri_model

        # Construct a model instance of ConnectionMongoDBEEConnection by calling from_dict on the json representation
        connection_mongo_dbee_connection_model = ConnectionMongoDBEEConnection.from_dict(connection_mongo_dbee_connection_model_json)
        assert connection_mongo_dbee_connection_model != False

        # Construct a model instance of ConnectionMongoDBEEConnection by calling from_dict on the json representation
        connection_mongo_dbee_connection_model_dict = ConnectionMongoDBEEConnection.from_dict(connection_mongo_dbee_connection_model_json).__dict__
        connection_mongo_dbee_connection_model2 = ConnectionMongoDBEEConnection(**connection_mongo_dbee_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_mongo_dbee_connection_model == connection_mongo_dbee_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_mongo_dbee_connection_model_json2 = connection_mongo_dbee_connection_model.to_dict()
        assert connection_mongo_dbee_connection_model_json2 == connection_mongo_dbee_connection_model_json

class TestModel_ConnectionMongoDBEEOpsManagerConnection():
    """
    Test Class for ConnectionMongoDBEEOpsManagerConnection
    """

    def test_connection_mongo_dbee_ops_manager_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionMongoDBEEOpsManagerConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        connection_uri_model = {} # ConnectionURI
        connection_uri_model['type'] = 'uri'
        connection_uri_model['composed'] = ['testString']
        connection_uri_model['scheme'] = 'testString'
        connection_uri_model['hosts'] = [connection_host_model]
        connection_uri_model['path'] = 'testString'
        connection_uri_model['query_options'] = {'foo': 'bar'}
        connection_uri_model['authentication'] = connection_authentication_model
        connection_uri_model['certificate'] = connection_certificate_model
        connection_uri_model['ssl'] = True
        connection_uri_model['browser_accessible'] = True

        # Construct a json representation of a ConnectionMongoDBEEOpsManagerConnection model
        connection_mongo_dbee_ops_manager_connection_model_json = {}
        connection_mongo_dbee_ops_manager_connection_model_json['ops_manager'] = connection_uri_model

        # Construct a model instance of ConnectionMongoDBEEOpsManagerConnection by calling from_dict on the json representation
        connection_mongo_dbee_ops_manager_connection_model = ConnectionMongoDBEEOpsManagerConnection.from_dict(connection_mongo_dbee_ops_manager_connection_model_json)
        assert connection_mongo_dbee_ops_manager_connection_model != False

        # Construct a model instance of ConnectionMongoDBEEOpsManagerConnection by calling from_dict on the json representation
        connection_mongo_dbee_ops_manager_connection_model_dict = ConnectionMongoDBEEOpsManagerConnection.from_dict(connection_mongo_dbee_ops_manager_connection_model_json).__dict__
        connection_mongo_dbee_ops_manager_connection_model2 = ConnectionMongoDBEEOpsManagerConnection(**connection_mongo_dbee_ops_manager_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_mongo_dbee_ops_manager_connection_model == connection_mongo_dbee_ops_manager_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_mongo_dbee_ops_manager_connection_model_json2 = connection_mongo_dbee_ops_manager_connection_model.to_dict()
        assert connection_mongo_dbee_ops_manager_connection_model_json2 == connection_mongo_dbee_ops_manager_connection_model_json

class TestModel_ConnectionMySQLConnection():
    """
    Test Class for ConnectionMySQLConnection
    """

    def test_connection_my_sql_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionMySQLConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        my_sql_connection_uri_model = {} # MySQLConnectionURI
        my_sql_connection_uri_model['type'] = 'uri'
        my_sql_connection_uri_model['composed'] = ['testString']
        my_sql_connection_uri_model['scheme'] = 'testString'
        my_sql_connection_uri_model['hosts'] = [connection_host_model]
        my_sql_connection_uri_model['path'] = 'testString'
        my_sql_connection_uri_model['query_options'] = {'foo': 'bar'}
        my_sql_connection_uri_model['authentication'] = connection_authentication_model
        my_sql_connection_uri_model['certificate'] = connection_certificate_model
        my_sql_connection_uri_model['ssl'] = True
        my_sql_connection_uri_model['browser_accessible'] = True
        my_sql_connection_uri_model['database'] = 'testString'

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {'foo': 'bar'}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_certificate_model

        # Construct a json representation of a ConnectionMySQLConnection model
        connection_my_sql_connection_model_json = {}
        connection_my_sql_connection_model_json['mysql'] = my_sql_connection_uri_model
        connection_my_sql_connection_model_json['cli'] = connection_cli_model

        # Construct a model instance of ConnectionMySQLConnection by calling from_dict on the json representation
        connection_my_sql_connection_model = ConnectionMySQLConnection.from_dict(connection_my_sql_connection_model_json)
        assert connection_my_sql_connection_model != False

        # Construct a model instance of ConnectionMySQLConnection by calling from_dict on the json representation
        connection_my_sql_connection_model_dict = ConnectionMySQLConnection.from_dict(connection_my_sql_connection_model_json).__dict__
        connection_my_sql_connection_model2 = ConnectionMySQLConnection(**connection_my_sql_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_my_sql_connection_model == connection_my_sql_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_my_sql_connection_model_json2 = connection_my_sql_connection_model.to_dict()
        assert connection_my_sql_connection_model_json2 == connection_my_sql_connection_model_json

class TestModel_ConnectionPostgreSQLConnection():
    """
    Test Class for ConnectionPostgreSQLConnection
    """

    def test_connection_postgre_sql_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionPostgreSQLConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        postgre_sql_connection_uri_model = {} # PostgreSQLConnectionURI
        postgre_sql_connection_uri_model['type'] = 'uri'
        postgre_sql_connection_uri_model['composed'] = ['testString']
        postgre_sql_connection_uri_model['scheme'] = 'testString'
        postgre_sql_connection_uri_model['hosts'] = [connection_host_model]
        postgre_sql_connection_uri_model['path'] = 'testString'
        postgre_sql_connection_uri_model['query_options'] = {'foo': 'bar'}
        postgre_sql_connection_uri_model['authentication'] = connection_authentication_model
        postgre_sql_connection_uri_model['certificate'] = connection_certificate_model
        postgre_sql_connection_uri_model['ssl'] = True
        postgre_sql_connection_uri_model['browser_accessible'] = True
        postgre_sql_connection_uri_model['database'] = 'testString'

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {'foo': 'bar'}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_certificate_model

        # Construct a json representation of a ConnectionPostgreSQLConnection model
        connection_postgre_sql_connection_model_json = {}
        connection_postgre_sql_connection_model_json['postgres'] = postgre_sql_connection_uri_model
        connection_postgre_sql_connection_model_json['cli'] = connection_cli_model

        # Construct a model instance of ConnectionPostgreSQLConnection by calling from_dict on the json representation
        connection_postgre_sql_connection_model = ConnectionPostgreSQLConnection.from_dict(connection_postgre_sql_connection_model_json)
        assert connection_postgre_sql_connection_model != False

        # Construct a model instance of ConnectionPostgreSQLConnection by calling from_dict on the json representation
        connection_postgre_sql_connection_model_dict = ConnectionPostgreSQLConnection.from_dict(connection_postgre_sql_connection_model_json).__dict__
        connection_postgre_sql_connection_model2 = ConnectionPostgreSQLConnection(**connection_postgre_sql_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_postgre_sql_connection_model == connection_postgre_sql_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_postgre_sql_connection_model_json2 = connection_postgre_sql_connection_model.to_dict()
        assert connection_postgre_sql_connection_model_json2 == connection_postgre_sql_connection_model_json

class TestModel_ConnectionRabbitMQConnection():
    """
    Test Class for ConnectionRabbitMQConnection
    """

    def test_connection_rabbit_mq_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionRabbitMQConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        connection_uri_model = {} # ConnectionURI
        connection_uri_model['type'] = 'uri'
        connection_uri_model['composed'] = ['testString']
        connection_uri_model['scheme'] = 'testString'
        connection_uri_model['hosts'] = [connection_host_model]
        connection_uri_model['path'] = 'testString'
        connection_uri_model['query_options'] = {'foo': 'bar'}
        connection_uri_model['authentication'] = connection_authentication_model
        connection_uri_model['certificate'] = connection_certificate_model
        connection_uri_model['ssl'] = True
        connection_uri_model['browser_accessible'] = True

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {'foo': 'bar'}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_certificate_model

        # Construct a json representation of a ConnectionRabbitMQConnection model
        connection_rabbit_mq_connection_model_json = {}
        connection_rabbit_mq_connection_model_json['amqps'] = connection_uri_model
        connection_rabbit_mq_connection_model_json['mqtts'] = connection_uri_model
        connection_rabbit_mq_connection_model_json['stomp_ssl'] = connection_uri_model
        connection_rabbit_mq_connection_model_json['https'] = connection_uri_model
        connection_rabbit_mq_connection_model_json['cli'] = connection_cli_model

        # Construct a model instance of ConnectionRabbitMQConnection by calling from_dict on the json representation
        connection_rabbit_mq_connection_model = ConnectionRabbitMQConnection.from_dict(connection_rabbit_mq_connection_model_json)
        assert connection_rabbit_mq_connection_model != False

        # Construct a model instance of ConnectionRabbitMQConnection by calling from_dict on the json representation
        connection_rabbit_mq_connection_model_dict = ConnectionRabbitMQConnection.from_dict(connection_rabbit_mq_connection_model_json).__dict__
        connection_rabbit_mq_connection_model2 = ConnectionRabbitMQConnection(**connection_rabbit_mq_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_rabbit_mq_connection_model == connection_rabbit_mq_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_rabbit_mq_connection_model_json2 = connection_rabbit_mq_connection_model.to_dict()
        assert connection_rabbit_mq_connection_model_json2 == connection_rabbit_mq_connection_model_json

class TestModel_ConnectionRedisConnection():
    """
    Test Class for ConnectionRedisConnection
    """

    def test_connection_redis_connection_serialization(self):
        """
        Test serialization/deserialization for ConnectionRedisConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        connection_host_model = {} # ConnectionHost
        connection_host_model['hostname'] = 'testString'
        connection_host_model['port'] = 38

        connection_authentication_model = {} # ConnectionAuthentication
        connection_authentication_model['method'] = 'testString'
        connection_authentication_model['username'] = 'testString'
        connection_authentication_model['password'] = 'testString'

        connection_certificate_model = {} # ConnectionCertificate
        connection_certificate_model['name'] = 'testString'
        connection_certificate_model['certificate_base64'] = 'testString'

        redis_connection_uri_model = {} # RedisConnectionURI
        redis_connection_uri_model['type'] = 'uri'
        redis_connection_uri_model['composed'] = ['testString']
        redis_connection_uri_model['scheme'] = 'testString'
        redis_connection_uri_model['hosts'] = [connection_host_model]
        redis_connection_uri_model['path'] = 'testString'
        redis_connection_uri_model['query_options'] = {'foo': 'bar'}
        redis_connection_uri_model['authentication'] = connection_authentication_model
        redis_connection_uri_model['certificate'] = connection_certificate_model
        redis_connection_uri_model['ssl'] = True
        redis_connection_uri_model['browser_accessible'] = True
        redis_connection_uri_model['database'] = 38

        connection_cli_model = {} # ConnectionCLI
        connection_cli_model['type'] = 'cli'
        connection_cli_model['composed'] = ['testString']
        connection_cli_model['environment'] = {'foo': 'bar'}
        connection_cli_model['bin'] = 'testString'
        connection_cli_model['arguments'] = [['testString']]
        connection_cli_model['certificate'] = connection_certificate_model

        # Construct a json representation of a ConnectionRedisConnection model
        connection_redis_connection_model_json = {}
        connection_redis_connection_model_json['rediss'] = redis_connection_uri_model
        connection_redis_connection_model_json['cli'] = connection_cli_model

        # Construct a model instance of ConnectionRedisConnection by calling from_dict on the json representation
        connection_redis_connection_model = ConnectionRedisConnection.from_dict(connection_redis_connection_model_json)
        assert connection_redis_connection_model != False

        # Construct a model instance of ConnectionRedisConnection by calling from_dict on the json representation
        connection_redis_connection_model_dict = ConnectionRedisConnection.from_dict(connection_redis_connection_model_json).__dict__
        connection_redis_connection_model2 = ConnectionRedisConnection(**connection_redis_connection_model_dict)

        # Verify the model instances are equivalent
        assert connection_redis_connection_model == connection_redis_connection_model2

        # Convert model instance back to dict and verify no loss of data
        connection_redis_connection_model_json2 = connection_redis_connection_model.to_dict()
        assert connection_redis_connection_model_json2 == connection_redis_connection_model_json

class TestModel_UserUpdatePasswordSetting():
    """
    Test Class for UserUpdatePasswordSetting
    """

    def test_user_update_password_setting_serialization(self):
        """
        Test serialization/deserialization for UserUpdatePasswordSetting
        """

        # Construct a json representation of a UserUpdatePasswordSetting model
        user_update_password_setting_model_json = {}
        user_update_password_setting_model_json['password'] = 'v3ry-1-secUre-pAssword-2'

        # Construct a model instance of UserUpdatePasswordSetting by calling from_dict on the json representation
        user_update_password_setting_model = UserUpdatePasswordSetting.from_dict(user_update_password_setting_model_json)
        assert user_update_password_setting_model != False

        # Construct a model instance of UserUpdatePasswordSetting by calling from_dict on the json representation
        user_update_password_setting_model_dict = UserUpdatePasswordSetting.from_dict(user_update_password_setting_model_json).__dict__
        user_update_password_setting_model2 = UserUpdatePasswordSetting(**user_update_password_setting_model_dict)

        # Verify the model instances are equivalent
        assert user_update_password_setting_model == user_update_password_setting_model2

        # Convert model instance back to dict and verify no loss of data
        user_update_password_setting_model_json2 = user_update_password_setting_model.to_dict()
        assert user_update_password_setting_model_json2 == user_update_password_setting_model_json

class TestModel_UserUpdateRedisRoleSetting():
    """
    Test Class for UserUpdateRedisRoleSetting
    """

    def test_user_update_redis_role_setting_serialization(self):
        """
        Test serialization/deserialization for UserUpdateRedisRoleSetting
        """

        # Construct a json representation of a UserUpdateRedisRoleSetting model
        user_update_redis_role_setting_model_json = {}
        user_update_redis_role_setting_model_json['role'] = '-@all -@read'

        # Construct a model instance of UserUpdateRedisRoleSetting by calling from_dict on the json representation
        user_update_redis_role_setting_model = UserUpdateRedisRoleSetting.from_dict(user_update_redis_role_setting_model_json)
        assert user_update_redis_role_setting_model != False

        # Construct a model instance of UserUpdateRedisRoleSetting by calling from_dict on the json representation
        user_update_redis_role_setting_model_dict = UserUpdateRedisRoleSetting.from_dict(user_update_redis_role_setting_model_json).__dict__
        user_update_redis_role_setting_model2 = UserUpdateRedisRoleSetting(**user_update_redis_role_setting_model_dict)

        # Verify the model instances are equivalent
        assert user_update_redis_role_setting_model == user_update_redis_role_setting_model2

        # Convert model instance back to dict and verify no loss of data
        user_update_redis_role_setting_model_json2 = user_update_redis_role_setting_model.to_dict()
        assert user_update_redis_role_setting_model_json2 == user_update_redis_role_setting_model_json

class TestModel_UserDatabaseUser():
    """
    Test Class for UserDatabaseUser
    """

    def test_user_database_user_serialization(self):
        """
        Test serialization/deserialization for UserDatabaseUser
        """

        # Construct a json representation of a UserDatabaseUser model
        user_database_user_model_json = {}
        user_database_user_model_json['username'] = 'user'
        user_database_user_model_json['password'] = 'v3ry-1-secUre-pAssword-2'

        # Construct a model instance of UserDatabaseUser by calling from_dict on the json representation
        user_database_user_model = UserDatabaseUser.from_dict(user_database_user_model_json)
        assert user_database_user_model != False

        # Construct a model instance of UserDatabaseUser by calling from_dict on the json representation
        user_database_user_model_dict = UserDatabaseUser.from_dict(user_database_user_model_json).__dict__
        user_database_user_model2 = UserDatabaseUser(**user_database_user_model_dict)

        # Verify the model instances are equivalent
        assert user_database_user_model == user_database_user_model2

        # Convert model instance back to dict and verify no loss of data
        user_database_user_model_json2 = user_database_user_model.to_dict()
        assert user_database_user_model_json2 == user_database_user_model_json

class TestModel_UserOpsManagerUser():
    """
    Test Class for UserOpsManagerUser
    """

    def test_user_ops_manager_user_serialization(self):
        """
        Test serialization/deserialization for UserOpsManagerUser
        """

        # Construct a json representation of a UserOpsManagerUser model
        user_ops_manager_user_model_json = {}
        user_ops_manager_user_model_json['username'] = 'user'
        user_ops_manager_user_model_json['password'] = 'v3ry-1-secUre-pAssword-2'
        user_ops_manager_user_model_json['role'] = 'group_data_access_admin'

        # Construct a model instance of UserOpsManagerUser by calling from_dict on the json representation
        user_ops_manager_user_model = UserOpsManagerUser.from_dict(user_ops_manager_user_model_json)
        assert user_ops_manager_user_model != False

        # Construct a model instance of UserOpsManagerUser by calling from_dict on the json representation
        user_ops_manager_user_model_dict = UserOpsManagerUser.from_dict(user_ops_manager_user_model_json).__dict__
        user_ops_manager_user_model2 = UserOpsManagerUser(**user_ops_manager_user_model_dict)

        # Verify the model instances are equivalent
        assert user_ops_manager_user_model == user_ops_manager_user_model2

        # Convert model instance back to dict and verify no loss of data
        user_ops_manager_user_model_json2 = user_ops_manager_user_model.to_dict()
        assert user_ops_manager_user_model_json2 == user_ops_manager_user_model_json

class TestModel_UserRedisDatabaseUser():
    """
    Test Class for UserRedisDatabaseUser
    """

    def test_user_redis_database_user_serialization(self):
        """
        Test serialization/deserialization for UserRedisDatabaseUser
        """

        # Construct a json representation of a UserRedisDatabaseUser model
        user_redis_database_user_model_json = {}
        user_redis_database_user_model_json['username'] = 'user'
        user_redis_database_user_model_json['password'] = 'v3ry-1-secUre-pAssword-2'
        user_redis_database_user_model_json['role'] = '-@all -@read'

        # Construct a model instance of UserRedisDatabaseUser by calling from_dict on the json representation
        user_redis_database_user_model = UserRedisDatabaseUser.from_dict(user_redis_database_user_model_json)
        assert user_redis_database_user_model != False

        # Construct a model instance of UserRedisDatabaseUser by calling from_dict on the json representation
        user_redis_database_user_model_dict = UserRedisDatabaseUser.from_dict(user_redis_database_user_model_json).__dict__
        user_redis_database_user_model2 = UserRedisDatabaseUser(**user_redis_database_user_model_dict)

        # Verify the model instances are equivalent
        assert user_redis_database_user_model == user_redis_database_user_model2

        # Convert model instance back to dict and verify no loss of data
        user_redis_database_user_model_json2 = user_redis_database_user_model.to_dict()
        assert user_redis_database_user_model_json2 == user_redis_database_user_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
