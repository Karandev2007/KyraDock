# <img src="https://github.com/user-attachments/assets/a8f2f3c1-0965-422e-9f21-fbb6588ca2df" alt="KyraAI" width="25" height="25" /> KyraDock - Smart AI Assistant Device 
![image](https://github.com/user-attachments/assets/eb03c991-78ed-4b81-a80c-4fb855df30ae)

---

# **KyraDock**

**KyraDock** is a **developer-focused, AI-powered smart assistant device** — inspired by the **Amazon Echo Show**, but designed with full control, speed, and extensibility in mind. It’s a desktop dock running on a Raspberry Pi that merges a **personal voice assistant**, a **Custom Deployment Environment**, **remote control capabilities**, and even **local smart home control**, all into one compact and customizable project.

KyraDock isn’t just a gadget — it’s your own **programmable Smart device**, ready for natural conversations, silent task execution, system automation, home integrations, and advanced control via voice or remote app. Think of it as **your own Echo Show, built for developers**.

---

## **What Makes KyraDock Special**

KyraDock isn’t just another AI assistant. It’s a fully integrated smart assistant device built for developers and privacy-conscious users. Here's what makes it different:

* **Always-On Voice Activation**
  Say “Hey Kyra” at any time to activate the assistant. No buttons, no taps, just your voice.

* **Conversational AI, On Your Terms**
  Kyra understands natural speech and responds using a fast, conversational AI. It supports a local language model for quick replies and offline queries, with fallback to Groq’s API for more complex responses when needed.

* **Interruptible, Natural Voice Output**
  Kyra speaks with a realistic female voice. You can interrupt her mid-sentence by saying the wake word again, allowing fast and fluid interactions.

* **Performs Real Actions**
  Kyra isn’t just about chat. She takes action. Whether it’s fetching the data, launching apps, managing the deployment environment, controlling smart home devices, or executing remote APIs.

* **Modular and Extendable**
  You can expand Kyra’s capabilities with simple Python modules, REST APIs, or even build your own addons.

* **Home Control Ready**
  KyraDock can control smart lights, switches, and other devices directly over Wi-Fi, no cloud or hub required. Perfect for private, local automation.

* **Custom Deployment Environment**
  KyraDock includes a local deployment environment that lets you run and manage apps, dashboards, and automation tools directly on the device. No VPS or internet required — with a cool CLI support!

* **Remote Control Built In**
  A dedicated dashboard and mobile-friendly interface lets you control KyraDock remotely. Whether you're nearby or far away, you can trigger actions, run scripts, or monitor your assistant in real time.

* **Privacy First**
  Wake word detection, basic speech processing, and even AI responses can run locally using lightweight models. Internet access is used only when needed, so your commands stay private.

* **Built for Real-World Use**
  KyraDock supports scheduled actions, background monitoring, interruptible flows, fallback voice AI, and real-time remote triggers.

---

## How KyraDock Works

1. **Wake Word Detection (Offline)**
   Uses a local voice model to continuously listen for “Hey Kyra” without sending any data online.

2. **Speech Recognition**
   After activation, Kyra can transcribe your speech using a local engine or fallback to Google Web Speech for higher accuracy when needed.

3. **AI Processing**
   Handles basic replies locally using a TinyLLM model. For more advanced tasks or fallback, Kyra uses Groq’s API.

4. **Natural Voice Output**
   Kyra responds using pyttsx3 with a soft, human-like voice. She speaks naturally and lets you interrupt at any time by saying the wake word again.

5. **Task Handling and Execution**
   Kyra can perform a wide range of actions, such as:

   * Launching programs or tools
   * Fetching data or weather info
   * Activity tracking
   * Home control
   * Controlling your PC or other devices
   * Notification Center & Smart Reminders, alarms

6. **Built-In Custom Deployment Environment**
   At the core of KyraDock is a built-in Custom Deployment Environment offering user to host, control, keep track and more of its applications with local access and advance CLI & SSH support.

7. **External Control Interface**
   KyraDock will support a full-featured external dashboard and mobile app. This brings all local APIs and functions to your fingertips for secure, real-time control from anywhere.

---

## 🧰 What You’ll Need (Bill of Materials)

| Component                 | Price (INR) | Price (USD) | Purpose                      | Buy Link                                                                                                                     |
| ------------------------- | ----------- | ----------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 5V Mini Fan               | ₹80         | \$0.93      | Cooling Raspberry Pi         | [robocraze](https://robocraze.com/products/5v-mini-fan-for-raspberry-pi?variant=40192541982873)                              |
| 5″ HDMI Touch Screen      | ₹2504       | \$29.25     | Visual Display + Touch Input | [robocraze](https://robocraze.com/products/5-inch-lcd-hdmi-touch-screen-display-tft-lcd-panel-module?variant=40193802895513) |
| 64GB SanDisk micro-SD     | ₹569        | \$6.60      | OS and storage               | [amazon](https://amzn.in/d/4g1hGiB)                                                                                          |
| HDMI to Micro-HDMI Cable  | ₹139        | \$1.62      | For Display                  | [robocraze](https://robocraze.com/products/hdmi-to-micro-hdmi-cable?variant=40193636597913)                                  |
| Amazon Basics 3W Speakers | ₹272        | \$3.15      | Voice Output                 | [amazon](https://amzn.in/d/egND9wG)                                                                                          |
| Ambrane Micro USB Cable   | ₹149        | \$1.73      | Power Display                | [amazon](https://amzn.in/d/fEbwvcv)                                                                                          |
| Ambrane USB Type-C Cable  | ₹169        | \$1.96      | Power Raspberry Pi           | [amazon](https://amzn.in/d/1RGyZ3g)                                                                                          |
| Wrap Sheet Film           | ₹288        | \$3.34      | External Body Finish         | [amazon](https://amzn.in/d/ezTv9b7)                                                                                          |
| Glue Sticks               | ₹150        | \$1.74      | Assembly Work                | [amazon](https://amzn.in/d/bpFMA49)                                                                                          |
| Raspberry Pi 4B (4GB)     | ₹5546       | \$64.05     | Main Controller Board        | [robocraze](https://robocraze.com/products/raspberry-pi-4-model-b-4gb-ram?_pos=3&_psq=Raspberry+Pi+4+Model+B&_ss=e&_v=1.0)                           |
| USB Microphone            | ₹567        | \$6.58      | Voice Input                  | [amazon](https://amzn.in/d/2ZB8z9S)                                                                                          |
| **Total**                 | **₹10,412** | **\~\$120.26** | —                            | —                                                                                                                            |

---

## 📸 Preview

![KyraDock](https://github.com/user-attachments/assets/847d73e6-36cc-4ed2-a811-5bd93344610f)
![KyraDock](https://github.com/user-attachments/assets/f74e9a25-acca-4d3e-aadd-b86518e19e96)
![KyraDock](https://github.com/user-attachments/assets/03c074bd-53fd-4274-bc67-7f8b21d9e39f)
