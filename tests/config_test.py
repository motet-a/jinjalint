import tempfile

from jinjalint.config import parse_config


def test_parse_config():
    with tempfile.NamedTemporaryFile() as f:
        f.write(b'hello = "worl" + "d"\n')
        f.seek(0)
        config = parse_config(f.name)
        assert config == {'hello': 'world'}
