from main import VarInt, ZigZag


class TestVarInt:
    @staticmethod
    def test_encode():
        assert VarInt.encode(127) == b'\x7f'  # 01111111
        assert VarInt.encode(500) == b'\x83t'  # 10000011 01110100

    @staticmethod
    def test_decode():
        assert VarInt.decode(b'\x7f') == 127
        assert VarInt.decode(b'\x83t') == 500


class TestZigZag:
    def test_encode(self):
        assert ZigZag.encode(157) == VarInt.encode(314)
        assert ZigZag.encode(-250) == VarInt.encode(499)

    def test_decode(self):
        bytes_value = VarInt.encode(500)
        assert ZigZag.decode(bytes_value) == 250

        bytes_value = VarInt.encode(499)
        assert ZigZag.decode(bytes_value) == -250
