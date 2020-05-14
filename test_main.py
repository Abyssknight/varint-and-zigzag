from main import VarInt, ZigZag


class TestVarInt:
    @staticmethod
    def test_encode():
        assert VarInt.encode(127).hex() == '7f'
        assert VarInt.encode(500).hex() == 'f403'
        assert VarInt.encode(1337).hex() == 'b90a'

    @staticmethod
    def test_decode():
        assert VarInt.decode(bytes.fromhex('7f')) == 127
        assert VarInt.decode(bytes.fromhex('f403')) == 500


class TestZigZag:
    def test_encode(self):
        assert ZigZag.encode(157) == VarInt.encode(314)
        assert ZigZag.encode(-250) == VarInt.encode(499)

    def test_decode(self):
        bytes_value = VarInt.encode(500)
        assert ZigZag.decode(bytes_value) == 250

        bytes_value = VarInt.encode(499)
        assert ZigZag.decode(bytes_value) == -250
