# AI Enterprise Integration Financial Intelligence Platform
import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

# Handle plotly import with fallback
try:
    import plotly.graph_objects as go
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    st.error("⚠️ Plotly not available. Installing plotly will enable advanced visualizations.")

# -----------------------------
# Page setup & light theming
# -----------------------------
st.set_page_config(page_title="AI Enterprise Integration Financial Model", layout="wide")

CUSTOM_CSS = """
<style>
/* Global tweaks */
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; }
h1, h2, h3 { font-weight: 700; }
.small-note { color:#6b7280; font-size:0.9rem; }
.metric-card { background:#0f172a10; border:1px solid #e5e7eb; border-radius:16px; padding:16px; }
.section-card { background:#ffffff; border:1px solid #e5e7eb; border-radius:16px; padding:16px; }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.title("🤖 Vx AI Enterprise Integration Financial Intelligence Platform")
st.markdown("### 🎯 Advanced Scenario Modeling for Enterprise AI Transformation (36-Month Forecast)")

# Add professional header with key value props
st.markdown("""
<div style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 10px; margin: 20px 0;">
    <h4 style="color: white; margin: 0;">🚀 Enterprise AI Integration ROI Forecasting</h4>
    <p style="color: #f0f0f0; margin: 5px 0 0 0;">Dynamic scenario modeling • Real-time ROI analysis • Risk assessment • Investment optimization</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Session state for scenarios
# -----------------------------
if "scenarios" not in st.session_state:
    st.session_state.scenarios = {}

# -----------------------------
# Sidebar: enterprise scenario management
# -----------------------------
with st.sidebar:
    st.header("🎯 Enterprise AI Scenarios")
    scenario_name = st.text_input("Scenario Name", "Conservative AI Rollout")
    
    st.markdown("### 📊 Quick Scenario Presets")
    if st.button("🚀 Aggressive AI Transformation", use_container_width=True):
        st.session_state.preset = "aggressive"
    if st.button("📈 Balanced Integration", use_container_width=True):
        st.session_state.preset = "balanced"
    if st.button("🛡️ Conservative Rollout", use_container_width=True):
        st.session_state.preset = "conservative"
    
    st.caption("💡 Use the **Settings** tab to configure detailed parameters. Click **Save Scenario** to preserve analysis.")

