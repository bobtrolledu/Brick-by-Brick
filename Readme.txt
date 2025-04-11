Brick-by-Brick Project README
=============================

This document serves as a comprehensive overview (similar to a directory listing or checklist) explaining the purpose of each folder and file in the Brick-by-Brick project.

----------------------------------------

Table of Contents
-----------------
1. Overview
2. Directory Structure
3. Backend (Flask) - "LegoDetection/app"
4. Frontend (Vite.js) - "LegoDetection/app/frontend"
5. Raspberry Pi Code - "LegoDetection/app/RaspberryPi_Code"
6. SolidWorks Files - "Solidworks"
7. Project Website Showcase - "LandingPage"
8. UML and Diagrams
9. Photos - "Photos"
10. Support Files
11. Installation and Usage
12. Contact and Links

----------------------------------------
1. Overview
-----------
Brick-by-Brick is a project that integrates hardware, software, and 3D mechanical design to create an automated system for detecting and manipulating LEGO bricks. The system is divided into three main software components:

1. A Flask backend ("LegoDetection/app"), responsible for server-side logic such as image processing and data handling.
2. A Vite.js frontend ("LegoDetection/app/frontend"), providing an intuitive web interface for the user.
3. Raspberry Pi code ("LegoDetection/app/RaspberryPi_Code"), which runs the hardware and triggers the mechanical components (motors, sensors, etc.).

Additionally, the project includes SolidWorks designs, UML diagrams, and other supporting materials for the design and mechanical aspects.

----------------------------------------
2. Directory Structure
-----------------------
Below is a high-level overview of the folder structure:

Brick-by-Brick/
├── .venv/ or venv/               # Virtual environment folder (Python environment)
├── LegoDetection/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── pieces.db
│   │   └── ...
│   │   ├── RaspberryPi_Code/
│   │   │   ├── sensor.py
│   │   │   ├── motor_control.py
│   │   │   ├── camera_capture.py
│   │   │   └── ...
│   │   ├── frontend/
│   │   │   ├── pages/
│   │   │   ├── public/
│   │   │   ├── package.json
│   │   │   ├── next.config.js
│   │   │   └── ...
├── Solidworks/
│   ├── FullAssembly.SLDASM
│   ├── Gantry Assembly/
│   ├── Timing Belt pulleys/
│   └── ...
├── Photos/
│   ├── Prototypes/
│   ├── Screenshots/
├── GitCommitHistory.txt
├── ClassUML-plantuml
├── SequenceUML-plantuml
├── CMPE246_DemoVideo.mp4
├── Readme.txt
├── README.md
├── requirements.txt
└── ...

----------------------------------------
3. Backend (Flask) - "LegoDetection"
----------------------------------------
The "LegoDetection/app" directory contains the backend Flask server code and related resources:

- "app/" folder:
  - __init__.py
      - Initializes the Flask application, sets up configuration, and imports modules.
  - app.py
      - The main Flask application file where routes are defined to communicate with the frontend and handle back-end logic.
  - pieces.db
      - Primary SQLLite3 database for storing LEGO piece information.

- .gitignore
  - Specifies files and folders to be ignored by Git (e.g., virtual environments, cache files).

----------------------------------------
4. Frontend (Vite.js) - "LegoDetection/app/frontend"
----------------------------------------
This directory contains the Vite.js application which serves as the project’s user interface:

- "src/screens/" folder:
  - Contains all Vite.js pages/routes. Each file corresponds to a specific route

- package.json:
  - Provides metadata for the project (name, version) and lists NPM dependencies along with scripts.

- vite.config.js:
  - Configuration file for Vite.js (e.g., custom webpack settings, environment variables).

To run the frontend:
  1. Navigate to "LegoDetection/app/frontend/".
  2. Run: npm install
  3. Then: npm run dev

----------------------------------------
5. Raspberry Pi Code - "RaspberryPi_Code"
----------------------------------------
Located under the "LegoDetection" folder, the "RaspberryPi_Code" contains all scripts necessary for operating hardware components on the Raspberry Pi:

- sensor.py:
  - Manages sensor reading logic (e.g., distance or color sensors).

- motor_control.py:
  - Contains functions to control motors or servos (such as those used in the gantry system).

- camera_capture.py:
  - Captures images for processing by the Flask application.

- Additional scripts:
  - For specific hardware tasks and support utilities.

