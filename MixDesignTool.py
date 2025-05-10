import streamlit as st 
import pandas as pd 

st.set_page_config(page_title="ACI Concrete Mix Design")
st.title("Automated Concrete Mix Design (ACI 211.1)")
st.markdown("""
# **Standard Practice for Selecting Proportions for Normal Weight Concrete (ACI 211.1-91)**  
## **Reported by ACI Committee**
""")
spg_ca= st.number_input("The value of specific gravity of Coarse Aggregate",min_value=0.00, max_value=4.00 )
spg_fa= st.number_input("The value of specific gravity of Fine Aggregate",min_value=0.00, max_value=4.00 )
fm_fa= st.number_input("The value of fineness modulus of Fine Aggregate",min_value=0.00, max_value=4.00 )
spg_ce= st.number_input("The value of specific gravity of Cement",min_value=0.00, max_value=5.00 )

st.write(f"The value of specific gravity of Coarse Aggregate is **{spg_ca}**")
st.write(f"The value of specific gravity of Fine Aggregate is **{spg_fa}**")
st.write(f"The value of fineness modulus of Fine Aggregate is **{fm_fa}**")
st.write(f"The value of specific gravity of Cement is **{spg_ce}**") 

# Step 01- Take input of fc
st.markdown("### Input the value of 28-day compressive strength in psi ")
st.markdown(" Please enter your **desired 28-day compressive strength in psi** ")

## Ask user for the desired 28-day compressive strength (psi)

fc_psi = st.number_input("What is your desired 28-day Compressive Strength (psi)?", min_value=2000.0, max_value=6000.0,  value=4000.0, step=500.0)

st.write(f"You have entered a compressive strength of **{fc_psi} psi**.")

# Step 02- Slump value 
st.markdown("### Input the value of slump ")
## Let the user pick a slump range
slump_range = st.selectbox(
    "Choose your desired slump range:",
    ["1-2 inch", "3-4 inch", "6-7 inch"]
)

st.write(f"Your selected slump range is **{slump_range}**.")

# Step 03- Air entrained or non-air entrained concrete
st.markdown("### Select the type of concrete")
st.markdown("""
#### **The structure will be exposed to severe wathering or not? **  
#### **If yes, select Air-Entrained concrete. If no, select Non-Air-Entrained concrete.**
""")
concrete_type = st.radio(
    "Select the type of concrete:",
    ("Air-Entrained", "Non-Air-Entrained")
)

st.write(f"You concrete type is: **{concrete_type}** concrete")

# Step 04- Finding water-cement ratio
st.markdown("### Select the value of water-cement ratio from the following table (Table 6.3.4(a))")

# Example Water-Cement Ratio Table based on fc_psi (psi) and concrete type
wc_table_data = {
    "fc_psi": [6000, 5000, 4000, 3000, 2000],
    "Non-Air-Entrained": [0.41, 0.48, 0.57, 0.68, 0.82],
    "Air-Entrained": [None, 0.40, 0.48, 0.59, 0.74]
}
## Convert to DataFrame
wc_df = pd.DataFrame(wc_table_data)

## Display the DataFrame as a table
st.write(wc_df)

wc_ratio= st.number_input("Following the table, What is your desired water-cement ratio (Select between 0.40-0.82?", min_value=0.00, max_value=10.00)

st.write(f"Desired Water-Cement Ratio **{wc_ratio}**")

# Step 05- Selecting nominal size of Aggregates and Water Content

st.markdown("### Select the size of nominal aggregates")

#slump range from user 
slump_range = st.selectbox("Select slump range:", ["1-2", "3-4", "6-7"])
if slump_range == "1-2":
    agg_table_data = {
        "Max Aggregate Size (in)": [3/8, 1/2, 3/4, 1, 1.5, 2, 3, 6],
        "Water - Non-Air-Entrained (lb/yd³)": [350, 335, 315, 300, 275, 260, 220, 190],
        "Water - Air-Entrained (lb/yd³)": [305, 295, 280, 270, 250, 240, 205, 180]
        
    }
    agg_df = pd.DataFrame(agg_table_data)
    st.write(agg_df)
