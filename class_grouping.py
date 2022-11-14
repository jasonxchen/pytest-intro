# pytest class_grouping.py
class TestClass:
    def test_one(self):
        x = "letterx"
        assert "r" in x
        
    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
        