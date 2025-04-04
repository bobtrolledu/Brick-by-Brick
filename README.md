# CMPE246-Group11

# 🧱 Brick by Brick Demo Video

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/-2BJYd74knk/0.jpg)](https://www.youtube.com/watch?v=-2BJYd74knk)

---

## 💡 Inspiration

With the rise of intelligent automation in warehouses and manufacturing, we were inspired to build a small-scale, AI-powered system that mimics industrial sorting robots. We wanted to create a smart embedded system that could **detect**, **classify**, and **sort physical objects** — all running locally on a **Raspberry Pi**, without relying on cloud computing or massive infrastructure.

Our goal was to integrate **computer vision** and **embedded hardware control** in a functional, real-time system that reflects the principles taught in CMPE 246.

---

## 🧠 What it does

**BRICK by BRICK** is a smart embedded platform that:

- Uses **computer vision** to detect and classify small objects in real time  
- Controls an **X-Y gantry system** to move and sort objects with precision  
- Runs entirely on a **Raspberry Pi 4**, integrating motors, camera, and logic locally  
- Demonstrates full-stack interaction: from hardware control to web-based monitoring

---

## 🛠️ How we built it

We built **BRICK by BRICK** as a real-time embedded system using:

- **Python** (for backend logic and GPIO control)  
- **OpenCV** + Brickognize API (for object classification)  
- **Raspberry Pi 4B** with camera module  
- **Stepper motors** + TMC2209 drivers for precise gantry movement  
- **Next.js + Vite** for optional frontend visual interface  
- **Flask + Websockets** for communication between UI and backend  
- **SolidWorks** for 3D modeling and gantry design  
- **SQLite3** for lightweight local storage  
- **GitHub** and **Agile methodology** for version control and collaboration

---

## 🚧 Challenges we ran into

- **Motor alignment issues**: One of our gantry axes frequently lost calibration, which required redesigning and reprinting the mount.
- **False object detection**: Our computer vision model struggled with lighting and contrast — we had to adjust preprocessing steps and tune thresholds.
- **Synchronization**: Ensuring real-time communication between vision processing and hardware motion was tricky without introducing lag.
- **Limited hardware resources**: Raspberry Pi had performance limits — we had to optimize vision code and reduce overhead.

---

## 🏆 Accomplishments we're proud of

- Fully functional, real-time sorting prototype  
- Seamless hardware-software integration  
- Responsive and modular backend using OOP principles  
- Aesthetic frontend design using React + custom UI  
- Operating entirely offline — no cloud dependencies  
- Built from scratch as a full-stack embedded system

---

## 📚 What we learned

- How to apply embedded systems theory (GPIO, architecture, OOP) into a real working product  
- How to debug motors, tune sensors, and calibrate mechanical systems  
- How to implement real-time computer vision with OpenCV  
- How to collaborate using GitHub Projects and agile sprints  
- How to present and film a technical demo in a clear and compelling way

---

## 🚀 What's next

- Add **Z-axis** support for 3D sorting  
- Train a **custom AI model** to replace Brickognize  
- Add a **web dashboard** for remote monitoring  
- Implement **reinforcement learning** for adaptive sorting  
- Integrate a **cloud logging system** for data tracking

---

## 👥 Team

| Name | Role |
|------|------|
| **Anson** | Team Lead, SolidWorks, Motors, Full Stack Dev |
| **Ye** | AI & Computer Vision, Backend Integration |
| **Yehezkiel** | SolidWorks, Marketing, Demo Filming |
| **Su** | Frontend Dev, Backend Assistant, UI Design |
