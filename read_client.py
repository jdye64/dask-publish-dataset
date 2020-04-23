from distributed import Client
import cudf
import time

if __name__ == '__main__':
    client = Client('localhost:8786')
    print(client)

    # Create a simple dataframe
    print("Readings 'names' published dataset from another process")
    gdf = client.get_dataset('names')
    print(gdf.head())