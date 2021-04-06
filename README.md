[![Build Status](https://travis-ci.com/IBM/cloud-databases-python-sdk.svg?branch=main)](https://travis-ci.com/IBM/cloud-databases-python-sdk)
[![Release](https://img.shields.io/github/v/release/IBM/cloud-databases-python-sdk)](https://github.com/IBM/cloud-databases-python-sdk/releases/latest)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ibm-cloud-databases)](https://pypi.org/project/ibm-cloud-databases/)
[![PyPI](https://img.shields.io/pypi/v/ibm-cloud-databases)](https://pypi.org/project/ibm-cloud-databases/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ibm-cloud-databases)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![codecov](https://codecov.io/gh/IBM/cloud-databases-python-sdk/branch/main/graph/badge.svg)](https://codecov.io/gh/IBM/cloud-databases-python-sdk)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)


# IBM Cloud Databases Python SDK

Python client library to interact with various [IBM Cloud Cloud Databases APIs](https://cloud.ibm.com/apidocs?category=cloud-databases).

Disclaimer: this SDK is being released initially as a **pre-release** version.
Changes might occur which impact applications that use this SDK.

## Table of Contents

<!--
  The TOC below is generated using the `markdown-toc` node package.

      https://github.com/jonschlinkert/markdown-toc

  You should regenerate the TOC after making changes to this file.

      npx markdown-toc -i README.md
  -->

<!-- toc -->

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using the SDK](#using-the-sdk)
- [Questions](#questions)
- [Issues](#issues)
- [Open source @ IBM](#open-source--ibm)
- [Contributing](#contributing)
- [License](#license)

<!-- tocstop -->

## Overview

The IBM Cloud Cloud Databases Python SDK allows developers to programmatically interact with the following
IBM Cloud services:

Service Name | Imported Class Name
--- | ---
[Cloud Databases](https://cloud.ibm.com/apidocs/cloud-databases-api/cloud-databases-api-v5) | clouddatabasesv5

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* Python 3.6 or above.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "ibm-cloud-databases>=0.0.1"
```

or

```bash
easy_install --upgrade "ibm-cloud-databases>=0.0.1"
```

## Using the SDK
For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/README.md)

## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.ibm.com/IBM/cloud-databases-python-sdk/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING.md](https://github.ibm.com/IBM/cloud-databases-python-sdk/blob/main/CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](https://github.ibm.com/IBM/cloud-databases-python-sdk/blob/main/LICENSE).