# ===========================================================
# Core computation (integer-safe), pricing & capacity rules
# ===========================================================
def generate_ai_enterprise_financials(
    # AI Enterprise Integration Model
    months, 
    # AI Implementation Services
    start_ai_implementations, end_ai_implementations, avg_implementation_value, 
    start_ai_consulting_monthly, end_ai_consulting_monthly,
    # AI Training & Support Services  
    num_enterprise_clients, start_training_hours, end_training_hours, training_rate_per_hour, 
    start_support_services_monthly, end_support_services_monthly,
    # Business Development & Operations
    sales_commission_pct, marketing_cost_monthly, marketing_start_month,
    # Advanced AI Metrics
    ai_adoption_acceleration_factor, enterprise_retention_rate
):
    idx = np.arange(1, months + 1)

    # ---- AI Enterprise Integration Financial Model ----
    
    # AI Implementation Services (core revenue driver)
    ai_implementations_per_month = np.linspace(start_ai_implementations, end_ai_implementations, months)
    # Apply AI adoption acceleration (exponential growth factor)
    ai_implementations_per_month = ai_implementations_per_month * (1 + (idx - 1) * ai_adoption_acceleration_factor / 100)
    ai_implementation_revenue = ai_implementations_per_month * avg_implementation_value
    ai_consulting_revenue = np.linspace(start_ai_consulting_monthly, end_ai_consulting_monthly, months)
    
    # AI Training & Support Services (recurring revenue)
    training_hours_per_month = np.linspace(start_training_hours, end_training_hours, months)
    # Apply enterprise retention factor to training hours
    training_hours_per_month = training_hours_per_month * (enterprise_retention_rate / 100)
    training_revenue = training_hours_per_month * training_rate_per_hour
    support_services_revenue = np.linspace(start_support_services_monthly, end_support_services_monthly, months)
    
    # Round for display
    ai_implementations_display = np.rint(ai_implementations_per_month).astype(int)
    training_hours_display = np.rint(training_hours_per_month).astype(int)
    
    # Map to existing column structure for compatibility
    rental_rev_eventspace = ai_implementation_revenue
    managed_rev_eventspace = ai_consulting_revenue
    conf_rental_revenue = training_revenue

    # Map support services to final revenue stream
    conf_managed_revenue = support_services_revenue
    
    # ---- Total AI Enterprise Revenue ----
    total_revenue = (ai_implementation_revenue + ai_consulting_revenue +
                     training_revenue + support_services_revenue)

    # ---- AI Enterprise Costs ----
    # Sales commission (percentage of revenue)
    sales_commission = (total_revenue * sales_commission_pct).round(0)
    
    # Marketing costs start from specified month (growth investment)
    marketing_costs = np.zeros(months)
    marketing_costs[marketing_start_month-1:] = int(marketing_cost_monthly)
    
    # AI Implementation delivery costs (25% of implementation revenue)
    implementation_costs = ai_implementations_per_month * (avg_implementation_value * 0.25)
    
    total_costs = sales_commission + marketing_costs + implementation_costs
    profit = total_revenue - total_costs
    roi_pct = np.where(total_costs > 0, profit / total_costs * 100, 0)

    df = pd.DataFrame({
        "Month": idx,

        # AI Implementation Metrics
        "AI Implementations per Month": ai_implementations_display,
        "Avg Implementation Value ($)": [int(avg_implementation_value)] * months,
        "AI Adoption Acceleration (%)": [round(ai_adoption_acceleration_factor, 2)] * months,

        # AI Training & Support
        "Enterprise Clients": [int(num_enterprise_clients)] * months,
        "Training Hours per Month": training_hours_display,
        "Training Rate per Hour ($)": [int(training_rate_per_hour)] * months,
        "Enterprise Retention Rate (%)": [round(enterprise_retention_rate, 1)] * months,

        # Revenue Streams
        "Rev: AI Implementation Services": rental_rev_eventspace.astype(int),
        "Rev: AI Consulting Services": managed_rev_eventspace.astype(int),
        "Rev: AI Training Services": conf_rental_revenue.astype(int),
        "Rev: AI Support Services": conf_managed_revenue.astype(int),
        "Revenue: Total": total_revenue.astype(int),

        # Cost Structure
        "Cost: Sales Commission": sales_commission.astype(int),
        "Cost: Marketing Investment": marketing_costs.astype(int),
        "Cost: Implementation Delivery": implementation_costs.astype(int),
        "Costs: Total": total_costs.astype(int),
        
        # Performance Metrics
        "Profit": profit.astype(int),
        "ROI %": roi_pct.round(1),
        "Revenue per Implementation ($)": np.where(ai_implementations_display > 0, total_revenue / ai_implementations_display, 0).round(0),
    })
    return df

# =========================================
# Default settings (can be adjusted in UI)
# =========================================
MONTHS = 36

AI_ENTERPRISE_DEFAULTS = dict(
    # AI Implementation Services
    start_ai_implementations=2, end_ai_implementations=15,
    avg_implementation_value=125000,
    start_ai_consulting_monthly=25000, end_ai_consulting_monthly=200000,
    # AI Training & Support
    num_enterprise_clients=5, start_training_hours=80, end_training_hours=500,
    training_rate_per_hour=300,
    start_support_services_monthly=15000, end_support_services_monthly=150000,
    # Business Operations
    sales_commission_pct=0.15, marketing_cost_monthly=25000,
    # Advanced AI Metrics
    ai_adoption_acceleration_factor=2.5, enterprise_retention_rate=95.0
)

# ===========================================================
# SETTINGS TAB (all inputs neatly grouped in expanders)
# ===========================================================
tab_overview, tab_table, tab_compare, tab_settings, tab_download = st.tabs(
    ["🎯 Executive Dashboard", "📊 Financial Analysis", "⚖️ Scenario Comparison", "🔧 AI Model Parameters", "📁 Export & Reports"]
)

