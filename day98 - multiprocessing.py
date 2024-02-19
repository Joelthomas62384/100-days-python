import multiprocessing
import requests
import os
from concurrent.futures import ProcessPoolExecutor

# Function to download a file from a given URL
def download_file(url):
    filename = os.path.basename(url)  # Extract filename from URL
    print(f"Started downloading {filename}")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        with open(f"files/{filename}", "wb") as f:
            f.write(response.content)
        print(f"Finished downloading {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

if __name__ == "__main__":
    # List of URLs to download files from
    urls = [
        "https://i.redd.it/idmbv0oydf671.jpg",
        "https://images.hdqwalls.com/wallpapers/looking-far-away-4k-lb.jpg"
    ]


    # processes = []
    # for url in urls:
    #     p = multiprocessing.Process(target=download_file, args=(url,))
    #     p.start()
    #     processes.append(p)

    # # Wait for all processes to finish
    # for p in processes:
    #     p.join()

    with ProcessPoolExecutor() as executor:
        results = executor.map(download_file,urls)
        for r in results:
            print(r)

