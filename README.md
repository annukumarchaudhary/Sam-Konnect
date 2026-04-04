# 🎓 Sam-Konnect: Real-Time WebRTC P2P Video Conferencing

Welcome to **Sam-Konnect**, an advanced, free, and secure browser-based peer-to-peer (P2P) video and audio calling application. 

**Developed By:** Annu Kumar Chaudhary , Ankur Dwivedi 
**Institution:** Ewing Christian College, Prayagraj (Major Project)

---

## 🚀 Overview
Sam-Konnect utilizes the power of **WebRTC** and **Socket.io** to establish direct peer-to-peer connections between users. Unlike traditional video conferencing apps that route your video through a central server, Sam-Konnect sends your media directly to the other participants. This results in ultra-low latency, crystal-clear quality, and maximum privacy.

## ✨ Key Features
* 🔒 **Maximum Privacy:** End-to-end P2P connection means no central server records your video.
* ⚡ **No Installation Required:** 100% browser-based. Just share a link and start talking.
* 📝 **Interactive Whiteboard:** Collaborate with your team in real-time.
* 🗣️ **Live Captions (Speech-to-Text):** Built-in speech recognition for accessibility.
* 📁 **Direct File Sharing:** Share files directly through WebRTC Data Channels instantly.
* 🎙️ **Active Speaker Detection:** Automatically highlights the person who is speaking.
* 🛡️ **Room Protection:** Secure your meetings with a username and password.

---

## 📊 Feature Comparison: Sam-Konnect vs. Zoom vs. Google Meet

| Feature / App | 🎓 Sam-Konnect | 🔵 Zoom | 🟢 Google Meet |
| :--- | :--- | :--- | :--- |
| **Technology Architecture** | **WebRTC P2P** (Direct) | Client-Server (SFU) | Client-Server (SFU) |
| **Meeting Time Limit** | **Unlimited** (Always Free) | 40 Minutes (Free tier) | 60 Minutes (Free tier) |
| **Privacy & Security** | **Highest** (No server routing) | High | High |
| **Screen Sharing** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Live Captions** | ✅ Yes (Web Speech API) | ✅ Yes | ✅ Yes |
| **Interactive Whiteboard**| ✅ Yes (Built-in) | ✅ Yes | ✅ Yes (Jamboard/Miro) |
| **Direct File Sharing** | ✅ Yes (Direct P2P, fast) | ✅ Yes (Via Cloud) | ❌ No (Drive needed) |
| **Cost** | **100% Free** | Paid for Premium | Paid for Premium |

### 🏆 Why Choose Sam-Konnect? (Key Advantages)
1. **True Peer-to-Peer (P2P) Privacy:** In traditional apps, your video goes to a server first. In Sam-Konnect, WebRTC sends video directly from your laptop to the other user's laptop. No central server can record or access the media stream.
2. **No Setup, No Limits:** No app installation required, and no 40-minute kick-outs. Users can communicate for unlimited hours in high quality directly from their browser.
3. **Data Channel File Sharing:** Bypasses cloud storage completely. WebRTC data channels allow users to send files securely and instantly P2P.

### ⚠️ The Honest Trade-off (Limitation)
Since Sam-Konnect is a pure P2P network, every user must send their video stream directly to everyone else in the room. 
* **The Sweet Spot:** Perfect for 2 to 15 participants (lag-free, highly secure, zero latency).
* **The Limit:** If 50+ people join, the browser will consume significant CPU and bandwidth to maintain 50 individual connections, unlike Zoom which offloads this to their central servers.

---

## 🛠️ Technology Stack
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (DOM manipulation & WebRTC API).
* **Backend Signaling:** Node.js, Express.js.
* **Real-time Engine:** Socket.io (for STUN/TURN signaling).
* **Security:** Crypto-js, JSON Web Tokens (JWT), xss (Cross-site scripting prevention).

---

## 💻 How to Run Locally

If you want to run this project on your own machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/annukumarchaudhary/Sam-Konnect.git](https://github.com/annukumarchaudhary/Sam-Konnect.git)
   cd Sam-Konnect