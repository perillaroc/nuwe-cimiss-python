# coding=UTF-8
from cma.music.DataQueryClient import DataQueryClient
import click
import pathlib


@click.command()
@click.option("--user", help="user name", required=True)
@click.option("--password", help="password name", required=True)
@click.option("--client-config", help="client config file")
@click.option("--output-dir", help="client config file")
def cli(user, password, output_dir, client_config=None):

    interface_id = "getNafpFileByTime"

    server_id = "NMIC_MUSIC_CMADAAS"

    params = {
        "dataCode": "NAFP_FOR_FTM_KWBC_GLB",
        "time": "20190917000000",
    }

    output_path = pathlib.Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    client = DataQueryClient(configFile=client_config)
    result = client.callAPI_to_downFile(
        user, password, interface_id, params, output_dir
    )

    print(result)


if __name__ == "__main__":
    cli()
