from main import VarInt, ZigZag


class TestVarInt:
    @staticmethod
    def test_encode():
        assert VarInt.encode(127) == b'7f'
        assert VarInt.encode(500) == b'f403'
        assert VarInt.encode(1337) == b'b90a'

    @staticmethod
    def test_decode():
        assert VarInt.decode(b'7f') == 127
        assert VarInt.decode(b'f403') == 500


class TestZigZag:
    def test_encode(self):
        assert ZigZag.encode(157) == VarInt.encode(314)
        assert ZigZag.encode(-250) == VarInt.encode(499)

    def test_decode(self):
        bytes_value = VarInt.encode(500)
        assert ZigZag.decode(bytes_value) == 250

        bytes_value = VarInt.encode(499)
        assert ZigZag.decode(bytes_value) == -250
