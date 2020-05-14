"""
varint 和 zigzag 算法的实现
"""
from functools import reduce


class VarInt:
    offset = 7
    varint_data_byte_bits = 0x7f
    varint_exists_next_byte_bit = 0x80

    @classmethod
    def encode(cls, int_value: int):
        every_bytes = bytearray()

        while True:
            first_bytes = int_value & cls.varint_data_byte_bits
            if not first_bytes:
                break

            every_bytes.append(first_bytes)
            int_value >>= cls.offset

        for idx in range(len(every_bytes) - 1):
            every_bytes[idx] |= cls.varint_exists_next_byte_bit

        return bytes(every_bytes)

    @classmethod
    def decode(cls, bytes_value: bytes):
        every_bytes = bytearray(bytes_value)

        for idx in range(len(every_bytes) - 1):
            every_bytes[idx] &= cls.varint_data_byte_bits
        every_bytes.reverse()

        return reduce(lambda x, y: x << cls.offset | y, every_bytes)


class ZigZag:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def encode(int_value: int):
        if int_value >= 0:
            return VarInt.encode(int_value * 2)
        else:
            return VarInt.encode(abs(int_value) * 2 - 1)

    @staticmethod
    def decode(bytes_value: bytes):
        int_value = VarInt.decode(bytes_value)
        if ZigZag.is_even(int_value):
            return int_value // 2
        else:
            return -(int_value + 1) // 2
