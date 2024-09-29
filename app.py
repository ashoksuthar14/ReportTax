import streamlit as st
import random
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="Tax Report", layout="centered")

# Header
st.title(" Tax Analysis Report")

# Step 1: Ask for user input
name = st.text_input("Enter your name:", placeholder="Your Name Here")
tax_analysis_completed = st.radio("Have you completed your tax analysis?", ('Yes', 'No'))

# Ensure the report is only shown if the name is provided and tax analysis is complete
if name and tax_analysis_completed == 'No':
    st.warning("Please complete your tax analysis using the provided tools, then return here to generate your report.")
    st.info("Steps to Complete Tax Analysis:")
    st.markdown("""
    1. **Gather All Relevant Documents**: Make sure you have your income statements, deductions, and other required documents.
    2. **Use Tax Analysis Tools**: Use tax analysis software to compute your deductions and liabilities.
    3. **Review Your Tax Data**: Verify that all income, deductions, and credits have been included correctly.
    4. **Submit the Tax Analysis**: Once you're satisfied with the analysis, come back here to generate your report.
    """)

# Display the report only if name is entered and analysis is complete
elif name and tax_analysis_completed == 'Yes':
    # Step 2: If analysis is complete, display the report

    # Header section
    st.title(f"Tax Report for {name}")
    st.markdown("**Assessment Year: 2024-2025**")

    # Random data generation for demonstration
    income = random.randint(500000, 1500000)
    deductions = random.randint(50000, 300000)
    taxable_income = income - deductions
    tax_paid = random.randint(100000, 200000)
    refund = max(0, tax_paid - (taxable_income * 0.2))  # Example calculation

    # Display random financial details
    st.subheader("Financial Summary")
    
    # Visualizing Income and Deductions
    st.write(f"**Total Income**: ₹ {income:,}")
    st.write(f"**Deductions**: ₹ {deductions:,}")
    st.write(f"**Taxable Income**: ₹ {taxable_income:,}")
    st.write(f"**Tax Paid**: ₹ {tax_paid:,}")
    st.write(f"**Refund Eligible**: ₹ {refund:,}")
    
    # Create bar chart for financial breakdown
    financial_data = {
        "Total Income": income,
        "Deductions": deductions,
        "Taxable Income": taxable_income,
        "Tax Paid": tax_paid,
        "Refund": refund
    }
    st.bar_chart(list(financial_data.values()), height=300)

    # Analysis section
    st.subheader("Report")

    # Suggestions to reduce taxes
    st.markdown("### Suggestions to reduce taxes:")
    st.write("""
    1. **Maximize Section 80C Deductions**: Ensure that you take full advantage of the ₹1.5 lakh limit under Section 80C.
    2. **Invest in NPS (National Pension System)**: This offers additional tax savings under Section 80CCD(1B).
    3. **Claim Medical Insurance**: Take deductions under Section 80D for health insurance premiums.
    4. **Home Loan Interest**: If you have a home loan, claim deductions on the interest paid under Section 24.
    5. **Charitable Contributions**: Donations to approved charitable organizations can help you save taxes under Section 80G.
    """)

    # Suggestions for refund usage
    st.markdown("### Suggestions to use refund money effectively:")
    st.write("""
    1. **Invest in Mutual Funds**: Invest in equity or debt funds to grow your wealth.
    2. **Build an Emergency Fund**: Keep 6 months' worth of expenses in a liquid fund for emergencies.
    3. **Repay High-Interest Debt**: If you have any high-interest loans (e.g., credit card debt), consider paying them off with the refund.
    4. **Invest in Retirement Funds**: Top up your retirement corpus by investing in long-term saving plans.
    5. **Consider Fixed Deposits**: For safe and assured returns, you can invest in fixed deposits.
    """)

    # Check if refund is zero before plotting pie chart
    if refund > 0:
        # Visualize Refund Allocation with Matplotlib
        st.subheader("Visualize Refund Allocation")
        refund_allocation = {
            'Mutual Funds': refund * 0.4,
            'Emergency Fund': refund * 0.2,
            'Debt Repayment': refund * 0.2,
            'Retirement Funds': refund * 0.1,
            'Fixed Deposits': refund * 0.1
        }
        
        # Create a pie chart using Matplotlib
        labels = list(refund_allocation.keys())
        sizes = list(refund_allocation.values())

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Display the pie chart in Streamlit
        st.pyplot(fig)
    else:
        st.info("No refund is available to allocate.")
else:
    st.info("Please enter your name and select whether you have completed your tax analysis.")
