import math
import streamlit as st

# PharmCalc: educational pharmacy calculation tools
# All calculations are for learning and verification, not prescribing.
# Deva Miruthula Thuhina

st.set_page_config(
    page_title="PharmCalc | Pharmacy Calculators",
    page_icon="💊",
    layout="wide",
)

st.title("💊 PharmCalc")
st.caption("Pharmacy calculations made simple | Educational prototype v1.0")

st.warning(
    "EDUCATIONAL USE ONLY: Results are mathematical estimates, not validated "
    "prescribing recommendations. Always verify inputs, units, product information, "
    "institutional protocols, and patient-specific factors with an appropriately "
    "qualified clinician. Do not use this prototype alone to make treatment decisions."
)

with st.sidebar:
    st.header("PharmCalc")
    st.write("Choose a calculator")
    calculator = st.radio(
        "Calculator",
        [
            "IV infusion",
            "Weight-based dose",
            "Creatinine clearance",
            "Pharmacokinetics",
        ],
        label_visibility="collapsed",
    )
    st.divider()
    st.caption("Version 1.0 | Built by Deva Miruthula Thuhina with Python + Streamlit")
    st.caption("Check every result independently before clinical use.")


def positive_number(label, key, help=None, default=1.0, step=1.0):
    """Show a positive numeric input and return its value."""
    return st.number_input(
        label,
        min_value=0.0,
        value=float(default),
        step=float(step),
        key=key,
        help=help,
    )

def show_result(label, value, unit, decimals=2):
    st.metric(label, f"{value:,.{decimals}f} {unit}")


if calculator == "IV infusion":
    st.header("IV Infusion Rate Calculator")
    st.write(
        "Calculate pump rate, gravity drop rate, infusion duration, or total volume. "
        "Choose the calculation that matches the values available to you."
    )

    mode = st.selectbox(
        "What do you want to calculate?",
        [
            "Pump rate (mL/hour) and drop rate (drops/minute)",
            "Infusion time",
            "Total volume infused",
        ],
    )

    if mode == "Pump rate (mL/hour) and drop rate (drops/minute)":
        col1, col2 = st.columns(2)
        with col1:
            volume_ml = positive_number(
                "Total volume (mL)", "iv_volume_rate", default=500, step=50
            )
            duration_hr = positive_number(
                "Infusion duration (hours)", "iv_duration_rate", default=4, step=0.5
            )
        with col2:
            drop_factor = st.selectbox(
                "Giving-set drop factor (drops/mL)",
                [10, 15, 20, 60],
                index=2,
                help="Use the drop factor printed on the giving-set packaging.",
            )

        if st.button("Calculate infusion rates", type="primary"):
            if volume_ml <= 0 or duration_hr <= 0:
                st.error("Volume and duration must both be greater than zero.")
            else:
                rate = volume_ml / duration_hr
                drops = (volume_ml * drop_factor) / (duration_hr * 60)
                st.subheader("Results")
                a, b = st.columns(2)
                with a:
                    show_result("Pump rate", rate, "mL/hour")
                with b:
                    show_result("Gravity drop rate", drops, "drops/minute", 0)
                st.info(
                    f"Gravity rate rounded to the nearest whole drop: "
                    f"**{round(drops)} drops/minute**."
                )
                with st.expander("Show formulas and working"):
                    st.latex(r"\text{Pump rate} = \frac{\text{Volume (mL)}}{\text{Time (hours)}}")
                    st.write(f"= {volume_ml:g} ÷ {duration_hr:g} = **{rate:.2f} mL/hour**")
                    st.latex(r"\text{Drop rate} = \frac{\text{Volume (mL)}\times\text{Drop factor (drops/mL)}}{\text{Time (minutes)}}")
                    st.write(
                        f"= ({volume_ml:g} × {drop_factor}) ÷ "
                        f"({duration_hr:g} × 60) = **{drops:.2f} drops/minute**"
                    )

    elif mode == "Infusion time":
        col1, col2 = st.columns(2)
        with col1:
            volume_ml = positive_number(
                "Total volume (mL)", "iv_volume_time", default=1000, step=50
            )
        with col2:
            rate = positive_number(
                "Pump rate (mL/hour)", "iv_rate_time", default=125, step=5
            )

        if st.button("Calculate infusion time", type="primary"):
            if volume_ml <= 0 or rate <= 0:
                st.error("Volume and rate must both be greater than zero.")
            else:
                hours = volume_ml / rate
                minutes_total = hours * 60
                st.subheader("Result")
                show_result("Infusion time", hours, "hours")
                st.write(
                    f"Equivalent time: **{int(minutes_total // 60)} hours "
                    f"{round(minutes_total % 60):02d} minutes**."
                )
                with st.expander("Show formula and working"):
                    st.latex(r"\text{Time (hours)} = \frac{\text{Volume (mL)}}{\text{Rate (mL/hour)}}")
                    st.write(f"= {volume_ml:g} ÷ {rate:g} = **{hours:.2f} hours**")

    else:
        col1, col2 = st.columns(2)
        with col1:
            rate = positive_number(
                "Pump rate (mL/hour)", "iv_rate_volume", default=100, step=5
            )
        with col2:
            duration_hr = positive_number(
                "Infusion duration (hours)", "iv_duration_volume", default=5, step=0.5
            )

        if st.button("Calculate total volume", type="primary"):
            if rate <= 0 or duration_hr <= 0:
                st.error("Rate and duration must both be greater than zero.")
            else:
                volume = rate * duration_hr
                st.subheader("Result")
                show_result("Total volume infused", volume, "mL")
                with st.expander("Show formula and working"):
                    st.latex(r"\text{Volume (mL)} = \text{Rate (mL/hour)}\times\text{Time (hours)}")
                    st.write(f"= {rate:g} × {duration_hr:g} = **{volume:.2f} mL**")

    st.caption(
        "Clinical check: verify the prescribed volume, route, fluid, pump settings, "
        "giving-set drop factor, and any maximum rate or fluid restriction. "
        "A calculated gravity rate is an estimate; drops cannot be delivered fractionally."
    )


