💌 Phishing Email Detection

This Python project detects phishing attempts in emails. It provides both CLI and GUI (Tkinter) interfaces. The program analyzes email content, identifies suspicious links and keywords, calculates a phishing score, and displays the results to the user.

Features

Automatically extracts URLs from email content.

Detects common phishing keywords.

Score-based analysis to flag potentially malicious emails.

GUI with a user-friendly interface using Tkinter.

CLI version demonstrates Base64 encoding for data privacy.

Analyze all .txt emails in a folder (GUI).

Installation

Python 3 must be installed.

Clone or download the project:

git clone https://github.com/username/phishing-detector.git
cd phishing-detector


To run the GUI version:

python gui_phishing_detector.py


To run the CLI version:

python phishing_detector.py

Usage
GUI

Paste the email content into the textbox or select a folder with .txt emails.

Click “📥 Analyze Single Email” or “📁 Analyze Folder of Emails”.

The results will appear below:

Score

Verdict (Likely Safe / Potential Phishing)

Found links

CLI

Add the email content to sample_email.txt.

Run the script in the terminal:

python phishing_detector.py


Output includes:

Email content

Found links

Total phishing score

Base64 encoded content (demo)

Code Overview
Core Functions

find_links(text) – Detects all URLs in the email content.

score_email(text) – Calculates a phishing score based on keywords and links.

encrypt_text(text) – Encodes text in Base64 (CLI demo).

GUI functions:

analyze_email_text() – Analyzes a single email.

analyze_folder() – Analyzes all .txt files in a folder.

display_results(email_text) – Shows score, verdict, and links in the GUI.

Scoring

Each suspicious keyword has a predefined weight.

Each URL adds +20 or +30 points (depending on version).

Score ≥50 triggers a potential phishing warning.

GUI Example Output
🔢 Score: 70
📝 Verdict: ⚠️ Potential phishing detected!
🔗 Found Links:
https://fake-login.com
https://urgent-action.com

CLI Example Output
Email content:

Dear user, please verify your account immediately by clicking the link below.

🔗 Found Links:
https://fake-login.com

📊 Total Phishing Score: 30

✅ This email is likely safe.

🔐 Base64 Encoded Content:
RGVhciB1c2VyLAo...

Development Suggestions

Extend the keyword list and scoring weights.

Add ML-based phishing detection.

Connect to email servers (Gmail/Outlook) for real-time analysis.
