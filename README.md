# 💊 PharmCalc – Pharmacy & Clinical Calculation Website

**PharmCalc** is a free, web-based pharmacy calculation tool developed using Python and Streamlit. It aims to simplify commonly used pharmaceutical and clinical calculations for pharmacy students and healthcare learners.

The project focuses on providing simple interfaces, transparent mathematical formulas, and step-by-step calculations.

🌐 **Live Website:** [Open PharmCalc](YOUR_STREAMLIT_APP_URL)

---

## 🚀 Features

### 1. IV Infusion Rate Calculator
- Infusion rate (mL/hour)
- Gravity drop rate (drops/minute)
- Total infusion time
- Total volume infused
- Giving-set drop factor selection
- Step-by-step calculations

### 2. Weight-Based Dose Calculator
- Dose calculation using mg/kg
- Total calculated dose (mg)
- Volume calculation based on concentration (mg/mL)

### 3. Creatinine Clearance Calculator
- Cockcroft–Gault equation
- Male and female equation coefficients
- Estimated creatinine clearance (mL/min)

### 4. Pharmacokinetics Calculator
- Elimination rate constant (k)
- Elimination half-life
- Volume of distribution (Vd)
- Drug clearance (CL)
- Loading dose
- Maintenance dose
- AUC after IV bolus

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Calculation logic |
| Streamlit | Web application framework |
| VS Code | Development environment |
| GitHub | Version control and source code hosting |
| Streamlit Community Cloud | Website deployment |

---

## 💻 Run Locally

### Prerequisites
- Python installed
- Visual Studio Code (recommended)
- Git (optional)

### Installation

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Navigate to the project folder**

```bash
cd PharmCalc
```

**3. Create a virtual environment**

```bash
python -m venv .venv
```

**4. Activate the environment**

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

**5. Install dependencies**

```bash
python -m pip install -r requirements.txt
```

**6. Run the application**

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at:

`http://localhost:8501`

---

## 📐 Calculation Principles

PharmCalc uses mathematical equations commonly taught in pharmacy and pharmacokinetics.

Examples:

**IV Infusion Rate**

Pump rate:

Rate (mL/hour) = Total volume (mL) / Time (hours)

Drop rate:

Drops/minute = [Volume (mL) × Drop factor (drops/mL)] / Time (minutes)

**Weight-Based Dose**

Dose (mg) = Weight (kg) × Prescribed dose (mg/kg)

**Creatinine Clearance**

Cockcroft–Gault equation:

CrCl = [(140 − Age) × Weight (kg)] / [72 × Serum creatinine (mg/dL)]

For the conventional female coefficient, multiply by 0.85.

**Elimination Half-Life**

t½ = 0.693 / k

---

## ⚠️ Clinical Disclaimer

PharmCalc is an educational project developed for learning and demonstration purposes.

- Results are mathematical estimates and are not validated prescribing recommendations.
- Always verify calculations independently.
- Confirm units, patient-specific parameters, drug references, and institutional protocols.
- Clinical decisions must be made by qualified healthcare professionals.
- This application is not a substitute for professional clinical judgement or validated clinical software.

---

## 🎯 Project Goals

- Develop useful pharmacy calculation software.
- Improve accessibility to common clinical calculations.
- Promote understanding of pharmacokinetic and pharmacodynamic concepts.
- Integrate pharmacy knowledge with programming.
- Gradually expand the application with additional pharmacy tools.

---

## 🔮 Future Development

Planned improvements include:

- Improved mobile-friendly interface
- Additional pharmacokinetic calculations
- More clinical calculation tools
- Expanded input validation
- Automated calculation testing
- User feedback and error reporting
- Improved documentation and clinical references

---

## 👨‍💻 Developer

**PharmCalc** is a student-developed project created as part of an exploration of programming and clinical pharmacy.

**Developed using:** Python and Streamlit.

---

⭐ If you find this project useful, consider starring the GitHub repository!

**PharmCalc – Making Pharmacy Calculations Simple.**
