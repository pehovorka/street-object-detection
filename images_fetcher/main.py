import urllib.request
import urllib.parse
import json
import base64
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from google.cloud import storage


def get_images_from_all_cameras():
    cameras_list_url = "https://bezpecnost.praha.eu/Intens.CrisisPortalInfrastructureApp/cameras?format=json"
    req = urllib.request.Request(cameras_list_url, data=None, headers={
        "User-Agent": "Chrome"})
    res = urllib.request.urlopen(req)
    cameras = json.load(res)["cameras"]

    for camera in cameras:
        camera_url = f"https://bezpecnost.praha.eu/Intens.CrisisPortalInfrastructureApp/cameras/{camera['id']}/image?"
        download_decode_save_image(camera_url, camera['name'], "images")


def download_decode_save_image(url: str, name: str = "image", path: str = ".",):
    req = urllib.request.Request(url, data=None, headers={
        "User-Agent": "Chrome"})
    res = urllib.request.urlopen(req)
    base64image = json.load(res)['contentBase64']

    filename = f"{path}/{name}.jpg"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as fh:
        fh.write(base64.b64decode(base64image))


def download_decode_save_to_bucket_image(url: str, name: str = "image", bucket: str = "theatre_dataset_images"):

    storage_client = storage.Client(project="ml-semestralka")
    bucket = storage_client.get_bucket(bucket)
    blob = bucket.blob(f'{name}.jpg')

    req = urllib.request.Request(url, data=None, headers={
        "User-Agent": "Chrome"})
    res = urllib.request.urlopen(req)
    base64image = json.load(res)['contentBase64']
    file = base64.b64decode(base64image)

    temp_location = "/tmp/image.jpg"
    os.makedirs(os.path.dirname(temp_location), exist_ok=True)
    with open(temp_location, "wb") as fh:
        fh.write(file)
    with open(temp_location, 'rb') as jpg:
        blob.upload_from_file(jpg, True, None, "image/jpg")


def download_national_theatre_image(data=None, context=None):
    url = "https://bezpecnost.praha.eu/Intens.CrisisPortalInfrastructureApp/cameras/500046/image"
    current_time = datetime.now(ZoneInfo("Europe/Prague"))
    download_decode_save_to_bucket_image(
        url, current_time.strftime("%Y-%m-%d %H:%M:%S"))
    return "Success!"
