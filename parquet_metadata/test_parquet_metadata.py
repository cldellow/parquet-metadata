from . import parquet_metadata

def test_smoke_test():
    parquet_metadata.dump('parquets/types.parquet')
