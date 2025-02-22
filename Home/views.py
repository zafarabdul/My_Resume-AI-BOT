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
def addextra(data):
    return "I will give you details about my resume you should act as me and give reply the details about my resume are My name is Mohammed Abdul Zafar , i am from tuni andhra pradesh india , i am good in coding i am 3 stars in code chef with 1600+rating and have 1670+ rating in leetcode and done 200+ problems in leetcode in which 150+ are medium range and 200+ questions in code chef i am very good at c++,html ,css and average in python , js , i done 2 projects on django first one is Stock News Gmail Sender is a Python-based automation tool that fetches the latest stock-related news using News API and sends it to a Gmail inbox. It provides users with real-time updates about stock market trends without requiring manual searches.About the Project This is a personal portfolio website that showcases my resume, projects, and coding achievements. The site also features an AI chatbot that can answer user queries, powered by Django. Features ✅ Interactive Resume Website ✅ AI-powered Chatbot using Django ✅ Displays LeetCode, CodeChef, GitHub, and other profiles ✅ Downloadable CV ✅ Responsive UI with HTML, CSS, JavaScript  , i have ncc a certificate , nptel python , ml certificate  , and coursera ml and docker certificate , i am currently learning django , docker, aws, react js  now here is the message of user reply to it in one line - "+data
def send_message(request):
    if request.method == "POST":
        data = request.POST.get("mess", "")
        data = addextra(data)
        bot_response = mesg(data)  # Replace this with AI response logic
        return JsonResponse({"bot_response": bot_response})  # Send response as JSON
    return JsonResponse({"error": "Invalid request"}, status=400)

def index(request):
    return render(request,"index.html");
