import hypersync
from hypersync import LogSelection, LogField, DataType, FieldSelection, ColumnMapping, TransactionField
import asyncio

async def collect_events():
    # choose network
    client = hypersync.HypersyncClient("https://gnosis.hypersync.xyz")

    query = hypersync.Query(
        from_block=0,
        # Select the logs we want
        logs=[LogSelection(
            # address=["0x9a47d4aE8f7C2075c2a953d9061aea14E23863E8", "0xE9f67C79700137Fe053276F0654423a19a302c69","0x97c599819C95Aaf1BBC9063f4c743cCfCE7bc591", "0x450Fc3eAc8b847a759Cb05790cE7A1f465ac0cE8","0x3D529c760F3EC4c89Bdd6549DDabE9097C1da6e9"], # cometh relayer
            address=["0xa6B71E26C5e0845f74c812102Ca7114b6a896AB2"], 
            topics=[["0x4f51faf6c4561ff95f067657e43439f0f856d97c04d9ec9070a6199ad418e235"]], # hub signup
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
        event_signature="ProxyCreation(address proxy, address singleton)",
    )

    await client.create_parquet_folder(query, config)


def main():
    asyncio.run(collect_events())
