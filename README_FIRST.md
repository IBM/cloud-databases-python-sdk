# IBM Cloud Python SDK Template Usage Instructions

This repository serves as a template for Python SDKs that are produced with the
[IBM OpenAPI SDK Generator](https://github.ibm.com/CloudEngineering/openapi-sdkgen).

You can use the contents of this repository to create your own Python SDK repository.

## Table of Contents
<!--
  The TOC below is generated using the `markdown-toc` node package.

      https://github.com/jonschlinkert/markdown-toc

  You should regenerate the TOC after making changes to this file.

      markdown-toc -i --maxdepth 4 README_FIRST.md
  -->

<!-- toc -->

- [How to use this repository](#how-to-use-this-repository)
  * [1. Create your new github repository from this template](#1-create-your-new-github-repository-from-this-template)
  * [2. Modify selected files](#2-modify-selected-files)
  * [3. Add one or more services to the project](#3-add-one-or-more-services-to-the-project)
  * [4. Test your SDK](#4-test-your-sdk)
- [Integration tests](#integration-tests)
- [Continuous Integration](#continuous-integration)
  * [Release management with semantic-release](#release-management-with-semantic-release)
  * [Publishing build outputs to PyPI](#publishing-build-outputs-to-pypi)
  * [Encrypting secrets](#encrypting-secrets)
- [Setting the ``User-Agent`` Header In Preparation for SDK Metrics Gathering](#setting-the-user-agent-header-in-preparation-for-sdk-metrics-gathering)

<!-- tocstop -->

## How to use this repository

### 1. Create your new github repository from this template
This SDK template repository is implemented as a
[github template](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template),
which makes it easy to create new projects from it.

To create a new SDK repository from this template, follow these instructions:
1. In your browser, open the link for this
[template repository](https://github.ibm.com/CloudEngineering/python-sdk-template).

2. Click on the `Use this template` button that appears next to the `Clone or download` button.

3. In the next window:
- Select the `Owner`. This is the github id or organization where the new repository should be created
- Enter the respository name (e.g. `platform-services-python-sdk`):
  - Recommendation: use a name of the form `<service-category>-<language>-sdk`, where:
    - `<service-category>` refers to the IBM Cloud service category associated with the services that
	  will be included in the project (e.g. `platform-services`)
    - `<language>` is the language associated with the SDK project (e.g. `python`)

4. Click the `Create repository from template` button to create the new repository
If your goal is to create the new SDK repository on the `Github Enterprise` server (github.ibm.com),
then you are finished creating the new repository and you can proceed to section 2.

On the other hand, if your goal is to create the new SDK repository on the `Public Github` server (github.com),
then perform these additional steps:

5. Create a new **EMPTY** repository on the Public Github server:
- Select "No template" for the "Repository template" option
- Select the `Owner` (your personal id or an organization)
- Enter the same respository name that you used when creating the new repository above (e.g. my-python-sdk)
- Do NOT select the `Initialize this repository with a README` option
- Select `None` for the `Add .gitignore` and `Add a license` options
- Click the `Create repository` button.
- After the new empty repository has been created, you will be at the main page
of your new repository, which will include this text:
```
...or push an existing repository from the command line

git remote add origin git@github.com:padamstx/my-python-sdk.git
git push -u origin main
```
- Take note of the two git commands listed above for your new repository, as we'll execute these later

6. Clone your new `Github Enterprise` repository (created in steps 1-3 above)
to your local development environment:

```sh
[/work/demos]
$ git clone git@github.ibm.com:phil-adams/my-python-sdk.git
Cloning into 'my-python-sdk'...
remote: Enumerating objects: 36, done.
remote: Counting objects: 100% (36/36), done.
remote: Compressing objects: 100% (32/32), done.
remote: Total 36 (delta 1), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (36/36), 28.74 KiB | 577.00 KiB/s, done.
Resolving deltas: 100% (1/1), done.
```

7. "cd" into your project's root directory:

```sh
[/work/demos]
$ cd my-python-sdk
[/work/demos/my-python-sdk]
$
```

8. Remove the existing remote:
```sh
[/work/demos/my-python-sdk]
$ git remote remove origin
```

9. Add a new remote which reflects your new `Public Github` repository:

```sh
[/work/demos/my-python-sdk]
$ git remote add origin git@github.com:padamstx/my-python-sdk.git
```

10. Push your local repository to the new remote (Public Github):

```sh
[/work/demos/my-python-sdk]
$ git push -u origin main
Enumerating objects: 36, done.
Counting objects: 100% (36/36), done.
Delta compression using up to 12 threads
Compressing objects: 100% (31/31), done.
Writing objects: 100% (36/36), 28.74 KiB | 28.74 MiB/s, done.
Total 36 (delta 1), reused 36 (delta 1)
remote: Resolving deltas: 100% (1/1), done.
To github.com:padamstx/my-python-sdk.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

You have now created your new SDK repository on the `Public Github` server.

You may want to now delete the new SDK repository that you created on the `Github Enterprise`
server since it will no longer be used now that you have created your repository on `Public Github`.


### 2. Modify selected files

#### Automatic Script

Use the `prepare_project.sh` script to perform the below modifications automatically.
It will delete the `example service` files and update the corresponding sections with the specified values.
Read through the manual steps below to understand the changes performed by the `prepare_project.sh` script.

Here is a description of the various options that you can pass to the script:
```bash
prepare_project.sh -n <sdk-package-name> -d <project-description> \
        -g <git-repo-url> -s <service-category-description> -a <author-email> -c <service-category-name>
```

Here is an example of how to run the script for the `platform-services-go-sdk` project:
```bash
cd <project-root>
./prepare_project.sh -n ibm_platform_services -d "IBM Cloud Platform Services Python SDK" \
       -g https://github.com/IBM/platform-services-python-sdk -s "Platform Services" -a email@ibm.com -c platform-services
```

- To list the files changed by the script, run : `git status`
- To view the changes made by this script, run: `git diff`
- To discard the changes made by the script, run `git checkout .`, or `git stash`
- If satisfied with the changes, then just commit the changes (e.g. `git commit -a -m "chore: prepare SDK project"`)


#### Manual Steps

- In this section, you'll modify various files within your new SDK repository to reflect
the proper names and settings for your specific project.

- The template repository comes with an example service included, but this should be removed
from your project.  Remove the following files:
  - test/unit/test_example_service_v1.py
  - test/integration/test_example_service_v1.py
  - mysdk/example_service_v1.py

- The root of the project contains a directory named `mysdk` which represents the python package
where all the generated service files will eventually be located.
Rename this directory to reflect the service category associated with your SDK project
(e.g. `ibm_platform_services`, `ibm_database_services`, `ibm_networking_services`, etc.).
Choose your package name wisely as it will also be used to form the package name when
publishing your package to [PyPI](https://pypi.org/).

- After renaming the `mysdk` package directory, you'll need to modify various files to
reflect the new package name:
  - pylint.sh
  - .bumpversion.cfg
  - README.md
  - setup.py
  - tox.ini
  - .travis.yml
  - mysdk/common.py
  - mysdk/version.py
  - test/unit/test_common.py

In the instructions that follow, your project's package name will be referred to as `<package>`.

- Recommended: After selecting the python package name for your new project, you can configure the
`apiPackage` configuration property within the API definition for each of the services that will be
included in your project.  This is helpful because the SDK generator will use this configuration
property as the package into which the generated service code will be written.
Otherwise, you will need to use the equivalent `--api-package <package>`
command-line option when running the SDK generator to generate each service into the project.
Here's an example of the configuration properties that you can add to each API definition:
```yaml
  info:
    x-codegen-config:
      python:
        apiPackage: '<package>'
```
  Details about SDK generator configuration properties can be found
[here](https://github.ibm.com/CloudEngineering/openapi-sdkgen/wiki/Config-Options)

- Next, here is a list of the various files within the project with comments
that will guide you in the required modifications:

  - `.bumpversion.cfg`:
    - modify instances of `mysdk` to be `<package>`

  - `<package>/version.py`:
    - set `__version__` to `0.0.1`
    - modify the comment to reflect your package name.

  - `<package>/common.py`:
    - modify SDK_NAME to reflect the name of your SDK project (e.g. `platform-services-python-sdk`)
    - modify instances of `mysdk` to be `<package>`.
    - follow the instructions in the `get_sdk_headers()` function.

  - `test/unit/test_common.py`
    - modify the code in `test_get_sdk_headers` to reflect the correct name of your project
      (e.g. `platform-services-python-sdk`).

  - `<package>/__init__.py`:
    - modify module docstring to contain a description for your package
      (e.g. `"""Python client library for the IBM Cloud Platform Services"""`)
    - comment out the import for `ExampleServiceV1` (later, you'll add a similar
      import for each service added to your project).

  - `pylint.sh`:
    - modify `mysdk` to be `<package>`

  - `requirements.txt`: make sure that the version specified for the `ibm_cloud_sdk_core` dependency
    is the most recent available by looking [here](https://github.com/IBM/python-sdk-core/releases).

  - `setup.py`:
    - set `__version__` to be 0.0.1
    - set `PACKAGE_NAME` to be `<package>`
    - in the `setup()` function call, modify the following parameters to reflect your project:
      - `description`
      - `author_email`
      - `url`

  - `tox.ini`:
    - change `mysdk` to be `<package>`

  - `.travis.yml`:
    - Uncomment the `matrix` section.
    - Remove the `jobs` section as this is only applicable to the template repository's build.

  - `README.md`:
    - Change the title to reflect your project; leave the version in the title as `0.0.1`
    - Change the `cloud.ibm.com/apidocs` link to reflect the correct service category
      (e.g. `platform-services`)
    - Change instances of `mysdk` to be `<package>`
    - In the Overview section, modify `IBM Cloud MySDK Python SDK` to reflect your project
      (e.g. `IBM Cloud Platform Services Python SDK`)
    - In the table of services, remove the entry for the example service; later you'll list each
      service contained in your SDK project in this table, along with a link to the online reference docs
      and the name of the generated service class.
    - In the "Issues" section, modify `<github-repo-url>` to reflect the Github URL for your project.
    - Note that the README.md file contains a link to a common README document where general
      SDK usage information can be found.
    - When finished, read through the document and make any other changes that might be necessary.

  - `CONTRIBUTING.md`:
    - In the "Issues" section, modify `<github-repo-url>` to reflect the Github URL for your project.

At this point, it's probably a good idea to commit the changes that you have made so far.
Be sure to use proper commit messages when committing changes (follow the link in `CONTRIBUTING.md`
to the common CONTRIBUTING document).
Example:
```sh
cd <project-root>
git commit -a -m "chore: prepare SDK project"
```

### 3. Add one or more services to the project
For each service that you'd like to add to your SDK project, follow
[these instructions](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/CONTRIBUTING_python.md#adding-a-new-service).


### 4. Test your SDK
SDK tests are organized into *unit* and *integration* tests, which are located in
`test/unit/` and `test/integration/`, respectively.
Unit tests mock the request framework and test that request objects are constructed properly.
Integration tests make requests to live service instances and test that the SDK works as intended
from end to end.

This repository uses [Pytest](https://docs.pytest.org/en/latest/) for its testing and mocking
framework. To run the tests, use the following commands:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install .
pytest test
```

## Integration tests
Integration tests can be generated by the SDK generator or developed by hand.
The recommended approach is to generate the integration tests and then modify them as
needed to form an effective set of integration tests. For information on how to generate
integration tests, please see
[this page](https://github.ibm.com/CloudEngineering/openapi-sdkgen/wiki/Generating-integration-tests).

For integration tests to run properly with an actual running instance of the service,
credentials (e.g. IAM api key, etc.) must be provided as external configuration properties.
Details about this can be found
[here](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/README.md#using-external-configuration).

An example integration test is located at `test/integration/test_example_service_v1.py`.
In order to run the "example service" integration test,
you'll need an actual running instance of the example service.
To run this service, clone the [Example Service repo](https://github.ibm.com/CloudEngineering/example-service)
and follow the instructions there for how to start up an instance of the example service.

Any additional files needed for testing (such as an image to send to a visual recognition service)
should be placed in `test/resources/`.

## Continuous Integration
This repository is set up to use [Travis](https://travis-ci.com/)
or [Travis Enterprise](https://travis.ibm.com) for continuous integration.

The `.travis.yml` file contains all the instructions necessary to run the build.
An example `.travis.yml` file is supplied with this template repository.

For details related to the `travis.yml` file, see
[this](https://docs.travis-ci.com/user/customizing-the-build/)

### Release management with semantic-release
The `.travis.yml` file included in this template repository is configured to
perform automated release management with
[semantic-release](https://semantic-release.gitbook.io/semantic-release/).
You can see the deployment-related steps in the `deploy` stage of the `.travis.yml` file.

BEFORE you enable automated builds in Travis and AFTER you perform the initial project preparation,
you should add an initial tag (`v0.0.1`) to your repo and push it to remote:
```sh
cd <project-root>
git tag v0.0.1
git push --tags
```
This creates an initial "baseline" which `semantic-release` will use when merging the initial set of
commits into the main branch.   This tag represents the initial version of the project.
After adding this tag, be sure to use proper commit messages when making changes to the project.
See the CONTRIBUTING document for information about commit messages.

When you configure your SDK project in Travis, be sure to set this environment variable in your
Travis build settings:
- `GH_TOKEN`: set this to the Github oauth token for a user having "push" access to your repository

If you are using `Travis Enterprise` (travis.ibm.com), you'll need to add these environment variables
as well:
- `GH_URL`: set this to the string `https://github.ibm.com`
- `GH_PREFIX`: set this to the string `/api/v3`

As a final step, be sure to uncomment the `deploy` stage within `.travis.yml`.

Once these steps have been completed, your project should be ready for automated release management
with `semantic-release`.  This means that whenever you merge a PR into the main branch, the commit
messages are analyzed by `semantic-release` to determine the next version number for the project
(i.e. a new patch, minor or major version).  Once that is determined, `semantic-release` will perform
actions to modify certain files within the project to reflect the new version, as well as
build a new entry in the project's changelog and add a tag for the new version.

### Publishing build outputs to PyPI
If you will be publishing your build outputs to
[PyPI](https://pypi.org/), you'll need to add this environment variable to your
Travis build settings:
- `PYPI_TOKEN`: set this to your [PyPI API token](https://pypi.org/help/#apitoken)

### Encrypting secrets
To run integration tests within a Travis build, you'll need to encrypt the file containing the
required external configuration properties.
For details on how to do this, please see
[this](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/EncryptingSecrets.md)


## Setting the ``User-Agent`` Header In Preparation for SDK Metrics Gathering

If you plan to gather metrics for your SDK, the `User-Agent` header value must be
a string similar to the following:
   `my-python-sdk/0.0.1 (lang=python; arch=x86_64; os=Linux; python.version=3.7.4)`

The key parts are the sdk name (`my-python-sdk`), version (`0.0.1`) and the
language name (`lang=python`).
This is required because the analytics data collector uses the User-Agent header included
with each request to gather usage data for IBM Cloud services.

The default implementation of the `get_sdk_headers` method provided in this SDK template
repository will need to be modified slightly for your SDK.
Replace the `my-python-sdk/0.0.1` part with the name and version of your
Python SDK. The rest of the system information should remain as-is.

For example, suppose your Python SDK project is called `platform-services-python-sdk` and its
version is `2.3.1`.
The `User-Agent` header value should be:
   `platform-services-python-sdk/2.3.1 (lang=python; arch=x86_64; os=Linux; python.version=3.7.4)`

__Note__: It is very important that the sdk name ends with the string `-sdk`,
as the analytics data collector uses this to gather usage data.

More information about the analytics tool, and other steps you should take to start gathering
metrics for your SDK can be found [here](https://github.ibm.com/CloudEngineering/sdk-analytics).
