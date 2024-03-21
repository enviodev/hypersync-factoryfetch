import polars as pl

def format_events():
    data = pl.read_parquet("data/decoded_logs.parquet")
    
    pool_addresses = data.select(pl.col('pool'))
    
    formatted_addresses = pool_addresses.with_columns(
        (pl.lit("0x") + pl.col('pool')).alias('formatted_pool')
    )
    
    with open('formatted_pool_addresses.txt', 'w') as f:
        for address in formatted_addresses['formatted_pool']:
            f.write(f'- {address}\n')