elif calculator == "Weight-based dose":
    st.header("Weight-based Dose Calculator")
    st.write("Calculate a mathematical dose from a supplied dose-per-weight value.")

    c1, c2 = st.columns(2)
    with c1:
        weight = positive_number("Patient weight (kg)", "dose_weight", default=20, step=0.5)
        prescribed = positive_number(
            "Dose (mg/kg)", "dose_mgkg", default=10, step=0.5,
            help="Enter a dose value from a verified reference or assignment."
        )
    with c2:
        concentration = positive_number(
            "Product concentration (mg/mL)", "dose_concentration", default=10, step=1,
            help="Optional concentration for calculating a corresponding volume."
        )

    if st.button("Calculate dose", type="primary"):
        if weight <= 0 or prescribed <= 0 or concentration <= 0:
            st.error("All values must be greater than zero.")
        else:
            total_dose = weight * prescribed
            volume = total_dose / concentration
            st.subheader("Mathematical result")
            x, y = st.columns(2)
            with x:
                show_result("Calculated dose", total_dose, "mg")
            with y:
                show_result("Corresponding volume", volume, "mL")
            with st.expander("Show formula and working"):
                st.latex(r"\text{Dose (mg)} = \text{Weight (kg)}\times\text{Dose (mg/kg)}")
                st.write(f"= {weight:g} × {prescribed:g} = **{total_dose:.2f} mg**")
                st.latex(r"\text{Volume (mL)} = \frac{\text{Dose (mg)}}{\text{Concentration (mg/mL)}}")
                st.write(f"= {total_dose:.2f} ÷ {concentration:g} = **{volume:.2f} mL**")
    st.caption(
        "This tool does not determine whether a mg/kg dose is appropriate. "
        "Check indication, age, maximum single/daily dose, renal/hepatic function, "
        "formulation, route, and the applicable reference."
    )


