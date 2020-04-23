from distributed import Client
import cudf
import time

if __name__ == '__main__':
    client = Client('localhost:8786')
    print(client)

    # Create a simple dataframe
    gdf = cudf.read_csv('names.csv')
    print(gdf.head())
    client.publish_dataset(names=gdf)

    while(1):
        time.sleep(10)
        print("tick")