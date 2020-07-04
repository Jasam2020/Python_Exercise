import requests

response = requests.get("http://ec2-3-19-239-145.us-east-2.compute.amazonaws.com/health.html")
print(response)
