JarvisAI - Modular Voice Assistant
Overview

JarvisAI is a Python-based voice-controlled personal assistant that can perform a variety of tasks, such as:

Searching Wikipedia

Opening websites like YouTube, Google, or StackOverflow

Telling jokes

Providing weather updates

Reading news headlines

Managing apps (open/close)

Remembering user notes

System commands (shutdown, restart, sleep)

It uses speech recognition, text-to-speech, and integrates external APIs for weather and news.

Features
1. Voice Interaction

Jarvis listens to your commands using a microphone.

Speaks responses with natural text-to-speech (TTS).

2. Information Fetching

Wikipedia search: Get summaries of any topic.

News: Fetch top news headlines using NewsAPI.

Weather: Real-time weather updates for any city using OpenWeatherMap API.

3. Web Automation

Open websites like YouTube, Google, or StackOverflow directly via voice commands.

Search Google without typing.

4. App Management

Open or close applications installed on your PC.

Customizable in app_processes dictionary.

5. Entertainment

Tell jokes with pyjokes.

6. Memory

Jarvis can remember notes during runtime and recall them when asked.

7. System Control

Shutdown, restart, or put your PC to sleep with voice commands.

Folder structure 

SmartDeskAI/
│
├── main.py
├── apis.py
├── weather.py
├── news.py
├── memory.txt
├── requirements.txt
└── README.md