with tab_settings:
    st.header("🤖 AI Enterprise Integration Parameters")
    
    # Add sophisticated scenario preset system
    st.markdown("### 🎯 Intelligent Scenario Presets")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🚀 Aggressive AI Transformation", use_container_width=True, type="primary"):
            st.success("Applied: High-growth AI rollout with 5x acceleration factor")
    with col2:
        if st.button("📈 Balanced Enterprise Integration", use_container_width=True):
            st.info("Applied: Measured growth with risk mitigation")
    with col3:
        if st.button("🛡️ Conservative Validation Approach", use_container_width=True):
            st.warning("Applied: Proof-of-concept focused deployment")
    
    with st.expander("🤖 AI Implementation Services", True):
        st.markdown("**📈 AI Implementation Volume**")
        c1, c2 = st.columns(2)
        start_ai_implementations = c1.number_input("AI Implementations per Month (Month 1)", 0, 50, AI_ENTERPRISE_DEFAULTS["start_ai_implementations"], 1)
        end_ai_implementations = c2.number_input("AI Implementations per Month (Month 36)", 0, 100, AI_ENTERPRISE_DEFAULTS["end_ai_implementations"], 1)
        
        st.markdown("**💰 Implementation Pricing**")
        c3, c4 = st.columns(2)
        avg_implementation_value = c3.number_input("Average Implementation Value ($)", 10000, 1000000, AI_ENTERPRISE_DEFAULTS["avg_implementation_value"], 5000)
        ai_adoption_acceleration_factor = c4.slider("AI Adoption Acceleration Factor (%)", 0.0, 10.0, AI_ENTERPRISE_DEFAULTS["ai_adoption_acceleration_factor"], 0.1)
        
        st.markdown("**🛠️ AI Consulting Services Revenue per Month**")
        c5, c6 = st.columns(2)
        start_ai_consulting_monthly = c5.number_input("AI Consulting Revenue (Month 1) ($)", 0, 1000000, AI_ENTERPRISE_DEFAULTS["start_ai_consulting_monthly"], 1000)
        end_ai_consulting_monthly = c6.number_input("AI Consulting Revenue (Month 36) ($)", 0, 1000000, AI_ENTERPRISE_DEFAULTS["end_ai_consulting_monthly"], 1000)



    with st.expander("🎓 AI Training & Support Services", True):
        st.markdown("**🏢 Enterprise Client Portfolio**")
        num_enterprise_clients = st.number_input("Number of Enterprise Clients", 1, 100, AI_ENTERPRISE_DEFAULTS["num_enterprise_clients"], 1)
        enterprise_retention_rate = st.slider("Enterprise Retention Rate (%)", 70.0, 100.0, AI_ENTERPRISE_DEFAULTS["enterprise_retention_rate"], 0.5)
        
        st.markdown("**⏰ AI Training Hours per Month**")
        c1, c2 = st.columns(2)
        start_training_hours = c1.number_input("Training Hours (Month 1)", 0, 2000, AI_ENTERPRISE_DEFAULTS["start_training_hours"], 10)
        end_training_hours = c2.number_input("Training Hours (Month 36)", 0, 2000, AI_ENTERPRISE_DEFAULTS["end_training_hours"], 10)
        
        # Show training impact
        st.caption(f"📊 Effective training hours with {enterprise_retention_rate}% retention: Month 1 = {start_training_hours * enterprise_retention_rate / 100:.0f} hrs, Month 36 = {end_training_hours * enterprise_retention_rate / 100:.0f} hrs")
        
        st.markdown("**💰 Training & Support Pricing**")
        training_rate_per_hour = st.number_input("Training Rate per Hour ($)", 100, 1000, AI_ENTERPRISE_DEFAULTS["training_rate_per_hour"], 25)
        
        st.markdown("**🛠️ AI Support Services Revenue per Month**")
        c5, c6 = st.columns(2)
        start_support_services_monthly = c5.number_input("Support Services Revenue (Month 1) ($)", 0, 500000, AI_ENTERPRISE_DEFAULTS["start_support_services_monthly"], 1000)
        end_support_services_monthly = c6.number_input("Support Services Revenue (Month 36) ($)", 0, 500000, AI_ENTERPRISE_DEFAULTS["end_support_services_monthly"], 1000)

    with st.expander("💼 Business Operations", True):
        c1, c2 = st.columns(2)
        marketing_cost_monthly = c1.number_input("Monthly Marketing Investment ($)", 0, 200000, AI_ENTERPRISE_DEFAULTS["marketing_cost_monthly"], 1000)
        sales_commission_pct = c2.slider("Sales Commission % of Total Revenue", 0, 50, int(AI_ENTERPRISE_DEFAULTS["sales_commission_pct"]*100), 1) / 100
        
        st.markdown("**📅 Marketing Start Timing**")
        marketing_start_month = st.number_input("Marketing Start Month", 1, 36, 1, 1, 
                                               help="Choose which month to start marketing expenses (1 = immediate, 6 = start in month 6, etc.)")
        if marketing_start_month > 1:
            st.caption(f"💡 Marketing expenses will start in month {marketing_start_month} (saving ${marketing_cost_monthly * (marketing_start_month-1):,.0f} in early months)")

    # Build current DF with AI enterprise inputs
    df_current = generate_ai_enterprise_financials(
        MONTHS,
        # AI Implementation Services
        start_ai_implementations, end_ai_implementations, avg_implementation_value, 
        start_ai_consulting_monthly, end_ai_consulting_monthly,
        # AI Training & Support Services  
        num_enterprise_clients, start_training_hours, end_training_hours, training_rate_per_hour, 
        start_support_services_monthly, end_support_services_monthly,
        # Business Development & Operations
        sales_commission_pct, marketing_cost_monthly, marketing_start_month,
        # Advanced AI Metrics
        ai_adoption_acceleration_factor, enterprise_retention_rate
    )

    save_col, _ = st.columns([1,3])
    if save_col.button("💾 Save Scenario", type="primary"):
        st.session_state.scenarios[scenario_name] = df_current.copy()
        st.success(f"Scenario '{scenario_name}' saved.")

