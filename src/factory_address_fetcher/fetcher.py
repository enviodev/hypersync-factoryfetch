import hypersync
from hypersync import LogSelection, LogField, DataType, FieldSelection, ColumnMapping, TransactionField
import asyncio

async def collect_events():
    # choose network
    client = hypersync.HypersyncClient("https://polygon.hypersync.xyz")

    query = hypersync.Query(
        from_block=0,
        # Select the logs we want
        logs=[LogSelection(
            address=["0x1F98431c8aD98523631AE4a59f267346ea31F984"], # uniswap factory
            topics=[["0x783cca1c0412dd0d695e784568c96da2e9c22ff989357a2e8b1d9b2b4e6b7118"]],
        )], 
        # Select the fields and tables we want
        field_selection=FieldSelection(
            log=[
                LogField.TOPIC0,
                LogField.TOPIC1,
                LogField.TOPIC2,
                LogField.TOPIC3,
                LogField.DATA,
                LogField.TRANSACTION_HASH,
            ],
            transaction=[
                # TransactionField.HASH,
                TransactionField.BLOCK_NUMBER,
            ]
        ),
    )

    config = hypersync.ParquetConfig(
        path="data",
        hex_output=True, 
        batch_size=1000000,
        concurrency=10,
        # column_mapping=ColumnMapping(
        #     # map value columns to float so we can do calculations with them
        #     decoded_log={
        #         "pool": DataType.FLOAT64,
        #     },
        #     transaction={
        #         TransactionField.BLOCK_NUMBER: DataType.,
        #     },
        # ),
        # give event signature so client can decode logs into decoded_logs.parquet file
        event_signature="PoolCreated(address indexed token0, address indexed token1, uint24 indexed fee, int24 tickSpacing, address pool)",
    )

    await client.create_parquet_folder(query, config)


def main():
    asyncio.run(collect_events())
