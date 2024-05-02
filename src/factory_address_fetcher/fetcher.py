import hypersync
from hypersync import LogSelection, LogField, DataType, FieldSelection, ColumnMapping, TransactionField
import asyncio

async def collect_events():
    # choose network
    client = hypersync.HypersyncClient("https://blast.hypersync.xyz")

    query = hypersync.Query(
        from_block=0,
        # Select the logs we want
        logs=[LogSelection(
            address=["0x5C346464d33F90bABaf70dB6388507CC889C1070"], # uniswap factory
            topics=[["0x0d3648bd0f6ba80134a33ba9275ac585d9d315f0ad8355cddefde31afa28d0e9"]],
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
                TransactionField.BLOCK_NUMBER,
            ]
        ),
    )

    config = hypersync.ParquetConfig(
        path="data-univ2-blast",
        hex_output=True, 
        batch_size=50000,
        concurrency=12,
        event_signature="PairCreated(address indexed token0, address indexed token1, address pair, uint random)",
    )

    await client.create_parquet_folder(query, config)


def main():
    asyncio.run(collect_events())