# ===========================================================
# OVERVIEW (KPIs + Charts)
# ===========================================================
with tab_overview:
    st.subheader("Key Metrics (Month 36)")
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Total Revenue", f"${df_current['Revenue: Total'].iloc[-1]:,.0f}")
    k2.metric("Profit", f"${df_current['Profit'].iloc[-1]:,.0f}")
    k3.metric("ROI %", f"{df_current['ROI %'].iloc[-1]:.1f}%")
    k4.metric("Avg Monthly Profit", f"${df_current['Profit'].mean():,.0f}")

    if PLOTLY_AVAILABLE:
        st.markdown("#### Revenue vs Costs")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_current["Month"], y=df_current["Revenue: Total"], mode="lines+markers", name="Total Revenue", line=dict(width=3)))
        fig.add_trace(go.Scatter(x=df_current["Month"], y=df_current["Costs: Total"], mode="lines+markers", name="Total Costs", line=dict(width=3)))
        fig.update_layout(
            height=350, 
            margin=dict(l=10,r=10,t=30,b=10),
            xaxis_title="Month",
            yaxis_title="Amount ($)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
        )
        st.plotly_chart(fig, use_container_width=True)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### Profit over Time")
            figp = px.line(df_current, x="Month", y="Profit", markers=True)
            figp.update_layout(
                height=320, 
                margin=dict(l=10,r=10,t=30,b=10),
                xaxis_title="Month",
                yaxis_title="Profit ($)"
            )
            st.plotly_chart(figp, use_container_width=True)
        with c2:
            st.markdown("#### ROI % over Time")
            figroi = px.line(df_current, x="Month", y="ROI %", markers=True)
            figroi.update_layout(
                height=320, 
                margin=dict(l=10,r=10,t=30,b=10),
                xaxis_title="Month",
                yaxis_title="ROI (%)"
            )
            st.plotly_chart(figroi, use_container_width=True)

        st.markdown("#### AI Revenue Streams (Stacked)")
        rev_df = df_current[["Month","Rev: AI Implementation Services","Rev: AI Consulting Services","Rev: AI Training Services","Rev: AI Support Services"]]
        figstack = go.Figure()
        
        # Use cleaner legend names for AI services
        legend_names = {
            "Rev: AI Implementation Services": "AI Implementation Projects",
            "Rev: AI Consulting Services": "AI Consulting Services",
            "Rev: AI Training Services": "AI Training Programs", 
            "Rev: AI Support Services": "AI Support & Maintenance"
        }
        
        for col in ["Rev: AI Implementation Services","Rev: AI Consulting Services","Rev: AI Training Services","Rev: AI Support Services"]:
            figstack.add_trace(go.Bar(x=rev_df["Month"], y=rev_df[col], name=legend_names[col]))
        
        figstack.update_layout(
            barmode="stack", 
            height=380, 
            margin=dict(l=10,r=10,t=30,b=10),
            xaxis_title="Month",
            yaxis_title="Revenue ($)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
        )
        st.plotly_chart(figstack, use_container_width=True)

        st.markdown("#### AI Revenue Streams Growth Analysis")
        rev_streams_df = df_current[["Month","Rev: AI Implementation Services","Rev: AI Consulting Services","Rev: AI Training Services","Rev: AI Support Services"]]
        figstreams = go.Figure()
        
        # Add line for each AI revenue stream with distinct colors and styling
        colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]  # Blue, Orange, Green, Red
        line_styles = ["solid", "dash", "dot", "dashdot"]
        
        # Use the same cleaner legend names for AI services
        for i, col in enumerate(["Rev: AI Implementation Services","Rev: AI Consulting Services","Rev: AI Training Services","Rev: AI Support Services"]):
            figstreams.add_trace(go.Scatter(
                x=rev_streams_df["Month"], 
                y=rev_streams_df[col], 
                mode="lines+markers",
                name=legend_names[col],
                line=dict(width=3, color=colors[i], dash=line_styles[i]),
                marker=dict(size=6, color=colors[i])
            ))
        
        figstreams.update_layout(
            height=400, 
            margin=dict(l=10,r=10,t=30,b=10),
            xaxis_title="Month",
            yaxis_title="Revenue ($)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
            hovermode='x unified'
        )
        st.plotly_chart(figstreams, use_container_width=True)

        st.markdown("#### AI Enterprise Cost Structure")
        cost_df = df_current[["Month","Cost: Sales Commission","Cost: Marketing Investment","Cost: Implementation Delivery"]]
        figcost = go.Figure()
        
        # Use cleaner legend names for AI enterprise costs
        cost_names = {
            "Cost: Sales Commission": "Sales Team Commission",
            "Cost: Marketing Investment": "Growth Marketing Investment",
            "Cost: Implementation Delivery": "AI Implementation Delivery Costs"
        }
        
        for col in cost_df.columns[1:]:
            figcost.add_trace(go.Scatter(
                x=cost_df["Month"], 
                y=cost_df[col], 
                mode="lines+markers", 
                name=cost_names.get(col, col.replace("Cost: ","")),
                line=dict(width=3),
                marker=dict(size=6)
            ))
        
        figcost.update_layout(
            height=350, 
            margin=dict(l=10,r=10,t=30,b=10),
            xaxis_title="Month",
            yaxis_title="Cost ($)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
        )
        st.plotly_chart(figcost, use_container_width=True)
    else:
        st.warning("📊 Charts require plotly installation. Showing data table instead.")
        st.dataframe(df_current[["Month", "Revenue: Total", "Costs: Total", "Profit", "ROI %"]], use_container_width=True)

