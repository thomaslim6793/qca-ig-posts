import requests
import json
import os
from datetime import datetime

# Define variables required for using Unsplash API
ACCESS_KEY = "JojQg5MlI4bH3scg1sQN4Am9-ytvq0Xw-eezzWx5tvE"
SECRET_KEY = "trgN82fiIFdISXYIhnQscbgtI4jUuYhdDciwvmHV8-c"
END_POINT = "https://api.unsplash.com/search/photos"

# Basic querying function 
def search_unsplash(query, page=1, per_page=10):
    """
    Search for photos on Unsplash based on the given query.

    Parameters:
    - query (str): The search term to use for the query.
    - page (int, optional): The page number to fetch. Default is 1.
    - per_page (int, optional): Number of items per page. Default is 10.
    
    Returns:
    - dict: JSON response from the Unsplash API containing details about 
            the photos that match the query, as well as metadata about 
            the search results.
    """
    headers = {
        'Authorization': f'Client-ID {ACCESS_KEY}'
    }
    
    params = {
        'query': query,
        'page': page,
        'per_page': per_page
    }
    
    response = requests.get(END_POINT, headers=headers, params=params)
    response.raise_for_status()  # Check if the request was successful
    return response.json()



# Example usage, fetch the first 100 images when querying "black lives matter"
# result = search_unsplash("black lives matter", page=1, per_page=100)
# print(result)


# Filter JSON response by date. 
def filter_by_date(json_response, start, end):
    """
    Filters images from the JSON response based on their 'created_at' date.
    
    Parameters:
    - json_response (dict): The JSON response from the Unsplash API.
    - start (str): The start date in 'YYYY-MM-DD' format.
    - end (str): The end date in 'YYYY-MM-DD' format.
    
    Returns:
    - list: A list of images filtered by the date criteria.
    """
    
    filtered_images = []

    # Convert start and end strings to date objects
    start_date = datetime.strptime(start, "%Y-%m-%d").date()
    end_date = datetime.strptime(end, "%Y-%m-%d").date()

    for image in json_response.get("results", []):
        image_date_str = image.get("created_at", "").split("T")[0]  # Extract the date part
        image_date = datetime.strptime(image_date_str, "%Y-%m-%d").date()

        if start_date <= image_date <= end_date:
            filtered_images.append(image)
    
    return filtered_images

# Example usage:
# result = search_unsplash("black lives matter", page=1, per_page=100)
# filtered_images = filter_by_date(result, "2020-05-01", "2020-12-31"


# Get n images given a query and date range
def query_in_date_range(query, start, end, count):
    """
    Queries the Unsplash API for images based on the given search term and filters them by date.
    
    Parameters:
    - query (str): The search term.
    - start (str): The start date in 'YYYY-MM-DD' format.
    - end (str): The end date in 'YYYY-MM-DD' format.
    - count (int): The number of images to retrieve.
    
    Returns:
    - str: A JSON string containing the list of images filtered by the date criteria.
    """
    
    collected_images = []
    page = 1
    per_page = 100  # Maximum allowed by most APIs for a single request

    while len(collected_images) < count:
        response = search_unsplash(query, page=page, per_page=per_page)
        filtered = filter_by_date(response, start, end)
        
        collected_images.extend(filtered)
        
        # Check if we've collected enough images or if there are no more results
        if len(filtered) == 0 or len(collected_images) >= count:
            break
        
        page += 1

    # Create a dictionary with the desired structure
    response_data = {
        'results': collected_images[:count],
        'total': len(collected_images[:count])
    }

    # Convert the dictionary to a JSON string
    return json.dumps(response_data)

# Example usage:
# json_response = query_in_date_range("black lives matter", "2020-05-01", "2020-12-31", 100)
# print(json_response)

# A function (for sanity check) containing dates of the images in json response. 
def list_of_dates_of_images(json_response) -> list:
    """
    Extracts the 'created_at' dates from the given JSON response.
    
    Parameters:
    - json_response (str): The JSON response containing image details.
    
    Returns:
    - list: A list of 'created_at' dates for each image in the response.
    """
    
    # Parse the JSON string to get a dictionary
    data = json.loads(json_response)
    
    # Extract the 'created_at' date for each image
    dates = [image['created_at'] for image in data.get('results', [])]
    
    return dates

# Example usage:
# json_response = query_in_date_range("black lives matter", "2020-05-01", "2020-12-31", 100)
# dates = list_of_dates_of_images(json_response)
# print(dates)

# Given a json response, download images into 'downloads' folder. 
def download_images_from_json(json_response, download_folder='downloads'):
    """
    Downloads images from the given JSON response.
    
    Parameters:
    - json_response (str): The JSON response containing image URLs.
    - download_folder (str, optional): The folder where images will be saved. Default is 'downloads'.
    
    Returns:
    - list: A list of file paths where images were saved.
    """
    
    # Parse the JSON string to get a dictionary
    data = json.loads(json_response)
    
    # Create the download folder if it doesn't exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    saved_files = []

    # Add a loop counter for auto-indexing
    for index, image in enumerate(data.get('results', []), start=1):
        # Create a filename using the loop counter
        filename = os.path.join(download_folder, f'image{index}.jpg')
        
        # Assuming the 'urls' field contains a 'full' subfield with the image URL
        image_url = image['urls']['full']
        
        # Download the image
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Raise an error for bad responses

        # Save the image to the file
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        saved_files.append(filename)

    return saved_files

# Example usage:
# json_response = query_in_date_range("black lives matter", "2020-05-01", "2020-12-31", 100)
# downloaded_files = download_images_from_json(json_response)
# print(downloaded_files)

import argparse 

parser = argparse.ArgumentParser(description="Download images from Unsplashed API based on search query and date range")

parser.add_argument("--title", type=str, required=True, help="Search query for Unsplash")
parser.add_argument("--start-date", type=str, required=True, help="Start date in YYYY-MM-DD format")
parser.add_argument("--end-date", type=str, required=True, help="End date in YYYY-MM-DD format")
parser.add_argument("--num_images", type=int, required=True, help="Number of images to download")

args = parser.parse_args()
json_response = query_in_date_range(args.title, args.start_date, args.end_date, args.num_images)
download_images_from_json(json_response)