elif slump_range == "3-4":
    agg_table_data = {
        "Max Aggregate Size (in)": [3/8, 1/2, 3/4, 1, 1.5, 2, 3, 6],
        "Water - Non-Air-Entrained (lb/yd³)": [385, 365, 340, 325, 300, 285, 245, 210],
        "Water - Air-Entrained (lb/yd³)": [340, 325, 305, 295, 275, 265, 225, 200]
        
    }
    agg_df = pd.DataFrame(agg_table_data)
    st.write(agg_df)
elif slump_range == "6-7":
    agg_table_data = {
        "Max Aggregate Size (in)": [3/8, 1/2, 3/4, 1, 1.5, 2, 3, 6],
        "Water - Non-Air-Entrained (lb/yd³)": [410, 385, 360, 340, 315, 300, 270, None],
        "Water - Air-Entrained (lb/yd³)": [365, 345, 325, 310, 290, 280, 260, None]
        
    }
    agg_df = pd.DataFrame(agg_table_data)
    st.write(agg_df)
else : 
    st.write("No desired slump value")

water_content= st.number_input("Following the table, What is your desired water content", min_value=100, max_value=500)

st.write(f"Desired Water Content is **{round(water_content)}** lb/yd³")


# Step 06: Selection of exposure for Air-entrained Concrete

st.markdown("### Select the percent of entrapped air")

exposure_range = st.selectbox("Please select your concrete type:", ["Non-air entrained","Air-entrained"])
if exposure_range == "Non-air entrained":
    exp_table_data = {
        "Max Aggregate Size (in)": [3/8, 1/2, 3/4, 1, 1.5, 2, 3, 6],
        "Approximate amount of entrapped air(%)":[3,2.5,2,1.5,1,0.5,0.3,0.2]
    }
    exp_df = pd.DataFrame(exp_table_data)
    st.write(exp_df)  
    entrapped_air= st.number_input("Approximate amount of entrapped air for Non-Air-Entrained Concrete(%)", min_value=0,max_value=10) 
    st.write(f"Entrapped air percentage is **{entrapped_air}**")

elif exposure_range == "Air-entrained":
    exp_table_data = {
        "Max Aggregate Size (in)": [3/8, 1/2, 3/4, 1, 1.5, 2, 3, 6],
        "Average total air content for Mild Exposure":[4.5,4,3.5,3,2.5,2,1.5,1],
        "Average total air content for Moderate Exposure":[6,5.5,5,4.5,4.5,4,3.5,3],
        "Average total air content for Severe Exposure":[7.5,7,6,6,5.5,5,4.5,4]
    }
    exp_df = pd.DataFrame(exp_table_data)
    st.write(exp_df) 
    entrapped_air= st.number_input("Average total air content(%)", min_value=0,max_value=10) 
    st.write(f"Average total air content(%) **{entrapped_air}**") 
else:
    st.write("Select your concrete type")

# Step 07: Cement Content

st.markdown("### Calculate the value of cement content from wc artio and water content")

st.write(f"Desired Water-Cement Ratio **{wc_ratio}**")
st.write(f"Desired Water Content **{water_content}**")
cement_content = water_content/ wc_ratio 
st.write(f"Desired Cement Content **{round(cement_content)}** lb/yd³")

# Step 08: Volume of Coarse aggregate
st.markdown("### Calculate the amount of Coarse Aggregate")
ca_table = {
    "Nominal Maximum Size of Aggregate": [3/8, 1/2, 3/4, 1, 1.5, 2, 3, 6],
    "Volume dry rodded CA per unit volume of concrete for FM 2.40": [0.50,0.59,0.66,0.71,0.75,0.78,0.82,0.87],
    "Volume dry rodded CA per unit volume of concrete for FM 2.60": [0.48,0.57,0.64,0.69,0.73,0.76,0.80,0.85],
    "Volume dry rodded CA per unit volume of concrete for FM 2.80": [0.46,0.55,0.62,0.67,0.71,0.74,0.78,0.83],
    "Volume dry rodded CA per unit volume of concrete for FM 3.00": [0.44,0.53,0.60,0.65,0.69,0.72,0.76,0.81],
}
ca_df= pd.DataFrame(ca_table)
st.write(ca_df)

