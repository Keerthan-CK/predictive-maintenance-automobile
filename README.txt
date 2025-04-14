
Predictive Maintenance for Automobiles using IoT and Machine Learning
====================================================================

This project presents an intelligent system that leverages IoT sensors and machine learning algorithms to predict maintenance needs in vehicles. The goal is to reduce unexpected breakdowns, optimize service schedules, and improve vehicle reliability through real-time monitoring and predictive analytics.

Project Components
------------------

Hardware:
- ESP32 Microcontroller – IoT data collection & transmission
- DHT11 Sensor – Measures temperature & humidity
- Accelerometer (ADXL345) – Detects vibrations and tilt for accident alerts
- Oil Level Sensor – Monitors lubricant levels
- 12V Lead-Acid Battery – Target of BMS (Battery Management System) predictions
- LCD Display + Buzzer – Real-time local alerts
- Zigbee Module – Wireless communication

Software & Tools:
- Arduino IDE – ESP32 programming
- Visual Studio Code – Development environment for:
  • Web Frontend (HTML, CSS, JS)
  • Flask Backend (Python)
  • SQLite Database
  • Machine Learning Model (Random Forest)
- Telegram Bot API – Remote alert notifications
- Jupyter Notebook – ML model training and testing

Machine Learning Model
----------------------
- Algorithm: Random Forest
- Trained using historical sensor data
- Predicts: Vehicle faults, battery degradation, and Remaining Useful Life (RUL)
- Input Features:
  • Cycle Index
  • Discharge Time (s)
  • Voltage Drop Time (3.6–3.4V)
  • Discharge Voltage (V)
  • Current (A)
  • Time at 4.15V (s)
  • Time Constant Current (s)

Web Dashboard
-------------
- Displays real-time data from sensors
- Accepts battery parameters from user
- Calculates: Approximate RUL and Estimated Charging Time

Alert Mechanisms
----------------
LCD + Buzzer:
- On-vehicle real-time alerts for faults and warnings

Telegram Bot:
- Sends remote alerts
- Allows users to query vehicle status

Key Features
------------
- Real-time monitoring of vehicle health
- Intelligent predictions using ML
- Dual alert mechanisms (local + remote)
- Dashboard interface for visualization
- Battery Management System (BMS) prediction

Getting Started
---------------
1. Clone the Repository:
   git clone https://github.com/your-username/predictive-maintenance-automobile.git

2. Setup Python Environment:
   pip install flask scikit-learn pandas sqlite3

3. Upload code to ESP32 using Arduino IDE

4. Run Flask Server:
   python app.py

5. Access Web Interface:
   Open http://localhost:5000 in your browser

License
-------
This project is licensed under the MIT License.
