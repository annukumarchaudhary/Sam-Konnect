<h1 align="center">SamKonnect</h1>

<br />

<p align="center">Free WebRTC - P2P - Simple, Secure, Fast Real-Time Video Conferences with support for up to 4k resolution and 60fps. It's compatible with all major browsers and platforms.</p>

<hr />

Sam Konnect is an advanced real-time communication platform that enables high-quality video and audio conferencing directly in the browser. Built using WebRTC and Node.js, it establishes direct peer-to-peer connections for low-latency and secure communication.

Key Features:


Secure Meetings: The app supports room protection, where it requires a valid username and password for joining the room.


Role Management: In our virtual room, the first participant to join will assume the role of the presenter.


IP Whitelisting: For extra security, access to the instance is restricted to only the specified IP addresses in the allowed list.


API Integration: The app provides an API where the response will give you a entrypoint / Room URL for your meeting.


Post-Meeting Redirect: Upon leaving the room, users who either opt out of providing feedback or if the survey is disabled will be redirected to a specified URL.


Usage Analytics: The system can track aggregated usage statistics in order to improve our service.

<details>
<summary>Start videoconference</summary>

<br/>

1. `Open` [SamKonnect](https://p2p.mirotalk.com/newcall) or [alternative link](https://mirotalk.up.railway.app/newcall).
2. `Choose` a room name and click **Join Room**.
3. `Grant` camera and microphone access.
4. `Share` the room URL and wait for participants to join the video conference.

</details>

<details open>
<summary>Quick start</summary>

<br/>

-   Before running SamKonnect, ensure you have `Node.js` installed. This project has been tested with Node versions [12.X](https://nodejs.org/en/blog/release/v12.22.1/), [14.X](https://nodejs.org/en/blog/release/v14.17.5/), [16.X](https://nodejs.org/en/blog/release/v16.15.1/) and [18.x](https://nodejs.org/en/download).

```bash
# clone this repo
$ git clone https://github.com/miroslavpejic85/mirotalk.git
# go to mirotalk dir
$ cd SamKonnect
# copy .env.template to .env (edit it according to your needs)
$ cp .env.template .env
# install dependencies
$ npm install
# start the server
$ npm start
```

-   Open [http://localhost:3000](http://localhost:3000) in your browser.

</details>
