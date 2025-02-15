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

obj = APIBase("torch.nn.utils.clip_grad_norm_")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.tensor([[[[-0.4106,  0.1677], [-0.6648, -0.5669]]]])

        result = nn.utils.clip_grad_norm_(x, max_norm=2.0)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.tensor([[[[-0.4106,  0.1677], [-0.6648, -0.5669]]]])

        result = nn.utils.clip_grad_norm_(x, max_norm=3.0, norm_type=1.0, error_if_nonfinite=True)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.tensor([[[[-0.4106,  0.1677], [-0.6648, -0.5669]]]])
        x.grad = torch.tensor([[[[-0.5, 12.343], [-10.4, -0.5669]]]])

        result = nn.utils.clip_grad_norm_(x, max_norm=3.0)
        output=x.grad
        """
    )
    obj.run(pytorch_code, ["result", "output"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.tensor([[[[-0.4106,  0.1677], [-0.6648, -0.5669]]]])
        x.grad = torch.tensor([[[[-0.6, 12.343], [-10.4, -0.5669]]]])

        result = nn.utils.clip_grad_norm_(x, max_norm=3.0, norm_type=2.0, error_if_nonfinite=True)
        output=x.grad
        """
    )
    obj.run(pytorch_code, ["result", "output"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.tensor([[[[-0.4106,  0.1677], [-0.6648, -0.5669]]]])
        linear = nn.Linear(in_features=2, out_features=5)
        output = linear(x)
        loss = torch.mean(output)
        loss.backward()

        result = nn.utils.clip_grad_norm_(linear.parameters(), max_norm=3.0, norm_type=2.0, error_if_nonfinite=True)
        output = list(linear.parameters())[1].grad
        """
    )
    obj.run(pytorch_code, ["result", "output"], check_stop_gradient=False)


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn as nn
        x = torch.ones([10, 2])
        linear = nn.Linear(in_features=2, out_features=5)
        output = linear(x)
        loss = torch.mean(output)
        loss.backward()

        result = nn.utils.clip_grad_norm_(linear.parameters(), max_norm=0.5, norm_type=1.0, error_if_nonfinite=True)
        output = list(linear.parameters())[1].grad
        """
    )
    obj.run(pytorch_code, ["result", "output"], check_stop_gradient=False)