ca_volume = st.number_input ("The volume of Coarse aggregate", min_value=0.00, max_value=1.00) 
st.write(f"The volume of Coarse Aggregate is **{ca_volume}**yd³ or **{ca_volume*27}** ft³")
unit_wt_ca= st.number_input ("The value of dry rodded unit weight of Coarse Aggregate is", min_value=0, max_value=1000)
st.write(f"Coarse aggregate weighs **{unit_wt_ca}** lb/ft³")
ca_content= (ca_volume*unit_wt_ca*27)
st.write (f"The quantity of Coarse aggregate is **{round(ca_content)}** lb")
st.markdown("### Now, you have to choose the method of Mixing")
mix_method= st.selectbox("Choose your method:", ["weight basis", "volume basis"])

if mix_method == "weight basis":
    concrete_weight_table={
        "Nominal Maximum Size of Aggregate": [3/8, 1/2, 3/4, 1, 1.5, 2, 3, 6],
        "Concrete weight for Non-Air-Entrained Concrete, lb/yd³":[3840,3890,3960,4010,4070,4120,4200,4260],
        "Concrete weight for Air-Entrained Concrete, lb/yd³":[3710,3760,3840,3850,3910,3950,4040,4110]
    }
    weight_df= pd.DataFrame(concrete_weight_table)
    st.write(weight_df)
    concrete_weight= st.number_input ("Enter the weight of concrete", min_value=2000, max_value=6000)
    st.write(f"The weight of a yd³ of concrete is {concrete_weight} lb")
    st.write("Now you have the following values:")
    st.write(f"Weight of Coarse Aggregate= **{ca_content}** lb")
    st.write(f"Weight of Water Content= **{water_content}** lb")
    st.write(f"Weight of Cement= **{round(cement_content)}** lb")
    total_weight = (ca_content) + (cement_content) + (water_content)
    st.write(f"Total= {round(total_weight)} lb")
    fa_content = (concrete_weight) - (total_weight)
    st.write(f"The weight of Fine Aggregate is **{round(fa_content)}** lb")
    batch_table= {
    "Ingridients": ["Water","Cement","Coarse aggregate", "fine aggregate"],
    "Based on Concrete Weight": [round(water_content),round(cement_content),round(ca_content),round(fa_content)]

    }
    batch_df= pd.DataFrame(batch_table)
    
    st.write(batch_df)
    mois_ca= st.number_input ("Moisture percent in Coarse Aggregate",min_value=0.00,max_value=10.00)
    mois_fa= st.number_input ("Moisture percent in Fine Aggregate",min_value=0.00,max_value=10.00)
    mul_ca= 1+ (mois_ca/100)
    mul_fa= 1+ (mois_fa/100)

    wetwt_ca= ca_content*mul_ca
    wetwt_fa= fa_content*mul_fa
    st.write(f"The wet weight of coarse aggregate **{round(wetwt_ca)}**")
    st.write(f"The wet weight of fine aggregate **{round(wetwt_fa)}**")

    abs_ca= st.number_input ("Absorption in Coarse Aggregate",min_value=0.01,max_value=10.00)
    abs_fa= st.number_input ("Absorption in Fine Aggregate",min_value=0.01,max_value=10.00)

    st.markdown ("The absorved water is not a part of mixing water and must be excluded from adjustment in added water")
    sw_ca= (mois_ca - abs_ca) / 100
    sw_fa= (mois_fa - abs_fa) / 100
    req_water= (water_content) - (sw_ca*ca_content) - (sw_fa*fa_content)
    st.write(f"The requirement for added water {round(req_water)} lb")

    st.markdown("The estimated batch weights for a yd³ of concrete ")
    final_table= {
    "Ingridients": ["Water,to be added","Cement","Coarse aggregate,wet", "fine aggregate,wet"],
    "Based on Concrete Weight": [round(req_water),round(cement_content),round(wetwt_ca),round(wetwt_fa)]

    }
    finaltable_df= pd.DataFrame(final_table)
    st.write(finaltable_df)

