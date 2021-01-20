# Lint as: python3
# Copyright 2020 Google LLC
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

"""Config file for distributing package via Pypi server."""

import os

import setuptools

_README = "README.md"
_EXT_README = "EXTERNAL_" + _README
path = _EXT_README if os.path.isfile(_EXT_README) else _README

with open(path, "r") as fh:
  long_description = fh.read()

setuptools.setup(
    name="gps-building-blocks",
    version="1.2.1",
    author="gPS Team",
    author_email="no-reply@google.com",
    description="Modules and tools useful for use with advanced data solutions on Google Ads, Google Marketing Platform and Google Cloud.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/google/gps_building_blocks",
    license="Apache Software License",
    packages=setuptools.find_packages(),
    install_requires=[
        "absl-py==0.9.0",
        "google-api-core==1.19.0",
        "google-api-python-client==1.9.1",
        "google-auth==1.16.0",
        "google-cloud-bigquery==1.22.0",
        "google-cloud-firestore==1.6.2",
        "google-cloud-storage==1.28.1",
        "google-cloud-pubsub==1.3.1",
        "requests==2.23.0",
        "six==1.15.0",
        "dataclasses; python_version<'3.7'"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
)