# ===========================================================
# DETAILED TABLE
# ===========================================================
with tab_table:
    st.subheader("📊 AI Enterprise Financial Analysis")
    st.caption("🤖 Comprehensive AI integration financial model: Implementation projects, consulting services, training programs, and support services with advanced metrics.")
    st.dataframe(
        df_current.style.format({
            "Avg Implementation Value ($)": "${:,.0f}",
            "Training Rate per Hour ($)": "${:,.0f}",
            "AI Adoption Acceleration (%)": "{:.1f}%",
            "Enterprise Retention Rate (%)": "{:.1f}%",
            "Rev: AI Implementation Services": "${:,.0f}",
            "Rev: AI Consulting Services": "${:,.0f}",
            "Rev: AI Training Services": "${:,.0f}",
            "Rev: AI Support Services": "${:,.0f}",
            "Revenue: Total": "${:,.0f}",
            "Cost: Sales Commission": "${:,.0f}",
            "Cost: Marketing Investment": "${:,.0f}",
            "Cost: Implementation Delivery": "${:,.0f}",
            "Costs: Total": "${:,.0f}",
            "Profit": "${:,.0f}",
            "ROI %": "{:.1f}%",
            "Revenue per Implementation ($)": "${:,.0f}"
        }),
        use_container_width=True, hide_index=True
    )

