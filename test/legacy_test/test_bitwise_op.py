#   Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.
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

import unittest

import numpy as np
from op_test import OpTest

import paddle

paddle.enable_static()


# ----------------- TEST OP: BitwiseAnd ----------------- #
class TestBitwiseAnd(OpTest):
    def setUp(self):
        self.op_type = "bitwise_and"
        self.python_api = paddle.tensor.logic.bitwise_and
        self.init_dtype()
        self.init_shape()
        self.init_bound()

        x = np.random.randint(
            self.low, self.high, self.x_shape, dtype=self.dtype
        )
        y = np.random.randint(
            self.low, self.high, self.y_shape, dtype=self.dtype
        )
        out = np.bitwise_and(x, y)

        self.inputs = {'X': x, 'Y': y}
        self.outputs = {'Out': out}

    def test_check_output(self):
        self.check_output(
            check_cinn=True, check_pir=True, check_symbol_infer=False
        )

    def test_check_grad(self):
        pass

    def init_dtype(self):
        self.dtype = np.int32

    def init_shape(self):
        self.x_shape = [2, 3, 4, 5]
        self.y_shape = [2, 3, 4, 5]

    def init_bound(self):
        self.low = -100
        self.high = 100


class TestBitwiseAnd_ZeroDim1(TestBitwiseAnd):
    def init_shape(self):
        self.x_shape = []
        self.y_shape = []


class TestBitwiseAnd_ZeroDim2(TestBitwiseAnd):
    def init_shape(self):
        self.x_shape = [2, 3, 4, 5]
        self.y_shape = []


class TestBitwiseAnd_ZeroDim3(TestBitwiseAnd):
    def init_shape(self):
        self.x_shape = []
        self.y_shape = [2, 3, 4, 5]


class TestBitwiseAndUInt8(TestBitwiseAnd):
    def init_dtype(self):
        self.dtype = np.uint8

    def init_bound(self):
        self.low = 0
        self.high = 100


class TestBitwiseAndInt8(TestBitwiseAnd):
    def init_dtype(self):
        self.dtype = np.int8

    def init_shape(self):
        self.x_shape = [4, 5]
        self.y_shape = [2, 3, 4, 5]


class TestBitwiseAndInt16(TestBitwiseAnd):
    def init_dtype(self):
        self.dtype = np.int16

    def init_shape(self):
        self.x_shape = [2, 3, 4, 5]
        self.y_shape = [4, 1]


class TestBitwiseAndInt64(TestBitwiseAnd):
    def init_dtype(self):
        self.dtype = np.int64

    def init_shape(self):
        self.x_shape = [1, 4, 1]
        self.y_shape = [2, 3, 4, 5]


class TestBitwiseAndBool(TestBitwiseAnd):
    def setUp(self):
        self.op_type = "bitwise_and"
        self.python_api = paddle.tensor.logic.bitwise_and

        self.init_shape()

        x = np.random.choice([True, False], self.x_shape)
        y = np.random.choice([True, False], self.y_shape)
        out = np.bitwise_and(x, y)

        self.inputs = {'X': x, 'Y': y}
        self.outputs = {'Out': out}


# ----------------- TEST OP: BitwiseOr ------------------ #
class TestBitwiseOr(OpTest):
    def setUp(self):
        self.op_type = "bitwise_or"
        self.python_api = paddle.tensor.logic.bitwise_or
        self.init_dtype()
        self.init_shape()
        self.init_bound()

        x = np.random.randint(
            self.low, self.high, self.x_shape, dtype=self.dtype
        )
        y = np.random.randint(
            self.low, self.high, self.y_shape, dtype=self.dtype
        )
        out = np.bitwise_or(x, y)

        self.inputs = {'X': x, 'Y': y}
        self.outputs = {'Out': out}

    def test_check_output(self):
        self.check_output(
            check_cinn=True, check_pir=True, check_symbol_infer=False
        )

    def test_check_grad(self):
        pass

    def init_dtype(self):
        self.dtype = np.int32

    def init_shape(self):
        self.x_shape = [2, 3, 4, 5]
        self.y_shape = [2, 3, 4, 5]

    def init_bound(self):
        self.low = -100
        self.high = 100