Note: You may need to install Raspberry Pi–specific libraries (e.g., RPi.GPIO) on your Raspberry Pi for proper functioning.

----------------------------------------
6. SolidWorks Files - "Solidworks"
----------------------------------------
This folder contains the mechanical CAD designs developed in SolidWorks:

- FullAssembly.SLDASM:
  - A complete assembly file showcasing the mechanical design.

- Gantry Assembly/ Frame Assembly/ Feeder Folder:
  - Contains sub-assemblies or part files related to the complete assembly.

----------------------------------------
7. Next.js Project Website
----------------------------------------
In addition to the main frontend interface, the project includes a dedicated Next.js website that showcases Brick-by-Brick. This website is designed to provide a complete overview and visual tour of the project, highlighting:

- **Project Overview and Features:**
  - Detailed information on the project concept, objectives, and key functionalities.
  - Interactive sections highlighting technological components including hardware, software, and mechanical designs.

- **Media and Visuals:**
  - Embedded photos, screenshots, and video demos demonstrating the project's progress and final outcome.
  - Links to prototype videos, online demos, and live presentations.

**To Run the Project Showcase Website:**
  1. Navigate to the website folder within `LegoDetection/frontend/`.
  2. Run: `npm install` to install all necessary dependencies.
  3. Start the development server with: `npm run dev`
  4. Visit `http://localhost:3000` in your web browser to explore the project showcase website.

This Next.js website functions as both a project demonstration tool and a comprehensive information portal for evaluators, collaborators, and interested viewers.

----------------------------------------
8. UML and Diagrams
----------------------------------------
The project contains UML and design diagrams in the following folders:

- ClassUML-plantuml:
  - Contains PlantUML text files (.plantuml) or image exports that detail class relationships within the project's software.

- SequenceUML-plantuml:
  - Contains sequence diagrams in PlantUML format representing system interactions (e.g., communication among the frontend, backend, and Raspberry Pi code).

Render these files using tools like PlantUML (https://plantuml.com/) to view the diagrams.

----------------------------------------
9. Photos
----------------------------------------
This section contains visual documentation of the project:

- Photos and Screenshots:
  - Screenshots: Contains screenshots of the application interfaces, diagrams, hardware setups, and any GUI components.
  - Prototypes: Includes photos or images of early prototypes, physical models, or any iterative design stages.

These images serve as visual evidence of the project’s development milestones and final product. Make sure to include high-quality images in these folders.

----------------------------------------
10. Support Files
----------------------------------------
Other important files included in the project:

- requirements.txt (in the project root):
  - A consolidated python requirements file if used for additional components or overall dependencies.

- GitCommitHistory.txt (in the project root):
  - A Git commit graph and history of the project

- .gitignore:
  - Multiple .gitignore files exist to exclude unnecessary files (e.g., virtual environments, cache, etc.).

- venv/ or .venv/:
  - The virtual environment directory for Python (typically not committed to source control).

----------------------------------------
11. Installation and Usage
----------------------------------------
Follow these steps to set up and run the project:

1. Clone the Repository:
   --------------------------------------------------
   git clone https://github.com/YourRepository/Brick-by-Brick.git
   cd Brick-by-Brick
   --------------------------------------------------

2. Set Up Virtual Environment:
   --------------------------------------------------
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   pip install -r LegoDetection/requirements.txt
   --------------------------------------------------

3. Run the Backend (Flask):
   --------------------------------------------------
   cd LegoDetection/app
   python run flask --no-debug
   --------------------------------------------------
   The Flask server should now run on a specified port (commonly http://localhost:5000).

4. Run the Frontend (Vite.js):
   --------------------------------------------------
   cd ../frontend
   npm install
   npm run dev
   --------------------------------------------------
   The Vite.js server should now run (commonly http://localhost:5173).

5. Raspberry Pi Code:
   - Transfer the "RaspberryPi_Code" folder to your Raspberry Pi.
   - Install any required libraries (e.g., RPi.GPIO) and run the respective scripts.

6. Accessing the Application:
   - Visit the frontend application in your browser (e.g., http://localhost:5173) and verify its communication with the backend.

----------------------------------------
12. Contact and Links
----------------------------------------
- GitHub: https://github.com/bobtrolledu/Brick-by-Brick
- YouTube/Demo Video: https://www.youtube.com/watch?v=-2BJYd74knk

Thank you for reviewing the Brick-by-Brick project documentation!