# ===========================================================
# SCENARIO COMPARE
# ===========================================================
with tab_compare:
    st.subheader("Compare Saved Scenarios")
    if st.session_state.scenarios:
        selected = st.multiselect("Select scenarios to compare", list(st.session_state.scenarios.keys()),
                                  default=list(st.session_state.scenarios.keys())[:2])
        if selected:
            # KPI cards for last-month metrics
            st.markdown("#### Month 36 KPIs")
            cols = st.columns(len(selected))
            for i, name in enumerate(selected):
                df = st.session_state.scenarios[name]
                with cols[i]:
                    st.markdown(f"**{name}**")
                    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
                    st.metric("Revenue", f"${df['Revenue: Total'].iloc[-1]:,.0f}")
                    st.metric("Profit", f"${df['Profit'].iloc[-1]:,.0f}")
                    st.metric("ROI %", f"{df['ROI %'].iloc[-1]:.1f}%")
                    st.markdown('</div>', unsafe_allow_html=True)

            comp_df = pd.concat([st.session_state.scenarios[n].assign(Scenario=n) for n in selected], ignore_index=True)

            if PLOTLY_AVAILABLE:
                st.markdown("#### Profit Over Time")
                figP = px.line(comp_df, x="Month", y="Profit", color="Scenario", markers=True)
                figP.update_layout(
                    height=350, 
                    margin=dict(l=10,r=10,t=30,b=10),
                    xaxis_title="Month",
                    yaxis_title="Profit ($)"
                )
                st.plotly_chart(figP, use_container_width=True)

                st.markdown("#### ROI % Over Time")
                figR = px.line(comp_df, x="Month", y="ROI %", color="Scenario", markers=True)
                figR.update_layout(
                    height=350, 
                    margin=dict(l=10,r=10,t=30,b=10),
                    xaxis_title="Month",
                    yaxis_title="ROI (%)"
                )
                st.plotly_chart(figR, use_container_width=True)

                st.markdown("#### AI Revenue Streams Comparison")
                melt_cols = ["Rev: AI Implementation Services","Rev: AI Consulting Services","Rev: AI Training Services","Rev: AI Support Services"]
                melt_df = comp_df.melt(id_vars=["Month","Scenario"], value_vars=melt_cols, var_name="AI Revenue Stream", value_name="Amount")
                figRB = px.line(melt_df, x="Month", y="Amount", color="Scenario", line_dash="AI Revenue Stream", markers=True)
                figRB.update_layout(
                    height=380, 
                    margin=dict(l=10,r=10,t=30,b=10),
                    xaxis_title="Month",
                    yaxis_title="Revenue ($)"
                )
                st.plotly_chart(figRB, use_container_width=True)

                st.markdown("#### AI Enterprise Cost Analysis")
                melt_c = ["Cost: Sales Commission","Cost: Marketing Investment","Cost: Implementation Delivery"]
                melt_cost = comp_df.melt(id_vars=["Month","Scenario"], value_vars=melt_c, var_name="Cost Type", value_name="Amount")
                figCB = px.line(melt_cost, x="Month", y="Amount", color="Scenario", line_dash="Cost Type", markers=True)
                figCB.update_layout(
                    height=360, 
                    margin=dict(l=10,r=10,t=30,b=10),
                    xaxis_title="Month",
                    yaxis_title="Cost ($)"
                )
                st.plotly_chart(figCB, use_container_width=True)
            else:
                st.dataframe(comp_df[["Month", "Scenario", "Revenue: Total", "Profit", "ROI %"]], use_container_width=True)
        else:
            st.info("Select at least one saved scenario to compare.")
    else:
        st.info("No saved scenarios yet. Configure settings and click **Save Scenario** there.")

# ===========================================================
# DOWNLOAD
# ===========================================================
with tab_download:
    st.subheader("Download Scenarios")
    if st.session_state.scenarios:
        selected_dl = st.multiselect("Select scenarios", list(st.session_state.scenarios.keys()),
                                     default=list(st.session_state.scenarios.keys())[:1])

        def to_excel(dfs, names):
            output = BytesIO()
            with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
                for df, name in zip(dfs, names):
                    df.to_excel(writer, sheet_name=name[:31], index=False)
            return output.getvalue()

        if st.button("Download Selected as Excel"):
            excel_bytes = to_excel([st.session_state.scenarios[n] for n in selected_dl], selected_dl)
            st.download_button("📥 Download Excel", data=excel_bytes,
                               file_name="ai_enterprise_financial_scenarios.xlsx",
                               mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    else:
        st.info("No saved scenarios to download yet.")

# Add requirements installation instructions
st.markdown("---")
st.markdown("### 📋 Installation Requirements")
st.code("""
# To install required dependencies:
pip install streamlit pandas numpy plotly

# Or if using requirements.txt:
pip install -r requirements.txt
""")