elif calculator == "Creatinine clearance":
    st.header("Creatinine Clearance – Cockcroft–Gault")
    st.write("An estimate of creatinine clearance using the Cockcroft–Gault equation.")

    c1, c2 = st.columns(2)
    with c1:
        age = st.number_input("Age (years)", min_value=18, max_value=120, value=60, step=1)
        weight = positive_number("Body weight (kg)", "cg_weight", default=70, step=1)
    with c2:
        scr = positive_number(
            "Serum creatinine (mg/dL)", "cg_scr", default=1.0, step=0.1
        )
        coefficient_label = st.selectbox(
            "Equation coefficient",
            ["Male coefficient (1.00)", "Female coefficient (0.85)"],
            help="Select the conventional coefficient used in the original equation. "
                 "This may not be appropriate for every individual.",
        )

    if st.button("Calculate creatinine clearance", type="primary"):
        if age <= 0 or weight <= 0 or scr <= 0:
            st.error("Age, weight, and serum creatinine must be greater than zero.")
        else:
            coefficient = 0.85 if coefficient_label.startswith("Female") else 1.0
            crcl = ((140 - age) * weight * coefficient) / (72 * scr)
            st.subheader("Estimated result")
            show_result("Creatinine clearance", crcl, "mL/min")
            with st.expander("Show formula and working"):
                st.latex(
                    r"CrCl = \frac{(140-\text{age})\times\text{weight (kg)}}"
                    r"{72\times SCr\text{ (mg/dL)}}\times\text{coefficient}"
                )
                st.write(
                    f"= ((140 − {age}) × {weight:g} × {coefficient}) ÷ "
                    f"(72 × {scr:g}) = **{crcl:.2f} mL/min**"
                )
    st.caption(
        "Limitations: this estimate may be unreliable with rapidly changing serum "
        "creatinine, acute kidney injury, pregnancy, extremes of body size, oedema, "
        "amputation, or low muscle mass. Weight selection and equation suitability "
        "require clinical judgement. Do not use this result alone to adjust a dose."
    )


