from dask_cuda import LocalCUDACluster
from distributed import Client
import cudf
import time

if __name__ == '__main__':
    cluster = LocalCUDACluster()
    client = Client(cluster)
    print(client)

    # Create a simple dataframe
    print("Readings 'names' published dataset from another process")
    gdf = client.get_dataset('names')
    print(gdf.head())