class TestBitwiseOr_ZeroDim1(TestBitwiseOr):
    def init_shape(self):
        self.x_shape = []
        self.y_shape = []


class TestBitwiseOr_ZeroDim2(TestBitwiseOr):
    def init_shape(self):
        self.x_shape = [2, 3, 4, 5]
        self.y_shape = []


class TestBitwiseOr_ZeroDim3(TestBitwiseOr):
    def init_shape(self):
        self.x_shape = []
        self.y_shape = [2, 3, 4, 5]


class TestBitwiseOrUInt8(TestBitwiseOr):
    def init_dtype(self):
        self.dtype = np.uint8

    def init_bound(self):
        self.low = 0
        self.high = 100


class TestBitwiseOrInt8(TestBitwiseOr):
    def init_dtype(self):
        self.dtype = np.int8

    def init_shape(self):
        self.x_shape = [4, 5]
        self.y_shape = [2, 3, 4, 5]


class TestBitwiseOrInt16(TestBitwiseOr):
    def init_dtype(self):
        self.dtype = np.int16

    def init_shape(self):
        self.x_shape = [2, 3, 4, 5]
        self.y_shape = [4, 1]


class TestBitwiseOrInt64(TestBitwiseOr):
    def init_dtype(self):
        self.dtype = np.int64

    def init_shape(self):
        self.x_shape = [1, 4, 1]
        self.y_shape = [2, 3, 4, 5]


class TestBitwiseOrBool(TestBitwiseOr):
    def setUp(self):
        self.op_type = "bitwise_or"
        self.python_api = paddle.tensor.logic.bitwise_or

        self.init_shape()

        x = np.random.choice([True, False], self.x_shape)
        y = np.random.choice([True, False], self.y_shape)
        out = np.bitwise_or(x, y)

        self.inputs = {'X': x, 'Y': y}
        self.outputs = {'Out': out}


# ----------------- TEST OP: BitwiseXor ---------------- #
class TestBitwiseXor(OpTest):
    def setUp(self):
        self.op_type = "bitwise_xor"
        self.python_api = paddle.tensor.logic.bitwise_xor

        self.init_dtype()
        self.init_shape()
        self.init_bound()

        x = np.random.randint(
            self.low, self.high, self.x_shape, dtype=self.dtype
        )
        y = np.random.randint(
            self.low, self.high, self.y_shape, dtype=self.dtype
        )
        out = np.bitwise_xor(x, y)

        self.inputs = {'X': x, 'Y': y}
        self.outputs = {'Out': out}

    def test_check_output(self):
        self.check_output(
            check_cinn=True, check_pir=True, check_symbol_infer=False
        )

    def test_check_grad(self):
        pass

    def init_dtype(self):
        self.dtype = np.int32

    def init_shape(self):
        self.x_shape = [2, 3, 4, 5]
        self.y_shape = [2, 3, 4, 5]

    def init_bound(self):
        self.low = -100
        self.high = 100


class TestBitwiseXor_ZeroDim1(TestBitwiseXor):
    def init_shape(self):
        self.x_shape = []
        self.y_shape = []


class TestBitwiseXor_ZeroDim2(TestBitwiseXor):
    def init_shape(self):
        self.x_shape = [2, 3, 4, 5]
        self.y_shape = []


class TestBitwiseXor_ZeroDim3(TestBitwiseXor):
    def init_shape(self):
        self.x_shape = []
        self.y_shape = [2, 3, 4, 5]


class TestBitwiseXorUInt8(TestBitwiseXor):
    def init_dtype(self):
        self.dtype = np.uint8

    def init_bound(self):
        self.low = 0
        self.high = 100


