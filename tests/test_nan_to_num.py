# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import textwrap

from apibase import APIBase

obj = APIBase("torch.nan_to_num")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([[1, 2], [3., float("nan")]])
        result = torch.nan_to_num(input)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([float('nan'), float('inf'), -float('inf'), 3.14])
        result = torch.nan_to_num(input, 0., 1., -1.)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([float('nan'), float('inf'), -float('inf'), 3.14])
        result = torch.nan_to_num(input=input, nan=0., posinf=1., neginf=-1.)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        input = torch.tensor([float('nan'), float('inf'), -float('inf'), 3.14])
        out = torch.ones([4]).float()
        result = torch.nan_to_num(input=input, nan=0., posinf=1., neginf=-1., out=out)
        """
    )
    obj.run(pytorch_code, ["result", "out"])
