# KyraDock

**KyraDock** is a **developer-focused, AI-powered smart assistant device** — inspired by the **Amazon Echo Show**, but designed with full control, speed, and extensibility in mind. It’s a desktop dock running on a Raspberry Pi that merges a **personal voice assistant**, a **local server**, and **remote control capabilities**, all into one compact and customizable project.

KyraDock isn’t just a gadget — it’s your own **programmable Smart device**, ready for natural conversations, silent task execution, system automation, and advanced integrations via voice or remote app. Think of it as **your own Echo Show, built for developers**.

---

## 🔥 What Makes KyraDock Special?

* 🔊 **Voice-Activated Smart Assistant** – Say “Hey Kyra” anytime to trigger the assistant and start speaking.
* 💬 **AI Conversations** – Get fast, smart replies powered by Groq’s Mistral model — ideal for productivity, reminders, search, and more.
* 🔁 **Interruptible Speaking** – Kyra speaks naturally with a female voice and can be interrupted anytime by saying the wake word again.
* 🛠️ **Performs Tasks** – From telling the weather to launching apps, controlling system functions, or running remote APIs — Kyra gets it done.
* 📡 **Built-in Server** – Includes a local web server to run applications, tools, or custom dashboards with GUI or voice access.
* 🧠 **Developer-Friendly** – Easily extend Kyra’s abilities with Python modules, APIs, or even voice-driven automation workflows.
* 🔧 **Modular Architecture** – Built to be modified. Add your own commands, connect devices, or expand it into a full home automation hub.
* 📱 **External Control Interface (Coming Soon)** – Control KyraDock remotely using a companion app or web dashboard to trigger any function — whether you’re across the room or across the world.

---

## 🧠 How KyraDock Works

1. **Wake Word Detection (Offline)**
   Uses a lightweight **Picovoice model** to listen for “Hey Kyra” – ensuring privacy and fast response.

2. **Speech-to-Text (Google Web Speech)**
   After wake-up, Kyra uses the **Google Speech API** to understand what you say.

3. **Smart AI Reply (Groq API)**
   Your spoken command is sent to **Groq's Mistral model**, a lightning-fast AI, which generates an intelligent reply.

4. **Speech Output (pyttsx3)**
   Kyra replies using a **female voice** with interrupt support — you can say “Hey Kyra” mid-sentence to stop her and change your command.

5. **Command Processing & Task Execution**
   Kyra can silently carry out actions like:

   * Telling the weather, jokes, or facts
   * Launching apps
   * Running APIs or system functions
   * Acting as a local voice interface for your own tools

6. **Local Web Server**
   KyraDock runs a lightweight **local server** with GUI + voice support. It can host:

   * Web apps or dashboards
   * Control panels
   * Custom automation tools

7. **External Control (Upcoming)**
   KyraDock will soon support a **remote companion app or web dashboard**, giving you external control of everything on the device — like a smart home control center, but developer-owned and locally run.

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
| Raspberry Pi 4B (8GB)     | ₹7429       | \$86.79     | Main Controller Board        | [robocraze](https://robocraze.com/products/raspberry-pi-4-model-b-8-gb-ram?variant=40193825308825)                           |
| USB Microphone            | ₹567        | \$6.58      | Voice Input                  | [amazon](https://amzn.in/d/2ZB8z9S)                                                                                          |
| **Total**                 | **₹12,316** | **\~\$143** | —                            | —                                                                                                                            |

---

## 📸 Preview

![KyraDock](https://github.com/user-attachments/assets/847d73e6-36cc-4ed2-a811-5bd93344610f)
![KyraDock](https://github.com/user-attachments/assets/f74e9a25-acca-4d3e-aadd-b86518e19e96)
![KyraDock](https://github.com/user-attachments/assets/03c074bd-53fd-4274-bc67-7f8b21d9e39f)
