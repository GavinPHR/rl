# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


def test_imports():
    from torchrl.data import (  # noqa: F401
        PrioritizedReplayBuffer,
        ReplayBuffer,
        TensorDict,
        TensorSpec,
    )
    from torchrl.envs import Transform, TransformedEnv  # noqa: F401
    from torchrl.envs.gym_like import GymLikeEnv  # noqa: F401
    from torchrl.modules import TensorDictModule  # noqa: F401
    from torchrl.objectives.costs.common import LossModule  # noqa: F401
