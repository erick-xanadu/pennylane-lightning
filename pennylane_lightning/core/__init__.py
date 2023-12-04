# Copyright 2018-2023 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""PennyLane lightning module."""

from pathlib import Path
from ._version import __version__


lightning_qubit_config_file = Path(__file__).parent / "src" / "lightning_qubit.toml"
lightning_kokkos_config_file = Path(__file__).parent / "src" / "lightning_kokkos.toml"
lightning_gpu_config_file = Path(__file__).parent / "src" / "lightning_gpu.toml"

__all__ = ["__version__", "lightning_qubit_config_file", "lightning_kokkos_config_file", "lightning_gpu_config_file"]
