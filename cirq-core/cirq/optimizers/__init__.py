# Copyright 2018 The Cirq Developers
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

"""Circuit transformation utilities."""

from cirq.optimizers.align_left import (
    AlignLeft,
)

from cirq.optimizers.align_right import (
    AlignRight,
)

from cirq.optimizers.drop_empty_moments import (
    DropEmptyMoments,
)

from cirq.optimizers.drop_negligible import (
    DropNegligible,
)

from cirq.optimizers.convert_to_cz_and_single_gates import (
    ConvertToCzAndSingleGates,
)

from cirq.optimizers.eject_phased_paulis import (
    EjectPhasedPaulis,
)

from cirq.optimizers.eject_z import (
    EjectZ,
)

from cirq.optimizers.expand_composite import (
    ExpandComposite,
)

from cirq.optimizers.merge_interactions import (
    MergeInteractions,
)

from cirq.optimizers.merge_interactions_to_sqrt_iswap import (
    MergeInteractionsToSqrtIswap,
)

from cirq.optimizers.merge_single_qubit_gates import (
    merge_single_qubit_gates_into_phased_x_z,
    merge_single_qubit_gates_into_phxz,
    MergeSingleQubitGates,
)

from cirq.optimizers.stratify import (
    stratified_circuit,
)
from cirq.optimizers.synchronize_terminal_measurements import (
    SynchronizeTerminalMeasurements,
)

from cirq.optimizers.three_qubit_decomposition import (
    three_qubit_matrix_to_operations,
)

from cirq.optimizers.two_qubit_decompositions import (
    two_qubit_matrix_to_operations,
    two_qubit_matrix_to_diagonal_and_operations,
)


from cirq.optimizers.two_qubit_to_sqrt_iswap import (
    two_qubit_matrix_to_sqrt_iswap_operations,
)

from cirq.optimizers.two_qubit_to_fsim import (
    decompose_two_qubit_interaction_into_four_fsim_gates,
)

from cirq import _compat

_compat.deprecated_submodule(
    new_module_name="cirq.transformers.analytical_decompositions.clifford_decomposition",
    old_parent="cirq.optimizers",
    old_child="clifford_decomposition",
    deadline="v0.16",
    create_attribute=True,
)

_compat.deprecated_submodule(
    new_module_name="cirq.transformers.analytical_decompositions.cphase_to_fsim",
    old_parent="cirq.optimizers",
    old_child="cphase_to_fsim",
    deadline="v0.16",
    create_attribute=True,
)

_compat.deprecated_submodule(
    new_module_name="cirq.transformers.analytical_decompositions.controlled_gate_decomposition",
    old_parent="cirq.optimizers",
    old_child="controlled_gate_decomposition",
    deadline="v0.16",
    create_attribute=True,
)

_compat.deprecated_submodule(
    new_module_name="cirq.transformers.analytical_decompositions.single_qubit_decompositions",
    old_parent="cirq.optimizers",
    old_child="decompositions",
    deadline="v0.16",
    create_attribute=True,
)
