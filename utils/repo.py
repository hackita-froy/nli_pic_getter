import os
import urllib.request

USER_HOME = os.path.expanduser("~")
ROOT_IMAGE_PATH = os.path.join(USER_HOME, "nli_images")

""" Creates and saves IE images in IE folder  """
def save_enteties_files(enteties):

    for entity in enteties:
        entity_path = os.path.join(ROOT_IMAGE_PATH, entity.ie_id)
        os.makedirs(entity_path, exist_ok=True)
        for file in entity.files_ids:
            urllib.request.urlretrieve("http://rosetta.nli.org.il/delivery/DeliveryManagerServlet?dps_pid={0}&dps_func=stream"
                                       .format(file), entity_path+"/{0}.jpg".format(file))
            print("wrote {0}".format(entity_path+"/{0}.jpg".format(file)))
            with open(entity_path+"/title.text", "w") as text_file:
                text_file.write(entity.title)