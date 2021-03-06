# Copyright 2018 Minds.ai, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from typing import Optional
from requests import PreparedRequest


class ZoomAPIException(Exception):
  def __init__(self,
               status_code: int,
               name: str,
               method: Optional[PreparedRequest],
               message: str):
    """Initializes container for holding HTTP status information.

    :param status_code: HTTP status code.
    :param name: HTTP status name.
    :param method: HTTP method used.
    :param message: Exception message/reason.
    """
    super(ZoomAPIException, self).__init__()
    self.status_code = status_code
    self.name = name
    self.method = method
    self.message = message

  def __str__(self) -> str:
    """Returns printable string with formatted exception message.
    Usage: print(ZoomAPIException)

    :return: formatted message containing exception information.
    """
    return f'HTTP_STATUS: {self.status_code}-{self.name}, {self.message}'

  def __repr__(self) -> str:
    """Returns class type when repr method called.

    :return: string containing exception class name.
    """
    return 'ZoomAPIException()'

  @property
  def http_method(self):
    """Returns request method.

    :return: String containing HTTP request method (GET, DELETE, etc.).
    """
    return self.method.method if self.method else None
