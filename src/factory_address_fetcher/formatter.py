import polars as pl

def format_events():
    data = pl.read_parquet("data-univ2-blast/decoded_logs.parquet")
    print(len(data))
    pool_addresses = data.select(pl.col('pair'))
    
    formatted_addresses = pool_addresses.with_columns(
        (pl.lit("0x") + pl.col('pair')).alias('formatted_pool')
    )
    
    with open('formatted_pool_addresses.txt', 'w') as f:
        for address in formatted_addresses['formatted_pool']:
            f.write(f'- {address}\n')