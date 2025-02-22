from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

def mesg(message):
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "deepseek/deepseek-r1:free",
        # google/gemini-2.0-flash-001
        "messages": [
        {
            "role": "user",
            "content": message
        }
        ],
        
    })
    )

    if response.status_code == 200:
        result = response.json()
        if 'choices' in result:
            return result['choices'][0]['message']['content']
        else:
            return "No 'choices' in response:", result

    else:
        return f"Error: {response.status_code}, {response.text}"

def send_message(request):
    if request.method == "POST":
        data = request.POST.get("mess", "")
        bot_response = mesg(data)  # Replace this with AI response logic
        return JsonResponse({"bot_response": bot_response})  # Send response as JSON
    return JsonResponse({"error": "Invalid request"}, status=400)

def index(request):
    return render(request,"index.html");