class TestBitwiseXorInt8(TestBitwiseXor):
    def init_dtype(self):
        self.dtype = np.int8

    def init_shape(self):
        self.x_shape = [4, 5]
        self.y_shape = [2, 3, 4, 5]


class TestBitwiseXorInt16(TestBitwiseXor):
    def init_dtype(self):
        self.dtype = np.int16

    def init_shape(self):
        self.x_shape = [2, 3, 4, 5]
        self.y_shape = [4, 1]


class TestBitwiseXorInt64(TestBitwiseXor):
    def init_dtype(self):
        self.dtype = np.int64

    def init_shape(self):
        self.x_shape = [1, 4, 1]
        self.y_shape = [2, 3, 4, 5]


class TestBitwiseXorBool(TestBitwiseXor):
    def setUp(self):
        self.op_type = "bitwise_xor"
        self.python_api = paddle.tensor.logic.bitwise_xor

        self.init_shape()

        x = np.random.choice([True, False], self.x_shape)
        y = np.random.choice([True, False], self.y_shape)
        out = np.bitwise_xor(x, y)

        self.inputs = {'X': x, 'Y': y}
        self.outputs = {'Out': out}


# ---------------  TEST OP: BitwiseNot ----------------- #
class TestBitwiseNot(OpTest):
    def setUp(self):
        self.op_type = "bitwise_not"
        self.python_api = paddle.tensor.logic.bitwise_not

        self.init_dtype()
        self.init_shape()
        self.init_bound()

        x = np.random.randint(
            self.low, self.high, self.x_shape, dtype=self.dtype
        )
        out = np.bitwise_not(x)

        self.inputs = {'X': x}
        self.outputs = {'Out': out}

    def test_check_output(self):
        self.check_output(
            check_cinn=True, check_pir=True, check_symbol_infer=False
        )

    def test_check_grad(self):
        pass

    def init_dtype(self):
        self.dtype = np.int32

    def init_shape(self):
        self.x_shape = [2, 3, 4, 5]

    def init_bound(self):
        self.low = -100
        self.high = 100


class TestBitwiseNot_ZeroDim(TestBitwiseNot):
    def init_shape(self):
        self.x_shape = []


class TestBitwiseNotUInt8(TestBitwiseNot):
    def init_dtype(self):
        self.dtype = np.uint8

    def init_bound(self):
        self.low = 0
        self.high = 100


class TestBitwiseNotInt8(TestBitwiseNot):
    def init_dtype(self):
        self.dtype = np.int8

    def init_shape(self):
        self.x_shape = [4, 5]


class TestBitwiseNotInt16(TestBitwiseNot):
    def init_dtype(self):
        self.dtype = np.int16

    def init_shape(self):
        self.x_shape = [2, 3, 4, 5]


class TestBitwiseNotInt64(TestBitwiseNot):
    def init_dtype(self):
        self.dtype = np.int64

    def init_shape(self):
        self.x_shape = [1, 4, 1]


class TestBitwiseNotBool(TestBitwiseNot):
    def setUp(self):
        self.op_type = "bitwise_not"
        self.python_api = paddle.tensor.logic.bitwise_not
        self.init_shape()

        x = np.random.choice([True, False], self.x_shape)
        out = np.bitwise_not(x)

        self.inputs = {'X': x}
        self.outputs = {'Out': out}


class TestBitwiseInvertApi(unittest.TestCase):
    def setUp(self):
        paddle.disable_static()

        self.dtype = np.int32
        self.shape = [2, 3, 4, 5]
        self.low = -100
        self.high = 100
        x = np.random.randint(self.low, self.high, self.shape, dtype=self.dtype)
        self.x = paddle.to_tensor(x)
        self.expected_out = np.bitwise_not(x)

    def test_bitwise_invert_out_of_place(self):
        result = paddle.bitwise_invert(self.x)
        np.testing.assert_array_equal(result.numpy(), self.expected_out)

    def test_bitwise_invert_in_place(self):
        x_copy = self.x.clone()
        x_copy.bitwise_invert_()
        np.testing.assert_array_equal(x_copy.numpy(), self.expected_out)


