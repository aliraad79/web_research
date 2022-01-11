import requests

package_name = "com.nbadigital.gametimelite"
data = {
    "properties": {
        "language": 2,
        "clientVersion": "web",
    },
    "singleRequest": {"appDetailsV2Request": {"packageName": package_name}},
}

response = requests.post(
    "https://api.cafebazaar.ir/rest-v1/process/AppDetailsV2Request",
    json=data,
)

apps_rows = response.json()["singleReply"]["appDetailsV2Reply"]["extraContentPageBodyInfo"]["pageBody"]["rows"]
for i in apps_rows:
    for j in i["simpleAppList"]["apps"]:
        info = j["info"]
        print(info["packageName"], info["rate"])
