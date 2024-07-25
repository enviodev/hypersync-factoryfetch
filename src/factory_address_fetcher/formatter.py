import polars as pl

def format_events():
    data = pl.read_parquet("data/decoded_logs.parquet")
    
    pool_addresses = data.select(pl.col('proxy'))
    
    formatted_addresses = pool_addresses.with_columns(
        (pl.lit("0x") + pl.col('proxy')).alias('formatted_proxy')
    )
    
    with open('formatted_proxy_addresses.txt', 'w') as f:
        for address in formatted_addresses['formatted_proxy']:
            f.write(f'          - {address}\n')