class TestBitwiseRorApi(unittest.TestCase):
    def setUp(self):
        paddle.disable_static()

        self.dtype = np.int64
        self.shape = [2, 3, 4, 5]
        self.low = -100
        self.high = 100
        self.np_x = np.random.randint(
            self.low, self.high, self.shape, dtype=self.dtype
        )
        self.pp_x = paddle.to_tensor(self.np_x)

    def test_bitwise_or_python_int(self):
        np_y = 4
        expected_out = np_y | self.np_x
        result = np_y | self.pp_x
        np.testing.assert_array_equal(result.numpy(), expected_out)

    def test_bitwise_or_python_bool(self):
        np_y = True
        expected_out = np_y | self.np_x
        result = np_y | self.pp_x
        np.testing.assert_array_equal(result.numpy(), expected_out)

    def test_bitwise_or_python_float_error(self):
        np_y = 3.5  # float should raise an error
        with self.assertRaises(TypeError):
            _ = np_y | self.pp_x

    def test_bitwise_or_tensor_zero_dim(self):
        np_y = np.random.randint(self.low, self.high, dtype=self.dtype)
        pp_y = paddle.to_tensor(np_y)
        expected_out = np_y | self.np_x
        result = pp_y | self.pp_x
        np.testing.assert_array_equal(result.numpy(), expected_out)

    def test_bitwise_or_tensor_int8(self):
        np_y = np.random.randint(self.low, self.high, self.shape, dtype=np.int8)
        pp_y = paddle.to_tensor(np_y, dtype='int8')
        expected_out = np_y | self.np_x.astype(np.int8)
        result = pp_y | self.pp_x.astype('int8')
        np.testing.assert_array_equal(result.numpy(), expected_out)

    def test_bitwise_or_tensor_int16(self):
        np_y = np.random.randint(
            self.low, self.high, self.shape, dtype=np.int16
        )
        pp_y = paddle.to_tensor(np_y, dtype='int16')
        expected_out = np_y | self.np_x.astype(np.int16)
        result = pp_y | self.pp_x.astype('int16')
        np.testing.assert_array_equal(result.numpy(), expected_out)

    def test_bitwise_or_tensor_int32(self):
        np_y = np.random.randint(
            self.low, self.high, self.shape, dtype=np.int32
        )
        pp_y = paddle.to_tensor(np_y, dtype='int32')
        expected_out = np_y | self.np_x.astype(np.int32)
        result = pp_y | self.pp_x.astype('int32')
        np.testing.assert_array_equal(result.numpy(), expected_out)

    def test_bitwise_or_tensor_int64(self):
        np_y = np.random.randint(
            self.low, self.high, self.shape, dtype=np.int64
        )
        pp_y = paddle.to_tensor(np_y, dtype='int64')
        expected_out = np_y | self.np_x
        result = pp_y | self.pp_x
        np.testing.assert_array_equal(result.numpy(), expected_out)

    def test_bitwise_or_tensor_uint8(self):
        np_y = np.random.randint(0, 255, self.shape, dtype=np.uint8)
        pp_y = paddle.to_tensor(np_y, dtype='uint8')
        expected_out = np_y | self.np_x.astype(np.uint8)
        result = pp_y | self.pp_x.astype('uint8')
        np.testing.assert_array_equal(result.numpy(), expected_out)

    def test_bitwise_or_tensor_bool(self):
        np_y = np.random.choice([True, False], size=self.shape)
        pp_y = paddle.to_tensor(np_y, dtype='bool')
        expected_out = np_y | self.np_x.astype(bool)
        result = pp_y | self.pp_x.astype('bool')
        np.testing.assert_array_equal(result.numpy(), expected_out)


if __name__ == "__main__":
    unittest.main()
