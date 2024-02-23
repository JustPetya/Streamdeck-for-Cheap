import os
from configparser import ConfigParser

script_dir = os.path.dirname(__file__)
this_path = os.path.join(script_dir, "settings.ini")
config = ConfigParser()
config.read(this_path)


class check_backend:
    @staticmethod
    def certificate():
        if "CERT" in config:
            print("Gathering CERT-section.")
            cert_section = config["CERT"]
            get_use_certs_str = cert_section.get("use_certs", "")
            if get_use_certs_str != "false":
                if get_use_certs_str != "true":
                    cert_section["use_certs"] = "false"
                    with open("settings.ini", "w") as configfile:
                        config.write(configfile)
                else:
                    certifi = True
                    return certifi
            else:
                certifi = False
                return certifi
        else:
            print("Gathering CERT-section failed.")
            return False

    @staticmethod
    def usr():
        if "USER" in config:
            print("Gathering USER-section.")
            user_section = config["USER"]
            get_update_str = user_section.get("update", "")
            if get_update_str != "true":
                if get_update_str != "false":
                    user_section["update"] = "true"
                    with open("settings.ini", "w") as configfile:
                        config.write(configfile)
                else:
                    update = False
                    return update
            else:
                update = True
                return update
        else:
            print("Gathering USER-section failed.")
            return False
