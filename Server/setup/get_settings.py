from configparser import ConfigParser

config = ConfigParser()


class check_backend:
    @staticmethod
    def _certificate():
        config.read("settings.ini")
        cert = config["CERT"]
        get_use_certs_str = cert.get("use_certs", "")
        if get_use_certs_str != "false":
            if get_use_certs_str != "true":
                cert["use_certs"] = "false"
                with open("settings.ini", "w") as configfile:
                    config.write(configfile)
            else:
                certifi = True
                return certifi
        else:
            certifi = False
            return certifi

    @staticmethod
    def _usr():
        user = config["USER"]
        get_update_str = user.get("update", "")
        if get_update_str != "true":
            if get_update_str != "false":
                user["update"] = "true"
                with open("settings.ini", "w") as configfile:
                    config.write(configfile)
            else:
                update = False
                return update
        else:
            update = True
            return update


def _check_content():
    config.read("settings.ini")
    content = config["CONTENT"]
    get_discord_str = content.get("discord", "")
    if get_discord_str != "true":
        if get_discord_str != "false":
            content["discord"] = "true"
            with open("settings.ini", "w") as configfile:
                config.write(configfile)
        else:
            discord = False
            return discord
    else:
        discord = True
        return discord

    get_filmora_str = content.get("filmora", "")
    if get_filmora_str != "true":
        if get_filmora_str != "false":
            content["filmora"] = "true"
            with open("settings.ini", "w") as configfile:
                config.write(configfile)
        else:
            filmora = False
            return filmora
    else:
        filmora = True
        return filmora

    get_music_str = content.get("music", "")
    if get_music_str != "true":
        if get_music_str != "false":
            content["music"] = "true"
            with open("settings.ini", "w") as configfile:
                config.write(configfile)
        else:
            music = False
            return music
    else:
        music = True
        return music

    get_obs_str = content.get("obs", "")
    if get_obs_str != "true":
        if get_obs_str != "false":
            content["obs"] = "true"
            with open("settings.ini", "w") as configfile:
                config.write(configfile)
        else:
            obs = False
            return obs
    else:
        obs = True
        return obs

    get_screenshot_str = content.get("screenshot", "")
    if get_screenshot_str != "true":
        if get_screenshot_str != "false":
            content["screenshot"] = "true"
            with open("settings.ini", "w") as configfile:
                config.write(configfile)
        else:
            screenshot = False
            return screenshot
    else:
        screenshot = True
        return screenshot

    get_sounds_str = content.get("sounds", "")
    if get_sounds_str != "true":
        if get_sounds_str != "false":
            content["sounds"] = "true"
            with open("settings.ini", "w") as configfile:
                config.write(configfile)
        else:
            sounds = False
            return sounds
    else:
        sounds = True
        return sounds

    get_audio_str = content.get("audio", "")
    if get_audio_str != "true":
        if get_audio_str != "false":
            content["audio"] = "true"
            with open("settings.ini", "w") as configfile:
                config.write(configfile)
        else:
            audio = False
            return audio
    else:
        audio = True
        return audio