elif mix_method == "volume basis": 
    st.write(f"The value of specific gravity of Coarse Aggregate is **{spg_ca}**")
    st.write(f"The value of specific gravity of Fine Aggregate is **{spg_fa}**")
    st.write(f"The value of fineness modulus of Fine Aggregate is **{fm_fa}**")
    st.write(f"Unit weight of water is 62.4 lb/ft³")
    vol_wat= (water_content)/ 62.4
    st.write (f"Volume of water is **{vol_wat:.2f}** ft³")
    st.write(f"The value of specific gravity of Cement is **{spg_ce}**") 
    vol_ce= (cement_content)/ (spg_ce*62.4)
    st.write (f"Volume of cement is **{vol_ce:.2f}** ft³")
    vol_ca=  (ca_content) / (spg_ca * 62.4)
    st.write (f"Volume of Coarse aggregate is **{vol_ca:.2f}** ft³")
    vol_air= st.number_input("Volume of entrapped air per yd³ is", min_value=0,max_value=10)
    st.write (f"Volume of entrapped air **{vol_air*27}** ft³ ")
    percent_air= (vol_air*27)/100
    total_vol= (vol_wat) + (vol_ce) + (vol_ca) + (percent_air)
    st.write (f"Total volume of ingridients except fine aggregate is **{total_vol:.2f}** ft³ ")
    vol_fa = 27 - (total_vol)
    st.write (f"Solid volume of Fine aggregate is {vol_fa:.2f} ft³")
    wt_fa= (vol_fa) * spg_fa * 62.4
    st.write(f"Required weight of Fine Aggregate is **{round(wt_fa)}**")
    

    batch_table= {
    "Ingridients": ["Water","Cement","Coarse aggregate", "fine aggregate"],
    
    "Based on Volume": [water_content,cement_content,ca_content,wt_fa] 

    }
    batch_df= pd.DataFrame(batch_table)
    st.write(batch_df)
    mois_ca= st.number_input ("Moisture percent in Coarse Aggregate",min_value=0.00,max_value=10.00)
    mois_fa= st.number_input ("Moisture percent in Fine Aggregate",min_value=0.00,max_value=10.00)
    mul_ca= 1+ (mois_ca/100)
    mul_fa= 1+ (mois_fa/100)
    concrete_weight_table={
        "Nominal Maximum Size of Aggregate": [3/8, 1/2, 3/4, 1, 1.5, 2, 3, 6],
        "Concrete weight for Non-Air-Entrained Concrete, lb/yd³":[3840,3890,3960,4010,4070,4120,4200,4260],
        "Concrete weight for Air-Entrained Concrete, lb/yd³":[3710,3760,3840,3850,3910,3950,4040,4110]
    }
    weight_df= pd.DataFrame(concrete_weight_table)
    st.write(weight_df)
    concrete_weight= st.number_input ("Enter the weight of concrete", min_value=3700, max_value=4200)
    st.write(f"The weight of a yd³ of concrete is **{concrete_weight}** lb")
    st.write(f"Weight of Coarse Aggregate= **{ca_content}** lb")
    st.write(f"Weight of Water Content= **{water_content}** lb")
    st.write(f"Weight of Cement= **{round(cement_content)}** lb")
    wetwt_ca= ca_content*mul_ca
    wetwt_fa= wt_fa*mul_fa
    st.write(f"The wet weight of coarse aggregate **{round(wetwt_ca)}**")
    st.write(f"The wet weight of Fine Aggregate is **{round(wetwt_fa)}**")

    abs_ca= st.number_input ("Absorption in Coarse Aggregate",min_value=0.01,max_value=10.00)
    abs_fa= st.number_input ("Absorption in Fine Aggregate",min_value=0.01,max_value=10.00)

    st.markdown ("The absorved water is not a part of mixing water and must be excluded from adjustment in added water")
    sw_ca= (mois_ca - abs_ca) / 100
    sw_fa= (mois_fa - abs_fa) / 100
    req_water= (water_content) - (sw_ca*ca_content) - (sw_fa*wt_fa)
    st.write(f"The requirement for added water {round(req_water)} lb")

    st.markdown("The estimated batch weights for a yd³ of concrete ")
    final_table= {
    "Ingridients": ["Water,to be added","Cement","Coarse aggregate,wet", "fine aggregate,wet"],
    "Based on Concrete Weight": [round(req_water),round(cement_content),round(wetwt_ca),round(wetwt_fa)]

    }
    finaltable_df= pd.DataFrame(final_table)
    st.write(finaltable_df)
else: 
    st.write("Do nothing")



    

