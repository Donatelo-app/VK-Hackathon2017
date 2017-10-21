import jinja2
import requests

get_upload_url = jinja2.Template("https://api.vk.com/method/photos.getOwnerCoverPhotoUploadServer?group_id={{group_id}}&crop_x=0&crop_y=0&crop_x2=1590&crop_y2=400&access_token={{access_token}}&v=5.64")
accept_url = jinja2.Template("https://api.vk.com/method/photos.saveOwnerCoverPhoto?hash={{phash}}&photo={{photo}}&access_token={{access_token}}&v=5.65")

def update_cover(group_id, access_token, cover):
    upload_url = requests.get(get_upload_url.render(group_id=group_id, access_token=access_token)).json()["response"]["upload_url"].replace("\\", "")
    response = requests.post(upload_url, files=dict(photo=cover)).json()
    
    accept_hash = response["hash"]
    accept_photo = response["photo"]
    
    requests.get(accept_url.render(phash=accept_hash, photo=accept_photo, access_token=access_token))