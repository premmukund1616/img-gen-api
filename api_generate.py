# api_generate.py

import json
import httpx

API_KEY = "v1-Z0FBQUFBQmxRV2p3Y0NzWUtuOTBLTGFrSFJrZlAtY2lGNFlSUW1JcnJ0Zzk3Z0o2d0xlNkY5VmJHMUQ2Zk1EbUUtZVRHOFpuY3FrZC0xMl9hM29ZX2Q4MzYweTZzMTFMUmc9PQ=="
IMAGE_GEN_API_URL = f"https://backend.buildpicoapps.com/aero/run/image-generation-api?pk={API_KEY}"

def handler(request):
    try:
        body = json.loads(request.body)
        prompt = body.get("message")

        if not prompt:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'message' in request body"})
            }

        payload = {"prompt": prompt}
        headers = {"Content-Type": "application/json"}

        response = httpx.post(IMAGE_GEN_API_URL, headers=headers, json=payload)

        if response.status_code != 200:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Image generation failed"})
            }

        image_url = response.json().get("image_url")

        return {
            "statusCode": 200,
            "body": json.dumps({"image_url": image_url})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