else:
    st.header("Pharmacokinetics Calculators")
    pk_tool = st.selectbox(
        "Select a calculation",
        [
            "Elimination rate constant (k) from two concentrations",
            "Half-life from elimination rate constant",
            "Volume of distribution (Vd)",
            "Clearance (CL) from k and Vd",
            "Loading dose (educational)",
            "Maintenance dose per interval (educational)",
            "AUC after IV bolus (educational)",
        ],
    )

    if pk_tool == "Elimination rate constant (k) from two concentrations":
        c1, c2 = st.columns(2)
        with c1:
            conc1 = positive_number("Earlier concentration (e.g., mg/L)", "pk_c1", default=20, step=1)
            conc2 = positive_number("Later concentration (same unit)", "pk_c2", default=10, step=1)
        with c2:
            interval = positive_number("Time between samples (hours)", "pk_interval", default=6, step=0.5)
        if st.button("Calculate k", type="primary"):
            if conc1 <= conc2 or conc2 <= 0 or interval <= 0:
                st.error("Earlier concentration must be greater than later concentration; all values must be positive.")
            else:
                k = math.log(conc1 / conc2) / interval
                st.metric("Elimination rate constant", f"{k:.4f} hour⁻¹")
                with st.expander("Formula and working"):
                    st.latex(r"k = \frac{\ln(C_1/C_2)}{t_2-t_1}")
                    st.write(f"= ln({conc1:g}/{conc2:g}) ÷ {interval:g} = **{k:.4f} hour⁻¹**")
        st.caption("Assumes first-order elimination and concentrations from the same patient under comparable conditions.")

    elif pk_tool == "Half-life from elimination rate constant":
        k = positive_number("Elimination rate constant (hour⁻¹)", "pk_k_half", default=0.1, step=0.01)
        if st.button("Calculate half-life", type="primary"):
            if k <= 0:
                st.error("The elimination rate constant must be greater than zero.")
            else:
                half = math.log(2) / k
                st.metric("Elimination half-life", f"{half:.2f} hours")
                with st.expander("Formula and working"):
                    st.latex(r"t_{1/2} = \frac{0.693}{k}")
                    st.write(f"= 0.693 ÷ {k:g} = **{half:.2f} hours**")

    elif pk_tool == "Volume of distribution (Vd)":
        c1, c2 = st.columns(2)
        with c1:
            amount = positive_number("Amount of drug in body (mg)", "pk_amount", default=500, step=10)
        with c2:
            concentration = positive_number("Plasma concentration (mg/L)", "pk_conc_vd", default=10, step=1)
        if st.button("Calculate Vd", type="primary"):
            if amount <= 0 or concentration <= 0:
                st.error("Amount and concentration must be greater than zero.")
            else:
                vd = amount / concentration
                st.metric("Apparent volume of distribution", f"{vd:.2f} L")
                with st.expander("Formula and working"):
                    st.latex(r"V_d = \frac{\text{Amount of drug in body}}{\text{Plasma concentration}}")
                    st.write(f"= {amount:g} ÷ {concentration:g} = **{vd:.2f} L**")
        st.caption("Use a concentration and drug amount that correspond to the same time point. For IV bolus calculations, confirm whether the concentration is an appropriate extrapolated initial concentration.")

    elif pk_tool == "Clearance (CL) from k and Vd":
        c1, c2 = st.columns(2)
        with c1:
            k = positive_number("Elimination rate constant (hour⁻¹)", "pk_k_cl", default=0.1, step=0.01)
        with c2:
            vd = positive_number("Volume of distribution (L)", "pk_vd_cl", default=40, step=1)
        if st.button("Calculate clearance", type="primary"):
            if k <= 0 or vd <= 0:
                st.error("Both values must be greater than zero.")
            else:
                clearance = k * vd
                st.metric("Clearance", f"{clearance:.2f} L/hour")
                with st.expander("Formula and working"):
                    st.latex(r"CL = k\times V_d")
                    st.write(f"= {k:g} × {vd:g} = **{clearance:.2f} L/hour**")

    elif pk_tool == "Loading dose (educational)":
        c1, c2 = st.columns(2)
        with c1:
            target = positive_number("Target plasma concentration (mg/L)", "pk_target_ld", default=10, step=1)
            vd = positive_number("Volume of distribution (L)", "pk_vd_ld", default=40, step=1)
        with c2:
            bioavailability = st.number_input(
                "Bioavailability (F, fraction)", min_value=0.01, max_value=1.0,
                value=1.0, step=0.05, help="Use 1.0 for a fully bioavailable IV dose."
            )
        if st.button("Calculate loading dose", type="primary"):
            dose = target * vd / bioavailability
            st.metric("Theoretical loading dose", f"{dose:.2f} mg")
            with st.expander("Formula and working"):
                st.latex(r"LD = \frac{C_{target}\times V_d}{F}")
                st.write(f"= ({target:g} × {vd:g}) ÷ {bioavailability:g} = **{dose:.2f} mg**")
        st.caption("A theoretical equation only. It does not account for salt factor, dosing weight, target range, toxicity, infusion limits, distribution phases, or patient-specific adjustments.")

    elif pk_tool == "Maintenance dose per interval (educational)":
        c1, c2 = st.columns(2)
        with c1:
            target_ss = positive_number("Target average steady-state concentration (mg/L)", "pk_target_md", default=10, step=1)
            clearance = positive_number("Clearance (L/hour)", "pk_cl_md", default=4, step=0.5)
        with c2:
            interval = positive_number("Dosing interval (hours)", "pk_tau_md", default=12, step=1)
            bioavailability = st.number_input(
                "Bioavailability (F, fraction)", min_value=0.01, max_value=1.0,
                value=1.0, step=0.05
            )
        if st.button("Calculate theoretical maintenance dose", type="primary"):
            dose = target_ss * clearance * interval / bioavailability
            st.metric("Theoretical dose per interval", f"{dose:.2f} mg")
            with st.expander("Formula and working"):
                st.latex(r"MD = \frac{C_{ss,avg}\times CL\times\tau}{F}")
                st.write(
                    f"= ({target_ss:g} × {clearance:g} × {interval:g}) ÷ "
                    f"{bioavailability:g} = **{dose:.2f} mg per interval**"
                )
        st.caption("Assumes linear pharmacokinetics and an appropriate average steady-state target. Actual regimens may require peak/trough targets, dose rounding, salt correction, infusion duration, and therapeutic drug monitoring.")

    else:  # AUC after IV bolus
        c1, c2 = st.columns(2)
        with c1:
            dose = positive_number("IV dose (mg)", "pk_dose_auc", default=500, step=10)
        with c2:
            clearance = positive_number("Clearance (L/hour)", "pk_cl_auc", default=4, step=0.5)
        if st.button("Calculate AUC", type="primary"):
            if dose <= 0 or clearance <= 0:
                st.error("Dose and clearance must be greater than zero.")
            else:
                auc = dose / clearance
                st.metric("AUC", f"{auc:.2f} mg·hour/L")
                with st.expander("Formula and working"):
                    st.latex(r"AUC_{0-\infty} = \frac{\text{IV dose}}{CL}")
                    st.write(f"= {dose:g} ÷ {clearance:g} = **{auc:.2f} mg·hour/L**")
        st.caption("This is the linear, systemic-exposure relationship for an IV dose under the stated assumptions. It is not a substitute for measured AUC or a validated therapeutic drug-monitoring method.")


st.divider()
st.caption(
    "PharmCalc is an educational student project. Calculations should be independently "
    "checked and are not a substitute for clinical assessment, validated software, "
    "institutional policy, or professional judgement."
)
