from dask_cuda import LocalCUDACluster
from distributed import Client
import cudf
import time

if __name__ == '__main__':
    cluster = LocalCUDACluster()
    client = Client(cluster)
    print(client)

    # Create a simple dataframe
    gdf = cudf.read_csv('names.csv')
    print(gdf.head())
    client.publish_dataset(names=gdf)

    while(1):
        time.sleep(10)
        print("tick")