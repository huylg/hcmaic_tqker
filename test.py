import requests
response = requests.get("http://giaothong.hochiminhcity.gov.vn/expandcameraplayer/?camId=5f000ab3942cda00169ee00b&camLocation=Ba%20Th%C3%A1ng%20Hai%20-%20L%C3%BD%20Th%C6%B0%E1%BB%9Dng%20Ki%E1%BB%87t%202&camMode=camera&videoUrl=https://d2zihajmogu5jn.cloudfront.net/bipbop-advanced/bipbop_16x9_variant.m3u8")

file = open("sample_image.png", "wb")
file.write(response.content)
file.close()
