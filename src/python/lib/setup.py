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
"""setup.py for libClusterFuzz."""
import setuptools

with open('README.md', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
    name='clusterfuzz',
    version='0.0.1',
    author='ClusterFuzz authors',
    author_email='clusterfuzz-announce@googlegroups.com',
    description='ClusterFuzz',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/google/clusterfuzz',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)

# TODO(ochang): Add and minimize dependencies.
