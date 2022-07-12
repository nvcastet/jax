# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for release_backend_clients."""

from absl.testing import absltest

import jax
from jax.config import config
from jax.experimental import clear_backends as cb
from jax._src import test_util as jtu
from jax._src.lib import xla_bridge as xb
from jax._src.lib import xla_client as xc

config.parse_flags_with_absl()


class ClearBackendsTest(jtu.JaxTestCase):

  def test_clear_backends(self):
    g = jax.jit(lambda x, y: x * y)
    self.assertEqual(g(1, 2), 2)
    if xc._version >= 79:
      self.assertNotEmpty(xb.get_backend().live_executables())
      cb.clear_backends()
      self.assertEmpty(xb.get_backend().live_executables())
      self.assertEqual(g(1, 2), 2)


if __name__ == "__main__":
  absltest.main(testLoader=jtu.JaxTestLoader())
