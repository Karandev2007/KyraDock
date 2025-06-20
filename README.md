# KyraDock
KyraDock is a smart, voice-activated assistant device — similar to an Echo Show, but built with freedom, speed, and customization in mind. It acts as a personal AI dock powered by advanced language models, designed to sit on your desk and respond instantly to your voice.

## What KyraDock Does
- Wake word activated – Say “Hey Kyra” to activate the assistant anytime.
- Voice command listener – After the wake word, Kyra listens to your commands and executes it.
- AI-powered conversations – Uses Groq’s blazing-fast Mistral model to answer naturally and intelligently.
- Smart talking – Speaks replies clearly using a female voice with interruption support (say “Hey Kyra” again to cut her off).
- Performs tasks – Can run non-verbal actions like system controls, app launches, or custom commands silently using external API on KyraDock or main device (example my laptop)
- External Control - Provides a external control over whole device using external API and web interface.
- Built-in local server – Integrates with a small powerful server capable of hosting websites, applications, etc with GUI support and Voice support.

## How It Works
1. Wake Word Detection (Offline)
Kyra uses a local Picovoice model to detect "Hey Kyra" entirely offline. This keeps response time fast and your data private.

2. Voice Recognition
After the wake word, Kyra listens using your microphone and transcribes your speech using the Google Web Speech API.

3. AI Brain (Groq API)
The query command is sent to Groq’s API model for a natural and smart response.

4. Text-to-Speech
Kyra speaks the answer using pyttsx3, running in a dedicated thread to allow interruptions. So if you change your mind or issue a new command, she’ll stop and listen again.

5. Background Commands & Server
Kyra isn’t just for chatting. She also runs other background tasks – like controlling system functions or triggering remote actions. It includes a small powerful server allowing deploying web applications and control over them using GUI or Voice.

![image](https://github.com/user-attachments/assets/847d73e6-36cc-4ed2-a811-5bd93344610f)
![image](https://github.com/user-attachments/assets/f74e9a25-acca-4d3e-aadd-b86518e19e96)
![image](https://github.com/user-attachments/assets/03c074bd-53fd-4274-bc67-7f8b21d9e39f)


--------------------------------------------------------------------------------------------------
BOM:
| Component | Price (INR) | Price (USD) | Purpose | URL |
| :--- | :--- | :--- | :--- | :--- |
| 5V Mini Fan | ₹80 | $0.93 | Cooling Raspberry Pi | [robocraze](https://robocraze.com/products/5v-mini-fan-for-raspberry-pi?variant=40192541982873) |
| 5″ Inch HDMI Touch LCD | ₹2504 | $29.25 | Display + touch input | [robocraze](https://robocraze.com/products/5-inch-lcd-hdmi-touch-screen-display-tft-lcd-panel-module?variant=40193802895513) |
| SanDisk 64 GB micro-SD Card | ₹569 | $6.60 | Storage for OS/apps | [amazon](https://amzn.in/d/4g1hGiB) |
| HDMI to micro-HDMI Cable | ₹139 | $1.62 | For external use | [robocraze](https://robocraze.com/products/hdmi-to-micro-hdmi-cable?variant=40193636597913) |
| amazon basics 3 Watt Speakers | ₹272 | $3.15 | Audio output | [amazon](https://amzn.in/d/egND9wG) |
| Ambrane Micro USB Cable | ₹149 | $1.73 | Power Input for Display | [amazon](https://amzn.in/d/fEbwvcv) |
| Ambrane Type C USB Cable | ₹169 | $1.96 | Power Input for Raspberry Pi | [amazon](https://amzn.in/d/1RGyZ3g) |
| Wrap Sheet Film | ₹288 | $3.34 | For KyraDock body | [amazon](https://amzn.in/d/ezTv9b7) |
| Glue Sticks | ₹150 | $1.74 | for assembling | [amazon](https://amzn.in/d/bpFMA49) |
| Raspberry Pi 4 Model B (8 GB) | ₹7429 | $86.79 | Main controller board | [robocraze](https://robocraze.com/products/raspberry-pi-4-model-b-8-gb-ram?variant=40193825308825) |
| USB Microphone | ₹567 | $6.58 | Audio input | [amazon](https://amzn.in/d/2ZB8z9S) |
| **Total** | **₹12,316** | **Approx $143** | | |
