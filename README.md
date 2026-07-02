# 🔒 Automated PII (Personally Identifiable Information) Anonymization Pipeline

A professional Python-based DevSecOps automation tool designed to secure production database exports by programmatically masking high-risk PII before it reaches development or testing environments. 

This project aligns directly with data protection principles outlined in **CompTIA Security+** and international compliance frameworks like **GDPR**.

## 📽️ Project Demonstration
Watch the full video walkthrough of the automation pipeline on [Loom Video Demo](https://www.loom.com/share/e1ca12576be349d397593f754d43415e).

## 🚀 The Enterprise Challenge
In modern engineering workflows, software developers and QA testers require realistic datasets to build features and run tests. However, duplicating real production databases into lower environments creates severe compliance violations and exposes actual user identities (names, credentials, tracking footprints) to unnecessary security risks.

## 🛠️ The Architecture & Solution
This project establishes a clean **Security Layer** between raw production assets and non-production environments. It achieves this by executing an automated **ETL (Extract, Transform, Load)** pipeline that strips identifying signatures while strictly preserving **Data Fidelity**.

Instead of deleting columns or replacing data with static blocks (e.g., `XXXXXX`), which would break application code and database schemas during testing, this tool swaps data with structurally identical, synthetic equivalents using **Pandas** and **Faker**.

### The Pipeline Architecture:
1. **Simulation Phase (`raw_data_generator.py`):** Simulates a raw, unmasked export from a production database containing high-risk PII columns and saves it as `raw_data.csv`.
2. **Ingestion Phase (`privacy-protector.py`):** Dynamically reads the dataset size, maps the target PII schemas, and loads the data into memory.
3. **Anonymization Phase:** Replaces sensitive cells with synthetically valid information.
4. **Export Phase:** Writes a clean, safe `masked_pii_data.csv` optimized for staging and testing environments.

## 📋 Monitored PII Columns & Compliance Mapping
The anonymization engine targets 5 distinct fields classified as high-risk under privacy regulations:

| Target Column | PII Classification | Structural Anonymization Strategy |
| :--- | :--- | :--- |
| `User_Name` | Direct Identifiable Data | Swapped with localized, synthetic full names |
| `Password` | Sensitive Authentication Credentials | Scrambled using high-entropy, multi-character synthetic strings |
| `Email_ID` | Direct Contact PII | Formatted cleanly with valid domains to preserve application logic |
| `Phone_Number` | Direct Contact PII | Replaced with structurally correct, realistic phone strings |
| `IP_Address` | Network Tracking Footprint / Location | Overwritten with valid IPv4 schemas to preserve network logs |

## 🧪 Technical Stack & Tools
* **Python 3** (Core Logic)
* **Virtual Environments (`.venv`)** (Local dependency isolation)
* **Pandas Library** (High-performance in-memory data structures and CSV manipulation)
* **Faker Library** (Synthetic data generation engine)

## 📖 How to Install & Run

Follow these steps to run the data security pipeline inside an isolated virtual environment.
(If you have never run a Python script before, follow these exact steps to download this project, set up your safe coding sandbox, and run the pipeline.)

### Prerequisites
Make sure you have **Python 3** and **Git** installed on your computer. If you are using Windows, I recommend running these commands inside the **PowerShell** terminal (or the terminal built directly into VS Code).

### Step 1: Clone the Project to Your Computer
Open your computer's terminal, navigate to the folder where you like to save your projects (like your Desktop or a Documents folder), and paste this command to download the code:
<code>git clone [https://github.com/Batina-Jennifer/automated-pii-anonymization.git](https://github.com/Batina-Jennifer/automated-pii-anonymization.git)</code>

### Step 2. Move Inside the Project Folder
You need to tell your terminal to step inside the project folder you just downloaded. Run this command:
<code>cd automated-pii-anonymization</code>

### Step 3: Turn on the Virtual Environment Sandbox
You will use an isolated sandbox called a virtual environment (.venv) so these packages don't mess up any other files on your machine. 
1. Create the sandbox folder: <code>python -m venv .venv</code>
2. Turn it on by running the command that matches your operating system:
* Windows (PowerShell): <code>.\\.venv\Scripts\Activate.ps1</code>
* Mac / Linux (Terminal): <code>source .venv/bin/activate</code> </br>
Look at the very left edge of your terminal line. You should now see (.venv) sitting in front of your folder path.

### Step 4: Install the Required Tools
Now that you are inside your safe sandbox, run this command to download the internal tools (pandas for handling spreadsheets and faker for creating the fake names): <code>pip install pandas faker</code>

### (Optional Step) Generate the Simulated "Production/Raw" Data
In case you don't have real data to work with, you can try to generate random realistic data to mask it later using the **raw_data_generator.py** to generate raw data to work it:
<code>python raw_data_generator.py</code> </br>

If you already have an existing file/data to work with, convert it to a **.csv** format --> Inside the "try" block in the privacy-protector.py, go to <code>df = pd.read_csv('raw_data.csv')</code>, and replace it with your original/actual file so that it looks like this: <code>df = pd.read_csv('<your_actual_file>.csv') </code>  

### Step 5: Run the Automated PII Anonymization PipeLine
Now, let's run your automated pii anonymization pipeline (priavcy-protector.py) to scrub that sensitive data and make it completely anonymous: <code>python privacy-protector.py</code>

## 🗒️The Results
The tool dynamically counts the rows, strips away all the real tracking footprints, and prints a neat preview of the sanitized data directly into your terminal. A brand new, 100% safe file called masked_pii_data.csv is created. You can now pass this file to any developer or tester without risking user privacy! </br>

Yayy!! You've successfully converted high-risk corporate data into a perfectly safe, compliance-friendly playground. Hand it off to your dev team, keep your legal department happy, and rest easy knowing user privacy is completely locked down! 🚀🔐
