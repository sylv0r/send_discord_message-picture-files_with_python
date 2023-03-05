import requests

# User's Token
header = {
    'authorization': "YOUR AUTHORISAZATION",
}

#your message
payload = {
    "content": "your message"
}

#your files
a="files/pic1.jpeg"
b="files/doc.txt"
c="files/pic2.png"
#you can more add files


#id of discord channel
channel1 = "000000000000000000"
channel2 = "000000000000000000"
#you can add more channel


# Channel where we send the message with files
channel_id = [channel1, channel2]


for channel in channel_id:
    # The files that we want to send in binary
    files = {
        "file1": (a, open(a, 'rb')),
        "file2": (b, open(b, 'rb')),
        "file3": (c, open(c, 'rb'))
    }
    r = requests.post(f"https://discord.com/api/v9/channels/{channel}/messages", data=payload, headers=header, files=files)
    print(channel + " send")

