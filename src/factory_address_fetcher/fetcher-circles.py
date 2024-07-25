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
            address=["0x29b9a7fBb8995b2423a71cC17cf9810798F6C543"], # circles hub 
            topics=[["0x8451019aab65b4193860ef723cb0d56b475a26a72b7bfc55c1dbd6121015285a"]], # hub signup
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
        event_signature="Signup(address indexed user, address token)",
    )

    await client.create_parquet_folder(query, config)


def main():
    asyncio.run(collect_events())
